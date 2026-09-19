# Phase 1 — Foundations (Weeks 1–10)

**Dates:** 2026-09-14 → 2026-11-22 (10 weeks)
**Budget:** ~190 hours (19h/week)
**Subjects:** Programming in C (Wk 1–3) · Data Structures (Wk 4–6) · Discrete Mathematics (Wk 7–10)
**Theme:** Rebuild the base every other subject stands on — and build the daily habit loop (lecture PM → PYQs next AM → error log → Saturday test).

---

## Why This Phase Exists

C and Data Structures are ~8–11 marks by themselves, and they're the language of Algorithms, OS and Compiler questions. Discrete Maths is ~5–8 marks directly, and it's the language of Algorithms, TOC and DBMS.

You write code every day, so C will feel familiar — **that's the trap.** GATE C questions are adversarial hand-tracing: static variables, pointer aliasing, precedence, side effects. "I'd never write code like this" is not an answer option. Discrete Maths hasn't been touched in 5+ years and needs slow, proof-aware learning.

The other goal is the **habit loop**. 72 weeks only works if the daily rhythm becomes automatic in these first 10 weeks.

---

## Phase Goals (end-of-phase state)

- [ ] Syllabus rows PD-1 … PD-14 and DM-1 … DM-10 all at confidence ≥3 in `trackers/subjects.md`
- [ ] All even-year + 2021 PYQs attempted for C, DS, Discrete Maths; odd-year PYQs used in Saturday tests
- [ ] PYQ accuracy ≥60% in each of C, DS, DM (≥70% is the Phase 5 target)
- [ ] Short notes written for every topic; `notes/formula-sheets/programming-ds.md` complete, `engineering-maths.md` started (DM section)
- [ ] Week 1 diagnostic logged in `trackers/mocks.md`
- [ ] Error log in daily use, redo success ≥70%
- [ ] 10 weekly reviews + 2 monthly reviews (Oct, Nov) written
- [ ] Adherence ≥70%

---

## How to Read the Weekly Tables

- **Lecture resource:** primary series from `resources.md` (GO Classes playlist for the subject). On the first day of each subject, map the playlist's video numbers to this week's topics and paste the mapping into that day's log.
- **PYQs:** GATE Overflow / GO PDF, following the PYQ Split Rule in `PLAN.md` (weekday AM = even years + 2021; Saturday = odd years; sealed 2022+ untouched).
- **Every AM** starts with 10–15 min of error-log redos (not repeated in each row).
- **Every PM** ends with 5 min of daily-log Reflection (not repeated in each row).

---

## Weekly Breakdown

### Week 1 — C: Operators, Control Flow, Functions, Scope (2026-09-14 → 2026-09-20)
**Hours: 19** | **Topics: PD-1, PD-2** | **Saturday: DIAGNOSTIC full paper**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Day-1 setup (20 min): open GO C playlist, map videos → Weeks 1–3 topics; GO PDF downloaded. Then lecture: data types, sizes, integer promotion, type conversion | GO Classes C Programming | Mapping in daily log; `notes/programming-ds/c-01-operators-control-flow.md` (start) |
| Mon | PM | Lecture: operators, precedence + associativity, short-circuit evaluation, side effects, sequence points | GO Classes C Programming | `c-01` |
| Tue | AM | PYQs: operators, precedence, expression output (PD-1) | GO tag programming-in-c | Daily log + error log |
| Tue | PM | Lecture: control flow — if/else chains, switch fall-through, loops, break/continue, loop output tracing | GO Classes C Programming | `c-01` (complete) |
| Wed | AM | PYQs: control flow + loop output tracing | GO tag programming-in-c | Daily log + error log |
| Wed | PM | Lecture: functions, call stack, return values; storage classes auto / static / extern / register | GO Classes C Programming | `notes/programming-ds/c-02-functions-storage-scope.md` |
| Thu | AM | PYQs: storage classes, static locals across calls | GO tag static / programming-in-c | Daily log + error log |
| Thu | PM | Lecture: scope — block/file scope, static vs dynamic scoping; parameter passing (value, pointer-reference; call-by-name / need concepts) | GO Classes C Programming | `c-02` (complete) |
| Fri | AM | PYQs: static vs dynamic scoping output, parameter passing | GO tag parameter-passing | Daily log + error log |
| Fri | PM | Consolidate: C precedence table + storage-class behaviour table | Own notes | `notes/formula-sheets/programming-ds.md` (start) |
| Sat | 09:00–12:00 | **DIAGNOSTIC:** GATE CS 2021 Set 1, full 3h, virtual calculator, no preparation. This is a baseline, not a judgement | GO exams page (original paper, test mode) | Score sheet |
| Sat | 12:00–13:00 | Score with GO key. Record section-wise marks (GA / maths / each subject). Error-log only the C + GA questions (rest is unstudied). GA hour is covered by the paper this week | GO answer key | `trackers/mocks.md` → Diagnostic D1 |
| Sun | — | Weekly review #1 + fill baseline in `trackers/progress.md` | — | `reviews/weekly/2026-09-14-to-2026-09-20.md` |

