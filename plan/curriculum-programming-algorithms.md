# Programming, Data Structures & Algorithms Curriculum

Sections 4 and 5 of the syllabus. **~15–19 marks per paper combined** — the single largest CS block. You write code for a living, which helps less than you'd think: GATE C questions are about *tracing* tricky code by hand (pointer aliasing, static variables, precedence, recursion), not writing clean code.

**Time budget:** C (Weeks 1–3), Data Structures (Weeks 4–6), Algorithms (Weeks 11–14) = 10 weeks, ~190h. Revision: Weeks 50–51.

**Language:** C only. Every example in notes is C. No C++ STL, no Python — GATE code is C.

---

## Programming in C (Weeks 1–3)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| PD-1 | Data types, sizes, integer promotion, operators, precedence & associativity, short-circuit, side effects, control flow (switch fall-through, loops) | 1 | `notes/programming-ds/c-01-operators-control-flow.md` | programming-in-c |
| PD-2 | Functions, call stack, storage classes (auto, static, extern, register), scope, static vs dynamic scoping, parameter passing (value, reference via pointers; call-by-name/need as concepts) | 1 | `notes/programming-ds/c-02-functions-storage-scope.md` | parameter-passing, static |
| PD-3 | Pointers — declaration, dereferencing, pointer arithmetic, pointer to pointer, arrays vs pointers, `const` with pointers | 2 | `notes/programming-ds/c-03-pointers.md` | pointers |
| PD-4 | Strings (char arrays, string literals, library behaviour), 2D arrays, arrays of pointers vs pointer to array, complex declarations | 2 | `notes/programming-ds/c-04-strings-2d-arrays.md` | strings, array |
| PD-5 | Recursion — tracing, output prediction, number of calls, recursion → recurrence | 3 | `notes/programming-ds/c-05-recursion.md` | recursion |
| PD-6 | Structures, unions, self-referential structs, `malloc`/`free`, dangling pointers, memory leaks, function pointers | 3 | `notes/programming-ds/c-06-structs-dynamic-memory.md` | structure, malloc |

**GATE-favourite question types:**
- "What is the output of this program?" with static locals, pointer aliasing, or `++` side effects (NAT)
- Static vs dynamic scoping output for the same program
- Recursive function — value returned / number of calls for input n (NAT)
- Complex pointer/array declarations — what does `*p[3]` vs `(*p)[3]` mean
- `sizeof` on arrays vs pointers passed to functions

**Common traps:** `sizeof` of an array parameter; undefined behaviour options (GATE sometimes marks "compiler dependent"); integer division; `char` overflow; string literal modification.

---

## Data Structures (Weeks 4–6)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| PD-7 | Arrays — row-major / column-major address calculation, lower/upper triangular storage | 4 | `notes/programming-ds/ds-01-arrays.md` | array |
| PD-8 | Stacks — implementation, infix ↔ postfix/prefix conversion, evaluation, stack permutations | 4 | `notes/programming-ds/ds-02-stacks.md` | stack |
| PD-9 | Queues — circular queue conditions, deque, priority queue idea, queue using stacks and vice versa | 4 | `notes/programming-ds/ds-03-queues.md` | queue |
| PD-10 | Linked lists — singly, doubly, circular; insertion/deletion/reversal code tracing | 5 | `notes/programming-ds/ds-04-linked-lists.md` | linked-list |
| PD-11 | Binary trees — properties (nodes/leaves/height), traversals, construct tree from traversals, counting trees | 5 | `notes/programming-ds/ds-05-binary-trees.md` | binary-tree |
| PD-12 | BST — insert/delete/search, traversal properties, number of BSTs; AVL rotations + height bounds | 5 | `notes/programming-ds/ds-06-bst-avl.md` | binary-search-tree, avl-tree |
| PD-13 | Binary heaps — array representation, heapify, build-heap O(n), insert/delete, k-th element questions | 6 | `notes/programming-ds/ds-07-heaps.md` | heap |
| PD-14 | Graphs — adjacency matrix/list, space/time trade-offs, BFS/DFS trees and edge types | 6 | `notes/programming-ds/ds-08-graphs.md` | graph-algorithms |

