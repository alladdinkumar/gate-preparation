# Topic Lectures — three alternatives per topic

`resources.md` lists **one playlist per subject**. That is right for a first pass and useless
when a single concept refuses to land at 21:00 on a Wednesday. This file is the other axis:
for each of the 124 syllabus topics, a search phrase and **three teachers who cover it**, so
"I don't get pipelining hazards" has three answers instead of a 40-video playlist.

**How it is used.** The planner shows `topic-videos.md`'s named videos first; the searches
below are the fallback for when a video is taken down or turns out to be wrong. The tags and
note paths live in `curriculum-*.md`, the videos in `topic-videos.md`, the searches here —
nothing is typed twice.

> The search phrases in this file are also what `webapp/tools/build_videos.py` searches
> YouTube with. Improve a phrase here and re-run it for that topic to get better videos.

**Rules for editing:**
- The search phrase is the valuable part. Write it as you would type it into YouTube.
- Alternatives are *keys* from the Sources table, not URLs — so a channel that moves is fixed
  in one row, not 124.
- Keep three. A fourth is noise; the point is a short ladder, not a library.
- Primary (`go`) first. The backups are for one stuck concept, not for re-watching a subject.

> Channel URLs and course IDs below are the ones verified in `resources.md` (2026-09-13).
> Topic links are channel-scoped *searches*, so they follow a channel's re-uploads and
> re-orderings instead of breaking. If a search comes back thin, the subject playlist in
> `resources.md` is still the fallback.

---

## Sources

`{q}` is replaced by the topic's search phrase, URL-encoded.

| Key | Name | URL |
|-----|------|-----|
| go | GO Classes | https://www.youtube.com/@GOClassesforGATECS/search?query={q} |
| smashers | Gate Smashers | https://www.youtube.com/@GateSmashers/search?query={q} |
| neso | Neso Academy | https://www.youtube.com/channel/UCQYMhOMi_Cdj1CEAU-fv80A/search?query={q} |
| ravula | Ravindrababu Ravula | https://www.youtube.com/channel/UCJjC1hn78yZqTf0vdTC6wAQ/search?query={q} |
| bari | Abdul Bari | https://www.youtube.com/@abdul_bari/search?query={q} |
| yt | YouTube (GATE CS) | https://www.youtube.com/results?search_query=GATE+CS+{q} |
| goclasses-site | GO Classes free courses | https://www.goclasses.in/s/store/courses |
| nptel | NPTEL course catalogue | https://nptel.ac.in/courses |
| nptel-daa | NPTEL Design and Analysis of Algorithms (Mukund) | https://nptel.ac.in/courses/106106131 |
| nptel-coa | NPTEL Computer Architecture and Organization (Sengupta) | https://nptel.ac.in/courses/106105163 |
| nptel-os | NPTEL Introduction to Operating Systems (Rebeiro) | https://nptel.ac.in/courses/106106144 |
| nptel-dbms | NPTEL Database Management System (Das) | https://nptel.ac.in/courses/106105175 |
| nptel-cn | NPTEL Computer Networks and Internet Protocol | https://nptel.ac.in/courses/106105183 |
| nptel-toc | NPTEL Theory of Computation (Tewari) | https://onlinecourses.nptel.ac.in/noc21_cs83/preview |
| nptel-cd | NPTEL Compiler Design (Chattopadhyay) | https://nptel.ac.in/courses/106105190 |
| mit-la | MIT 18.06 Linear Algebra (Strang) | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ |
| mit-dm | MIT 6.042J Mathematics for CS | https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/ |
| mit-prob | MIT RES.6-012 Introduction to Probability (Tsitsiklis) | https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/ |
| 3b1b-calc | 3Blue1Brown Essence of Calculus | https://www.3blue1brown.com/topics/calculus |
| indiabix | IndiaBix drills | https://www.indiabix.com |

---

