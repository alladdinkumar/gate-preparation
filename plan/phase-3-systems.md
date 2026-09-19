# Phase 3 — Systems: COA, Operating Systems, DBMS (Weeks 23–36)

**Dates:** 2027-02-15 → 2027-05-23 (14 weeks)
**Budget:** ~266 hours (19h/week)
**Subjects:** COA (Wk 23–27) · Operating Systems (Wk 28–32) · DBMS (Wk 33–36)
**Theme:** The three subjects that together carry ~23–30 marks. Numerical-heavy — speed and formula precision matter as much as understanding.

---

## Why This Phase Exists

COA, OS and DBMS are consistently among the highest-weight subjects (COA 8–13, OS 7–10, DBMS 5–8 marks recently). The order is a dependency chain: COA uses Digital Logic from Phase 2, and OS paging / TLB / disk questions reuse COA's memory hierarchy.

Your day job gives OS intuition a head start. Don't let that turn into skimming. GATE OS is `fork()` counting, semaphore traces and page-fault arithmetic.

**New in this phase — interleaved quiz.** From Week 28, every Wednesday PM opens with a 30-minute, 10-question mixed quiz on an *earlier* subject (listed in the table), then a shorter 60-minute lecture. It's the cheapest defence against forgetting Phase 1–2.

---

## Phase Goals (end-of-phase state)

- [ ] Syllabus rows CO-1 … CO-10, OS-1 … OS-10, DB-1 … DB-11 at confidence ≥3
- [ ] PYQ accuracy ≥60% in COA, OS, DBMS
- [ ] Formula sheets complete: `coa.md`, `os.md`, `dbms.md`
- [ ] Interleaved quizzes: 9 done (Weeks 28–36), average ≥60%
- [ ] Phase 1–2 subjects: each revised at least once in this phase (`trackers/revision.md`)
- [ ] GA mixed-set score ≥12/15 by Week 36
- [ ] Adherence ≥70%

---

## How to Read the Weekly Tables

Same conventions as Phases 1–2 (primary GO Classes lectures; PYQ Split Rule; AM starts with redos; PM ends with Reflection). **Wed PM from Week 28 = 30-min interleaved quiz (subject named) + 60-min lecture.** Quiz questions: pre-2000 PYQs or GO Classes free practice, 10 questions, timed.

---

## Weekly Breakdown

### Week 23 — COA: Instruction Formats + Addressing Modes (2027-02-15 → 2027-02-21)
**Hours: 19** | **Topics: CO-1, CO-2** | **GA rotation 5: Vocabulary + reading**

**If your GATE 2027 practice paper is on 20/21 Feb:** it replaces this Saturday's test. Log it in `trackers/mocks.md` as G27.

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DL-8. Map COA playlist → Weeks 23–27 | GO PYQs; GO Classes COA | Error log; mapping |
| Mon | PM | Lecture: stored-program concept, instruction cycle, instruction formats, 0 / 1 / 2 / 3-address instructions | GO Classes COA | `notes/coa/co-01-instruction-formats.md` |
| Tue | AM | PYQs: instruction formats, evaluating expressions with n-address code | GO tag machine-instructions | Daily log + error log |
| Tue | PM | Lecture: expanding opcode technique, RISC vs CISC | GO Classes COA | `co-01` (complete) |
| Wed | AM | PYQs: expanding opcode — number of instructions possible (NAT) | GO tag machine-instructions | Daily log + error log |
| Wed | PM | Lecture: addressing modes 1 — immediate, direct, indirect, register, register-indirect | GO Classes COA | `notes/coa/co-02-addressing-modes.md` |
| Thu | AM | PYQs: identify the addressing mode | GO tag addressing-modes | Daily log + error log |
| Thu | PM | Lecture: addressing modes 2 — indexed, base-register, PC-relative, auto-increment / decrement; effective address calculation | GO Classes COA | `co-02` (complete) |
| Fri | AM | PYQs: effective address (NAT) | GO tag addressing-modes | Daily log + error log |
| Fri | PM | Start `notes/formula-sheets/coa.md`; worked effective-address examples | Own notes / backup: NPTEL COA (Sengupta) | Formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs CO-1, CO-2 + 5 DL carry-over | GO PYQs (odd years) | Topic test T23 |
| Sat | 11:00–12:00 | GA rotation 5 — Vocabulary + reading / sequencing | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Digital Logic** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #23 | — | `reviews/weekly/2027-02-15-to-2027-02-21.md` |