**Resources:**
- GO Classes C Programming — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHgzQutUHGzqMjA1z7XJ_Uya
- GATE Overflow C PYQs — https://gateoverflow.in/tag/pointers (pattern: `gateoverflow.in/tag/<topic>`)
- TCS iON virtual calculator — https://www.tcsion.com/OnlineAssessment/ScientificCalculator/Calculator.html
- Reference: K&R Ch 2–4

---

### Week 2 — C: Pointers, Strings, 2D Arrays (2026-09-21 → 2026-09-27)
**Hours: 19** | **Topics: PD-3, PD-4** | **GA rotation 2: Grammar**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo diagnostic C/GA errors; mixed unseen PYQs on PD-1/PD-2 | GO PYQs | Error log |
| Mon | PM | Lecture: pointers — declaration, `&` / `*`, pointer to pointer, NULL, pointers and functions | GO Classes C Programming | `notes/programming-ds/c-03-pointers.md` |
| Tue | AM | PYQs: pointer basics, swap-style output questions | GO tag pointers | Daily log + error log |
| Tue | PM | Lecture: pointer arithmetic, arrays vs pointers, array decay, `const` with pointers | GO Classes C Programming | `c-03` |
| Wed | AM | PYQs: pointer arithmetic, array–pointer equivalence | GO tag pointers, array | Daily log + error log |
| Wed | PM | Lecture: strings — char arrays vs string literals, `strlen` / `sizeof`, string function behaviour | GO Classes C Programming | `notes/programming-ds/c-04-strings-2d-arrays.md` |
| Thu | AM | PYQs: strings | GO tag strings | Daily log + error log |
| Thu | PM | Lecture: 2D arrays, arrays of pointers vs pointer to array, complex declarations (right-left rule) | GO Classes C Programming | `c-04` (complete) |
| Fri | AM | PYQs: 2D arrays, declarations | GO tag array | Daily log + error log |
| Fri | PM | Concept-repair slot: re-watch the single weakest pointer segment (backup series only if needed); write a "pointer traps" list | NPTEL C (backup) | `c-03` traps section |
| Sat | 09:00–11:00 | Timed topic test: ~25 odd-year PYQs, PD-1 … PD-4, negative marking | GO PYQs (odd years) | `trackers/mocks.md` topic test T2 |
| Sat | 11:00–12:00 | GA rotation 2 — Grammar | GO PDF Vol 1 GA + IndiaBix | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #2. (Sep monthly review skipped — only 2 weeks; fold into October's) | — | `reviews/weekly/2026-09-21-to-2026-09-27.md` |

**Reminder:** GATE 2027 regular registration closes **27 Sep 2026** (late fee until 5 Oct) — only if you decided on the practice attempt.

---

### Week 3 — C: Recursion, Structs, Dynamic Memory (2026-09-28 → 2026-10-04)
**Hours: 19** | **Topics: PD-5, PD-6** | **GA rotation 3: Data interpretation**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs on PD-3/PD-4 | GO PYQs | Error log |
| Mon | PM | Lecture: recursion — tracing, call trees, output prediction | GO Classes C Programming | `notes/programming-ds/c-05-recursion.md` |
| Tue | AM | PYQs: recursive function output | GO tag recursion | Daily log + error log |
| Tue | PM | Lecture: recursion — counting calls, return value for n, recursion → recurrence relation | GO Classes C Programming | `c-05` (complete) |
| Wed | AM | PYQs: recursion NATs (number of calls, value returned) | GO tag recursion | Daily log + error log |
| Wed | PM | Lecture: structures, unions, self-referential structs, `sizeof` of struct/union | GO Classes C Programming | `notes/programming-ds/c-06-structs-dynamic-memory.md` |
| Thu | AM | PYQs: structures, unions | GO tag structure | Daily log + error log |
| Thu | PM | Lecture: `malloc` / `free`, dangling pointers, memory leaks, function pointers | GO Classes C Programming | `c-06` (complete) |
| Fri | AM | PYQs: dynamic memory + mixed C | GO tag malloc, programming-in-c | Daily log + error log |
| Fri | PM | C wrap-up: finish C section of the formula sheet; "top 10 C traps" | Own notes | `notes/formula-sheets/programming-ds.md` |
| Sat | 09:00–11:00 | **C subject test:** ~30 odd-year PYQs across PD-1 … PD-6 | GO PYQs (odd years) | Topic test T3 |
| Sat | 11:00–12:00 | GA rotation 3 — Data interpretation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis; **R1 revision of C** (re-read all C notes) | — | `trackers/revision.md` R1 C |
| Sun | — | Weekly review #3 | — | `reviews/weekly/2026-09-28-to-2026-10-04.md` |

