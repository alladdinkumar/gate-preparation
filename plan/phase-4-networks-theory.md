# Phase 4 — Computer Networks + Theory of Computation + Compiler Design (Weeks 37–49)

**Dates:** 2027-05-24 → 2027-08-22 (13 weeks)
**Budget:** ~247 hours (19h/week)
**Subjects:** Computer Networks (Wk 37–41) · Theory of Computation (Wk 42–46) · Compiler Design (Wk 47–49)
**Theme:** Finish the first pass of the entire syllabus. On Sunday 2027-08-22, every syllabus row has been studied once.

---

## Why This Phase Exists

CN (~8–9 marks), TOC (~7–9) and CD (~5–8) together are ~20–26 marks. CN is where your day job helps most — use the saved time on the arithmetic (CRC, sliding windows, congestion window, fragmentation).

TOC is pure theory with very repetitive questions. CD comes last because lexical analysis needs regular languages and parsing needs CFGs.

The interleaved Wednesday quiz continues through all 13 weeks. By Week 49 it has cycled through every earlier subject at least once in Phase 3–4.

**Mid-phase external date:** the GATE 2028 brochure is expected around **Jul/Aug 2027**. The monthly reviews in Weeks 45 and 50 check for it, then re-verify `syllabus.md` and `exam-info.md`.

---

## Phase Goals (end-of-phase state)

- [ ] Syllabus rows CN-1 … CN-11, TC-1 … TC-8, CD-1 … CD-8 at confidence ≥3
- [ ] **Every syllabus row in `trackers/subjects.md` has "lecture done = yes" and "short notes = yes"**
- [ ] PYQ accuracy ≥60% in CN, TOC, CD
- [ ] Formula sheets complete: `cn.md`, `toc.md`, `compiler.md` (all 10 subject sheets now exist)
- [ ] 13 interleaved quizzes done, average ≥65%
- [ ] GA mixed-set score ≥12/15
- [ ] Adherence ≥70%

---

## How to Read the Weekly Tables

Same conventions as Phase 3. **Wed PM = 30-min interleaved quiz (subject named) + 60-min lecture.**

---

## Weekly Breakdown

### Week 37 — CN: Layering, Switching, Performance Metrics (2027-05-24 → 2027-05-30)
**Hours: 19** | **Topics: CN-1, CN-2** | **GA rotation 1: Numerical computation** | **Interleaved quiz: COA**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; mixed DBMS PYQs for the weakest DB topic (top-up). Map CN playlist → Weeks 37–41 | GO PYQs; GO Classes CN | Error log; mapping |
| Mon | PM | Lecture: principles of layering — OSI vs TCP/IP, encapsulation, PDUs, which device operates at which layer | GO Classes Computer Networks | `notes/cn/cn-01-layering.md` |
| Tue | AM | PYQs: layering, layer responsibilities | GO tag network-layering | Daily log + error log |
| Tue | PM | Lecture: switching — circuit vs packet vs virtual circuit, datagram networks, message vs packet switching | GO Classes Computer Networks | `notes/cn/cn-02-switching-performance.md` |
| Wed | AM | PYQs: switching comparisons | GO tag network-switching | Daily log + error log |
| Wed | PM | **Interleaved quiz: COA (30 min)** → Lecture: delays — transmission, propagation, queuing, processing | Quiz: pre-2000 COA PYQs; GO Classes CN | Quiz score in `trackers/revision.md`; `cn-02` |
| Thu | AM | PYQs: delay calculations (NAT) | GO tag communication | Daily log + error log |
| Thu | PM | Lecture: throughput, bandwidth, utilisation, multi-hop store-and-forward delay, packet vs message switching total delay | GO Classes Computer Networks | `cn-02` (complete) |
| Fri | AM | PYQs: throughput / total delay (NAT) | GO tag communication | Daily log + error log |
| Fri | PM | Start `notes/formula-sheets/cn.md` (delay + throughput); worked multi-hop problems | Own notes / backup: NPTEL CN & IP | Formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs CN-1, CN-2 + 5 DBMS carry-over | GO PYQs (odd years) | Topic test T37 |
| Sat | 11:00–12:00 | GA rotation 1 — Numerical computation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: DBMS formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #37 **+ Monthly review (May 2027)** | — | `reviews/weekly/2027-05-24-to-2027-05-30.md` + `reviews/monthly/2027-05.md` |

