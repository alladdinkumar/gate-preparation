# Theory Curriculum — Theory of Computation, Compiler Design

Sections 6 and 7 of the syllabus. **~11–17 marks per paper combined.** Both are pure theory with no day-job overlap, but the question banks are very repetitive. TOC is "identify the language class" and "count DFA states". CD is "parse table conflicts" and "liveness / constant propagation on a CFG". Accuracy here can reach 85%+ with enough PYQ repetition.

**Time budget:** TOC (Weeks 42–46), Compiler Design (Weeks 47–49) = 8 weeks, ~152h. Revision: Weeks 59–60.

Compiler Design is last on purpose: lexical analysis needs regular languages, and parsing needs CFGs — both from TOC the weeks before.

---

## Theory of Computation (Weeks 42–46)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| TC-1 | Finite automata — DFA, NFA, ε-NFA, subset construction, DFA minimisation, product construction, counting minimum states | 42 | `notes/toc/tc-01-finite-automata.md` | finite-automata, minimal-state-automata |
| TC-2 | Regular expressions — RE ↔ FA conversion, identities, equivalence of REs, describing languages | 42 | `notes/toc/tc-02-regular-expressions.md` | regular-expression |
| TC-3 | Regular languages — closure properties (union, intersection, complement, reversal, homomorphism, quotient), pumping lemma, Myhill–Nerode intuition, is-this-language-regular | 43 | `notes/toc/tc-03-regular-languages.md` | regular-language, pumping-lemma |
| TC-4 | Context-free grammars — derivations, parse trees, ambiguity, simplification (useless / ε / unit productions), CNF, GNF | 44 | `notes/toc/tc-04-cfg.md` | context-free-grammar |
| TC-5 | Push-down automata — acceptance by final state / empty stack, DPDA vs NPDA, CFG ↔ PDA | 44 | `notes/toc/tc-05-pda.md` | pushdown-automata |
| TC-6 | Context-free languages — closure properties, pumping lemma for CFLs, DCFL properties, is-this-language-CFL | 45 | `notes/toc/tc-06-context-free-languages.md` | context-free-language |
| TC-7 | Turing machines — variants, recursive vs recursively enumerable languages, closure properties, Chomsky hierarchy | 46 | `notes/toc/tc-07-turing-machines.md` | turing-machine, recursive-and-recursively-enumerable-languages |
| TC-8 | Decidability — decidable / undecidable problems table for each language class, halting problem, Rice's theorem, reductions | 46 | `notes/toc/tc-08-decidability.md` | decidability |

**GATE-favourite question types:**
- Minimum number of states in a DFA for a language (NAT)
- Which of these languages are regular / CFL / not CFL (MSQ) — the most repeated TOC question type
- Is RE1 ≡ RE2? Which string is not in L(RE)?
- Closure: "L1 regular, L2 CFL — what is L1 ∩ L2?"
- Decidability table: "Is emptiness decidable for CFLs? Is equivalence decidable for DCFLs?"
- Rice's theorem applications (MSQ)

**Keep a one-page table** in `notes/formula-sheets/toc.md`: closure properties × language class, decidability × language class. It answers ~30% of TOC questions on its own.

---

## Compiler Design (Weeks 47–49)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| CD-1 | Phases of a compiler, symbol table, lexical analysis — tokens, lexemes, counting tokens in C code, lexical errors | 47 | `notes/compiler/cd-01-lexical-analysis.md` | lexical-analysis |
| CD-2 | Top-down parsing — left recursion + left factoring removal, FIRST and FOLLOW, LL(1) table + conflicts, recursive descent | 47 | `notes/compiler/cd-02-top-down-parsing.md` | parsing, first-and-follow, ll-parser |
| CD-3 | Bottom-up parsing — handles, shift-reduce, LR(0) items, SLR(1), CLR(1), LALR(1) (state counts, conflicts, power hierarchy), operator precedence parsing | 48 | `notes/compiler/cd-03-bottom-up-parsing.md` | lr-parser, slr-parser, lalr-parser |
| CD-4 | Syntax-directed translation — synthesised vs inherited attributes, S-attributed vs L-attributed, evaluating SDT output on a parse tree | 48 | `notes/compiler/cd-04-sdt.md` | syntax-directed-translation |
| CD-5 | Runtime environments — activation records, stack allocation, static vs dynamic scoping, access links, parameter passing, heap management | 49 | `notes/compiler/cd-05-runtime-environments.md` | runtime-environment |
| CD-6 | Intermediate code generation — three-address code, quadruples/triples, DAG for expressions, SSA basics, counting temporaries | 49 | `notes/compiler/cd-06-intermediate-code.md` | intermediate-code |
| CD-7 | Local optimisation — basic blocks, control-flow graph, DAG-based optimisation, constant folding, dead code, peephole | 49 | `notes/compiler/cd-07-local-optimisation.md` | code-optimization |
| CD-8 | Data flow analyses — constant propagation, liveness analysis (live variables at a point), common subexpression elimination (available expressions) | 49 | `notes/compiler/cd-08-data-flow-analysis.md` | live-variable, data-flow-analysis |

**GATE-favourite question types:**
- Number of tokens in a C snippet (NAT)
- Which grammar is LL(1) / SLR(1) / LALR(1)? Number of states / conflicts (MSQ, NAT)
- FIRST / FOLLOW set of a nonterminal
- Output printed by an SDT on an input string
- Minimum number of nodes/edges in a DAG, or minimum temporaries in 3AC (NAT)
- Live variables at the exit of a block; constant value after propagation

---

## Formula / Fact Sheets

- End of Week 46: `notes/formula-sheets/toc.md` — closure table, decidability table, pumping lemma templates, standard non-regular / non-CFL languages
- End of Week 49: `notes/formula-sheets/compiler.md` — parser power hierarchy, FIRST/FOLLOW procedure, LR item rules, data-flow equations

---

## Tracking

`trackers/subjects.md` rows TC-1 … TC-8, CD-1 … CD-8.