## Programming in C

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| PD-1 | C operators precedence associativity short circuit | go, smashers, yt |
| PD-2 | C storage classes static extern scope parameter passing | go, smashers, yt |
| PD-3 | C pointers pointer arithmetic arrays and pointers | go, smashers, yt |
| PD-4 | C strings 2D arrays array of pointers declarations | go, smashers, yt |
| PD-5 | C recursion output tracing number of function calls | go, smashers, bari |
| PD-6 | C structures unions malloc free function pointers | go, smashers, yt |

## Data Structures

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| PD-7 | row major column major array address calculation | go, smashers, yt |
| PD-8 | stack infix postfix prefix conversion evaluation | go, smashers, bari |
| PD-9 | circular queue deque queue using stacks | go, smashers, bari |
| PD-10 | linked list insertion deletion reversal code | go, smashers, bari |
| PD-11 | binary tree properties traversals construct from traversal | go, smashers, bari |
| PD-12 | binary search tree AVL tree rotations height | go, smashers, bari |
| PD-13 | binary heap heapify build heap complexity | go, smashers, bari |
| PD-14 | graph representation adjacency matrix list BFS DFS | go, smashers, bari |

## Algorithms

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| AL-1 | asymptotic notation big O omega theta growth rate | go, bari, nptel-daa |
| AL-2 | recurrence relation master theorem recursion tree | go, bari, nptel-daa |
| AL-3 | sorting algorithms comparison lower bound counting radix | go, bari, nptel-daa |
| AL-4 | hashing chaining open addressing linear probing | go, bari, nptel-daa |
| AL-5 | divide and conquer merge sort quick sort analysis | go, bari, nptel-daa |
| AL-6 | greedy algorithm Huffman coding fractional knapsack | go, bari, nptel-daa |
| AL-7 | BFS DFS topological sort strongly connected components | go, bari, nptel-daa |
| AL-8 | minimum spanning tree Kruskal Prim | go, bari, nptel-daa |
| AL-9 | shortest path Dijkstra Bellman Ford Floyd Warshall | go, bari, nptel-daa |
| AL-10 | dynamic programming LCS 0/1 knapsack matrix chain | go, bari, nptel-daa |

## Discrete Mathematics

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| DM-1 | propositional logic tautology equivalence CNF inference | go, smashers, mit-dm |
| DM-2 | first order logic quantifiers translation validity | go, smashers, mit-dm |
| DM-3 | sets relations reflexive symmetric transitive closure | go, smashers, mit-dm |
| DM-4 | functions injective surjective bijective counting | go, smashers, mit-dm |
| DM-5 | partial order Hasse diagram lattice | go, smashers, mit-dm |
| DM-6 | group theory subgroup cyclic group Lagrange theorem | go, smashers, mit-dm |
| DM-7 | permutations combinations pigeonhole inclusion exclusion | go, smashers, mit-dm |
| DM-8 | recurrence relation solving homogeneous particular | go, smashers, mit-dm |
| DM-9 | generating functions discrete mathematics | go, yt, mit-dm |
| DM-10 | graph theory connectivity matching colouring planarity | go, smashers, mit-dm |

## Linear Algebra

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| LA-1 | matrix rank special matrices properties | go, smashers, mit-la |
| LA-2 | determinant properties cofactor adjoint | go, smashers, mit-la |
| LA-3 | system of linear equations consistency rank method | go, smashers, mit-la |
| LA-4 | eigenvalues eigenvectors Cayley Hamilton theorem | go, smashers, mit-la |
| LA-5 | LU decomposition solved example | go, yt, mit-la |

## Calculus

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| CA-1 | limits L'Hopital rule standard limits | goclasses-site, smashers, 3b1b-calc |
| CA-2 | continuity and differentiability conditions | goclasses-site, smashers, 3b1b-calc |
| CA-3 | maxima minima first second derivative test | goclasses-site, smashers, 3b1b-calc |
| CA-4 | Rolle theorem Lagrange mean value theorem | goclasses-site, smashers, yt |
| CA-5 | definite integral properties evaluation | goclasses-site, smashers, 3b1b-calc |