---

### Week 24 — COA: ALU, Computer Arithmetic, Control Unit (2027-02-22 → 2027-02-28)
**Hours: 19** | **Topics: CO-3, CO-4** | **GA rotation 6: Mensuration + geometry**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CO-1, CO-2 | GO PYQs | Error log |
| Mon | PM | Lecture: ALU design — adders inside the ALU, status flags (carry, overflow, zero, sign), fast adders recap | GO Classes COA | `notes/coa/co-03-alu-arithmetic.md` |
| Tue | AM | PYQs: flags, ALU behaviour | GO tag computer-arithmetic | Daily log + error log |
| Tue | PM | Lecture: Booth's multiplication, restoring + non-restoring division | GO Classes COA | `co-03` (complete) |
| Wed | AM | PYQs: Booth's recoding, number of additions / subtractions | GO tag booths-algorithm | Daily log + error log |
| Wed | PM | Lecture: CPU datapath (single / multi-bus), micro-operations, hardwired control unit design | GO Classes COA | `notes/coa/co-04-control-unit.md` |
| Thu | AM | PYQs: micro-operation sequences, datapath | GO tag data-path | Daily log + error log |
| Thu | PM | Lecture: microprogrammed control — horizontal vs vertical microprogramming, control memory size, control word format | GO Classes COA | `co-04` (complete) |
| Fri | AM | PYQs: control word size / control memory (NAT) | GO tag microprogramming | Daily log + error log |
| Fri | PM | Untimed practice: micro-operation sequences for fetch / execute on paper | GO Classes COA practice | `co-04` worked examples |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs CO-3, CO-4 | GO PYQs (odd years) | Topic test T24 |
| Sat | 11:00–12:00 | GA rotation 6 — Mensuration + geometry | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #24 **+ Monthly review (February 2027)** | — | `reviews/weekly/2027-02-22-to-2027-02-28.md` + `reviews/monthly/2027-02.md` |

---

### Week 25 — COA: Memory Hierarchy + Cache (2027-03-01 → 2027-03-07)
**Hours: 19** | **Topics: CO-5, CO-6** | **GA rotation 7: Statistics + probability + PnC**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CO-3, CO-4 | GO PYQs | Error log |
| Mon | PM | Lecture: memory hierarchy, locality of reference, AMAT — hierarchical vs simultaneous access | GO Classes COA | `notes/coa/co-05-memory-hierarchy.md` |
| Tue | AM | PYQs: AMAT (NAT) | GO tag cache-memory | Daily log + error log |
| Tue | PM | Lecture: memory interfacing — RAM / ROM chips, decoders, address space allocation, chips required | GO Classes COA | `co-05` (complete) |
| Wed | AM | PYQs: memory interfacing | GO tag memory-interfacing | Daily log + error log |
| Wed | PM | Lecture: cache — direct mapping, tag / line / offset bits, hardware | GO Classes COA | `notes/coa/co-06-cache-mapping.md` |
| Thu | AM | PYQs: direct mapping bit split, misses for an access sequence | GO tag cache-memory | Daily log + error log |
| Thu | PM | Lecture: set-associative + fully associative mapping, comparator count, tag memory size | GO Classes COA | `co-06` |
| Fri | AM | PYQs: set-associative bit split (NAT) | GO tag cache-memory | Daily log + error log |
| Fri | PM | Lecture: cache replacement (FIFO / LRU), miss types, write-through vs write-back, multi-level caches | GO Classes COA | `co-06` (complete) + formula sheet (cache section) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs CO-5, CO-6 | GO PYQs (odd years) | Topic test T25 |
| Sat | 11:00–12:00 | GA rotation 7 — Statistics + probability + PnC | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Linear Algebra + Calculus** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #25 | — | `reviews/weekly/2027-03-01-to-2027-03-07.md` |

---

