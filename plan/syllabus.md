# GATE CS Syllabus — Official Text + Study Map

**Source:** GATE 2027 CS syllabus PDF, IIT Madras (organising institute) — https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/CS_GATE2027_Syllabus.pdf
**GA syllabus:** https://gate2027.iitm.ac.in/static/doc/GATE2027_Syllabus/GA_GATE2027_Syllabus.pdf

> **Re-check when the GATE 2028 brochure is released (~Jul/Aug 2027).** Syllabus changes are rare but real (CS was trimmed in 2021 and CN was reworded later). If anything changes, the coach updates this file and `trackers/subjects.md` in that month's review.

---

## Paper Structure

| Section | Marks |
|---------|-------|
| General Aptitude (GA) | 15 |
| Engineering Mathematics + CS subjects | 85 |
| **Total** | **100** (65 questions, 3 hours) |

Engineering Mathematics is typically ~13 of the 85. Full pattern and marking scheme: `exam-info.md`.

---

## Official Syllabus (verbatim) → Study Map

Each section below: official text first, then the topic breakdown used in `trackers/subjects.md`, with the first-pass week.

### General Aptitude (common to all papers)

**Official — Verbal Aptitude:** Basic English grammar: tenses, articles, adjectives, prepositions, conjunctions, verb-noun agreement, and other parts of speech. Basic vocabulary: words, idioms, and phrases in context. Reading and comprehension, Narrative sequencing.

**Official — Quantitative Aptitude:** Data interpretation: data graphs (bar graphs, pie charts, and other graphs representing data), 2-and 3-dimensional plots, maps, and tables. Numerical computation and estimation: ratios, percentages, powers, exponents and logarithms, permutations and combinations, and series. Mensuration and geometry, Elementary statistics and probability.

**Official — Analytical Aptitude:** Logic: deduction and induction, Analogy, Numerical relations and reasoning.

**Official — Spatial Aptitude:** Transformation of shapes: translation, rotation, scaling, mirroring, assembling, and grouping paper folding, cutting, and patterns in 2 and 3 dimensions.

| # | Topic | When |
|---|-------|------|
| GA-1 | Grammar (tenses, articles, adjectives, prepositions, conjunctions, verb-noun agreement) | Sat rotation, all phases |
| GA-2 | Vocabulary, idioms, phrases in context | Sat rotation |
| GA-3 | Reading comprehension, narrative sequencing | Sat rotation |
| GA-4 | Numerical computation + estimation: ratios, percentages, powers, exponents, logs, series | Sat rotation |
| GA-5 | Data interpretation (bar, pie, 2D/3D plots, maps, tables) | Sat rotation |
| GA-6 | Mensuration, geometry | Sat rotation |
| GA-7 | Elementary statistics + probability, permutations | Sat rotation |
| GA-8 | Logic: deduction, induction, analogy, numerical relations | Sat rotation |
| GA-9 | Spatial: transformations, paper folding / cutting, 2D/3D patterns | Sat rotation |

---

### Section 1: Engineering Mathematics

**Official — Discrete Mathematics:** Propositional and first order logic. Sets, relations, functions, partial orders and lattices. Monoids, Groups. Graphs: connectivity, matching, colouring. Combinatorics: counting, recurrence relations, generating functions.

| # | Topic | Week |
|---|-------|------|
| DM-1 | Propositional logic (connectives, tautology, equivalence, normal forms, inference) | 7 |
| DM-2 | First order logic (quantifiers, nested quantifiers, translation, validity) | 7 |
| DM-3 | Sets, relations (properties, closures, equivalence relations) | 8 |
| DM-4 | Functions (injective/surjective/bijective, counting functions) | 8 |
| DM-5 | Partial orders, Hasse diagrams, lattices | 8 |
| DM-6 | Monoids, groups (subgroups, cyclic groups, Lagrange) | 9 |
| DM-7 | Counting: PnC, pigeonhole, inclusion–exclusion | 9 |
| DM-8 | Recurrence relations | 10 |
| DM-9 | Generating functions | 10 |
| DM-10 | Graphs: connectivity, matching, colouring (+ degree, Euler/Hamilton, planarity basics) | 10 |