## Probability & Statistics

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| PS-1 | conditional probability Bayes theorem | goclasses-site, smashers, mit-prob |
| PS-2 | random variable expectation variance | goclasses-site, smashers, mit-prob |
| PS-3 | mean median mode standard deviation | goclasses-site, smashers, mit-prob |
| PS-4 | binomial distribution Poisson distribution | goclasses-site, smashers, mit-prob |
| PS-5 | uniform normal exponential distribution | goclasses-site, smashers, mit-prob |

## Digital Logic

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| DL-1 | number system conversion 1s 2s complement Gray code | go, neso, smashers |
| DL-2 | fixed point representation range overflow detection | go, neso, smashers |
| DL-3 | IEEE 754 floating point representation bias | go, neso, smashers |
| DL-4 | Boolean algebra minimization SOP POS duality | go, neso, smashers |
| DL-5 | K map don't care Quine McCluskey tabular method | go, neso, smashers |
| DL-6 | combinational circuits multiplexer decoder encoder adder | go, neso, smashers |
| DL-7 | latches flip flops SR JK D T conversion timing | go, neso, smashers |
| DL-8 | counters synchronous asynchronous shift register FSM | go, neso, smashers |

## Computer Organisation & Architecture

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| CO-1 | instruction format expanding opcode instruction set | go, smashers, nptel-coa |
| CO-2 | addressing modes computer organization | go, smashers, nptel-coa |
| CO-3 | Booth algorithm multiplication ALU computer arithmetic | go, smashers, nptel-coa |
| CO-4 | hardwired vs microprogrammed control unit | go, smashers, nptel-coa |
| CO-5 | memory hierarchy average memory access time interfacing | go, smashers, nptel-coa |
| CO-6 | cache mapping direct set associative replacement write policy | go, smashers, nptel-coa |
| CO-7 | disk performance seek time rotational latency | go, smashers, nptel-coa |
| CO-8 | interrupts DMA input output interface | go, smashers, nptel-coa |
| CO-9 | instruction pipelining speedup throughput efficiency | go, smashers, nptel-coa |
| CO-10 | pipeline hazards data control structural branch penalty | go, smashers, nptel-coa |

## Operating Systems

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| OS-1 | fork system call counting processes process states | go, smashers, nptel-os |
| OS-2 | user level vs kernel level threads multithreading models | go, smashers, nptel-os |
| OS-3 | CPU scheduling FCFS SJF SRTF round robin Gantt | go, smashers, nptel-os |
| OS-4 | inter process communication shared memory message passing | go, smashers, nptel-os |
| OS-5 | critical section Peterson solution semaphore monitor | go, smashers, nptel-os |
| OS-6 | deadlock prevention avoidance banker algorithm detection | go, smashers, nptel-os |
| OS-7 | disk scheduling FCFS SSTF SCAN C-SCAN LOOK | go, smashers, nptel-os |
| OS-8 | paging segmentation multilevel page table TLB | go, smashers, nptel-os |
| OS-9 | demand paging page replacement Belady thrashing working set | go, smashers, nptel-os |
| OS-10 | file allocation methods inode directory structure free space | go, smashers, nptel-os |

## Databases

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| DB-1 | ER model cardinality ER diagram to relational table | go, smashers, nptel-dbms |
| DB-2 | relational model keys candidate key integrity constraints | go, smashers, nptel-dbms |
| DB-3 | relational algebra operators division | go, smashers, ravula |
| DB-4 | tuple relational calculus | go, ravula, nptel-dbms |
| DB-5 | SQL nested correlated query aggregate NULL semantics | go, smashers, nptel-dbms |
| DB-6 | functional dependency attribute closure candidate keys | go, smashers, ravula |
| DB-7 | normalization 1NF 2NF 3NF BCNF lossless dependency preserving | go, smashers, ravula |
| DB-8 | file organization indexing primary clustered secondary | go, smashers, nptel-dbms |
| DB-9 | B tree B+ tree order insertion number of nodes | go, smashers, nptel-dbms |
| DB-10 | ACID schedules conflict view serializability recoverability | go, smashers, ravula |
| DB-11 | two phase locking timestamp ordering concurrency control | go, smashers, ravula |