---

### Week 4 — DS: Arrays, Stacks, Queues (2026-10-05 → 2026-10-11)
**Hours: 19** | **Topics: PD-7, PD-8, PD-9** | **GA rotation 4: Logic + reasoning**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; 10 mixed C PYQs (pre-2000 top-up) to keep C warm. Map DS playlist → Weeks 4–6 | GO PYQs; GO Classes DS | Error log; mapping |
| Mon | PM | Lecture: arrays — row-major / column-major address formulas, non-zero lower bounds, triangular matrix storage | GO Classes Data Structures | `notes/programming-ds/ds-01-arrays.md` |
| Tue | AM | PYQs: array address calculation (NAT) | GO tag array | Daily log + error log |
| Tue | PM | Lecture: stacks — array/list implementation, infix → postfix / prefix conversion | GO Classes Data Structures | `notes/programming-ds/ds-02-stacks.md` |
| Wed | AM | PYQs: expression conversion | GO tag stack | Daily log + error log |
| Wed | PM | Lecture: postfix evaluation, stack permutations, recursion ↔ stack | GO Classes Data Structures | `ds-02` (complete) |
| Thu | AM | PYQs: evaluation, minimum stack size, valid permutations | GO tag stack | Daily log + error log |
| Thu | PM | Lecture: queues — circular queue full/empty conditions, deque, queue using stacks and stack using queues | GO Classes Data Structures | `notes/programming-ds/ds-03-queues.md` |
| Fri | AM | PYQs: queues | GO tag queue | Daily log + error log |
| Fri | PM | Priority queue concept + untimed practice on stack/queue code-completion questions | GO Classes practice / backup: Gate Smashers DS | `ds-03` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs PD-7 … PD-9 + 5 C carry-over | GO PYQs (odd years) | Topic test T4 |
| Sat | 11:00–12:00 | GA rotation 4 — Logic + reasoning | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #4 | — | `reviews/weekly/2026-10-05-to-2026-10-11.md` |

---

### Week 5 — DS: Linked Lists, Binary Trees, BST / AVL (2026-10-12 → 2026-10-18)
**Hours: 19** | **Topics: PD-10, PD-11, PD-12** | **GA rotation 5: Vocabulary + reading**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs PD-7 … PD-9 | GO PYQs | Error log |
| Mon | PM | Lecture: linked lists — singly, doubly, circular; insert / delete / reverse code tracing | GO Classes Data Structures | `notes/programming-ds/ds-04-linked-lists.md` |
| Tue | AM | PYQs: linked-list code tracing and missing-line questions | GO tag linked-list | Daily log + error log |
| Tue | PM | Lecture: binary trees — node/leaf/height relationships, full vs complete, traversals | GO Classes Data Structures | `notes/programming-ds/ds-05-binary-trees.md` |
| Wed | AM | PYQs: tree properties (NAT) | GO tag binary-tree | Daily log + error log |
| Wed | PM | Lecture: construct tree from traversals, counting distinct trees (Catalan numbers) | GO Classes Data Structures | `ds-05` (complete) |
| Thu | AM | PYQs: traversals, tree construction | GO tag binary-tree | Daily log + error log |
| Thu | PM | Lecture: BST insert / delete / search; number of BSTs; AVL rotations + height bounds | GO Classes Data Structures | `notes/programming-ds/ds-06-bst-avl.md` |
| Fri | AM | PYQs: BST and AVL | GO tag binary-search-tree, avl-tree | Daily log + error log |
| Fri | PM | AVL deep-dive: min nodes for height h recurrence, worked rotations on paper | GO Classes DS / backup: Gate Smashers DS | `ds-06` (complete) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs PD-10 … PD-12 | GO PYQs (odd years) | Topic test T5 |
| Sat | 11:00–12:00 | GA rotation 5 — Vocabulary + reading / sequencing | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #5 | — | `reviews/weekly/2026-10-12-to-2026-10-18.md` |