---

### Week 38 — CN: Data Link Layer — Error Detection + Sliding Window (2027-05-31 → 2027-06-06)
**Hours: 19** | **Topics: CN-3, CN-4** | **GA rotation 2: Grammar** | **Interleaved quiz: Operating Systems**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CN-1, CN-2 | GO PYQs | Error log |
| Mon | PM | Lecture: framing (bit / byte stuffing); error detection — parity, 2D parity | GO Classes Computer Networks | `notes/cn/cn-03-error-detection.md` |
| Tue | AM | PYQs: stuffing, parity | GO tag error-detection | Daily log + error log |
| Tue | PM | Lecture: CRC (polynomial division, detection capability), checksum, Hamming distance + Hamming code | GO Classes Computer Networks | `cn-03` (complete) |
| Wed | AM | PYQs: CRC remainder / transmitted frame (NAT), Hamming distance | GO tag crc-polynomial | Daily log + error log |
| Wed | PM | **Interleaved quiz: OS (30 min)** → Lecture: stop-and-wait ARQ, efficiency, timeouts | Quiz: pre-2000 OS PYQs; GO Classes CN | Quiz score; `notes/cn/cn-04-sliding-window.md` |
| Thu | AM | PYQs: stop-and-wait efficiency (NAT) | GO tag sliding-window | Daily log + error log |
| Thu | PM | Lecture: Go-Back-N + Selective Repeat — window sizes vs sequence-number bits, retransmissions count | GO Classes Computer Networks | `cn-04` |
| Fri | AM | PYQs: GBN / SR windows, retransmissions (NAT) | GO tag sliding-window | Daily log + error log |
| Fri | PM | Sliding-window efficiency, piggybacking; formula sheet (CRC, windows) | GO Classes CN / Own notes | `cn-04` (complete) + `notes/formula-sheets/cn.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs CN-3, CN-4 | GO PYQs (odd years) | Topic test T38 |
| Sat | 11:00–12:00 | GA rotation 2 — Grammar | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #38 | — | `reviews/weekly/2027-05-31-to-2027-06-06.md` |

---

### Week 39 — CN: Medium Access Control + Ethernet (2027-06-07 → 2027-06-13)
**Hours: 19** | **Topics: CN-5** | **GA rotation 3: Data interpretation** | **Interleaved quiz: DBMS**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CN-3, CN-4 | GO PYQs | Error log |
| Mon | PM | Lecture: MAC problem; pure + slotted ALOHA (throughput, max efficiency) | GO Classes Computer Networks | `notes/cn/cn-05-mac-ethernet.md` |
| Tue | AM | PYQs: ALOHA throughput (NAT) | GO tag mac-protocol | Daily log + error log |
| Tue | PM | Lecture: CSMA variants, CSMA/CD — collision detection, minimum frame size, binary exponential backoff | GO Classes Computer Networks | `cn-05` |
| Wed | AM | PYQs: CSMA/CD minimum frame size (NAT), backoff probability | GO tag mac-protocol | Daily log + error log |
| Wed | PM | **Interleaved quiz: DBMS (30 min)** → Lecture: token passing / token ring, efficiency, early vs delayed token release | Quiz: pre-2000 DBMS PYQs; GO Classes CN | Quiz score; `cn-05` |
| Thu | AM | PYQs: token ring efficiency | GO tag token-ring | Daily log + error log |
| Thu | PM | Lecture: Ethernet — frame format, MAC addressing, min / max frame, switches + bridges (learning, forwarding) | GO Classes Computer Networks | `cn-05` (complete) |
| Fri | AM | PYQs: Ethernet + mixed MAC | GO tag ethernet | Daily log + error log |
| Fri | PM | MAC formula sheet section; worked CSMA/CD + ALOHA problems | Own notes / backup: Gate Smashers CN | `notes/formula-sheets/cn.md` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs CN-5 + 5 sliding-window carry-over | GO PYQs (odd years) | Topic test T39 |
| Sat | 11:00–12:00 | GA rotation 3 — Data interpretation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Algorithms formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #39 | — | `reviews/weekly/2027-06-07-to-2027-06-13.md` |

---

### Week 40 — CN: IPv4, CIDR, Fragmentation, NAT, Routing (2027-06-14 → 2027-06-20)
**Hours: 19** | **Topics: CN-6, CN-7, CN-8** | **GA rotation 4: Logic + reasoning** | **Interleaved quiz: C + Data Structures**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CN-5 | GO PYQs | Error log |
| Mon | PM | Lecture: IPv4 addressing — classful (legacy), CIDR notation, subnet masks, network / broadcast addresses, host counts | GO Classes Computer Networks | `notes/cn/cn-06-ipv4-cidr-subnetting.md` |
| Tue | AM | PYQs: subnet / broadcast address, number of hosts (NAT) | GO tag subnetting | Daily log + error log |
| Tue | PM | Lecture: subnetting + supernetting, variable-length subnets, longest prefix match forwarding | GO Classes Computer Networks | `cn-06` (complete) |
| Wed | AM | PYQs: longest prefix match → interface | GO tag ip-addressing | Daily log + error log |
| Wed | PM | **Interleaved quiz: C + DS (30 min)** → Lecture: IPv4 header, fragmentation (identification, offset, MF flag), NAT | Quiz: pre-2000 PDS PYQs; GO Classes CN | Quiz score; `notes/cn/cn-07-fragmentation-nat.md` |
| Thu | AM | PYQs: fragments + offsets (NAT), NAT | GO tag ip-fragmentation | Daily log + error log |
| Thu | PM | Lecture: distance vector routing — Bellman–Ford updates, count-to-infinity, split horizon / poisoned reverse | GO Classes Computer Networks | `notes/cn/cn-08-routing.md` |
| Fri | AM | PYQs: DV table after updates | GO tag routing | Daily log + error log |
| Fri | PM | Lecture: link state routing — LSP flooding, Dijkstra per router, DV vs LS comparison; formula sheet (CIDR + fragmentation) | GO Classes CN | `cn-08` (complete) + `notes/formula-sheets/cn.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs CN-6 … CN-8 | GO PYQs (odd years) | Topic test T40 |
| Sat | 11:00–12:00 | GA rotation 4 — Logic + reasoning | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #40 | — | `reviews/weekly/2027-06-14-to-2027-06-20.md` |

