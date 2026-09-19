# Digital Logic & COA Curriculum

Sections 2 and 3 of the syllabus. **~13–18 marks per paper combined**, and COA has been trending up (12, 9, 8 marks in 2023–2025). These are numerical-heavy, formula-driven subjects with no day-job overlap — plan for them to feel slow at first. Accuracy climbs fast once the question patterns are familiar.

**Time budget:** Digital Logic (Weeks 19–22), COA (Weeks 23–27) = 9 weeks, ~171h. Revision: Weeks 54–55.

Digital Logic comes immediately before COA on purpose: number representation, adders and flip-flops are COA's vocabulary.

---

## Digital Logic (Weeks 19–22)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| DL-1 | Number systems — base conversion, 1's/2's complement, signed magnitude, BCD, Gray code | 19 | `notes/digital-logic/dl-01-number-systems.md` | number-representation |
| DL-2 | Fixed point representation — range, overflow detection, signed arithmetic | 19 | `notes/digital-logic/dl-02-fixed-point.md` | number-representation, overflow |
| DL-3 | Floating point — IEEE 754 single/double, bias, special values, normalised range, precision | 19 | `notes/digital-logic/dl-03-ieee754.md` | ieee-representation |
| DL-4 | Boolean algebra — laws, duality, SOP/POS, canonical forms, minterms/maxterms, algebraic minimisation, functionally complete sets, self-dual functions | 19 | `notes/digital-logic/dl-04-boolean-algebra.md` | boolean-algebra |
| DL-5 | K-maps (2–5 variables, don't-cares, prime/essential prime implicants) + tabular (Quine–McCluskey) method | 20 | `notes/digital-logic/dl-05-kmap-tabular.md` | k-map, min-sum-of-products-form |
| DL-6 | Combinational circuits — half/full adder, ripple-carry & carry-lookahead, subtractor, MUX (function implementation), decoder, encoder, comparator; gate delays | 20 | `notes/digital-logic/dl-06-combinational.md` | combinational-circuit, multiplexer |
| DL-7 | Sequential circuits — SR/JK/D/T latches & flip-flops, characteristic/excitation tables, conversions, race-around, setup/hold, max clock frequency | 21 | `notes/digital-logic/dl-07-flip-flops.md` | flip-flop, sequential-circuit |
| DL-8 | Counters (asynchronous/synchronous, mod-N, ring, Johnson), shift registers, FSM (Mealy/Moore) design, state minimisation | 22 | `notes/digital-logic/dl-08-counters-fsm.md` | counter, finite-state-machine |

**GATE-favourite question types:**
- Number of minterms / essential prime implicants for a function (NAT)
- IEEE 754 hex → decimal value, or smallest/largest representable
- Range of n-bit 2's complement; overflow in a given addition
- Implement f with a 4:1 MUX — which inputs
- Counter sequence / mod of a given circuit; state after k clock pulses
- Max clock frequency given gate/flip-flop delays (NAT)

---

## Computer Organization & Architecture (Weeks 23–27)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| CO-1 | Machine instructions — instruction formats, 0/1/2/3-address, expanding opcode technique, RISC vs CISC | 23 | `notes/coa/co-01-instruction-formats.md` | machine-instructions |
| CO-2 | Addressing modes — immediate, direct, indirect, register, indexed, relative, auto-inc/dec; effective address calculation | 23 | `notes/coa/co-02-addressing-modes.md` | addressing-modes |
| CO-3 | ALU design + computer arithmetic — adders, Booth's multiplication, restoring/non-restoring division, carry-lookahead delay | 24 | `notes/coa/co-03-alu-arithmetic.md` | booths-algorithm |
| CO-4 | Control unit — hardwired vs microprogrammed, horizontal vs vertical microprogramming, control word size | 24 | `notes/coa/co-04-control-unit.md` | microprogramming |
| CO-5 | Memory hierarchy — locality, AMAT (hierarchical vs simultaneous access), memory interfacing, chip/decoder sizing | 25 | `notes/coa/co-05-memory-hierarchy.md` | memory-interfacing |
| CO-6 | Cache — direct, set-associative, fully associative mapping; tag/index/offset bits; hit ratio; LRU/FIFO in cache; write-through vs write-back | 25 | `notes/coa/co-06-cache-mapping.md` | cache-memory |
| CO-7 | Secondary storage — disk geometry, seek/rotational latency, transfer time, capacity (NAT) | 26 | `notes/coa/co-07-disk.md` | disk |
| CO-8 | I/O interface — programmed I/O, interrupt-driven I/O (vectored, priority, daisy chaining), DMA, DMA transfer-rate calculations | 26 | `notes/coa/co-08-io-interrupts-dma.md` | interrupts, dma |
| CO-9 | Instruction pipelining — stage delays, latch delay, speedup, throughput, non-uniform stages | 27 | `notes/coa/co-09-pipelining.md` | pipelining |
| CO-10 | Pipeline hazards — data (forwarding), control (branch penalty, prediction), structural; stall counting with timing diagrams | 27 | `notes/coa/co-10-pipeline-hazards.md` | pipelining |

**GATE-favourite question types:**
- Tag / index / offset bits for a cache configuration (NAT)
- Number of cache misses for an access sequence (NAT)
- AMAT for a 2- or 3-level hierarchy (NAT)
- Pipeline speedup / time to execute N instructions with stalls (NAT)
- Effective address given the mode (NAT)
- Number of 2-address and 1-address instructions possible with expanding opcode (NAT)
- DMA: fraction of CPU time consumed / transfer rate

**Common traps:** hierarchical vs simultaneous AMAT formula; word vs byte addressing; counting the first instruction's time in pipelines; forgetting inter-stage latch delay.

---

## Formula Sheets

- End of Week 22: `notes/formula-sheets/digital-logic.md` — complement ranges, IEEE 754 layout + special values, flip-flop tables, counter formulas
- End of Week 27: `notes/formula-sheets/coa.md` — cache bit split, AMAT variants, disk time, pipeline formulas, DMA formulas

---

## Tracking

`trackers/subjects.md` rows DL-1 … DL-8 and CO-1 … CO-10.