**Official — Linear Algebra:** Matrices, determinants, system of linear equations, eigenvalues and eigenvectors, LU decomposition.

| # | Topic | Week |
|---|-------|------|
| LA-1 | Matrices, rank, special matrices | 15 |
| LA-2 | Determinants | 15 |
| LA-3 | System of linear equations (consistency, rank method) | 15 |
| LA-4 | Eigenvalues and eigenvectors (properties, Cayley–Hamilton) | 15 |
| LA-5 | LU decomposition | 15 |

**Official — Calculus:** Limits, continuity and differentiability, Maxima and minima, Mean value theorem, Integration.

| # | Topic | Week |
|---|-------|------|
| CA-1 | Limits (L'Hôpital, standard limits) | 16 |
| CA-2 | Continuity and differentiability | 16 |
| CA-3 | Maxima and minima | 16 |
| CA-4 | Mean value theorems (Rolle, Lagrange) | 16 |
| CA-5 | Integration (definite integrals, properties) | 16 |

**Official — Probability and Statistics:** Random variables, Uniform, normal, exponential, Poisson and binomial distributions. Mean, median, mode and standard deviation. Conditional probability and Bayes theorem.

| # | Topic | Week |
|---|-------|------|
| PS-1 | Basic probability, conditional probability, Bayes theorem | 17 |
| PS-2 | Random variables, expectation, variance | 17 |
| PS-3 | Mean, median, mode, standard deviation | 17 |
| PS-4 | Discrete distributions: binomial, Poisson | 18 |
| PS-5 | Continuous distributions: uniform, normal, exponential | 18 |

---

### Section 2: Digital Logic

**Official:** Boolean algebra and minimization – algebraic technique, Karnaugh map, tabular method. Design of combinational and sequential circuits. Number representation and arithmetic (fixed and floating point).

| # | Topic | Week |
|---|-------|------|
| DL-1 | Number systems, conversions, complements | 19 |
| DL-2 | Fixed point representation + arithmetic, overflow | 19 |
| DL-3 | Floating point (IEEE 754) | 19 |
| DL-4 | Boolean algebra, algebraic minimization, SOP/POS, duality | 19 |
| DL-5 | Karnaugh maps (incl. don't-cares), tabular (Quine–McCluskey) method | 20 |
| DL-6 | Combinational circuits: adders, subtractors, MUX, decoders, encoders, comparators | 20 |
| DL-7 | Sequential circuits: latches, flip-flops, conversions, timing | 21 |
| DL-8 | Counters (sync/async, mod-N), shift registers, FSM design | 22 |

---

### Section 3: Computer Organization and Architecture

**Official:** Instruction set and addressing modes. Design of arithmetic and logic unit (ALU). Design of control unit – hardwired and microprogrammed. Memory interfacing and hierarchy: performance, cache memory mapping. I/O interface (interrupt and DMA). Instruction pipelining, pipeline hazards.

| # | Topic | Week |
|---|-------|------|
| CO-1 | Instruction set, instruction formats, expanding opcodes | 23 |
| CO-2 | Addressing modes | 23 |
| CO-3 | ALU design, computer arithmetic (Booth's, fast adders) | 24 |
| CO-4 | Control unit: hardwired vs microprogrammed | 24 |
| CO-5 | Memory hierarchy, performance (AMAT), memory interfacing | 25 |
| CO-6 | Cache memory mapping (direct, set-associative, fully associative), replacement, write policies | 25 |
| CO-7 | Secondary storage (disk performance) | 26 |
| CO-8 | I/O interface: interrupts, DMA | 26 |
| CO-9 | Instruction pipelining (speedup, throughput) | 27 |
| CO-10 | Pipeline hazards (data, control, structural), stalls, branch penalty | 27 |

---

### Section 4: Programming and Data Structures

**Official:** Programming in C. Recursion. Arrays, stacks, queues, linked lists, trees, binary search trees, binary heaps, graphs.

| # | Topic | Week |
|---|-------|------|
| PD-1 | C basics: data types, operators, precedence/associativity, control flow | 1 |
| PD-2 | Functions, storage classes, scope (static/dynamic scoping), parameter passing | 1 |
| PD-3 | Pointers, pointer arithmetic, arrays and pointers | 2 |
| PD-4 | Strings, 2D arrays, arrays of pointers | 2 |
| PD-5 | Recursion (tracing, recurrence of calls) | 3 |
| PD-6 | Structures, unions, dynamic memory, function pointers | 3 |
| PD-7 | Arrays (row/column major addressing) | 4 |
| PD-8 | Stacks (applications: infix/postfix/prefix, evaluation) | 4 |
| PD-9 | Queues (circular, deque, queue via stacks) | 4 |
| PD-10 | Linked lists (singly, doubly, circular) | 5 |
| PD-11 | Trees: binary tree properties, traversals, construction | 5 |
| PD-12 | Binary search trees (+ AVL basics) | 5 |
| PD-13 | Binary heaps (build-heap, heapify, operations) | 6 |
| PD-14 | Graphs: representation, BFS/DFS basics | 6 |

---

### Section 5: Algorithms

**Official:** Searching, sorting, hashing. Asymptotic worst case time and space complexity. Algorithm design techniques: greedy, dynamic programming and divide‐and‐conquer. Graph traversals, minimum spanning trees, shortest paths.

| # | Topic | Week |
|---|-------|------|
| AL-1 | Asymptotic notation, comparing functions, time/space of code | 11 |
| AL-2 | Recurrences: substitution, recursion tree, master theorem | 11 |
| AL-3 | Searching, sorting (comparison sorts, lower bound, counting/radix) | 12 |
| AL-4 | Hashing (chaining, open addressing, probing) | 12 |
| AL-5 | Divide and conquer (merge sort, quick sort, binary search, matrix mult.) | 12 |
| AL-6 | Greedy (activity selection, Huffman, fractional knapsack, job sequencing) | 13 |
| AL-7 | Graph traversals: BFS, DFS, topological sort, connected/strongly connected components | 13 |
| AL-8 | Minimum spanning trees (Kruskal, Prim) | 13 |
| AL-9 | Shortest paths (Dijkstra, Bellman–Ford, Floyd–Warshall) | 14 |
| AL-10 | Dynamic programming (LCS, 0/1 knapsack, MCM, subset sum, OBST) | 14 |

---

### Section 6: Theory of Computation

**Official:** Regular expressions and finite automata. Context-free grammars and push-down automata. Regular and context-free languages, pumping lemma. Turing machines and undecidability.

| # | Topic | Week |
|---|-------|------|
| TC-1 | Finite automata: DFA, NFA, ε-NFA, conversions, minimization | 42 |
| TC-2 | Regular expressions, RE ↔ FA | 42 |
| TC-3 | Regular languages: closure properties, pumping lemma, identifying regularity | 43 |
| TC-4 | Context-free grammars, ambiguity, simplification, normal forms | 44 |
| TC-5 | Push-down automata (DPDA vs NPDA) | 44 |
| TC-6 | Context-free languages: closure, pumping lemma, DCFL | 45 |
| TC-7 | Turing machines, recursive vs recursively enumerable languages | 46 |
| TC-8 | Decidability, undecidability, Rice's theorem, reductions | 46 |

---

### Section 7: Compiler Design

**Official:** Lexical analysis, parsing, syntax-directed translation. Runtime environments. Intermediate code generation. Local optimisation, Data flow analyses: constant propagation, liveness analysis, common sub expression elimination.

| # | Topic | Week |
|---|-------|------|
| CD-1 | Phases of a compiler, lexical analysis (tokens, counting tokens) | 47 |
| CD-2 | Top-down parsing: FIRST/FOLLOW, LL(1), recursive descent | 47 |
| CD-3 | Bottom-up parsing: LR(0), SLR(1), LALR(1), CLR(1), operator precedence | 48 |
| CD-4 | Syntax-directed translation (S- and L-attributed) | 48 |
| CD-5 | Runtime environments (activation records, parameter passing, scoping) | 49 |
| CD-6 | Intermediate code generation (3-address code, quadruples, DAGs, SSA basics) | 49 |
| CD-7 | Local optimisation (basic blocks, DAG-based, peephole) | 49 |
| CD-8 | Data flow analyses: constant propagation, liveness, common subexpression elimination | 49 |

---

### Section 8: Operating System

**Official:** System calls, processes, threads, inter‐process communication, concurrency and synchronization. Deadlock. CPU and I/O scheduling. Memory management and virtual memory. File systems.

| # | Topic | Week |
|---|-------|------|
| OS-1 | System calls, processes, fork() counting, process states | 28 |
| OS-2 | Threads (user vs kernel, models) | 28 |
| OS-3 | CPU scheduling (FCFS, SJF, SRTF, RR, priority, multilevel) | 28 |
| OS-4 | Inter-process communication | 29 |
| OS-5 | Concurrency + synchronization: critical section, Peterson, semaphores, monitors, classic problems | 29 |
| OS-6 | Deadlock: conditions, prevention, avoidance (Banker's), detection | 30 |
| OS-7 | I/O and disk scheduling (FCFS, SSTF, SCAN, C-SCAN, LOOK) | 30 |
| OS-8 | Memory management: contiguous allocation, paging, segmentation, multi-level page tables, TLB | 31 |
| OS-9 | Virtual memory: demand paging, page replacement, Belady, thrashing, working set | 32 |
| OS-10 | File systems: allocation methods, inodes, directory structure, free-space | 32 |

---

### Section 9: Databases

**Official:** ER‐model. Relational model: relational algebra, tuple calculus, SQL. Integrity constraints, normal forms. File organization, indexing (e.g., B and B+ trees). Transactions and concurrency control.

| # | Topic | Week |
|---|-------|------|
| DB-1 | ER model (entities, relationships, cardinality, ER → tables) | 33 |
| DB-2 | Relational model, keys, integrity constraints | 33 |
| DB-3 | Relational algebra | 33 |
| DB-4 | Tuple relational calculus | 33 |
| DB-5 | SQL (joins, nested/correlated queries, aggregates, NULL semantics) | 34 |
| DB-6 | Functional dependencies, closures, candidate keys | 34 |
| DB-7 | Normal forms (1NF–BCNF), lossless join, dependency preservation | 34 |
| DB-8 | File organization, indexing (primary, clustered, secondary) | 35 |
| DB-9 | B trees and B+ trees (order, insertion, node counts) | 35 |
| DB-10 | Transactions: ACID, schedules, conflict/view serializability, recoverability | 36 |
| DB-11 | Concurrency control: 2PL variants, timestamp ordering, deadlock handling | 36 |

---

### Section 10: Computer Networks

**Official:** Principles of Layering; Basics of switching (circuit, packet and virtual circuit) and performance metrics; Data link layer: error detection, Medium Access Control, Ethernet; Distance vector and link state routing; IPv4 - Fragmentation, CIDR Notation, Network Address Translation; TCP- flow control and congestion control, socket API; DNS and HTTP.

| # | Topic | Week |
|---|-------|------|
| CN-1 | Principles of layering (OSI, TCP/IP) | 37 |
| CN-2 | Switching (circuit, packet, virtual circuit) + performance metrics (delays, throughput, utilisation) | 37 |
| CN-3 | Data link: framing, error detection (parity, CRC, checksum, Hamming) | 38 |
| CN-4 | Sliding window flow control (stop-and-wait, GBN, SR) — foundation for TCP | 38 |
| CN-5 | Medium Access Control (ALOHA, CSMA/CD, token passing), Ethernet | 39 |
| CN-6 | IPv4 addressing, CIDR, subnetting, supernetting | 40 |
| CN-7 | IPv4 fragmentation, NAT | 40 |
| CN-8 | Routing: distance vector, link state | 40 |
| CN-9 | TCP: connection management, flow control, congestion control; UDP | 41 |
| CN-10 | Socket API | 41 |
| CN-11 | DNS and HTTP | 41 |

---

## Coverage Rule

Every row ID above (GA-1 … CN-11) has a matching row in `trackers/subjects.md` (GA rows live in `trackers/aptitude.md`). If the syllabus changes, both files change together.