---

### Week 41 — CN: TCP, UDP, Sockets, DNS, HTTP (2027-06-21 → 2027-06-27)
**Hours: 19** | **Topics: CN-9, CN-10, CN-11** | **GA rotation 5: Vocabulary + reading** | **Interleaved quiz: Engineering Maths**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CN-6 … CN-8 | GO PYQs | Error log |
| Mon | PM | Lecture: TCP — header, 3-way handshake, connection teardown, states, sequence-number wrap-around time | GO Classes Computer Networks | `notes/cn/cn-09-tcp-udp.md` |
| Tue | AM | PYQs: TCP handshake, sequence numbers, wrap-around (NAT) | GO tag tcp | Daily log + error log |
| Tue | PM | Lecture: TCP flow control (receiver window), UDP header + use cases | GO Classes Computer Networks | `cn-09` |
| Wed | AM | PYQs: flow control, UDP | GO tag tcp, udp | Daily log + error log |
| Wed | PM | **Interleaved quiz: Engineering Maths (30 min)** → Lecture: TCP congestion control — slow start, congestion avoidance (AIMD), threshold, timeout vs 3 duplicate ACKs | Quiz: pre-2000 maths PYQs; GO Classes CN | Quiz score; `cn-09` (complete) |
| Thu | AM | PYQs: congestion window after k RTTs (NAT) | GO tag congestion-control | Daily log + error log |
| Thu | PM | Lecture: socket API — TCP server / client call sequence, UDP sockets | GO Classes Computer Networks | `notes/cn/cn-10-socket-api.md` |
| Fri | AM | PYQs: socket call order, mixed TCP | GO tag sockets | Daily log + error log |
| Fri | PM | Lecture: DNS (resolution, recursive vs iterative, records) + HTTP (persistent vs non-persistent, RTT counting) → **finish `notes/formula-sheets/cn.md`** | GO Classes CN | `notes/cn/cn-11-dns-http.md` + formula sheet (complete) |
| Sat | 09:00–11:00 | **CN subject test:** ~30 odd-year PYQs CN-1 … CN-11 | GO PYQs (odd years) | Topic test T41 |
| Sat | 11:00–12:00 | GA rotation 5 — Vocabulary + reading / sequencing | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, CN confidence ratings in `subjects.md` | — | Error log |
| Sun | — | Weekly review #41 **+ Monthly review (June 2027)** | — | `reviews/weekly/2027-06-21-to-2027-06-27.md` + `reviews/monthly/2027-06.md` |