### Week 26 — COA: Secondary Storage + I/O (2027-03-08 → 2027-03-14)
**Hours: 19** | **Topics: CO-7, CO-8** | **GA rotation 8: Spatial aptitude**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CO-5, CO-6 | GO PYQs | Error log |
| Mon | PM | Lecture: disk structure — platters, tracks, sectors, cylinders; capacity; seek time, rotational latency, transfer time | GO Classes COA | `notes/coa/co-07-disk.md` |
| Tue | AM | PYQs: disk capacity + access time (NAT) | GO tag disk | Daily log + error log |
| Tue | PM | Lecture: I/O organisation — memory-mapped vs isolated I/O, programmed I/O, interrupt-driven I/O | GO Classes COA | `notes/coa/co-08-io-interrupts-dma.md` |
| Wed | AM | PYQs: programmed vs interrupt I/O | GO tag interrupts | Daily log + error log |
| Wed | PM | Lecture: interrupt handling — vectored interrupts, priority, daisy chaining, nested interrupts | GO Classes COA | `co-08` |
| Thu | AM | PYQs: interrupts | GO tag interrupts | Daily log + error log |
| Thu | PM | Lecture: DMA — DMA controller, burst vs cycle-stealing mode, CPU time consumed, transfer-rate calculations | GO Classes COA | `co-08` (complete) |
| Fri | AM | PYQs: DMA (NAT) | GO tag dma | Daily log + error log |
| Fri | PM | Formula sheet: disk + DMA formulas; mixed untimed memory + I/O practice | Own notes | `notes/formula-sheets/coa.md` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs CO-7, CO-8 + 5 cache carry-over | GO PYQs (odd years) | Topic test T26 |
| Sat | 11:00–12:00 | GA rotation 8 — Spatial aptitude | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #26 | — | `reviews/weekly/2027-03-08-to-2027-03-14.md` |

---

### Week 27 — COA: Pipelining + Hazards (2027-03-15 → 2027-03-21)
**Hours: 19** | **Topics: CO-9, CO-10** | **GA rotation 9: Mixed timed GA section**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CO-7, CO-8 | GO PYQs | Error log |
| Mon | PM | Lecture: pipelining basics — stages, clock period with latch delay, speedup, throughput, efficiency | GO Classes COA | `notes/coa/co-09-pipelining.md` |
| Tue | AM | PYQs: speedup / throughput (NAT) | GO tag pipelining | Daily log + error log |
| Tue | PM | Lecture: non-uniform stage delays, time to execute N instructions, pipeline vs non-pipeline comparison | GO Classes COA | `co-09` (complete) |
| Wed | AM | PYQs: execution time for N instructions (NAT) | GO tag pipelining | Daily log + error log |
| Wed | PM | Lecture: data hazards — dependencies, stalls, operand forwarding; timing diagrams | GO Classes COA | `notes/coa/co-10-pipeline-hazards.md` |
| Thu | AM | PYQs: stalls with / without forwarding | GO tag pipelining | Daily log + error log |
| Thu | PM | Lecture: control hazards (branch penalty, prediction, flushing), structural hazards | GO Classes COA | `co-10` (complete) |
| Fri | AM | Mixed COA PYQs: all remaining even-year questions | GO PYQs | Daily log + error log |
| Fri | PM | **Finish `notes/formula-sheets/coa.md`** + R1 revision of all COA notes | Own notes | Formula sheet (complete) |
| Sat | 09:00–11:00 | **COA subject test:** ~30 odd-year PYQs CO-1 … CO-10 | GO PYQs (odd years) | Topic test T27 |
| Sat | 11:00–12:00 | GA rotation 9 — one full GA section, 25 min timed, score /15 | GA PYQs | `trackers/aptitude.md` mixed-set score |
| Sat | 12:00–13:00 | Error analysis, COA confidence ratings in `subjects.md` | — | Error log |
| Sun | — | Weekly review #27 | — | `reviews/weekly/2027-03-15-to-2027-03-21.md` |

**Resources:**
- GO Classes COA — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjMdZR3GYQ2KZio0NKczrik
- Backup: NPTEL Computer Architecture and Organization (Indranil Sengupta, Kamalika Datta) — https://nptel.ac.in/courses/106105163
- Reference: Hamacher — Computer Organization; Patterson & Hennessy

---

