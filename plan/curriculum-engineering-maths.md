# Engineering Mathematics Curriculum — Discrete Maths, Linear Algebra, Calculus, Probability

Section 1 of the syllabus. **~10–13 marks per paper**, and Discrete Maths quietly powers Algorithms, TOC, DBMS and Compiler Design. This is the highest-leverage block for someone 5 years out of college: the concepts are finite, the question styles repeat, and accuracy can reach 85%+.

**Time budget:** 8 weeks in first pass (Weeks 7–10, 15–18) = ~152h. Revision: Weeks 52–53.

**Primary resources:** GO Classes Discrete Mathematics + Linear Algebra playlists, GO Classes free Engineering Mathematics course (Calculus, Probability). Links in `resources.md`.

---

## Discrete Mathematics (Weeks 7–10)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| DM-1 | Propositional logic — connectives, truth tables, tautology/contradiction, logical equivalence, CNF/DNF, rules of inference | 7 | `notes/maths/dm-01-propositional-logic.md` | propositional-logic |
| DM-2 | First order logic — predicates, quantifiers, nested quantifiers, English ↔ FOL translation, validity | 7 | `notes/maths/dm-02-first-order-logic.md` | first-order-logic |
| DM-3 | Sets, relations — properties (reflexive, symmetric, antisymmetric, transitive), closures, equivalence relations + classes, counting relations | 8 | `notes/maths/dm-03-sets-relations.md` | set-theory, relations |
| DM-4 | Functions — one-one, onto, bijection, composition, inverse, counting functions | 8 | `notes/maths/dm-04-functions.md` | functions |
| DM-5 | Partial orders, Hasse diagrams, lattices (bounded, complemented, distributive) | 8 | `notes/maths/dm-05-posets-lattices.md` | partial-order, lattice |
| DM-6 | Algebraic structures — semigroup, monoid, group, abelian, subgroups, cyclic groups, order, Lagrange's theorem | 9 | `notes/maths/dm-06-groups.md` | group-theory |
| DM-7 | Counting — sum/product rule, PnC, with repetition, pigeonhole, inclusion–exclusion, derangements | 9 | `notes/maths/dm-07-counting.md` | combinatory, pigeonhole-principle |
| DM-8 | Recurrence relations — homogeneous / non-homogeneous linear recurrences, solving | 10 | `notes/maths/dm-08-recurrences.md` | recurrence-relation |
| DM-9 | Generating functions — ordinary GFs, coefficient extraction, counting with GFs | 10 | `notes/maths/dm-09-generating-functions.md` | generating-functions |
| DM-10 | Graph theory — degree sequence, connectivity, cut vertices/edges, Euler/Hamilton, bipartite, matching, vertex/edge colouring, chromatic number, planarity basics | 10 | `notes/maths/dm-10-graph-theory.md` | graph-connectivity, graph-matching, graph-coloring |

**GATE-favourite question types** (rehearse these patterns, not just the theory):
- "Which of the following is a tautology / logically equivalent?" — MSQ, easy to lose on one option
- English sentence → FOL: "Not every student who passes is happy"
- Count reflexive / symmetric / antisymmetric relations on an n-element set (NAT)
- Is this POSET a lattice? Is it complemented / distributive?
- Order of an element, number of generators of a cyclic group
- Number of onto functions, derangements, integer solutions with constraints (NAT)
- Solve a recurrence / find the coefficient of x^k in a GF (NAT)
- Chromatic number, max matching, number of edges given degree constraints

**Common traps:** vacuous truth in implications; "only if" direction; antisymmetric ≠ not symmetric; counting functions vs relations; forgetting the empty relation.

---

## Linear Algebra (Week 15)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| LA-1 | Matrices — types, rank, row echelon form, inverse | 15 | `notes/maths/la-01-matrices-rank.md` | rank-of-matrix |
| LA-2 | Determinants — properties, cofactor expansion, special matrices | 15 | `notes/maths/la-02-determinants.md` | determinant |
| LA-3 | System of linear equations — consistency, unique / infinite / no solution, rank method | 15 | `notes/maths/la-03-linear-systems.md` | system-of-equations |
| LA-4 | Eigenvalues and eigenvectors — characteristic equation, properties (trace, det, powers, inverse), Cayley–Hamilton, diagonalisability | 15 | `notes/maths/la-04-eigen.md` | eigen-value |
| LA-5 | LU decomposition | 15 | `notes/maths/la-05-lu-decomposition.md` | lu-decomposition |

**GATE-favourite question types:**
- Eigenvalues of a special matrix without full computation (triangular, rank-1, A², A⁻¹)
- Rank of a structured matrix (NAT)
- For what value of k does the system have infinite solutions?
- Determinant / eigen properties combined in an MSQ

---

## Calculus (Week 16)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| CA-1 | Limits — standard limits, L'Hôpital's rule, indeterminate forms | 16 | `notes/maths/ca-01-limits.md` | limits |
| CA-2 | Continuity and differentiability — piecewise functions, absolute-value style functions | 16 | `notes/maths/ca-02-continuity-differentiability.md` | continuity, differentiation |
| CA-3 | Maxima and minima — first/second derivative tests, on closed intervals | 16 | `notes/maths/ca-03-maxima-minima.md` | maxima-minima |
| CA-4 | Mean value theorems — Rolle's, Lagrange's | 16 | `notes/maths/ca-04-mean-value-theorem.md` | mean-value-theorem |
| CA-5 | Integration — definite integrals, properties, substitution, by parts | 16 | `notes/maths/ca-05-integration.md` | integration |

**GATE-favourite question types:** limit evaluation (NAT), differentiability at a point of a piecewise function, maximum value on an interval, definite integral with symmetry tricks.

---

## Probability & Statistics (Weeks 17–18)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| PS-1 | Probability basics, conditional probability, independence, total probability, Bayes theorem | 17 | `notes/maths/ps-01-conditional-bayes.md` | conditional-probability, bayes-theorem |
| PS-2 | Random variables — PMF/PDF/CDF, expectation, variance, linearity of expectation | 17 | `notes/maths/ps-02-random-variables.md` | random-variable, expectation |
| PS-3 | Descriptive statistics — mean, median, mode, standard deviation | 17 | `notes/maths/ps-03-descriptive-stats.md` | statistics |
| PS-4 | Discrete distributions — binomial, Poisson (mean, variance, when to use) | 18 | `notes/maths/ps-04-binomial-poisson.md` | binomial-distribution, poisson-distribution |
| PS-5 | Continuous distributions — uniform, normal (standardisation), exponential (memoryless) | 18 | `notes/maths/ps-05-continuous-distributions.md` | uniform-distribution, normal-distribution, exponential-distribution |

**GATE-favourite question types:** Bayes with a medical-test / defective-item setup, expected number of trials, expectation via linearity (indicator variables), memoryless property, variance of a sum.

---

## Formula Sheet

By end of Week 18: `notes/formula-sheets/engineering-maths.md` — one page each for DM counting formulas, LA properties, calculus standard results, distribution table (PMF/PDF, mean, variance). Revised again in Week 53 and Phase 7.

---

## Tracking

`trackers/subjects.md` has one row per topic ID above (DM-1 … PS-5), with lecture done / short notes / PYQs attempted / correct / accuracy / confidence / last revisited. Spaced repetition: any topic not revisited in 21+ days is flagged in `trackers/revision.md`.