**Resources:**
- GO Classes Computer Networks — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHim3NUSNOb7ffyhaE5MSkmE
- Backup: NPTEL Computer Networks and Internet Protocol — https://nptel.ac.in/courses/106105183
- Reference: Kurose & Ross; Forouzan

---

### Week 42 — TOC: Finite Automata + Regular Expressions (2027-06-28 → 2027-07-04)
**Hours: 19** | **Topics: TC-1, TC-2** | **GA rotation 6: Mensuration + geometry** | **Interleaved quiz: Digital Logic**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CN-9 … CN-11. Map TOC playlist → Weeks 42–46 | GO PYQs; GO Classes TOC | Error log; mapping |
| Mon | PM | Lecture: alphabets, strings, languages; DFA design (divisibility, substring, counting patterns) | GO Classes Theory of Computation | `notes/toc/tc-01-finite-automata.md` |
| Tue | AM | PYQs: DFA for a language, language of a DFA | GO tag finite-automata | Daily log + error log |
| Tue | PM | Lecture: NFA, ε-NFA, subset construction, NFA → DFA state blow-up | GO Classes Theory of Computation | `tc-01` |
| Wed | AM | PYQs: NFA → DFA, states after conversion | GO tag finite-automata | Daily log + error log |
| Wed | PM | **Interleaved quiz: Digital Logic (30 min)** → Lecture: DFA minimisation (partition / table-filling), minimum number of states | Quiz: pre-2000 DL PYQs; GO Classes TOC | Quiz score; `tc-01` (complete) |
| Thu | AM | PYQs: minimum DFA states (NAT) | GO tag minimal-state-automata | Daily log + error log |
| Thu | PM | Lecture: regular expressions — identities, RE → ε-NFA | GO Classes Theory of Computation | `notes/toc/tc-02-regular-expressions.md` |
| Fri | AM | PYQs: RE equivalence, strings in / not in L(RE) | GO tag regular-expression | Daily log + error log |
| Fri | PM | Lecture: FA → RE (state elimination / Arden's theorem); start `notes/formula-sheets/toc.md` | GO Classes TOC / backup: Neso Academy TOC | `tc-02` (complete) + formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs TC-1, TC-2 | GO PYQs (odd years) | Topic test T42 |
| Sat | 11:00–12:00 | GA rotation 6 — Mensuration + geometry | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: CN formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #42 | — | `reviews/weekly/2027-06-28-to-2027-07-04.md` |

---

### Week 43 — TOC: Regular Languages — Closure, Pumping Lemma (2027-07-05 → 2027-07-11)
**Hours: 19** | **Topics: TC-3** | **GA rotation 7: Statistics + probability + PnC** | **Interleaved quiz: COA**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs TC-1, TC-2 | GO PYQs | Error log |
| Mon | PM | Lecture: closure properties of regular languages — union, intersection, complement, concatenation, star, reversal | GO Classes Theory of Computation | `notes/toc/tc-03-regular-languages.md` |
| Tue | AM | PYQs: closure-based questions | GO tag regular-language | Daily log + error log |
| Tue | PM | Lecture: homomorphism, inverse homomorphism, quotient; product construction | GO Classes Theory of Computation | `tc-03` |
| Wed | AM | PYQs: closure under operations (MSQ) | GO tag closure-property | Daily log + error log |
| Wed | PM | **Interleaved quiz: COA (30 min)** → Lecture: pumping lemma for regular languages — statement, proof template | Quiz: pre-2000 COA PYQs; GO Classes TOC | Quiz score; `tc-03` |
| Thu | AM | PYQs: pumping lemma | GO tag pumping-lemma | Daily log + error log |
| Thu | PM | Lecture: identifying regular vs non-regular — standard patterns (aⁿbⁿ, ww, count comparisons, finite-memory test), Myhill–Nerode intuition | GO Classes Theory of Computation | `tc-03` (complete) |
| Fri | AM | PYQs: "which languages are regular?" (MSQ) | GO tag regular-language | Daily log + error log |
| Fri | PM | Decision properties of regular languages + start the **closure / decidability table** in the TOC formula sheet | Own notes | `notes/formula-sheets/toc.md` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs TC-3 + 5 FA carry-over | GO PYQs (odd years) | Topic test T43 |
| Sat | 11:00–12:00 | GA rotation 7 — Statistics + probability + PnC | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #43 | — | `reviews/weekly/2027-07-05-to-2027-07-11.md` |

---

### Week 44 — TOC: Context-Free Grammars + PDA (2027-07-12 → 2027-07-18)
**Hours: 19** | **Topics: TC-4, TC-5** | **GA rotation 8: Spatial aptitude** | **Interleaved quiz: Operating Systems**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs TC-3 | GO PYQs | Error log |
| Mon | PM | Lecture: CFGs — derivations (leftmost / rightmost), parse trees, language generated by a grammar | GO Classes Theory of Computation | `notes/toc/tc-04-cfg.md` |
| Tue | AM | PYQs: language of a grammar | GO tag context-free-grammar | Daily log + error log |
| Tue | PM | Lecture: ambiguity; simplification (useless, ε, unit productions); CNF, GNF — derivation length | GO Classes Theory of Computation | `tc-04` (complete) |
| Wed | AM | PYQs: ambiguity, CNF derivation steps (NAT) | GO tag context-free-grammar | Daily log + error log |
| Wed | PM | **Interleaved quiz: OS (30 min)** → Lecture: PDA — definition, acceptance by final state vs empty stack | Quiz: pre-2000 OS PYQs; GO Classes TOC | Quiz score; `notes/toc/tc-05-pda.md` |
| Thu | AM | PYQs: language accepted by a PDA | GO tag pushdown-automata | Daily log + error log |
| Thu | PM | Lecture: designing PDAs, DPDA vs NPDA (power difference) | GO Classes Theory of Computation | `tc-05` |
| Fri | AM | PYQs: DPDA vs NPDA | GO tag pushdown-automata | Daily log + error log |
| Fri | PM | Lecture: CFG ↔ PDA equivalence (idea level); practice designing grammars for standard languages | GO Classes TOC / backup: NPTEL TOC (Tewari) | `tc-05` (complete) |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs TC-4, TC-5 | GO PYQs (odd years) | Topic test T44 |
| Sat | 11:00–12:00 | GA rotation 8 — Spatial aptitude | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Discrete Maths formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #44 | — | `reviews/weekly/2027-07-12-to-2027-07-18.md` |

---

### Week 45 — TOC: Context-Free Languages (2027-07-19 → 2027-07-25)
**Hours: 19** | **Topics: TC-6** | **GA rotation 9: Mixed timed GA section** | **Interleaved quiz: DBMS**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs TC-4, TC-5 | GO PYQs | Error log |
| Mon | PM | Lecture: CFL closure — union, concatenation, star; not intersection / complement; CFL ∩ regular | GO Classes Theory of Computation | `notes/toc/tc-06-context-free-languages.md` |
| Tue | AM | PYQs: CFL closure (MSQ) | GO tag context-free-language | Daily log + error log |
| Tue | PM | Lecture: pumping lemma for CFLs | GO Classes Theory of Computation | `tc-06` |
| Wed | AM | PYQs: pumping lemma for CFLs | GO tag pumping-lemma | Daily log + error log |
| Wed | PM | **Interleaved quiz: DBMS (30 min)** → Lecture: DCFLs — properties, closure (complement yes, union no), relation to LR grammars | Quiz: pre-2000 DBMS PYQs; GO Classes TOC | Quiz score; `tc-06` |
| Thu | AM | PYQs: DCFL questions | GO tag dcfl | Daily log + error log |
| Thu | PM | Lecture: identifying CFL vs non-CFL (aⁿbⁿcⁿ, ww, counting patterns), membership (CYK idea), decision properties of CFLs | GO Classes Theory of Computation | `tc-06` (complete) |
| Fri | AM | PYQs: "which languages are CFL / DCFL / regular?" (MSQ) | GO tag context-free-language | Daily log + error log |
| Fri | PM | Extend the closure table (regular / DCFL / CFL columns) in the TOC formula sheet | Own notes | `notes/formula-sheets/toc.md` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs TC-6 + 5 regular-language carry-over | GO PYQs (odd years) | Topic test T45 |
| Sat | 11:00–12:00 | GA rotation 9 — one full GA section, 25 min timed, score /15 | GA PYQs | `trackers/aptitude.md` mixed-set score |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #45 **+ Monthly review (July 2027)** — check whether the GATE 2028 brochure is out; if yes, verify `syllabus.md` + `exam-info.md` | — | `reviews/weekly/2027-07-19-to-2027-07-25.md` + `reviews/monthly/2027-07.md` |

---

### Week 46 — TOC: Turing Machines + Decidability (2027-07-26 → 2027-08-01)
**Hours: 19** | **Topics: TC-7, TC-8** | **GA rotation 1: Numerical computation** | **Interleaved quiz: Computer Networks**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs TC-6 | GO PYQs | Error log |
| Mon | PM | Lecture: Turing machines — definition, design, variants (multi-tape, non-deterministic) and their equivalence | GO Classes Theory of Computation | `notes/toc/tc-07-turing-machines.md` |
| Tue | AM | PYQs: TM behaviour | GO tag turing-machine | Daily log + error log |
| Tue | PM | Lecture: recursive vs recursively enumerable languages, closure properties, Chomsky hierarchy (incl. CSL / LBA mention) | GO Classes Theory of Computation | `tc-07` (complete) |
| Wed | AM | PYQs: REC / RE closure, hierarchy | GO tag recursive-and-recursively-enumerable-languages | Daily log + error log |
| Wed | PM | **Interleaved quiz: CN (30 min)** → Lecture: decidability — halting problem, reductions, undecidable problems for each language class | Quiz: pre-2000 CN PYQs; GO Classes TOC | Quiz score; `notes/toc/tc-08-decidability.md` |
| Thu | AM | PYQs: decidability table questions | GO tag decidability | Daily log + error log |
| Thu | PM | Lecture: Rice's theorem — trivial vs non-trivial properties, applications | GO Classes Theory of Computation | `tc-08` (complete) |
| Fri | AM | PYQs: Rice's theorem, mixed decidability (MSQ) | GO tag decidability | Daily log + error log |
| Fri | PM | **Finish `notes/formula-sheets/toc.md`** — full closure table + decidability table + standard languages list; R1 revision of all TOC notes | Own notes | Formula sheet (complete) |
| Sat | 09:00–11:00 | **TOC subject test:** ~30 odd-year PYQs TC-1 … TC-8 | GO PYQs (odd years) | Topic test T46 |
| Sat | 11:00–12:00 | GA rotation 1 — Numerical computation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, TOC confidence ratings in `subjects.md` | — | Error log |
| Sun | — | Weekly review #46 | — | `reviews/weekly/2027-07-26-to-2027-08-01.md` |

**Resources:**
- GO Classes Theory of Computation — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHhXeEdbXsi34ePvUjL8I-Q9
- Backup: Neso Academy TOC — https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev
- Backup: NPTEL Theory of Computation (Raghunath Tewari) — https://onlinecourses.nptel.ac.in/noc21_cs83/preview
- Reference: Peter Linz; Hopcroft–Motwani–Ullman

---

### Week 47 — Compiler Design: Lexical Analysis + Top-Down Parsing (2027-08-02 → 2027-08-08)
**Hours: 19** | **Topics: CD-1, CD-2** | **GA rotation 2: Grammar** | **Interleaved quiz: Algorithms**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs TC-7, TC-8. Map CD playlist → Weeks 47–49 | GO PYQs; GO Classes CD | Error log; mapping |
| Mon | PM | Lecture: compiler phases, symbol table, lexical analysis — tokens, lexemes, patterns, counting tokens, lexical errors | GO Classes Compiler Design | `notes/compiler/cd-01-lexical-analysis.md` |
| Tue | AM | PYQs: token counting (NAT), phase responsibilities | GO tag lexical-analysis | Daily log + error log |
| Tue | PM | Lecture: grammar preparation — left recursion removal, left factoring; FIRST sets | GO Classes Compiler Design | `notes/compiler/cd-02-top-down-parsing.md` |
| Wed | AM | PYQs: FIRST sets, left recursion | GO tag first-and-follow | Daily log + error log |
| Wed | PM | **Interleaved quiz: Algorithms (30 min)** → Lecture: FOLLOW sets, LL(1) parsing table construction | Quiz: pre-2000 Algo PYQs; GO Classes CD | Quiz score; `cd-02` |
| Thu | AM | PYQs: FOLLOW sets, LL(1) table entries | GO tag ll-parser | Daily log + error log |
| Thu | PM | Lecture: LL(1) conflicts — is this grammar LL(1)?; recursive descent parsing | GO Classes Compiler Design | `cd-02` (complete) |
| Fri | AM | PYQs: is the grammar LL(1)? | GO tag ll-parser, parsing | Daily log + error log |
| Fri | PM | Worked FIRST / FOLLOW / LL(1) tables on paper for 3 grammars; start `notes/formula-sheets/compiler.md` | Own notes / backup: NPTEL Compiler Design | Formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs CD-1, CD-2 + 5 TOC carry-over | GO PYQs (odd years) | Topic test T47 |
| Sat | 11:00–12:00 | GA rotation 2 — Grammar | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: COA formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #47 | — | `reviews/weekly/2027-08-02-to-2027-08-08.md` |

---

### Week 48 — Compiler Design: Bottom-Up Parsing + SDT (2027-08-09 → 2027-08-15)
**Hours: 19** | **Topics: CD-3, CD-4** | **GA rotation 3: Data interpretation** | **Interleaved quiz: Discrete Maths**

(15 Aug is a public holiday — if it frees a Sunday-adjacent block, keep it as rest.)

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CD-1, CD-2 | GO PYQs | Error log |
| Mon | PM | Lecture: bottom-up parsing — handles, shift-reduce parsing, shift-reduce / reduce-reduce conflicts; operator precedence parsing | GO Classes Compiler Design | `notes/compiler/cd-03-bottom-up-parsing.md` |
| Tue | AM | PYQs: handles, shift-reduce sequences, operator precedence | GO tag parsing | Daily log + error log |
| Tue | PM | Lecture: LR(0) items, closure / goto, canonical collection, LR(0) table | GO Classes Compiler Design | `cd-03` |
| Wed | AM | PYQs: LR(0) states (NAT), conflicts | GO tag lr-parser | Daily log + error log |
| Wed | PM | **Interleaved quiz: Discrete Maths (30 min)** → Lecture: SLR(1) — FOLLOW-based reduce entries, SLR conflicts | Quiz: pre-2000 DM PYQs; GO Classes CD | Quiz score; `cd-03` |
| Thu | AM | PYQs: SLR(1) conflicts | GO tag slr-parser | Daily log + error log |
| Thu | PM | Lecture: CLR(1) + LALR(1) — LR(1) items, lookaheads, merging states, state counts, parser power hierarchy | GO Classes Compiler Design | `cd-03` (complete) |
| Fri | AM | PYQs: LALR vs CLR states / conflicts (MSQ, NAT) | GO tag lalr-parser | Daily log + error log |
| Fri | PM | Lecture: syntax-directed translation — synthesised vs inherited attributes, S- vs L-attributed, evaluating SDT output | GO Classes Compiler Design | `notes/compiler/cd-04-sdt.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs CD-3, CD-4 | GO PYQs (odd years) | Topic test T48 |
| Sat | 11:00–12:00 | GA rotation 3 — Data interpretation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #48 | — | `reviews/weekly/2027-08-09-to-2027-08-15.md` |

---

### Week 49 — Compiler Design: Runtime, IR, Optimisation, Data Flow + FIRST PASS COMPLETE (2027-08-16 → 2027-08-22)
**Hours: 19** | **Topics: CD-5 … CD-8** | **GA rotation 4: Logic + reasoning** | **Interleaved quiz: TOC**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs CD-3, CD-4 | GO PYQs | Error log |
| Mon | PM | Lecture: runtime environments — activation records, stack allocation, access links, static vs dynamic scoping, parameter passing, heap | GO Classes Compiler Design | `notes/compiler/cd-05-runtime-environments.md` |
| Tue | AM | PYQs: activation records, scoping output | GO tag runtime-environment | Daily log + error log |
| Tue | PM | Lecture: intermediate code — three-address code, quadruples / triples, DAG for expressions, SSA basics | GO Classes Compiler Design | `notes/compiler/cd-06-intermediate-code.md` |
| Wed | AM | PYQs: minimum temporaries / DAG nodes (NAT) | GO tag intermediate-code | Daily log + error log |
| Wed | PM | **Interleaved quiz: TOC (30 min)** → Lecture: basic blocks, control-flow graphs, local optimisation (DAG-based, constant folding, dead code, peephole) | Quiz: pre-2000 TOC PYQs; GO Classes CD | Quiz score; `notes/compiler/cd-07-local-optimisation.md` |
| Thu | AM | PYQs: basic blocks, local optimisation | GO tag code-optimization | Daily log + error log |
| Thu | PM | Lecture: data flow analysis — liveness analysis, constant propagation | GO Classes Compiler Design | `notes/compiler/cd-08-data-flow-analysis.md` |
| Fri | AM | PYQs: live variables, constant propagation | GO tag live-variable | Daily log + error log |
| Fri | PM | Lecture: common subexpression elimination / available expressions → **finish `notes/formula-sheets/compiler.md`** | GO Classes CD | `cd-08` (complete) + formula sheet (complete) |
| Sat | 09:00–11:00 | **Compiler Design subject test:** ~30 odd-year PYQs CD-1 … CD-8 | GO PYQs (odd years) | Topic test T49 |
| Sat | 11:00–12:00 | GA rotation 4 — Logic + reasoning | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + walk the **Phase 4 exit checklist** + full `subjects.md` audit (every row) | — | Exit checklist answers |
| Sun | — | Weekly review #49 + **Phase 4 retrospective + first-pass retrospective** (which subjects need the most Phase 5 time) | — | `reviews/weekly/2027-08-16-to-2027-08-22.md` |

**Resources:**
- GO Classes Compiler Design — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjy3eH_qRImIs5dVUTpr9ga
- Backup: NPTEL Compiler Design (Santanu Chattopadhyay) — https://nptel.ac.in/courses/106105190
- Backup: Ravindrababu Ravula — https://www.youtube.com/channel/UCJjC1hn78yZqTf0vdTC6wAQ
- Reference: Aho, Lam, Sethi, Ullman (Dragon Book)

---

## Daily Quota Cheat Sheet

| Slot | PYQ target | Lecture time |
|------|------------|--------------|
| Mon–Fri AM | 15–20 PYQs + redos (TOC classification MSQs are quick; CN numericals are slow) | — |
| Mon–Fri PM | 0 (Wed: 10-question interleaved quiz) | 60–70 min lecture + 20 min notes |
| Sat 09:00–11:00 | 20–30 odd-year PYQs, timed | — |
| Sat 11:00–12:00 | 20–25 GA questions | — |

---

## Phase-4 Exit Criteria

Before moving to Phase 5 (Mon 2027-08-23), confirm:

- [ ] CN / TC / CD rows at confidence ≥3 in `trackers/subjects.md`
- [ ] **Every syllabus row: lecture done + short notes done**
- [ ] PYQ accuracy ≥60% in CN, TOC, CD
- [ ] CRC, window sizes, CIDR / subnetting, fragmentation, congestion window done in <4 min each
- [ ] Can classify a language as regular / DCFL / CFL / REC / RE and answer closure + decidability questions from memory
- [ ] Can build FIRST / FOLLOW and decide LL(1) / SLR(1) / LALR(1) for a small grammar in <6 min
- [ ] All 10 subject formula sheets exist
- [ ] Adherence ≥70%

If any of these are "no", **extend Phase 4 by 1 week** (out of Phase 5). Don't start revision with a subject that was never finished.