---

### Week 6 — DS: Heaps, Graphs + PDS Wrap-up (2026-10-19 → 2026-10-25)
**Hours: 19** | **Topics: PD-13, PD-14** | **GA rotation 6: Mensuration + geometry**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs PD-10 … PD-12 | GO PYQs | Error log |
| Mon | PM | Lecture: binary heap — array representation, heapify, build-heap in O(n) | GO Classes Data Structures | `notes/programming-ds/ds-07-heaps.md` |
| Tue | AM | PYQs: heap structure, valid heap arrays | GO tag heap | Daily log + error log |
| Tue | PM | Lecture: heap insert / delete-min / k-th smallest, d-ary heaps | GO Classes Data Structures | `ds-07` (complete) |
| Wed | AM | PYQs: heap after operation sequences (array contents) | GO tag heap | Daily log + error log |
| Wed | PM | Lecture: graphs — adjacency matrix vs list (space/time), BFS / DFS basics | GO Classes Data Structures | `notes/programming-ds/ds-08-graphs.md` |
| Thu | AM | PYQs: graph representation, BFS / DFS order | GO tag graph-algorithms | Daily log + error log |
| Thu | PM | PDS wrap-up: DS section of the formula sheet (node-count formulas, heap facts, complexity of DS operations) | Own notes | `notes/formula-sheets/programming-ds.md` (complete) |
| Fri | AM | Mixed PDS PYQs: all remaining even-year questions across PD-1 … PD-14 | GO PYQs | Daily log + error log |
| Fri | PM | **R1 revision** of DS notes (Weeks 4–5) | Own notes | `trackers/revision.md` R1 DS |
| Sat | 09:00–11:00 | **PDS subject test:** ~30 odd-year PYQs, C + DS | GO PYQs (odd years) | Topic test T6 |
| Sat | 11:00–12:00 | GA rotation 6 — Mensuration + geometry | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, PDS confidence ratings in `subjects.md` | — | Error log |
| Sun | — | Weekly review #6 **+ Monthly review (October 2026, first)** | — | `reviews/weekly/2026-10-19-to-2026-10-25.md` + `reviews/monthly/2026-10.md` |

**Resources:**
- GO Classes Data Structures — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHi_0QW5bavzLyAJZ0ozFTJ3
- Backup: Gate Smashers Data Structure — https://www.youtube.com/playlist?list=PLxCzCOWd7aiEwaANNt3OqJPVIxwp2ebiT

---

### Week 7 — Discrete Maths: Propositional + First Order Logic (2026-10-26 → 2026-11-01)
**Hours: 19** | **Topics: DM-1, DM-2** | **GA rotation 7: Statistics + probability + PnC**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; 10 mixed PDS PYQs (top-up). Map DM playlist → Weeks 7–10 | GO PYQs; GO Classes DM | Error log; mapping |
| Mon | PM | Lecture: propositional logic — connectives, truth tables, tautology / contradiction / contingency, logical equivalence laws | GO Classes Discrete Mathematics | `notes/maths/dm-01-propositional-logic.md` |
| Tue | AM | PYQs: tautology, equivalence | GO tag propositional-logic | Daily log + error log |
| Tue | PM | Lecture: normal forms (CNF / DNF), rules of inference, validity of arguments | GO Classes Discrete Mathematics | `dm-01` (complete) |
| Wed | AM | PYQs: inference, argument validity | GO tag propositional-logic | Daily log + error log |
| Wed | PM | Lecture: first order logic — predicates, quantifiers, negation, nested quantifiers | GO Classes Discrete Mathematics | `notes/maths/dm-02-first-order-logic.md` |
| Thu | AM | PYQs: quantifier equivalences | GO tag first-order-logic | Daily log + error log |
| Thu | PM | Lecture: English ↔ FOL translation, validity of FOL formulas | GO Classes Discrete Mathematics | `dm-02` (complete) |
| Fri | AM | PYQs: FOL translation + validity | GO tag first-order-logic | Daily log + error log |
| Fri | PM | Consolidate equivalence laws + quantifier rules; concept repair from Rosen Ch 1 if needed | Rosen Ch 1 / MIT 6.042J (backup) | `notes/formula-sheets/engineering-maths.md` (start, DM section) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs DM-1, DM-2 + 5 PDS carry-over | GO PYQs (odd years) | Topic test T7 |
| Sat | 11:00–12:00 | GA rotation 7 — Statistics + probability + PnC | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #7 | — | `reviews/weekly/2026-10-26-to-2026-11-01.md` |