## Computer Networks

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| CN-1 | OSI model TCP IP layering | go, smashers, nptel-cn |
| CN-2 | circuit switching packet switching delay throughput | go, smashers, nptel-cn |
| CN-3 | framing CRC checksum Hamming code error detection | go, smashers, nptel-cn |
| CN-4 | stop and wait go back N selective repeat sliding window | go, smashers, nptel-cn |
| CN-5 | ALOHA CSMA CD token passing Ethernet | go, smashers, nptel-cn |
| CN-6 | IPv4 addressing CIDR subnetting supernetting | go, smashers, nptel-cn |
| CN-7 | IP fragmentation NAT | go, smashers, nptel-cn |
| CN-8 | distance vector link state routing algorithm | go, smashers, nptel-cn |
| CN-9 | TCP connection management flow control congestion control UDP | go, smashers, nptel-cn |
| CN-10 | socket programming API | go, yt, nptel-cn |
| CN-11 | DNS HTTP application layer | go, smashers, nptel-cn |

## Theory of Computation

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| TC-1 | DFA NFA epsilon NFA subset construction minimization | go, neso, ravula |
| TC-2 | regular expression to finite automata conversion | go, neso, ravula |
| TC-3 | regular language closure properties pumping lemma | go, neso, nptel-toc |
| TC-4 | context free grammar ambiguity CNF GNF simplification | go, neso, ravula |
| TC-5 | pushdown automata DPDA NPDA | go, neso, ravula |
| TC-6 | context free language closure pumping lemma DCFL | go, neso, nptel-toc |
| TC-7 | Turing machine recursive recursively enumerable languages | go, neso, nptel-toc |
| TC-8 | decidability undecidability Rice theorem reduction | go, neso, nptel-toc |

## Compiler Design

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| CD-1 | phases of compiler lexical analysis counting tokens | go, ravula, nptel-cd |
| CD-2 | FIRST FOLLOW LL(1) parsing table recursive descent | go, ravula, nptel-cd |
| CD-3 | LR(0) SLR(1) LALR(1) CLR(1) parsing operator precedence | go, ravula, nptel-cd |
| CD-4 | syntax directed translation S attributed L attributed | go, ravula, nptel-cd |
| CD-5 | runtime environment activation record scoping | go, ravula, nptel-cd |
| CD-6 | three address code quadruples DAG intermediate code | go, ravula, nptel-cd |
| CD-7 | basic blocks peephole local optimization | go, ravula, nptel-cd |
| CD-8 | data flow analysis liveness constant propagation common subexpression | go, ravula, nptel-cd |

## General Aptitude

| # | Search phrase | Alternatives |
|---|---------------|--------------|
| GA-1 | English grammar tenses articles prepositions subject verb agreement | yt, indiabix, smashers |
| GA-2 | vocabulary idioms phrases in context aptitude | yt, indiabix, smashers |
| GA-3 | reading comprehension narrative sequencing aptitude | yt, indiabix, smashers |
| GA-4 | ratio percentage exponents logarithms series aptitude | yt, indiabix, smashers |
| GA-5 | data interpretation bar graph pie chart tables | yt, indiabix, smashers |
| GA-6 | mensuration geometry aptitude | yt, indiabix, smashers |
| GA-7 | elementary statistics probability permutations aptitude | yt, indiabix, smashers |
| GA-8 | logical reasoning deduction induction analogy | yt, indiabix, smashers |
| GA-9 | spatial aptitude paper folding cutting 3D patterns | yt, indiabix, smashers |