### Week 28 — OS: Processes, Threads, CPU Scheduling (2027-03-22 → 2027-03-28)
**Hours: 19** | **Topics: OS-1, OS-2, OS-3** | **GA rotation 1: Numerical computation** | **Interleaved quiz: C**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; mixed COA PYQs (top-up) for the weakest COA topic. Map OS playlist → Weeks 28–32 | GO PYQs; GO Classes OS | Error log; mapping |
| Mon | PM | Lecture: OS role, system calls, user vs kernel mode, process concept, PCB, process states + transitions, context switch | GO Classes Operating Systems | `notes/os/os-01-processes-syscalls.md` |
| Tue | AM | PYQs: system calls, process states | GO tag process | Daily log + error log |
| Tue | PM | Lecture: `fork()` semantics — counting processes / printed lines in loops; threads — user vs kernel, multithreading models, what threads share | GO Classes Operating Systems | `os-01` (complete) + `notes/os/os-02-threads.md` |
| Wed | AM | PYQs: `fork()` counting (NAT), threads | GO tag fork-system-call, threads | Daily log + error log |
| Wed | PM | **Interleaved quiz: C (30 min)** → Lecture: CPU scheduling criteria, FCFS, SJF | Quiz: pre-2000 C PYQs; GO Classes OS | Quiz score in `trackers/revision.md`; `notes/os/os-03-cpu-scheduling.md` |
| Thu | AM | PYQs: FCFS / SJF waiting + turnaround (NAT) | GO tag process-scheduling | Daily log + error log |
| Thu | PM | Lecture: SRTF, round robin (quantum effects), priority (aging), multilevel queue + feedback queue | GO Classes Operating Systems | `os-03` (complete) |
| Fri | AM | PYQs: SRTF / RR / priority (NAT) | GO tag process-scheduling | Daily log + error log |
| Fri | PM | Worked Gantt charts on paper (untimed) + start `notes/formula-sheets/os.md` | Own notes / backup: Gate Smashers OS | Formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs OS-1 … OS-3 | GO PYQs (odd years) | Topic test T28 |
| Sat | 11:00–12:00 | GA rotation 1 — Numerical computation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #28 **+ Monthly review (March 2027)** | — | `reviews/weekly/2027-03-22-to-2027-03-28.md` + `reviews/monthly/2027-03.md` |

---

