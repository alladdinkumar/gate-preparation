# Systems Curriculum — Operating Systems, DBMS, Computer Networks

Sections 8, 9 and 10 of the syllabus. **~21–27 marks per paper combined.** This is where the day job helps most — you run processes, threads, TCP, TLS, DNS and load balancers every week. But GATE doesn't ask "how does it work in production?". It asks "how many page faults with LRU on this reference string?". Treat practical intuition as a head start on *understanding*, not on *scoring*.

**Time budget:** OS (Weeks 28–32), DBMS (Weeks 33–36), CN (Weeks 37–41) = 14 weeks, ~266h. Revision: Weeks 56–58.

---

## Operating Systems (Weeks 28–32)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| OS-1 | System calls, process concept, PCB, process states, `fork()` — counting processes / printed lines, context switch | 28 | `notes/os/os-01-processes-syscalls.md` | fork-system-call, process |
| OS-2 | Threads — user vs kernel threads, multithreading models, what's shared | 28 | `notes/os/os-02-threads.md` | threads |
| OS-3 | CPU scheduling — FCFS, SJF, SRTF, RR, priority (preemptive/non), multilevel queue/feedback; Gantt charts, waiting/turnaround time, starvation | 28 | `notes/os/os-03-cpu-scheduling.md` | process-scheduling |
| OS-4 | Inter-process communication — shared memory, message passing, pipes | 29 | `notes/os/os-04-ipc.md` | inter-process-communication |
| OS-5 | Concurrency + synchronization — race conditions, critical section requirements (mutual exclusion, progress, bounded waiting), Peterson's, TSL, semaphores (counting/binary), monitors, producer–consumer, readers–writers, dining philosophers | 29 | `notes/os/os-05-synchronization.md` | process-synchronization, semaphore |
| OS-6 | Deadlock — Coffman conditions, resource allocation graph, prevention, avoidance (Banker's algorithm, safe state), detection + recovery; minimum resources to avoid deadlock | 30 | `notes/os/os-06-deadlock.md` | deadlock-prevention-avoidance-detection, bankers-algorithm |
| OS-7 | I/O + disk scheduling — FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK; total head movement | 30 | `notes/os/os-07-disk-scheduling.md` | disk-scheduling |
| OS-8 | Memory management — contiguous allocation (first/best/worst fit, fragmentation), paging, page table size, multi-level paging, inverted page table, TLB + EMAT, segmentation | 31 | `notes/os/os-08-paging-segmentation.md` | paging, translation-lookaside-buffer |
| OS-9 | Virtual memory — demand paging, page faults, effective access time, page replacement (FIFO, optimal, LRU), Belady's anomaly, thrashing, working set, frame allocation | 32 | `notes/os/os-09-virtual-memory.md` | page-replacement, virtual-memory |
| OS-10 | File systems — file allocation (contiguous, linked, indexed), inode + max file size, directory structures, free-space management | 32 | `notes/os/os-10-file-systems.md` | file-system |

**GATE-favourite question types:**
- Number of child processes / lines printed with `fork()` in loops (NAT)
- Average waiting / turnaround time (NAT)
- Which synchronisation code satisfies mutual exclusion but not progress (MSQ)
- Semaphore value after a sequence of operations (NAT)
- Minimum number of resources so deadlock never occurs (NAT)
- Page table size / number of levels / EMAT with TLB (NAT)
- Page faults for a reference string under FIFO / LRU / optimal (NAT)
- Max file size with direct + single/double/triple indirect blocks (NAT)

---

## Databases (Weeks 33–36)

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| DB-1 | ER model — entity sets, attributes (composite, multivalued, derived), relationship cardinality + participation, weak entities, minimum tables for an ER diagram | 33 | `notes/dbms/db-01-er-model.md` | er-diagram |
| DB-2 | Relational model — super/candidate/primary/foreign keys, integrity constraints, referential actions (cascade, set null) | 33 | `notes/dbms/db-02-relational-model-keys.md` | referential-integrity, candidate-key |
| DB-3 | Relational algebra — select, project, join variants, division, rename; result cardinality bounds | 33 | `notes/dbms/db-03-relational-algebra.md` | relational-algebra |
| DB-4 | Tuple relational calculus — safe expressions, equivalence with RA | 33 | `notes/dbms/db-04-tuple-calculus.md` | tuple-calculus |
| DB-5 | SQL — joins, nested and correlated subqueries, GROUP BY / HAVING, aggregates, NULL semantics, EXISTS / ALL / ANY | 34 | `notes/dbms/db-05-sql.md` | sql |
| DB-6 | Functional dependencies — Armstrong's axioms, attribute closure, minimal cover, candidate key finding, counting super keys | 34 | `notes/dbms/db-06-functional-dependencies.md` | functional-dependency |
| DB-7 | Normal forms — 1NF, 2NF, 3NF, BCNF; lossless-join and dependency-preserving decomposition; highest normal form of a relation | 34 | `notes/dbms/db-07-normal-forms.md` | database-normalization |
| DB-8 | File organization + indexing — heap / sorted files, primary, clustering, secondary indexes, dense vs sparse, multilevel index block accesses | 35 | `notes/dbms/db-08-indexing.md` | indexing |
| DB-9 | B trees and B+ trees — order calculation from block size, insertion + splits, min/max nodes/keys at a level, height | 35 | `notes/dbms/db-09-b-bplus-trees.md` | b-tree |
| DB-10 | Transactions — ACID, schedules, conflict vs view serializability (precedence graph), recoverable / cascadeless / strict schedules | 36 | `notes/dbms/db-10-transactions-serializability.md` | transaction-and-concurrency, conflict-serializable |
| DB-11 | Concurrency control — basic / strict / rigorous 2PL, timestamp ordering (Thomas write rule), deadlock prevention (wait-die, wound-wait) | 36 | `notes/dbms/db-11-concurrency-control.md` | two-phase-locking-protocol, timestamp-ordering |

**GATE-favourite question types:**
- Number of rows returned by an SQL query on given tables (NAT)
- Highest normal form / is decomposition lossless and dependency-preserving
- Number of candidate keys / super keys (NAT)
- B+ tree order from block size, key and pointer sizes (NAT)
- Conflict-serializable? Which schedules are recoverable? (MSQ)
- Minimum tables for an ER diagram (NAT)

---

## Computer Networks (Weeks 37–41)

The official CN syllabus is narrower than older textbooks. Stick to it: no application layer beyond **DNS and HTTP**.

| # | Topic | Week | Note file | GO tag (search) |
|---|-------|------|-----------|-----------------|
| CN-1 | Principles of layering — OSI vs TCP/IP, encapsulation, which device works at which layer | 37 | `notes/cn/cn-01-layering.md` | network-layering |
| CN-2 | Switching — circuit vs packet vs virtual circuit; performance metrics: transmission, propagation, queuing, processing delay; throughput, bandwidth, utilisation | 37 | `notes/cn/cn-02-switching-performance.md` | network-switching, communication |
| CN-3 | Data link layer — framing (bit/byte stuffing), error detection: parity, CRC (division), checksum, Hamming distance / code | 38 | `notes/cn/cn-03-error-detection.md` | crc-polynomial, error-detection |
| CN-4 | Sliding window — stop-and-wait, Go-Back-N, Selective Repeat; efficiency, sequence number bits, window sizes (foundation for TCP flow control) | 38 | `notes/cn/cn-04-sliding-window.md` | sliding-window |
| CN-5 | Medium Access Control — pure/slotted ALOHA, CSMA, CSMA/CD (min frame size), token passing; Ethernet frame + addressing | 39 | `notes/cn/cn-05-mac-ethernet.md` | mac-protocol, ethernet |
| CN-6 | IPv4 — address classes (legacy), CIDR notation, subnetting, supernetting, longest prefix match, IPv4 header | 40 | `notes/cn/cn-06-ipv4-cidr-subnetting.md` | subnetting, ip-addressing |
| CN-7 | IPv4 fragmentation (offset, MF flag, counting fragments) + Network Address Translation | 40 | `notes/cn/cn-07-fragmentation-nat.md` | ip-fragmentation |
| CN-8 | Routing — distance vector (Bellman–Ford, count-to-infinity, split horizon), link state (Dijkstra, flooding of LSPs) | 40 | `notes/cn/cn-08-routing.md` | routing |
| CN-9 | TCP — header, 3-way handshake, connection teardown, flow control (receiver window), congestion control (slow start, AIMD, fast retransmit/recovery, threshold), sequence number wrap-around; UDP | 41 | `notes/cn/cn-09-tcp-udp.md` | tcp, congestion-control |
| CN-10 | Socket API — socket/bind/listen/accept/connect sequence for TCP and UDP | 41 | `notes/cn/cn-10-socket-api.md` | sockets |
| CN-11 | DNS (resolution, record types, recursive vs iterative) and HTTP (persistent vs non-persistent, RTT counting, methods) | 41 | `notes/cn/cn-11-dns-http.md` | dns, http |

**GATE-favourite question types:**
- Total delay / throughput for a link (NAT)
- CRC remainder / transmitted bits (NAT)
- Max window size or sequence-number bits for GBN / SR (NAT)
- Minimum frame size for CSMA/CD (NAT)
- Subnet / broadcast address, number of hosts, longest prefix match to an interface
- Number of fragments + offset of the last fragment (NAT)
- TCP congestion window after k RTTs with a timeout (NAT)
- Correct system-call order for a TCP server (MCQ)

**Where your day job helps:** TCP handshake, DNS resolution, HTTP persistent connections, NAT — you'll read these fast. Spend the saved time on CRC, sliding window and congestion window arithmetic.

---

## Formula Sheets

- End of Week 32: `notes/formula-sheets/os.md` — scheduling metrics, EMAT/EAT, page table size, inode max file size, disk scheduling
- End of Week 36: `notes/formula-sheets/dbms.md` — closure procedure, NF tests, B/B+ order formulas, index block accesses
- End of Week 41: `notes/formula-sheets/cn.md` — delay formulas, ALOHA/CSMA efficiency, sliding window, CIDR, fragmentation, congestion window

---

## Tracking

`trackers/subjects.md` rows OS-1 … OS-10, DB-1 … DB-11, CN-1 … CN-11.