---

### Week 8 — Discrete Maths: Sets, Relations, Functions, Posets, Lattices (2026-11-02 → 2026-11-08)
**Hours: 19** | **Topics: DM-3, DM-4, DM-5** | **GA rotation 8: Spatial aptitude**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year logic PYQs | GO PYQs | Error log |
| Mon | PM | Lecture: sets, relations, relation properties (reflexive, irreflexive, symmetric, antisymmetric, asymmetric, transitive) | GO Classes Discrete Mathematics | `notes/maths/dm-03-sets-relations.md` |
| Tue | AM | PYQs: relation properties | GO tag relations | Daily log + error log |
| Tue | PM | Lecture: closures, equivalence relations + classes, partitions, counting relations with properties | GO Classes Discrete Mathematics | `dm-03` (complete) |
| Wed | AM | PYQs: counting relations (NAT), equivalence classes | GO tag relations, set-theory | Daily log + error log |
| Wed | PM | Lecture: functions — injective, surjective, bijective, composition, inverse, counting functions | GO Classes Discrete Mathematics | `notes/maths/dm-04-functions.md` |
| Thu | AM | PYQs: functions | GO tag functions | Daily log + error log |
| Thu | PM | Lecture: partial orders, Hasse diagrams, lub / glb, lattices | GO Classes Discrete Mathematics | `notes/maths/dm-05-posets-lattices.md` |
| Fri | AM | PYQs: POSET / lattice identification | GO tag partial-order, lattice | Daily log + error log |
| Fri | PM | Lecture: bounded, complemented, distributive lattices; Boolean algebra as a lattice | GO Classes Discrete Mathematics | `dm-05` (complete) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs DM-3 … DM-5 | GO PYQs (odd years) | Topic test T8 |
| Sat | 11:00–12:00 | GA rotation 8 — Spatial aptitude (draw every question) | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis; **R1 revision** of logic notes (Week 7) | — | `trackers/revision.md` |
| Sun | — | Weekly review #8 | — | `reviews/weekly/2026-11-02-to-2026-11-08.md` |

---