### Week 29 — OS: IPC, Concurrency + Synchronization (2027-03-29 → 2027-04-04)
**Hours: 19** | **Topics: OS-4, OS-5** | **GA rotation 2: Grammar** | **Interleaved quiz: Data Structures**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs OS-1 … OS-3 | GO PYQs | Error log |
| Mon | PM | Lecture: IPC (shared memory, message passing, pipes); race conditions; critical-section requirements — mutual exclusion, progress, bounded waiting | GO Classes Operating Systems | `notes/os/os-04-ipc.md` + `notes/os/os-05-synchronization.md` (start) |
| Tue | AM | PYQs: IPC, critical section properties | GO tag inter-process-communication, process-synchronization | Daily log + error log |
| Tue | PM | Lecture: software solutions (lock variable, strict alternation, Peterson's), hardware solutions (TSL, disabling interrupts) | GO Classes Operating Systems | `os-05` |
| Wed | AM | PYQs: does this code satisfy ME / progress / bounded waiting? (MSQ) | GO tag process-synchronization | Daily log + error log |
| Wed | PM | **Interleaved quiz: Data Structures (30 min)** → Lecture: semaphores — counting / binary, wait / signal, blocking vs busy waiting | Quiz: pre-2000 DS PYQs; GO Classes OS | Quiz score; `os-05` |
| Thu | AM | PYQs: semaphore value after operations (NAT) | GO tag semaphore | Daily log + error log |
| Thu | PM | Lecture: classic problems — producer–consumer, readers–writers, dining philosophers | GO Classes Operating Systems | `os-05` |
| Fri | AM | PYQs: classic synchronisation problems | GO tag process-synchronization | Daily log + error log |
| Fri | PM | Lecture: monitors + condition variables; trace-the-interleaving practice on paper | GO Classes OS / backup: NPTEL Intro to OS (Rebeiro) | `os-05` (complete) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs OS-4, OS-5 | GO PYQs (odd years) | Topic test T29 |
| Sat | 11:00–12:00 | GA rotation 2 — Grammar | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Probability** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #29 | — | `reviews/weekly/2027-03-29-to-2027-04-04.md` |

---

### Week 30 — OS: Deadlock + Disk Scheduling (2027-04-05 → 2027-04-11)
**Hours: 19** | **Topics: OS-6, OS-7** | **GA rotation 3: Data interpretation** | **Interleaved quiz: Discrete Maths**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs OS-4, OS-5 | GO PYQs | Error log |
| Mon | PM | Lecture: deadlock — Coffman conditions, resource allocation graphs, single vs multi-instance cycles | GO Classes Operating Systems | `notes/os/os-06-deadlock.md` |
| Tue | AM | PYQs: deadlock conditions, RAG | GO tag deadlock-prevention-avoidance-detection | Daily log + error log |
| Tue | PM | Lecture: deadlock prevention; avoidance — safe state, Banker's safety algorithm | GO Classes Operating Systems | `os-06` |
| Wed | AM | PYQs: Banker's safe sequence | GO tag bankers-algorithm | Daily log + error log |
| Wed | PM | **Interleaved quiz: Discrete Maths (30 min)** → Lecture: Banker's resource-request, deadlock detection + recovery, minimum resources to guarantee no deadlock | Quiz: pre-2000 DM PYQs; GO Classes OS | Quiz score; `os-06` (complete) |
| Thu | AM | PYQs: minimum resources (NAT), detection | GO tag deadlock-prevention-avoidance-detection | Daily log + error log |
| Thu | PM | Lecture: disk scheduling — FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK | GO Classes Operating Systems | `notes/os/os-07-disk-scheduling.md` |
| Fri | AM | PYQs: total head movement (NAT) | GO tag disk-scheduling | Daily log + error log |
| Fri | PM | OS formula sheet: deadlock formulas + disk scheduling; worked head-movement charts | Own notes | `notes/formula-sheets/os.md` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs OS-6, OS-7 + 5 sync carry-over | GO PYQs (odd years) | Topic test T30 |
| Sat | 11:00–12:00 | GA rotation 3 — Data interpretation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #30 | — | `reviews/weekly/2027-04-05-to-2027-04-11.md` |

---

### Week 31 — OS: Memory Management (2027-04-12 → 2027-04-18)
**Hours: 19** | **Topics: OS-8** | **GA rotation 4: Logic + reasoning** | **Interleaved quiz: Algorithms**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs OS-6, OS-7 | GO PYQs | Error log |
| Mon | PM | Lecture: contiguous allocation — fixed / variable partitions, first / best / worst / next fit, internal vs external fragmentation, compaction | GO Classes Operating Systems | `notes/os/os-08-paging-segmentation.md` |
| Tue | AM | PYQs: allocation strategies, fragmentation | GO tag memory-management | Daily log + error log |
| Tue | PM | Lecture: paging — logical / physical address split, page table entry, page table size | GO Classes Operating Systems | `os-08` |
| Wed | AM | PYQs: address split, page table size (NAT) | GO tag paging | Daily log + error log |
| Wed | PM | **Interleaved quiz: Algorithms (30 min)** → Lecture: multi-level paging, inverted page tables, hashed page tables | Quiz: pre-2000 Algo PYQs; GO Classes OS | Quiz score; `os-08` |
| Thu | AM | PYQs: number of levels, multi-level sizes (NAT) | GO tag paging | Daily log + error log |
| Thu | PM | Lecture: TLB — EMAT with TLB hit ratio, multi-level + TLB combinations | GO Classes Operating Systems | `os-08` |
| Fri | AM | PYQs: EMAT (NAT) | GO tag translation-lookaside-buffer | Daily log + error log |
| Fri | PM | Lecture: segmentation, segment tables, segmented paging; formula sheet: paging formulas | GO Classes OS | `os-08` (complete) + `notes/formula-sheets/os.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs OS-8 | GO PYQs (odd years) | Topic test T31 |
| Sat | 11:00–12:00 | GA rotation 4 — Logic + reasoning | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: COA (cache + pipeline formulas)** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #31 | — | `reviews/weekly/2027-04-12-to-2027-04-18.md` |

---

### Week 32 — OS: Virtual Memory + File Systems (2027-04-19 → 2027-04-25)
**Hours: 19** | **Topics: OS-9, OS-10** | **GA rotation 5: Vocabulary + reading** | **Interleaved quiz: Engineering Maths**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs OS-8 | GO PYQs | Error log |
| Mon | PM | Lecture: demand paging, page-fault handling steps, effective access time with page faults | GO Classes Operating Systems | `notes/os/os-09-virtual-memory.md` |
| Tue | AM | PYQs: EAT with page faults (NAT) | GO tag virtual-memory | Daily log + error log |
| Tue | PM | Lecture: page replacement — FIFO, optimal, LRU (counter / stack), Belady's anomaly | GO Classes Operating Systems | `os-09` |
| Wed | AM | PYQs: page faults for a reference string (NAT) | GO tag page-replacement | Daily log + error log |
| Wed | PM | **Interleaved quiz: Engineering Maths (30 min)** → Lecture: thrashing, working-set model, frame allocation, page size trade-offs | Quiz: pre-2000 maths PYQs; GO Classes OS | Quiz score; `os-09` (complete) |
| Thu | AM | PYQs: thrashing, working set | GO tag virtual-memory | Daily log + error log |
| Thu | PM | Lecture: file systems — contiguous / linked / indexed allocation, FAT, inode structure, maximum file size | GO Classes Operating Systems | `notes/os/os-10-file-systems.md` |
| Fri | AM | PYQs: inode max file size (NAT), allocation | GO tag file-system | Daily log + error log |
| Fri | PM | Lecture: directory structures, free-space management (bit vector, linked list) → **finish `notes/formula-sheets/os.md`** | GO Classes OS | `os-10` (complete) + formula sheet (complete) |
| Sat | 09:00–11:00 | **OS subject test:** ~30 odd-year PYQs OS-1 … OS-10 | GO PYQs (odd years) | Topic test T32 |
| Sat | 11:00–12:00 | GA rotation 5 — Vocabulary + reading / sequencing | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, OS confidence ratings in `subjects.md` | — | Error log |
| Sun | — | Weekly review #32 **+ Monthly review (April 2027)** | — | `reviews/weekly/2027-04-19-to-2027-04-25.md` + `reviews/monthly/2027-04.md` |

**Resources:**
- GO Classes Operating Systems — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHixlIaarIXGPy-eggJQMxd_
- Backup: NPTEL Introduction to Operating Systems (Chester Rebeiro) — https://nptel.ac.in/courses/106106144
- Backup: Gate Smashers — https://www.youtube.com/@GateSmashers/playlists
- Reference: Galvin — Operating System Concepts, Ch 3–14

---

### Week 33 — DBMS: ER Model, Relational Model, Relational Algebra, TRC (2027-04-26 → 2027-05-02)
**Hours: 19** | **Topics: DB-1 … DB-4** | **GA rotation 6: Mensuration + geometry** | **Interleaved quiz: Digital Logic**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year OS PYQs (OS-9, OS-10). Map DBMS playlist → Weeks 33–36 | GO PYQs; GO Classes DBMS | Error log; mapping |
| Mon | PM | Lecture: ER model — entities, attribute types, relationships, cardinality, participation, weak entities | GO Classes DBMS | `notes/dbms/db-01-er-model.md` |
| Tue | AM | PYQs: ER diagrams | GO tag er-diagram | Daily log + error log |
| Tue | PM | Lecture: ER → relational mapping, minimum tables; keys (super / candidate / primary / foreign), integrity constraints, referential actions | GO Classes DBMS | `db-01` (complete) + `notes/dbms/db-02-relational-model-keys.md` |
| Wed | AM | PYQs: minimum tables (NAT), referential integrity | GO tag er-diagram, referential-integrity | Daily log + error log |
| Wed | PM | **Interleaved quiz: Digital Logic (30 min)** → Lecture: relational algebra — select, project, union, difference, cartesian product, rename | Quiz: pre-2000 DL PYQs; GO Classes DBMS | Quiz score; `notes/dbms/db-03-relational-algebra.md` |
| Thu | AM | PYQs: relational algebra basics | GO tag relational-algebra | Daily log + error log |
| Thu | PM | Lecture: joins (natural, theta, outer), division, result cardinality bounds | GO Classes DBMS | `db-03` (complete) |
| Fri | AM | PYQs: RA query output / cardinality (NAT) | GO tag relational-algebra | Daily log + error log |
| Fri | PM | Lecture: tuple relational calculus — syntax, safe expressions, equivalence with RA | GO Classes DBMS | `notes/dbms/db-04-tuple-calculus.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs DB-1 … DB-4 | GO PYQs (odd years) | Topic test T33 |
| Sat | 11:00–12:00 | GA rotation 6 — Mensuration + geometry | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #33 | — | `reviews/weekly/2027-04-26-to-2027-05-02.md` |

---

### Week 34 — DBMS: SQL, Functional Dependencies, Normal Forms (2027-05-03 → 2027-05-09)
**Hours: 19** | **Topics: DB-5, DB-6, DB-7** | **GA rotation 7: Statistics + probability + PnC** | **Interleaved quiz: COA**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DB-1 … DB-4 | GO PYQs | Error log |
| Mon | PM | Lecture: SQL — SELECT semantics, joins, aggregates, GROUP BY / HAVING, NULL + three-valued logic | GO Classes DBMS | `notes/dbms/db-05-sql.md` |
| Tue | AM | PYQs: SQL output rows (NAT) | GO tag sql | Daily log + error log |
| Tue | PM | Lecture: nested + correlated subqueries, EXISTS / IN / ALL / ANY, set operations, duplicates | GO Classes DBMS | `db-05` (complete) |
| Wed | AM | PYQs: correlated subqueries | GO tag sql | Daily log + error log |
| Wed | PM | **Interleaved quiz: COA (30 min)** → Lecture: functional dependencies, Armstrong's axioms, attribute closure, candidate key finding | Quiz: pre-2000 COA PYQs; GO Classes DBMS | Quiz score; `notes/dbms/db-06-functional-dependencies.md` |
| Thu | AM | PYQs: closures, candidate keys, number of super keys (NAT) | GO tag functional-dependency, candidate-key | Daily log + error log |
| Thu | PM | Lecture: minimal cover, equivalence of FD sets; 1NF, 2NF, 3NF | GO Classes DBMS | `db-06` (complete) + `notes/dbms/db-07-normal-forms.md` |
| Fri | AM | PYQs: highest normal form | GO tag database-normalization | Daily log + error log |
| Fri | PM | Lecture: BCNF, lossless-join test, dependency preservation, decomposition algorithms | GO Classes DBMS | `db-07` (complete) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs DB-5 … DB-7 | GO PYQs (odd years) | Topic test T34 |
| Sat | 11:00–12:00 | GA rotation 7 — Statistics + probability + PnC | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Operating Systems formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #34 | — | `reviews/weekly/2027-05-03-to-2027-05-09.md` |

---

### Week 35 — DBMS: File Organization, Indexing, B / B+ Trees (2027-05-10 → 2027-05-16)
**Hours: 19** | **Topics: DB-8, DB-9** | **GA rotation 8: Spatial aptitude** | **Interleaved quiz: Discrete Maths**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DB-5 … DB-7 | GO PYQs | Error log |
| Mon | PM | Lecture: file organisation — records, blocking factor, heap / sorted / hashed files, block accesses | GO Classes DBMS | `notes/dbms/db-08-indexing.md` |
| Tue | AM | PYQs: blocking factor, block accesses (NAT) | GO tag indexing | Daily log + error log |
| Tue | PM | Lecture: indexing — primary, clustering, secondary; dense vs sparse; multilevel index | GO Classes DBMS | `db-08` (complete) |
| Wed | AM | PYQs: index blocks + multilevel accesses (NAT) | GO tag indexing | Daily log + error log |
| Wed | PM | **Interleaved quiz: Discrete Maths (30 min)** → Lecture: B tree — structure, order from block size, search, insertion | Quiz: pre-2000 DM PYQs; GO Classes DBMS | Quiz score; `notes/dbms/db-09-b-bplus-trees.md` |
| Thu | AM | PYQs: B tree order (NAT) | GO tag b-tree | Daily log + error log |
| Thu | PM | Lecture: B tree deletion; B+ tree — internal vs leaf order, structure, why databases use it | GO Classes DBMS | `db-09` |
| Fri | AM | PYQs: B+ tree order, min / max keys at a level (NAT) | GO tag b-tree | Daily log + error log |
| Fri | PM | Lecture / practice: B+ tree insertions with splits on paper, height bounds | GO Classes DBMS / backup: NPTEL DBMS (Das) | `db-09` (complete) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs DB-8, DB-9 + 5 normalisation carry-over | GO PYQs (odd years) | Topic test T35 |
| Sat | 11:00–12:00 | GA rotation 8 — Spatial aptitude | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #35 | — | `reviews/weekly/2027-05-10-to-2027-05-16.md` |

---

### Week 36 — DBMS: Transactions + Concurrency Control + Phase 3 Wrap (2027-05-17 → 2027-05-23)
**Hours: 19** | **Topics: DB-10, DB-11** | **GA rotation 9: Mixed timed GA section** | **Interleaved quiz: Algorithms**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DB-8, DB-9 | GO PYQs | Error log |
| Mon | PM | Lecture: transactions — ACID, states, schedules; recoverable, cascadeless, strict schedules | GO Classes DBMS | `notes/dbms/db-10-transactions-serializability.md` |
| Tue | AM | PYQs: recoverability classification (MSQ) | GO tag transaction-and-concurrency | Daily log + error log |
| Tue | PM | Lecture: conflict serializability (precedence graph), view serializability, counting equivalent serial schedules | GO Classes DBMS | `db-10` (complete) |
| Wed | AM | PYQs: conflict / view serializable? | GO tag conflict-serializable | Daily log + error log |
| Wed | PM | **Interleaved quiz: Algorithms (30 min)** → Lecture: lock-based protocols — shared / exclusive, basic 2PL, strict 2PL, rigorous 2PL | Quiz: pre-2000 Algo PYQs; GO Classes DBMS | Quiz score; `notes/dbms/db-11-concurrency-control.md` |
| Thu | AM | PYQs: 2PL variants | GO tag two-phase-locking-protocol | Daily log + error log |
| Thu | PM | Lecture: timestamp ordering, Thomas write rule, deadlock prevention (wait-die, wound-wait) | GO Classes DBMS | `db-11` (complete) |
| Fri | AM | Mixed DBMS PYQs: all remaining even-year questions | GO PYQs | Daily log + error log |
| Fri | PM | **Finish `notes/formula-sheets/dbms.md`** + Phase 3 audit (CO / OS / DB confidence in `subjects.md`, 5 weakest topics) | Own notes; `trackers/subjects.md` | Formula sheet (complete); audit |
| Sat | 09:00–11:00 | **DBMS subject test:** ~30 odd-year PYQs DB-1 … DB-11 | GO PYQs (odd years) | Topic test T36 |
| Sat | 11:00–12:00 | GA rotation 9 — one full GA section, 25 min timed, score /15 | GA PYQs | `trackers/aptitude.md` mixed-set score |
| Sat | 12:00–13:00 | Error analysis + walk the **Phase 3 exit checklist** below | — | Exit checklist answers |
| Sun | — | Weekly review #36 + **Phase 3 retrospective** | — | `reviews/weekly/2027-05-17-to-2027-05-23.md` |

**Resources:**
- GO Classes DBMS — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHhUXFx03wy3uFeCXRw6qlm8
- Backup: NPTEL Data Base Management System (Partha Pratim Das) — https://nptel.ac.in/courses/106105175
- Reference: Korth — Database System Concepts; Navathe

---

## Daily Quota Cheat Sheet

| Slot | PYQ target | Lecture time |
|------|------------|--------------|
| Mon–Fri AM | 12–15 PYQs + redos (long numericals: allow 5–6 min for 2-markers) | — |
| Mon–Fri PM | 0 (Wed: 10-question interleaved quiz from Wk 28) | 60–70 min lecture + 20 min notes |
| Sat 09:00–11:00 | 20–30 odd-year PYQs, timed | — |
| Sat 11:00–12:00 | 20–25 GA questions | — |

---

## Phase-3 Exit Criteria

Before moving to Phase 4 (Mon 2027-05-24), confirm:

- [ ] CO / OS / DB rows at confidence ≥3 in `trackers/subjects.md`
- [ ] PYQ accuracy ≥60% in COA, OS, DBMS
- [ ] Cache bit split, AMAT, pipeline time and EMAT computed correctly in <4 min each
- [ ] Page faults for FIFO / LRU / optimal, `fork()` counts and Banker's safety done in <4 min each
- [ ] Candidate keys, highest normal form and B+ tree order found in <4 min each
- [ ] Formula sheets complete: coa, os, dbms
- [ ] Interleaved quiz average ≥60%; no Phase 1–2 subject unrevised for >30 days
- [ ] Adherence ≥70%

If any of these are "no", **extend Phase 3 by 1 week** (out of Phase 5).