**GATE-favourite question types:**
- Address of A[i][j] in row/column major with a non-zero lower bound (NAT)
- Postfix evaluation / minimum stack size needed
- Number of nodes/leaves/height relationships in complete / full / AVL trees (NAT)
- Heap after a sequence of inserts/deletes — array contents
- Level-order / preorder of BST after insertions
- Linked-list code with a missing line — which option fixes it

---

## Algorithms (Weeks 11–14)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| AL-1 | Asymptotic notation (O, Ω, Θ, o, ω), comparing growth rates, time/space of loops | 11 | `notes/algorithms/al-01-asymptotic.md` | asymptotic-notation, time-complexity |
| AL-2 | Recurrences — substitution, recursion tree, master theorem (+ extended cases) | 11 | `notes/algorithms/al-02-recurrences.md` | recurrence-relation, master-theorem |
| AL-3 | Searching and sorting — binary search, insertion/selection/bubble, merge, quick (best/worst/average), heap sort, stability, in-place, comparison lower bound, counting/radix sort | 12 | `notes/algorithms/al-03-searching-sorting.md` | sorting, quick-sort, merge-sort |
| AL-4 | Hashing — hash functions, chaining, open addressing (linear/quadratic/double), load factor, expected probes | 12 | `notes/algorithms/al-04-hashing.md` | hashing |
| AL-5 | Divide and conquer — merge sort, quick sort, binary search, closest pair idea, Strassen, max-min | 12 | `notes/algorithms/al-05-divide-conquer.md` | divide-and-conquer |
| AL-6 | Greedy — activity selection, fractional knapsack, Huffman coding, job sequencing, optimal merge | 13 | `notes/algorithms/al-06-greedy.md` | greedy-algorithms, huffman-code |
| AL-7 | Graph traversals — BFS, DFS, discovery/finish times, topological sort, connected + strongly connected components | 13 | `notes/algorithms/al-07-graph-traversals.md` | dfs, bfs, topological-sort |
| AL-8 | Minimum spanning trees — Kruskal, Prim, cut property, uniqueness, MST weight questions | 13 | `notes/algorithms/al-08-mst.md` | minimum-spanning-tree |
| AL-9 | Shortest paths — Dijkstra (negative-edge failure), Bellman–Ford, Floyd–Warshall | 14 | `notes/algorithms/al-09-shortest-paths.md` | shortest-path, dijkstras-algorithm |
| AL-10 | Dynamic programming — LCS, 0/1 knapsack, matrix chain multiplication, subset sum, edit distance, OBST idea | 14 | `notes/algorithms/al-10-dynamic-programming.md` | dynamic-programming |

**GATE-favourite question types:**
- Time complexity of a nested / logarithmic loop (NAT with log terms)
- Solve T(n) — pick the Θ bound
- Number of swaps / comparisons for a sorting algorithm on a specific input (NAT)
- Expected probes / final hash table contents
- MST weight; which edges can / must be in every MST
- Dijkstra order of vertex finalisation; does it work with this negative edge?
- DP table value for a specific cell (LCS length, knapsack value — NAT)
- Huffman average code length (NAT)

**Common traps:** best vs worst case of quicksort depends on pivot rule stated; "stable" vs "in-place" MSQs; master theorem gap cases; DFS edge classification in undirected graphs.

---

## Formula / Fact Sheets

- End of Week 6: `notes/formula-sheets/programming-ds.md` — C precedence table, storage class behaviour, tree/heap node-count formulas
- End of Week 14: `notes/formula-sheets/algorithms.md` — complexity table (all sorts, graph algos, DP), master theorem cases

---

## Tracking

`trackers/subjects.md` rows PD-1 … PD-14 and AL-1 … AL-10. Accuracy <50% after 30 PYQs in a subject triggers the remediation block in `PLAN.md`.