### Week 9 — Discrete Maths: Groups + Combinatorics (2026-11-09 → 2026-11-15)
**Hours: 19** | **Topics: DM-6, DM-7** | **GA rotation 9: Mixed timed GA section**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DM-3 … DM-5 | GO PYQs | Error log |
| Mon | PM | Lecture: algebraic structures — closure, associativity, identity, inverse; semigroup, monoid, group, abelian group | GO Classes Discrete Mathematics | `notes/maths/dm-06-groups.md` |
| Tue | AM | PYQs: identify the structure | GO tag group-theory | Daily log + error log |
| Tue | PM | Lecture: subgroups, cyclic groups, generators, order of an element, Lagrange's theorem | GO Classes Discrete Mathematics | `dm-06` (complete) |
| Wed | AM | PYQs: cyclic groups, order, generators (NAT) | GO tag group-theory | Daily log + error log |
| Wed | PM | Lecture: counting — sum / product rule, permutations, combinations, with repetition, stars and bars | GO Classes Discrete Mathematics | `notes/maths/dm-07-counting.md` |
| Thu | AM | PYQs: PnC (NAT) | GO tag combinatory | Daily log + error log |
| Thu | PM | Lecture: pigeonhole principle, inclusion–exclusion, derangements, counting onto functions | GO Classes Discrete Mathematics | `dm-07` (complete) |
| Fri | AM | PYQs: pigeonhole, inclusion–exclusion | GO tag pigeonhole-principle, combinatory | Daily log + error log |
| Fri | PM | Counting formula sheet + untimed mixed counting practice | GO Classes DM free course practice | `notes/formula-sheets/engineering-maths.md` (counting) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs DM-6, DM-7 + 5 relations carry-over | GO PYQs (odd years) | Topic test T9 |
| Sat | 11:00–12:00 | GA rotation 9 — one full 10-question GA section, 25 min timed, score /15 | GA PYQs (other branches' papers) | `trackers/aptitude.md` mixed-set score |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #9 | — | `reviews/weekly/2026-11-09-to-2026-11-15.md` |

---

### Week 10 — Discrete Maths: Recurrences, Generating Functions, Graph Theory (2026-11-16 → 2026-11-22)
**Hours: 19** | **Topics: DM-8, DM-9, DM-10** | **GA rotation 1: Numerical computation**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DM-6, DM-7 | GO PYQs | Error log |
| Mon | PM | Lecture: recurrence relations — formulating, homogeneous linear, characteristic roots (distinct / repeated) | GO Classes Discrete Mathematics | `notes/maths/dm-08-recurrences.md` |
| Tue | AM | PYQs: solve / formulate recurrences | GO tag recurrence-relation | Daily log + error log |
| Tue | PM | Lecture: non-homogeneous recurrences (particular solutions) | GO Classes Discrete Mathematics | `dm-08` (complete) |
| Wed | AM | PYQs: recurrences (NAT) | GO tag recurrence-relation | Daily log + error log |
| Wed | PM | Lecture: generating functions — closed forms, coefficient extraction, counting with GFs | GO Classes Discrete Mathematics | `notes/maths/dm-09-generating-functions.md` |
| Thu | AM | PYQs: generating functions | GO tag generating-functions | Daily log + error log |
| Thu | PM | Lecture: graph theory 1 — degree sequences, handshaking, connectivity, cut vertices / edges, Euler + Hamilton, bipartite | GO Classes DM / GO Graph Theory playlist | `notes/maths/dm-10-graph-theory.md` |
| Fri | AM | PYQs: connectivity, degree, Euler / Hamilton | GO tag graph-connectivity | Daily log + error log |
| Fri | PM | Lecture: graph theory 2 — matching, vertex / edge colouring, chromatic number, planarity + Euler's formula | GO Classes Graph Theory playlist | `dm-10` (complete) |
| Sat | 09:00–11:00 | **DM subject test:** ~30 odd-year PYQs across DM-1 … DM-10 | GO PYQs (odd years) | Topic test T10 |
| Sat | 11:00–12:00 | GA rotation 1 — Numerical computation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + walk the **Phase 1 exit checklist** below | — | Exit checklist answers in daily log |
| Sun | — | Weekly review #10 + **Phase 1 retrospective** (phase transition questions from `PLAN.md`) | — | `reviews/weekly/2026-11-16-to-2026-11-22.md` |

(Matching / colouring even-year PYQs roll into Week 11 Monday AM.)

**Resources:**
- GO Classes Discrete Mathematics — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHgjPQN2GtCVOCgrkH2zCkSU
- GO Classes Graph Theory — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjQoj0k-BlI9zXE0QKdl-lI
- Backup: MIT OCW 6.042J — https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/
- Reference: Rosen — Ch 1 (logic), 2 & 9 (sets, relations), 6 & 8 (counting, recurrences, GFs), 10 (graphs)

---

## Daily Quota Cheat Sheet

| Slot | PYQ target | Lecture time |
|------|------------|--------------|
| Mon–Fri AM | 10–15 PYQs (C output tracing: 10 is fine) + redos | — |
| Mon–Fri PM | 0 | 60–70 min lecture + 20 min notes |
| Sat 09:00–11:00 | 20–30 odd-year PYQs, timed | — |
| Sat 11:00–12:00 | 20–25 GA questions | — |

---

## Phase-1 Exit Criteria

Before moving to Phase 2 (Mon 2026-11-23), confirm:

- [ ] PD-1 … PD-14 and DM-1 … DM-10 at confidence ≥3 in `trackers/subjects.md`
- [ ] PYQ accuracy ≥60% in C, DS and DM separately
- [ ] Can trace a static-variable + pointer-aliasing C program on paper without running it
- [ ] Can compute tree / heap node-count relationships and array addresses without looking up formulas
- [ ] Can count relations / functions / onto functions and solve a linear recurrence without notes
- [ ] Formula sheet for PDS complete; DM section started
- [ ] Error-log redo success ≥70%
- [ ] Adherence ≥70%

If any of these are "no", **extend Phase 1 by 1 week** (the extension comes out of Phase 5). Don't bluff your way into Algorithms — it's built on exactly these.
