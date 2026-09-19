# Topic Videos — the actual lecture for each topic

One row per video: **the video itself**, not a playlist and not a channel.
`topic-lectures.md` said *where* to look; this file says *what to watch*, because
"open the C playlist" is not an answer when the C playlist turns out to be nine
videos about structs.

**How these were chosen.** For each topic, YouTube was searched for the topic's
phrase, results were ranked by channel and by title match, and the best three from
three different teachers were kept. **Every id below was then confirmed against
YouTube's oEmbed endpoint**, which rejects anything that does not exist or cannot
be embedded — the title and channel columns are the ones YouTube returned, not the
ones the search page claimed. Nothing here was typed from memory.

**What this does not do:** it matches on titles, not on full video descriptions.
A title that lies will get through. If a link is wrong, delete the row — the
planner falls back to the channel search in `topic-lectures.md` for that topic.

Regenerate with `python webapp/tools/build_videos.py` (all topics) or pass topic
ids to redo only those.

| # | Video ID | Channel | Title |
|---|----------|---------|-------|
| GA-1 | 40NjNyuCC20 | GO Classes for GATE CS | Verbal Aptitude (English Grammar) Part 1 / Many GATE PYQs / English Grammar Concepts for GATE |
| GA-1 | 8fmdqgxu7KI | Unacademy Computer Science | Prepositions / L 7 / Parts of Speech / Udaan Batch / GATE 2022 CSE / Mita Ma'am |
| GA-1 | V2bgxPi2WTI | Husen Naikar | 2 PUC Articles, Prepositions & Subject Verb Agreement/ 4 Marks Fix Question 2025 |
| GA-1 | mAackn9_zMU | Ed Sharpener | Basic introduction to Tenses of English Grammar for GATE general Aptitude. |
| GA-2 | pF0DxztZV48 | BBM English Classes | Many Words from One Word( Word is the Gate of Knowledge), including related words (Phrases, Idioms) |
| GA-2 | HOrU4zQrnds | TalentSprint Aptitude Prep | Idioms and Phrases / Part 2 / Vocabulary / Grammar / English / TalentSprint Aptitude Prep |
| GA-2 | rXjqAYUqO9A | VAIR TISS Community | TISSNET 2024: Top 50 Idioms and Phrases You Must Know  Part 2 / Vocabulary / Verbal Ability |
| GA-2 | e9MnOfg7jbA | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | English Vocabulary for GATE Exam / Vocabulary Words / Learn with Fun / BYJU'S GATE |
| GA-3 | MQ_q8dL3I0E | Unacademy Computer Science | Comprehension / L 54 / Udaan Batch / GATE 2022 CSE / Mita Ma'am |
| GA-4 | hxXA4gTeQRM | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Exponents & Logarithm / Engineering Aptitude for GATE 2021 / Part 2 / Rakesh Talreja / Gradeup |
| GA-4 | -h83f3J1jR4 | PRERANA Scheme | Numerical Computation and Estimation - Series |
| GA-4 | le5D8_q094U | Jobs & Careers | Aptitude Made Easy – Problems on Logarithms Full series, Learn maths #withme #StayHome |
| GA-4 | jhiC0CPbg4s | Advit Mittal | IOCL All Branches Non-Technical Revision / Lecture 1/6 / Ratios, Percentages, Logs & More / 30+ MCQs |
| GA-5 | QrMroHQTnBA | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Data Interpretation / General Aptitude / GATE 2023 / Rakesh Sir |
| GA-5 | VknbMLNXXBY | Vidyagram | UPSSSC PET 2025 / 📊Data Interpretation (Bar Graph) 📈 & Pie Chart / हलवा Solutions/ Aditya Ranjan Sir |
| GA-5 | xtj2ylwGwrg | imran sir maths | Data interpretation Tricks / Pie Chart / How to Solve Data interpretation Questions Easily |
| GA-5 | 3x7yEL78n10 | CVCORP | Data Interpretation(Part -1) // Pie Chart // Most Frequently Asked Questions in TCS NQT #cvcorp |
| GA-6 | FQlBpl3DE9Y | BYJU'S Exam Prep GATE & ESE: CE, ME & XE | Mensuration & Geometry / General Aptitude / GATE 2023 Exam / Rakesh Sir |
| GA-6 | Zgz4vEAfAA0 | Education 4u | Mensuration Circle / Aptitude / Part-13 / Pratik Shrivastava |
| GA-7 | Q_u3Lt5AV3c | Gate Smashers | Lec-1: Fundamental Principle Of Counting (Basic Permutation) / Probability and Statistics |
| GA-7 | 2iH-An5dKA4 | CSE concepts with Parinita | 20. Probability and Statistics for gate / Probability aptitude tricks/ Permutations and Combinations |
| GA-7 | lhbuJ5i0sgo | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Principle of Counting / Permutations & Combinations / GATE, ESE & PSU 2023 Exam / Rakesh Talreja |
| GA-7 | o-1_ajA3RqI | Unacademy Computer Science | Probability / Lec 9 / General Aptitude / Sankalp Batch / GATE 2021 CSE |
| GA-8 | taDtnU4CyWk | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Deductive Reasoning / General Aptitude / NIELIT & ISRO 2023 / BYJU'S GATE |
| GA-8 | vfOk8LAah0E | S Chand Academy | Logic / PART-I: VERBAL REASONING / Section-II: Logical Deduction / Chapter-1 / Reasoning |
| GA-9 | pxsVnSTMDrg | GO Classes for GATE CS | Spatial Aptitude / Transformation of shapes / GO Classes |
| GA-9 | J5JqXvOu6Wg | EXAM DOST - Ankit Goyal | Transformation of shapes Translation, Rotation, Scaling, Reflection / General Aptitude / GATE 2024 |
| GA-9 | Y3pezDnMlOo | BIOTECHWALI-Nidhi Sharma | Lec 2 : SCALING OF SHAPES / SPATIAL APTITUDE // GENERAL APTITUDE // GATE2024 #gate |
| GA-9 | XWZiaurdYgA | PRERANA Scheme | Spatial Aptitude: Transformation of Shapes |
| DL-1 | 2t2mQMcUNGo | Gate Smashers | Lec-15: Ranges of Sign Magnitude, 1’s & 2’s Complement / Number System |
| DL-1 | 1k71RxUtgUY | Neso Academy | Data Representation using Signed Magnitude |
| DL-1 | 7dhxySvTCbY | Sudhakar Atchala | Signed and Unsigned binary number representation / Sign magnitude / One's complement / Two's /DLD/CO |
| DL-2 | 7towQUO9aZI | Neso Academy | Overflow in Signed and Unsigned Numbers |
| DL-2 | XV91bg6KvmQ | Gate Smashers | Lec-6 What are Signed & Unsigned Numbers / Arithmetic Operations / Number system |
| DL-2 | xzah5O_93ZU | NPTEL-NOC IITM | #15 Machine Representation of Numbers / Overflow / Underflow / Condition Number |
| DL-3 | TaDrBnRS0_Q | Neso Academy | IEEE 754 - Single and Double Precision |
| DL-3 | 4gNs7B4ZTjc | Gate Smashers | Lec-10: Floating Point Representation with examples / Number System |
| DL-3 | T_Wxrp-2DZQ | Last moment tuitions | Floating Point Number Representation in IEEE 754 in Hindi / COA Lectures |
| DL-4 | fV6YWEJhP-M | GO Classes for GATE CS | Boolean Functions whose Complement & Dual are Same / Boolean Algebra / Digital Logic / Deepak Poonia |
| DL-4 | 3LwfL2u6GXY | Sudhakar Atchala | Minterms and Maxterms in Boolean Algebra // SOP // POS / Digital Logic Design / Digital Electronics |
| DL-4 | GmY4Gz-WL7Y | Gate Smashers | Lec-9: Self Dual Function / How to find Self Dual Function of Any Boolean Expression with 1 variable |
| DL-5 | V9aV2qTSlFg | Gate Smashers | Lec -14: Essential Prime Implicants vs Prime Implicants / K-Map Minimization with examples |
| DL-5 | l1jgq0R5EwQ | Neso Academy | Quine-McCluskey Minimization Technique (Tabular Method) |
| DL-5 | Yq4pbtvVoaQ | Unacademy Computer Science | Quine- McCluskey METHOD (TABULAR METHOD) With Don’t care-lect35 |
| DL-6 | zm71wFsj-fs | Gate Smashers | Lec -15: Half Adder / Combinational Circuits /Digital Electronics |
| DL-6 | u863cwgdlnA | Neso Academy | Full Adder Implementation using Decoder |
| DL-6 | tvXOTfBnPtM | One Bit Extra | Combinational Circuits: Adders, Subtractors, Multiplexer, Demultiplexer, Encoder & Decoder for BCA |
| DL-6 | Ik0Usp4KHTU | Sudhakar Atchala | Half Adder // Combinational Circuit // Digital Logic Design // Digital Electronics // DLD // DE |
| DL-7 | ij2CY8PmWoM | Gate Smashers | Lec - 31: SR flip flop Characteristic & Excitation Table / Sequential Circuits |
| DL-7 | ntiv1g7G_C4 | Neso Academy | Analysis of Clocked Sequential Circuits (with D Flip Flop) |
| DL-7 | _ViCif5u0Lg | Sudhakar Atchala | SR latch using NAND gate // Flip Flops // Digital Logic Design(DLD) // Digital Electronics (DE) |
| DL-8 | sdQO4ryAovs | Gate Smashers | Lec - 42: Synchronous vs Asynchronous counter / Digital Electronics |
| DL-8 | 5vkWccb7uO4 | Neso Academy | How to Design Synchronous Counters / 2-Bit Synchronous Up Counter |
| DL-8 | 9J_ageaT3Rw | Sudhakar Atchala | Synchronous vs Asynchronous Counters // Differences // What is //Digital Logic Design // Electronics |
| CO-1 | BMNbc3Rbs80 | GO Classes for GATE CS | Expanding Opcode Technique - ALL GATE PYQs / GATE CSE 2020, 2018, 1992, 1988 / Computer Architecture |
| CO-1 | u-sp4gBAJKI | Gate Smashers | L-1.17: Register Stack Organisation / Zero Address Instructions / COA |
| CO-1 | PJdrDp6DXEQ | Prof. Ravindrababu Ravula | COA / Machine Instructions & Addressing Modes / Computer organization based on Registers / RBR |
| CO-2 | M7nHnMEuQRY | GO Classes for GATE CS | Addressing Modes Part 1 / Direct, Indirect, Immediate, Register Addressing Modes / with NOTES |
| CO-2 | 5A677So9epQ | Gate Smashers | L-2.7: Direct Addressing Mode // Computer Organization and Architecture |
| CO-2 | EyTpOjoIqdA | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Addressing Modes and Applications / Computer Organization Architecture (COA) / GATE CSE 2023 |
| CO-3 | meSn0UXmgac | Neso Academy | The Concept of Booth’s Algorithm |
| CO-3 | M0znE3jqaxs | Gate Smashers | L-1.9: Arithmetic Instructions(Data Manipulation) in Computer Organisation and Architecture |
| CO-3 | DIp4GqSCZho | Education 4u | Booths algoritham in Computer Organization / Multiplication / COA / Lec-31 / Bhanu Priya |
| CO-4 | OXz7wKHr0_I | Gate Smashers | L-1.12: Program Control Instructions(Types of Control Instructions) / Computer Organization |
| CO-4 | 7QJxchHoa_w | Unacademy Computer Science | COA / Control Unit: Hardwired & Microprogrammed / Lec 7 / GATE CSE/IT 2021 Crash Course |
| CO-4 | Bsh_WYIlLXs | Sudhakar Atchala | Timing and Control // Design Of Hardwired Control Unit // Computer Organization |
| CO-5 | v49Qv5CrgdY | GO Classes for GATE CS | Average Memory Access Time AMAT - Part 1 / Cache Memory / Complete Lecture |
| CO-5 | lQcU4WwVALI | Neso Academy | Memory Hierarchy & Interfacing |
| CO-5 | zwovvWfkuSg | Gate Smashers | L-3.1: Memory Hierarchy in Computer Architecture / Access time, Speed, Size, Cost / All Imp Points |
| CO-6 | e8ZrvrNdp9o | Gate Smashers | L-3.15: FIFO Cache Replacement Policy with example / Computer Organisation and Architecture |
| CO-6 | OxaYvJquPe0 | Neso Academy | Direct Memory Mapping – Solved Examples |
| CO-6 | beqOrVgxsA0 | Sudhakar Atchala | Cache Memory //Direct Mapping/Associative Mapping-Set Associative-Computer Organization Architecture |
| CO-7 | udZi6uiR8bM | Gate Smashers | L-6.2: Disk Access Time with Example / Seek Time, Rotational Time and Transfer Time |
| CO-7 | YGOlvcTlrYc | Neso Academy | Hard Disk Drives (Solved Problems) - Set 3 |
| CO-7 | JZCBuVJGvcg | Unacademy Computer Science | Magnetic Disk: Platter, Track, Sector, Access Time / L-42 / COA 2.0 / GATE 2022 / Vishvadeep Gothi |
| CO-8 | qhbgkyi_fbw | Gate Smashers | Question on DMA (Direct Memory Access) / Input/Output Organization/ COA / UGC NTA NET June 2021 |
| CO-8 | VMIFc5y3peE | GO Classes for GATE CS | I/O Interfacing Lec 1 -  I/O Devices, Interface, Memory Mapped I/O, Isolated I/O / With NOTES |
| CO-8 | WGX_Wg79iY0 | Sudhakar Atchala | Interrupt Initiated I/O/Priority/ Daisy Chaining/Parallel Priority Encoder/Cycle / Modes of Transfer |
| CO-9 | R9s34-lnd9k | Gate Smashers | L-4.3: Pipelining Vs Non-Pipelining / Instruction Execution / Speedup, Efficiency, Utilization / COA |
| CO-9 | nMzmke0cyMQ | KnowledgeGATE by Sanchit Sir | Pipelining In Depth / Numericals on Speedup, Efficiency, CPI / Pipelining in Computer Architecture |
| CO-9 | -rwmE49WC_I | NPTEL IIT Guwahati | Instruction Pipeline & Performance - I |
| CO-10 | hM2Srz6EZWU | GO Classes for GATE CS | Pipeline Lec 5 - Control Hazards / Branch Prediction / with NOTES / Pipeline Complete Course |
| CO-10 | qn7zf_OSLsk | Gate Smashers | L-4.7: Structural Hazards in Pipelining / Types of Hazards with Example in Hindi |
| CO-10 | Gp2cwH740O0 | NPTEL IIT Guwahati | Lec 9: Control Hazards and Branch Prediction |
| DM-1 | HcS4lqXxrV4 | Neso Academy | Rules of Inference - Definition & Types of Inference Rules |
| DM-1 | B6xo-2A8ano | GO Classes for GATE CS | Propositional Logic - GATE PYQs Part 1 / Discrete Mathematics / GO Classes / Deepak Poonia |
| DM-1 | dzUXeAmddZE | Gate Smashers | Question on Mathematical Logic / Discrete Maths / UGC NTA NET May/June 2021 |
| DM-1 | udp92HTtVLc | Sudhakar Atchala | Rules of Inference // 8 Solved Examples // Rule P // Rule  T // Rule  CP // DMS // MFCS |
| DM-2 | IeCiksHTzjA | GO Classes for GATE CS | English to First Order Logic Translation Part 3 / Numerical Quantification / Discrete Mathematics |
| DM-2 | UN6Hd4UlrnM | Neso Academy | Quantifiers |
| DM-2 | 8Do6tC7ZDG0 | Sudhakar Atchala | Predicate Logic // Statement  Function  // Quantifiers // Universal  // Existential  // DMS // MFCS |
| DM-2 | ttCEJ59q8WM | Unacademy Computer Science | 15 GATE PYQs on Predicate Logic within 30 Seconds Using 1 Single Trick / Sweta Kumari |
| DM-3 | kSKmoNnXmHM | Gate Smashers | Comparison of All Relations / Reflexive,Irreflexive,Transitive, Symmetric,Antisymmetric, Asymmetric |
| DM-3 | SgQJlKLWJmY | Neso Academy | Closure of Relations – Part 1 |
| DM-3 | 0MMmaOcm6Jc | Education 4u - Hindi | reflexive symmetric transitive relations in hindi / types of relations / Niharika Panda |
| DM-4 | jqaNaJRrg3s | Gate Smashers | ONTO Function(Surjection) / Surjective Function / Discrete Mathematics |
| DM-4 | 6RJt0cvaM1k | GO Classes for GATE CS | Lecture 16 - Bijective Proofs / Combinatorics / Discrete Mathematics / GO Classes / Deepak Poonia |
| DM-4 | cCJ4KoYI6Jg | Sudhakar Atchala | Introduction to Functions in DMS // Definition of Function // Examples of functions // MFCS |
| DM-4 | ojHAAqgW1_M | The Math Sorcerer | Functions, Domain, Codomain, Injective(one to one), Surjective(onto), Bijective Functions |
| DM-5 | h5Lv5ZeNl0g | Gate Smashers | Partial Order Relation / POSET in Discrete Mathematics |
| DM-5 | i8XeVATqeag | Neso Academy | Hasse Diagram |
| DM-5 | nNw8XRbW0_w | KnowledgeGATE by Sanchit Sir | 2.15 / Practice problem on  Partial Order Relations, POSET in HINDI POSET lattice Hasse Diagram |
| DM-6 | Zb4OWjHL3yU | GO Classes for GATE CS | Group Theory - Marathon - Part 3 / ALL in ONE / GATE PYQs |
| DM-6 | _i_XRDXcCJY | Gate Smashers | Algebraic structure in Discrete Mathematics |
| DM-6 | cpYaUnqKXWc | KnowledgeGATE by Sanchit Sir | 2 / Closure property / Algebraic Structures in Discrete Mathematics in HINDI / Group theory |
| DM-7 | Q3MAJAJrgz0 | GO Classes for GATE CS | Lecture 24A - Inclusion Exclusion Principle / Combinatorics / Discrete Mathematics / Deepak Poonia |
| DM-7 | Q_u3Lt5AV3c | Gate Smashers | Lec-1: Fundamental Principle Of Counting (Basic Permutation) / Probability and Statistics |
| DM-7 | 0o3fFWUN90o | Unacademy Computer Science | L- 11 / Problems on Inclusion- Exclusion principle / Combinatorics Complete GATE course / Jay Bansal |
| DM-8 | cjO6uo8rBbE | GO Classes for GATE CS | 55 Fifty-Five Questions on Recurrence Relations / Solving Recurrence Relations with ALL GATE PYQs |
| DM-8 | NW-naslChdo | Gate Smashers | L-2.1: What is Recurrence Relation/ How to Write Binary Search Recurrence Relation/How we Solve them |
| DM-8 | I_sPnRVc2wk | Sudhakar Atchala | First Order linear Homogeneous Recurrence Relations // 2 Solved Examples // DMS // MFCS // GATE |
| DM-9 | uahuw03mX6I | GO Classes for GATE CS | Lecture 25A - Generating Functions Part 1 / Combinatorics / Discrete Mathematics / Deepak Poonia |
| DM-9 | vdiY7aPAd4I | Sudhakar Atchala | Find the Coefficient of Generating Function // Recurrence Relations // Discrete Mathematics // DMS |
| DM-9 | lOA_OpSH1LU | Unacademy Computer Science | L- 16 / Generating Functions / Combinatorics Complete GATE course / Jay Bansal |
| DM-10 | mNzp9uJ9Ehc | GO Classes for GATE CS | Graph Theory Lecture 15 - Euler and Hamiltonian Cycle, Graphs / Discrete Mathematics / Deepak Poonia |
| DM-10 | 5eKDQmTzX2A | Gate Smashers | Introduction to Graph Theory / Basics of Graph Theory / Imp for GATE and UGC NET |
| DM-10 | 052VkKhIaQ4 | Abdul Bari | 6.3 Graph Coloring Problem - Backtracking |
| LA-1 | HOKCXJGgTYw | Gate Smashers | Lec-13: Rank of Matrix (Echelon Form Method) / Linear Algebra |
| LA-1 | rFYr4V3zFxQ | GO Classes for GATE DA | Lecture 20: Projection Matrix / GATE DA /  Linear Algebra  / Sachin Mittal |
| LA-1 | uaZg1tinVVg | ADITYA Higher Mathematics | Properties of Rank of Matrices // CSIR NET mathematics linear algebra // GATE mathematics tricks |
| LA-1 | I5fFV5mz7so | Santoshi Classes | Properties of some special Unitary Matrices Involutory Matrices Idempotent Matrices csir net gate du |
| LA-2 | 2Vz52J4YSMk | Gate Smashers | Lec-7: Properties Of Determinants / Linear Algebra |
| LA-2 | MesPYPsDXMw | GO Classes for GATE CS | Lecture 7a.  Determinant of a Matrix / Linear Algebra / Sachin Mittal / GO Classes |
| LA-2 | Y_Vow9__fwY | NPTEL-NOC IITM | mod02lec14 - Determinants and their properties |
| LA-3 | 0okwJbBHpQY | Gate Smashers | Lec-16: System of Homogeneous Linear Equation / Linear Algebra |
| LA-3 | DaMpZ3IEmwE | NPTEL IIT Kharagpur | Lecture 36: System of Linear Equations |
| LA-3 | zCw9VIkDpTo | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | 51 Most Expected Questions of Linear Algebra (Part-1) (Rank & Linear System of Equations) |
| LA-3 | povS4KL3nR8 | maths voice | Consistency of system of linear equations using rank method |
| LA-4 | Ca6AWNkJaXw | GO Classes for GATE CS | Lecture 8a. Introduction to Eigenvalues and Eigenvectors / Geometric Interpretations /Linear Algebra |
| LA-4 | S97O036JwvQ | Gate Smashers | Lec-19; Cayley-Hamilton Theorem / Linear Algebra |
| LA-4 | Ad8vA5iHstA | Paathshala Pandit | Cayley Hamilton Theorem / Eigenvalues and Eigenvectors / Engineering Mathematics / GATE |
| LA-4 | ungSZ2RHFSA | ArrowSpace Engineering | Matrix Algebra - Eigenvalues & Eigenvectors / Mathematics / Cayley-Hamilton Theorem / GATE |
| LA-5 | PAat5sF1shc | GO Classes for GATE CS | Lecture 11a.  LU Decomposition / Shortcut to Find Decomposition / Linear Algebra / Sachin Mittal |
| LA-5 | QI3sYryDxr8 | NPTEL-NOC IITM | Gauss Jordan and LU Decomposition |
| LA-5 | GguYHV8Xov0 | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | LU Decomposition / Linear Algebra / Engineering Mathematics for GATE 2023 Exam Prep / BYJU'S GATE |
| CA-1 | hA585QAk83s | GO Classes for GATE CS | Limit and Continuity with ALL GATE PYQs / Revision and Practice / Calculus |
| CA-1 | bh2tJyVTc80 | Prof. Ravindrababu Ravula | EM / Calculus / Limits / Introduction to limits / Ravindrababu Ravula / Free GATE CS Classes |
| CA-2 | hA585QAk83s | GO Classes for GATE CS | Limit and Continuity with ALL GATE PYQs / Revision and Practice / Calculus |
| CA-2 | IXft4RWtTlQ | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Continuity & Differentiability / GATE 2023 Engineering Mathematics / Complete Concept / BYJU'S GATE |
| CA-2 | LAMVK-eiqVs | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Continuity & Differentiability / GATE 2023 Engineering Mathematics Questions Practice / BYJU'S GATE |
| CA-3 | BgBeNoD4BSE | GO Classes for GATE DA | Second Derivative Test / Differentiability / Maxima Minima / Concave up or Down / GATE CSE & DA |
| CA-3 | sAGcjqb3qjg | Unacademy Computer Science | Maxima and Minima - 1 / Calculus / Lec 7 / Engineering Mathematics / Sankalp Batch / GATE 2021 |
| CA-3 | CyP9fgrx2Yg | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Maxima & Minima / GATE 2023 Engineering Mathematics / Free Online GATE Concept Class |
| CA-3 | sxXuaDou83c | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Maxima and Minima / GATE Engineering Maths 2023 Exam / Free Online GATE Class - P1 / BYJU'S GATE |
| CA-4 | xcHGp3oKPWE | GO Classes for GATE DA | Intermediate Mean Value Theorem / Rolle's theorem / Lagrange Mean Value Theorem / GATE CSE & DA |
| CA-4 | 0apMXhWG_W8 | NPTEL IIT Kharagpur | Lecture 02: Mean Value Theorems |
| CA-4 | joDPBU51nCM | NPTEL-NOC IITM | 37. Using Rolle’s theorem and Mean valuetheorem - Part 1 |
| CA-5 | QDgVGmvA4GM | NPTEL IIT Kharagpur | Lecture 37: Evaluation of Definite Integrals using Properties of Fourier Transform |
| CA-5 | kENeYEIK52c | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | GATE 2024 / Engineering Mathematics / Definite Integrals / Definite Integrals Properties / BYJU'S |
| CA-5 | 2ODALMaUmc0 | PW English Medium | Definite Integration 02 / Properties of Definite Integrals / Pure English / 12th / JEE\CUET |
| CA-5 | yMAyao2BBAE | Apni Kaksha Official | 6.. Properties of Definite Integrals / Integration / Class 12 Maths |
| PS-1 | yFgJUb7fzfs | GO Classes for GATE DA | Probability for GATE DA/CS: L8 / Bayes Theorem & GATE PYQ's / Sachin Mittal / Ex Amazon |
| PS-1 | SktJqrYereQ | Gate Smashers | Lec-48: Bayes Theorem & Total Probability with Examples |
| PS-1 | SfVwSAQyGmk | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Bayes Theorem Probability / Engineering Mathematics / Probability for GATE 2024 / BYJU'S GATE |
| PS-2 | tYOdYmzBZyY | GO Classes for GATE CS | Marathon Series : EM / Topic Random Variables In Probability |
| PS-2 | 2n1hapVMHL0 | Gate Smashers | Lec-15: Random Variable / Probability and Statistics |
| PS-2 | 4nTkK5C3ObU | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Discrete Random Variables / Probability & Distributions / GATE Engineering Mathematics / BYJU'S GATE |
| PS-3 | ecY2x1xU1mE | Gate Smashers | Lec-19: Mean, Median & Mode / Probability and Statistics |
| PS-3 | gztHr1btVa8 | NPTEL IIT Guwahati | Lec 73: Probability Distribution and Basic Descriptive Statistics |
| PS-3 | EQoiuJIBwMI | NPTEL IIT Bombay | Week 1: Lecture 2: Descriptive Statistics-II |
| PS-3 | W8NaUtkM46o | The Organic Chemistry Tutor | Data & Statistics - Mean, Median, Mode, Range, & Standard Deviation - SAT Math Part 44 |
| PS-4 | zv7_EwPyzCo | Gate Smashers | Lec-20: Poisson Distribution / Probability and Statistics |
| PS-4 | Mo0VeTHGKLY | NPTEL IIT Delhi | Common Discrete Distributions |
| PS-4 | IE1tDUnzJQw | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Binomial & Poisson / Probability and Distributions / GATE Engineering Mathematics / BYJU'S GATE |
| PS-5 | RVDDgjgNPM4 | GO Classes for GATE DA | Probability for GATE DA/CS: L40 / Exponential Distribution / Sachin Mittal / Ex Amazon |
| PS-5 | gxQOaeoQ3Sk | Gate Smashers | Lec-25: General Continuous Distribution / Probability and Statistics |
| PS-5 | OQNTi4D2tfE | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Continuous Random Variables / Probability and Distributions / GATE Engineering Mathematics / BYJU'S |
| PD-1 | 8H9G621pQq0 | Neso Academy | Precedence and Associativity of Operators |
| PD-1 | ql2F5Am3_9E | Gate Smashers | Typecasting in C programming / Implicit & Explicit type conversions |
| PD-1 | WGQRInmOBM8 | Neso Academy | Logical Operators in C |
| PD-2 | jaiKkW2j2Wo | Gate Smashers | Introduction to Storage Classes in C &  its types / Programming in C Language |
| PD-2 | 1ZicYbTSAD4 | Unacademy Computer Science | Storage Classes / Auto Extern Register Static / L 13 / GATE 2024/25 / C Language / Vishvadeep Gothi |
| PD-2 | H68DUS--mUY | Neso Academy | Static and Dynamic Scoping (Solved Question 2) |
| PD-3 | N9-FbTtFwH4 | Gate Smashers | Array & Pointers in C Programming with examples |
| PD-3 | b3G9RjG4l2s | Neso Academy | Declaring & Initializing Pointers in C |
| PD-3 | IuDJeGqEZ3A | Jenny's Lectures CS IT | C_71 Pointers in C - part 1/ Introduction to pointers in C / C Programming Tutorials |
| PD-4 | F4N9pLFN7Os | GO Classes for GATE CS | Pointer Summary 2: Array initialisation / Char Array vs Strings in C |
| PD-4 | cqX54iGlqBY | Gate Smashers | Array of Pointers, Character Array in C Programming with examples / C language in Hindi |
| PD-4 | AefKSoNpZtQ | Neso Academy | Array of Strings |
| PD-5 | kepBmgvWNDw | Neso Academy | Recursion in C |
| PD-5 | azXr6nTaD9M | Gate Smashers | Recursion in Programming / Smallest Recursive Program / Recursion using stack |
| PD-5 | KQZIBckWK-s | Jenny's Lectures CS IT | C_104 Recursion in C / Introduction to Recursion |
| PD-6 | TqmvFpwke34 | Gate Smashers | Union in C programming / Structure vs Union |
| PD-6 | qG0wUzuBI_A | Neso Academy | Releasing the Dynamically Allocated Memory using free() |
| PD-6 | XZO-h8Alfp4 | Unacademy Computer Science | Structure and Union in C Programming / Lecture 10 / GATE 2024/25 / C Language / Vishvadeep Gothi |
| PD-6 | 18TvrtTg2cE | Gate Smashers | Malloc() in C Programming / Dynamic Allocation |
| PD-7 | mzfhcfa0Ra0 | Gate Smashers | Lec-7: 3D Arrays / Addressing in 3D Arrays / Row Major Order |
| PD-7 | MJZd6uPi88E | Abdul Bari | Row-Major and Column-Major Mapping |
| PD-7 | 3fOPOUnkcdQ | Neso Academy | Processing the Multidimensional Array Elements (or) Address Arithmetic of Multidimensional Arrays |
| PD-8 | XfX5jlzWQsg | Neso Academy | Application of Stacks (Infix to Postfix) - Part 1 |
| PD-8 | N1Sr-j-cf4c | Gate Smashers | Lec-40: Infix to postfix Conversion using Stack / Infix➡️Postfix Conversion with examples |
| PD-8 | o6vj5l_W2h8 | Jenny's Lectures CS IT | 3.9 Evaluation of Prefix and Postfix expressions using Stack / Data Structures |
| PD-9 | HqPJF2L5h9U | Abdul Bari | 2.6.3 Heap - Heap Sort - Heapify - Priority Queues |
| PD-9 | YMzZTTO2MpE | Gate Smashers | Lec-46: Introduction to Queue Data structure with real life example / Data Structure #queue |
| PD-9 | D80AB1WkzRk | Neso Academy | Queues / Chapter-7 / Data Structures / nesoacademy.org |
| PD-10 | Sn_9Nrrks0w | Gate Smashers | Lec-79: Deletion in Linked List |
| PD-10 | jgqg6Qw68_Q | Neso Academy | Single Linked List (Inserting a Node at the Beginning) |
| PD-10 | 7yNUXcOcHwE | Jenny's Lectures CS IT | 2.12 Deletion from Doubly Linked List (beginning,end,specific position) / Data Structures Tutorials |
| PD-11 | 226yEA0fWmA | GO Classes for GATE CS | Lecture 1: Binary Trees PYQs / DS and Algorithms PYQ Series / MANY GATE PYQs |
| PD-11 | z0Vnno96_MA | Gate Smashers | Lec-52: Introduction to Trees / Binary Tree, Almost Complete Binary Tree, Full BT, Complete |
| PD-11 | aZjYr87r1b8 | Abdul Bari | 10.2  B Trees and B+ Trees. How they are useful in Databases |
| PD-12 | sXABdGalFNg | Gate Smashers | Lec-53: Binary Search Tree in Data Structure / Insertion and Traversal in BST |
| PD-12 | jDM6_TnYIqE | Abdul Bari | 10.1 AVL Tree - Insertion and Rotations |
| PD-12 | 226yEA0fWmA | GO Classes for GATE CS | Lecture 1: Binary Trees PYQs / DS and Algorithms PYQ Series / MANY GATE PYQs |
| PD-13 | 8noP3YjjJCM | Gate Smashers | L-3.16: Build Heap in O(n) time complexity / Heapify Method / Full Derivation with example |
| PD-13 | HqPJF2L5h9U | Abdul Bari | 2.6.3 Heap - Heap Sort - Heapify - Priority Queues |
| PD-13 | Q_eia3jC9Ts | Jenny's Lectures CS IT | 7.9 Heap Sort / Heapify Method / Build Max Heap Algorithm / Sorting Algorithms |
| PD-14 | N2P7w22tN9c | Gate Smashers | L-4.15: BFS & DFS / Breadth First Search / Depth First Search / Graph Traversing / DAA |
| PD-14 | pcKY4hjDrxk | Abdul Bari | 5.1 Graph Traversals - BFS & DFS -Breadth First Search and Depth First Search |
| PD-14 | vf-cxgUXcMk | Jenny's Lectures CS IT | 6.2 BFS and DFS Graph Traversals/ Breadth First Search and Depth First Search / Data structures |
| AL-1 | 7dz8Iaf_weM | Gate Smashers | L-1.3: Asymptotic Notations / Big O / Big Omega / Theta Notations / Most Imp Topic Of Algorithm |
| AL-1 | A03oI0znAoc | Abdul Bari | 1.8.1 Asymptotic Notations Big Oh - Omega - Theta #1 |
| AL-1 | -uO5ngF9WuY | Neso Academy | Big Omega and Big Theta Notations (Solved Problems) |
| AL-2 | FBKjvXGGCJM | Gate Smashers | L-2.6: Recurrence Relation [ T(n)= 8T(n/2) + n^2 ] / Master Theorem / Example#1 / Algorithm |
| AL-2 | cjO6uo8rBbE | GO Classes for GATE CS | 55 Fifty-Five Questions on Recurrence Relations / Solving Recurrence Relations with ALL GATE PYQs |
| AL-2 | OynWkEj0S-s | Abdul Bari | 2.4.1 Masters Theorem in Algorithms for Dividing Function #1 |
| AL-3 | gBz44smaa9A | Gate Smashers | L-1.6: Time Complexities of all Searching and Sorting Algorithms in 10 minute / GATE & other Exams |
| AL-3 | Il45xNUHGp0 | Jenny's Lectures CS IT | 7.13 Radix Sort - Easiest explanation with Code / Sorting Algorithms / Data Structures Tutorials |
| AL-3 | 7h1s2SojIRw | Abdul Bari | 2.8.1  QuickSort Algorithm |
| AL-4 | go45eeMrwA4 | Gate Smashers | L-6.5: Imp Question on Hashing / Linear Probing for Collision in Hash Table / GATE Questions |
| AL-4 | htO1CUf0YQ0 | Sudhakar Atchala | collision resolution techniques/Separate Chaining/open addressing/linear probing/Quadratic/Double |
| AL-4 | zeMa9sg-VJM | Jenny's Lectures CS IT | 8.1 Hashing Techniques to Resolve Collision/ Separate Chaining and Linear Probing / Data structure |
| AL-5 | tWCaFVJMUi8 | Gate Smashers | L-3.1: How Quick Sort Works / Performance of Quick Sort with Example / Divide and Conquer |
| AL-5 | mB5HXBb_HY8 | Abdul Bari | 2.7.2.  Merge Sort Algorithm |
| AL-5 | FDRqYdjDMMc | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Divide and Conquer - Merge Sort and Quick Sort / Algorithms / GATE Computer Science (CSE) 2023 |
| AL-6 | uDS8AkTAcIU | Gate Smashers | L-4.3: Huffman Coding Algorithm in Hindi with Example / Greedy Techniques(Algorithm) |
| AL-6 | co4_ahEDCho | Abdul Bari | 3.4 Huffman Coding - Greedy Method |
| AL-6 | xZfmHVi7FMg | Jenny's Lectures CS IT | Fractional Knapsack Problem using Greedy Method / Example / Data structures and algorithms |
| AL-7 | pcKY4hjDrxk | Abdul Bari | 5.1 Graph Traversals - BFS & DFS -Breadth First Search and Depth First Search |
| AL-7 | N2P7w22tN9c | Gate Smashers | L-4.15: BFS & DFS / Breadth First Search / Depth First Search / Graph Traversing / DAA |
| AL-7 | vf-cxgUXcMk | Jenny's Lectures CS IT | 6.2 BFS and DFS Graph Traversals/ Breadth First Search and Depth First Search / Data structures |
| AL-8 | W2eDnCoCTuc | GO Classes for GATE CS | Minimum Spanning Trees / Prims and Kruskal's algorithm / ALL Tricky PYQs / GATE CSE and DA / InDepth |
| AL-8 | _KX8GDvRzBc | Gate Smashers | L-4.9: Prim's Algorithm for Minimum Cost Spanning Tree / Prims vs Kruskal |
| AL-8 | 4ZlRH0eK-qQ | Abdul Bari | 3.5 Prims and Kruskals Algorithms - Greedy Method |
| AL-9 | SiI03wnREt4 | Gate Smashers | L-4.13: Bellman Ford Algorithm / Dijkstra's Vs Bellman Ford / Single Source Shortest Path |
| AL-9 | 2raV0H9KqY8 | Abdul Bari | Shortest Path Algorithms (Dijkstra and Bellman-Ford)  - Simplified |
| AL-9 | Gc4mWrmJBsw | Jenny's Lectures CS IT | 6.15 Floyd Warshall Algorithm All Pair Shortest Path algorithm / Data Structures and Algorithms |
| AL-10 | prx1psByp7U | Abdul Bari | 4.3 Matrix Chain Multiplication - Dynamic Programming |
| AL-10 | i8NqAEsZn54 | Gate Smashers | L-5.3: 0/1 Knapsack Problem /Dynamic Programming /Recursive Equation /Recursion Tree Time Complexity |
| AL-10 | yfUrkU4EjJ4 | KnowledgeGATE by Sanchit Sir | Longest Common Subsequence / LCS / Dynamic Programming / Design and Analysis of Algorithms |
| OS-1 | IFEFVXvjiHY | Neso Academy | fork() and exec() System Calls |
| OS-1 | ixq5cpdEO2Q | Gate Smashers | L-1.8: Fork System call with Example / Fork() system call questions |
| OS-1 | clYXGBVuEgE | Sudhakar Atchala | Process Control Block In Operating Systems //  PCB In OS  //   Process In operating systems |
| OS-2 | -NONm-Jq34Y | Gate Smashers | L-1.12: User Level Vs Kernel Level Thread in Operating System / All Imp Points |
| OS-2 | aq2ZiD6ztZI | GO Classes for GATE CS | System Calls, Fork-exec, and Threads /  GATE PYQs / Most Conceptual Revision / Operating System |
| OS-2 | HW2Wcx-ktsc | Neso Academy | Multithreading Models & Hyperthreading |
| OS-2 | AvsXoy9rstY | Unacademy Computer Science | Threads & Multithreading / L 12 / Operating System / GATE 2022 #VishvadeepGothi |
| OS-3 | MZdVAVMgNpA | Gate Smashers | L-2.3: First Come First Serve(FCFS) CPU Scheduling Algorithm with Example |
| OS-3 | 7DoP1L9nAAs | Neso Academy | Scheduling Algorithms - First Come First Served (FCFS) |
| OS-3 | FKyFuP_qvBM | Prof. Ravindrababu Ravula | OS / Process Management / SRTF with processes contains CPU and IO time example 2 / RBR |
| OS-4 | fSMVWmGPqlM | Sudhakar Atchala | Inter Process Communication / Shared Memory  / Message Passing / Operating System / IPC  / OS |
| OS-4 | uHtzOFwgD74 | Neso Academy | Shared Memory Systems |
| OS-4 | 3Eaw1SSIqRg | Gate Smashers | L-3.1: Process Synchronization / Process Types / Race Condition / Operating System-1 |
| OS-5 | qMQsd7Iy5jo | Gate Smashers | L-3.4: Critical Section Problem /  Mutual Exclusion, Progress and Bounded Waiting / Operating System |
| OS-5 | XDIOC2EY5JE | Neso Academy | Semaphores |
| OS-5 | FsiJHTOJANg | GO Classes for GATE CS | Process Synchronisation - GATE PYQs / Operating System Revision / GO Classes / Sachin Mittal |
| OS-6 | k8BHyy6gBls | Gate Smashers | L-4.6: GATE 2018 Question on Banker's Algorithm / Deadlock avoidance / Operating System |
| OS-6 | 2-7JGoy52Qo | Jenny's Lectures CS IT | Lec25 Deadlock Detection and Recovery : Wait-for Graph and Banker's algorithm / Operating System |
| OS-6 | 5LfAco9JbCE | Unacademy Computer Science | Deadlock Avoidance & Banker's Safety Algorithm / L 23 / Operating System / GATE 2022 CSE |
| OS-7 | yP89YlEGCqA | Gate Smashers | L-6.4: FCFS in Disk scheduling with Example / Operating System |
| OS-7 | dEt7mr9R_Z8 | Last moment tuitions | FCFS SSTF SCAN CSCAN LOOK CLOOK Solved Example in Hindi / Disk Scheduling Sums / OS Lectures |
| OS-7 | p48PdudrrgU | Sudhakar Atchala | FCFS Disk Scheduling Algorithm // Operating System / OS |
| OS-8 | N3rG_1CEQkQ | Gate Smashers | L-5.5: First Fit, Next Fit, Best Fit, Worst fit Memory Allocation / Memory Management / OS |
| OS-8 | UbRdxUnn_q4 | Unacademy Computer Science | Memory Management: Contiguous Technique / L 28 / Operating System / GATE 2022 CSE #VishvadeepGothi |
| OS-8 | Ppar8irEAFE | Parul's E-Diary | 47. Translation Lookaside Buffer(TLB), Inverted Page Table, Multilevel Page Table //  Paging Issues |
| OS-8 | LSZw2Km_nHo | CSE Gawd - English | Multi-Level & Inverted Paging, TLB, Segmentation in Operating System / English |
| OS-9 | pR1uhp--COc | Gate Smashers | L-5.23: Belady's Anomaly in FIFO page Replacement with example / Operating System |
| OS-9 | 3CC7WOwDjac | Sudhakar Atchala | Virtual Memory or Demand Paging or Page Faults in operating systems |
| OS-9 | DXU7SqsYDvg | Jenny's Lectures CS IT | Lec29 Page Replacement Algorithms / LRU and optimal / Operating Systems |
| OS-10 | J6wVO4pvUCw | Gate Smashers | L-7.3: Allocation Methods in operating system in hindi / Contiguous vs NonContiguous |
| OS-10 | l5G3kWVT-Tk | GO Classes for GATE CS | File System Implementation From Scratch / Operating Systems / GO Classes |
| OS-10 | gK6L3v1b8AM | Sudhakar Atchala | Allocation Methods / File Allocation Methods / Contiguous / linked / indexed / chain / os / files |
| DB-1 | WEo3g6Ir-vA | Gate Smashers | Lec-17: Types of Attributes in ER Model / Full Concept / DBMS in Hindi |
| DB-1 | wOD02sezmX8 | Neso Academy | Basic Concepts of Entity-Relationship Model |
| DB-1 | PpT3Hh66nAM | Sudhakar Atchala | ER Model in DBMS // Entity // Attribute // Entity Set // Types of Attributes // Relationship // Degr |
| DB-2 | YTJdBA9wZro | Gate Smashers | Lec-8: Integrity Constraints in Database with Examples |
| DB-2 | uPOGPL2C0_8 | Neso Academy | Relational Model Constraints |
| DB-2 | u9AbgVyV0fI | GO Classes for GATE CS | The Relational Model - Complete Summary & GATE PYQs / ALL In One / DBMS / With NOTES / Deepak Poonia |
| DB-3 | Zzjy-q667r0 | GO Classes for GATE CS | Division Operation in Relational Algebra / BEST Detailed Complete Explanation / DBMS / Deepak Poonia |
| DB-3 | 2Q3B2mrrpAw | Gate Smashers | Lec-57: Rename Operator in Relational Algebra / Database Management System (DBMS) |
| DB-3 | 5qIl-TGGk0g | Neso Academy | Relational Algebra (Division Operation) |
| DB-4 | 4xb6ODQ9XFM | Neso Academy | Tuple Relational Calculus (Formal Definition) |
| DB-4 | SnsrohgiPo0 | Gate Smashers | Lec-58: Tuple Calculus in DBMS with examples |
| DB-4 | h3pJZbed9M8 | GO Classes for GATE CS | Relational Algebra - GATE PYQs / DBMS / With NOTES / Deepak Poonia |
| DB-5 | _yog7h4BokQ | Gate Smashers | Lec-67: SQL Queries and Subqueries (part-1) / Database Management System |
| DB-5 | zb6vXpZVo1E | GO Classes for GATE CS | SQL GATE Questions - Part 1 - Complete Analysis / DBMS / GO Classes / Deepak Poonia |
| DB-5 | 7X1ZospJ5gU | GO Classes for GATE CS | SQL - GATE PYQs - Part 2 - Complete Analysis / DBMS / With NOTES / Deepak Poonia |
| DB-6 | bSdvM_0hzgc | Gate Smashers | Lec-26: Finding Closure of Functional dependency in DBMS / Easiest & Simplest way |
| DB-6 | CmptL647fAA | Prof. Ravindrababu Ravula | Normalization in DBMS / Functional Dependency / Attribute Closure / Candidate Key / Lec 3 / Prof.RBR |
| DB-6 | l8OLJIw8Dq0 | GO Classes for GATE CS | Functional Dependency - ALL GATE CS PYQs / Normalization / DBMS |
| DB-7 | EGEwkad_llA | Gate Smashers | Lec-33: All Normal Forms with Real life examples / 1NF 2NF 3NF BCNF 4NF 5NF / All in One |
| DB-7 | ouhXEFJORTo | GO Classes for GATE CS | Normalization Lecture 2 - 3NF Normal Forms / DBMS / Transitive Dependency / Deepak Poonia |
| DB-7 | O16btnzfuYU | Jenny's Lectures CS IT | Lec 11: Second Normal Form in DBMS / 2NF in DBMS / Normalization in DBMS |
| DB-8 | EbsiJ86T1RE | GO Classes for GATE CS | 32 Questions on Indexes - Primary Index, Clustering Index, Secondary Indexing / DBMS / Deepak Poonia |
| DB-8 | vjrHiaIfOl8 | Gate Smashers | Lec-110: Types Of Indexes / Most Important Video on Indexing |
| DB-8 | O-Mbn6VI1zc | KnowledgeGATE by Sanchit Sir | 5.4 Types of Indexing in DBMS / Primary / Clustered / Secondary / Sparse / Dense |
| DB-9 | V-ayKf1CWQE | Gate Smashers | Lec-118: Order of B+ Tree / Order of Leaf Node & Non Leaf Node in B+Tree |
| DB-9 | aZjYr87r1b8 | Abdul Bari | 10.2  B Trees and B+ Trees. How they are useful in Databases |
| DB-9 | Ay2AbTk_QEg | Jenny's Lectures CS IT | 5.24 Insertion in B-tree of Order 3 / B-Tree Example / Data structures and algorithms |
| DB-10 | g2gZKA8E1yA | Gate Smashers | Lec-94: Irrecoverable Vs Recoverable Schedules in Transactions / DBMS |
| DB-10 | 20qVCnk122k | Unacademy Computer Science | DBMS / Lecture - 28 / Serializable Schedules and Conflict Serializability / Vishvadeep Gothi |
| DB-10 | quz6gV7oDFI | KnowledgeGATE by Sanchit Sir | 8.2 Basic Idea of Transaction in DBMS |
| DB-11 | z8Yqn91akV8 | Gate Smashers | Lec-104: Strict 2PL, Rigorous 2PL and Conservative 2PLSchedule / 2 Phase Locking in DBMS |
| DB-11 | gM76xs2NEgE | GO Classes for GATE CS | Timestamp Ordering Protocol - Complete Summary & 50 Practice Questions / Concurrency Control / DBMS |
| DB-11 | uh2rEWZnztY | Unacademy Computer Science | DBMS / Lecture - 31 / Locking Protocols: Shared & Exclusive Locks / Vishvadeep Gothi / GATE 2023 |
| CN-1 | rW1jPlYgp_0 | Gate Smashers | Lec-41: Network Layer / Responsibilities of Network Layer / OSI Model / Computer Networks |
| CN-1 | FewtLNsjtRA | Neso Academy | Layering in Computer Networks |
| CN-1 | APVCgkqWcQ4 | KnowledgeGATE by Sanchit Sir | Computer Networks / CN in one shot / Complete GATE Course / Hindi #withsanchitsir |
| CN-2 | _0mE6PH1E4c | Gate Smashers | Lec-18: Packet Switching In Computer Networks / Imp for GATE and UGC NET |
| CN-2 | -HlJ4psu5aU | Neso Academy | Switching Techniques in Computer Networks |
| CN-2 | W0K_LR4_Q7E | Education 4u | Packet switching / CN / Computer Networks / Lec-48 / Bhanu Priya |
| CN-3 | 2U6kPu0dfqI | Gate Smashers | Lec-27: Framing in Data Link Layer / Bit Stuffing vs Byte(Character) Stuffing |
| CN-3 | 1A_NcXxdoCc | Neso Academy | Hamming Code / Error Detection |
| CN-3 | wE0quzvXDMM | GO Classes for GATE CS | Marathon Series : Computer Networks / Topic 1: Data Link Layer (Stop-Wait and Sliding Window) |
| CN-4 | yNedVgNyE8Q | Gate Smashers | Lec-26: Various Flow Control Protocols / Stop&Wait , GoBackN & Selective repeat in Data Link Layer |
| CN-4 | oms65hqUe80 | GO Classes for GATE CS | Efficiency,Throughput/ Relation Between WindowSize & Sequence No. Sliding Window / With NOTES |
| CN-4 | Oipm5DdYYAs | Prof. Ravindrababu Ravula | CN /  Flow Control methods / Selective Repeat and comparison between all sliding window protocols |
| CN-5 | WYM9nFYnYAg | Gate Smashers | Lec-33: What is Pure Aloha in Hindi / MAC Layer Protocol |
| CN-5 | j4-r0e7DjqY | Neso Academy | Pure Aloha |
| CN-5 | 2LXiMqV67Uk | Unacademy Computer Science | Medium Access Control - 2 / Computer Network / Lec 15 / GATE CSE/IT 2021 CSE Exam |
| CN-6 | wvvoT-dpr8o | Gate Smashers | Lec-51: Subnetting in CIDR Addressing / Classless Interdomain Routing in Hindi with Example |
| CN-6 | 86RDE_bP1Bs | Prof. Ravindrababu Ravula | CN / IP address Subnetting Supernetting / Classless Inter Domain Routing (CIDR) /Ravindrababu Ravula |
| CN-6 | phOlq9SuscM | Neso Academy | IPv4 Address (Part 1) |
| CN-7 | k8VgrqDOIUo | Gate Smashers | Lec-55: Fragmentation(MTU) of IPv4 Datagram / Identification, Flags and Fragment Offset / Networks |
| CN-7 | dYjdfwbmb3Y | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | Fragmentation of IPv4 / Computer Network / GATE 2024 CSE / Computer Science Engineering #ByjusGate |
| CN-7 | 47PUj7OSGkA | Gate Smashers | Lec-66: NAT Explained - Network Address Translation with example in Hindi |
| CN-7 | zoFSxIuS5Ro | Gate Smashers | Lec-54: IPv4 Header Format – All Fields Explained in Hindi / Computer Networks |
| CN-8 | 7MBmSzQ_TA4 | GO Classes for GATE CS | Marathon: CN / Topic 3:  (Subnetting, Supernetting, Distance Vector Routing, and Link State Routing) |
| CN-8 | 5ZuP5qjbKSI | Gate Smashers | Lec-62: Distance vector routing algorithm in hindi / Computer Networks |
| CN-8 | JMzbdR9iBFY | Sudhakar Atchala | Distance Vector Routing Algorithm in Computer Networks |
| CN-9 | ZFk-SJk7pp4 | GO Classes for GATE CS | Marathon Series : CN / Topic 4: Transport Layer (UDP, TCP Flow, Error and Congestion Control) |
| CN-9 | 0bc_T_pEZmo | Gate Smashers | Lec-74: TCP Congestion Control in Computer Networks in Hindi |
| CN-9 | wvPe4Zb0tUA | Neso Academy | The TCP/IP Protocol Suite |
| CN-10 | uagKTbohimU | Neso Academy | Sockets in Operating System |
| CN-10 | XTVTlEhGS6w | Gate Smashers | Lec-86: Socket Programming in Computer Networks |
| CN-10 | x7obJLN7FcQ | NPTEL IIT Kharagpur | Lecture 24 : Socket Programming – I |
| CN-11 | BZISxpdl4lQ | Gate Smashers | Lec-81: Domain Name Server(DNS) & its types in Hindi / All about DNS |
| CN-11 | 6qphWU5FXnM | Education 4u | Application layer protocols / DNS / SMTP  / Data Communication / Lec-36 / Bhanu Priya |
| CN-11 | _0v-MG8e52U | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | GATE 2024 CSE / Computer Network / Types of DNS Servers / BYJU'S GATE |
| CN-11 | pnoWCK82apU | Gate Smashers | Lec-83: HTTP, FTP, SMTP, POP / All Application Layer Protocols / Computer Networks |
| TC-1 | h4v7x0IMhtI | Gate Smashers | Lec-23: Conversion from Epsilon ε-NFA to DFA with example / Eliminate Epsilon ε-moves |
| TC-1 | WSGcmaHNBFM | Neso Academy | Conversion of Epsilon NFA to NFA |
| TC-1 | rGxyc-CJGRk | Sudhakar Atchala | Minimization of Finite Automata // Equivalence /Partition // Table Filling /Myhill Nerode /DFA / NFA |
| TC-2 | FF8qFPnt-a0 | GO Classes for GATE CS | Regular Expressions - ALL GATE PYQs - Part 1 / Finite Automata / Theory of Computation / With NOTES |
| TC-2 | QddGS_Revb4 | Gate Smashers | Lec-30: Regular Expressions for Finite Languages Example 1 / TOC |
| TC-2 | RxfXyvfTsgQ | Neso Academy | Conversion of Regular Expression to Finite Automata |
| TC-3 | Q-HAP2Ade8I | Gate Smashers | Lec-41: Homomorphism in Regular Languages / closure Properties / TOC |
| TC-3 | dikEDuepOtI | Neso Academy | Pumping Lemma (For Regular Languages) |
| TC-3 | X2VNkQBqXwo | GO Classes for GATE CS | Pumping Lemma for Regular Languages Part-1/ Theory of Computation / GO Classes / With NOTES / Deepak |
| TC-4 | ZXBh4TgJRLs | GO Classes for GATE CS | Context Free Grammar - ALL GATE PYQs - Part 1 / CFG / Regular Grammars / Theory of Computation |
| TC-4 | BLt4pJRBZdA | Gate Smashers | Lec-51: Remove Unit Production from CFG(Context Free Grammar) in Hindi |
| TC-4 | 5_tfVe7ED3g | Neso Academy | Context Free Grammar & Context Free Language |
| TC-5 | WqDkuKn20L4 | GO Classes for GATE CS | PDA - ALL GATE PYQs - Part 1 / Pushdown Automata / Theory of Computation / With NOTES |
| TC-5 | 7lcwlNNCP1E | Gate Smashers | Lec-55: What is Pushdown Automata in TOC / Definition & Explanation in Hindi |
| TC-5 | TEQcJybMMFU | Neso Academy | Pushdown Automata Example - Even Palindrome (Part 1) |
| TC-6 | 0KsU-gavbE4 | Gate Smashers | Lec-44: Closure Properties of CFL (Context Free Languages) with explanation in Hindi |
| TC-6 | eQ0XkUk3qGk | Neso Academy | Pumping Lemma (For Context Free Languages) - Examples (Part 1) |
| TC-6 | B_4mguOU2aY | Unacademy Computer Science | Theory of Computation / Closure properties of CFLs and DCFLs - 2 / Lec 42 / GATE CSE 2021 Exam |
| TC-7 | oCBi3g0N358 | Gate Smashers | Lec-64: Recursive vs Recursive Enumerable Languages / TOC |
| TC-7 | PvLaPKPzq2I | Neso Academy | Turing Machine - Introduction (Part 1) |
| TC-7 | Ik8t15qL5dI | Prof. Ravindrababu Ravula | TOC / Turing Machine / Turing Machine Example / Ravindrababu Ravula / Free GATE CS Classes |
| TC-8 | _fXmwTm_vgY | GO Classes for GATE CS | Decidability and Undecidability : BEST Quick Revision : Part 1 |
| TC-8 | FvqG9RQWIQc | Gate Smashers | Lec-65: Decidability & Undecidability table in toc for all languages |
| TC-8 | JfX7VK7ocRU | Neso Academy | Decidability and Undecidability |
| CD-1 | PT9iWM80PDU | Gate Smashers | Lec-2: Phases of Compiler with examples / Compiler Design |
| CD-1 | TwxPhPvIGEM | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | GATE 2024 Computer Science / Compiler Design / Lexical Analysis Phase (Tokens/Lexemes) / BYJU'S GATE |
| CD-1 | fpRwDEwbRG0 | Vishal sharma | Phases of Compiler + Lexical Analyzer + Tokens, Lexemes & Patterns / Compiler Design Unit 1 Complete |
| CD-1 | MZ9NZdZteG4 | Neso Academy | Lexical Analyzer – Tokenization |
| CD-2 | iddRD8tJi44 | Neso Academy | Top Down Parsers - Recursive Descent Parsers |
| CD-2 | 7wlyOkz61ig | Gate Smashers | Lec-18: How to Parse SDT (Top Down vs Bottom Up Parsing) / Syntax Directed Translation |
| CD-2 | _uSlP91jmTM | Prof. Ravindrababu Ravula | CD / Parsers / Examples on how to find first and follow in LL(1) / Ravindrababu Ravula /Free GATE CS |
| CD-3 | sMxqUQc_jHQ | Gate Smashers | Lec-13: CLR Parsing Table / LR(1) Canonical Items |
| CD-3 | Nxj0g1mk5Ak | Prof. Ravindrababu Ravula | CD / Parsers / Conflicts and examples of CLR(1) and LALR(1) / Ravindrababu Ravula / Free GATE CS |
| CD-3 | NDBqpf0PHnw | BYJU'S Exam Prep GATE & ESE: EE,EC,IN,CS | LALR(1), CLR(1) Parser / Compiler Design / GATE 2023 Computer Science Engineering (CSE) Exam |
| CD-4 | SN4Ocl7MM2k | GO Classes for GATE CS | SDT - ALL GATE PYQs / Syntax Directed Translation Scheme / Semantic Analysis / Compiler Design |
| CD-4 | _CloXDbYAAg | Gate Smashers | Lec-17: What is SDT(Syntax Directed Translation) & its Applications / Semantic Analysis |
| CD-4 | rdnAJBoFKOw | Prof. Ravindrababu Ravula | CD / Syntax Directed Translation / S attributed and L attributed definitions / Ravindrababu Ravula |
| CD-5 | kx2cnll1p4E | Prof. Ravindrababu Ravula | CD / Runtime environment / Introduction to Runtime environment / Ravindrababu Ravula / Free GATE CS |
| CD-5 | SaKfQX_tQrs | Neso Academy | Runtime Environment & Code Optimization / Chapter-7 / Compiler Design / nesoacademy.org |
| CD-5 | 0bS7KhVvZFc | NPTEL - Special Lecture Series | Runtime Environments I |
| CD-6 | -ybmWJ3i-mw | Unacademy Computer Science | Intermediate code: Quadruples, Triples ,DAG |
| CD-6 | _4e3rmt_NoA | GO Classes for GATE CS | Intermediate Codes : Three Address Codes(TAC) and Static Single Assignment(SSA) |
| CD-6 | j-bLeUysUiE | Gate Smashers | Lec-22: Intermediate Code Generation with example |
| CD-7 | w6We9GzY8Ew | GO Classes for GATE CS | IR Code Optimization - Introduction / Local Optimisation, Data Flow Analyses / Compiler Design |
| CD-7 | clb4tnEm8l4 | Gate Smashers | Lec-24: Peephole Optimization in Compiler / Dead code elimination / Strength reduction |
| CD-7 | OKSlupcFGjc | Sudhakar Atchala | Optimization of Basic Blocks in compiler Design |
| CD-8 | oBAqib3LDi4 | GO Classes for GATE CS | Available Expression Analysis, Common Subexpression Elimination, Copy Propagation |
| CD-8 | LNjyBTLWk3g | Prof. Ravindrababu Ravula | CD /Directed Acyclic Graph/Common sub expression elimination, copy propagation, constant propagation |
| CD-8 | clb4tnEm8l4 | Gate Smashers | Lec-24: Peephole Optimization in Compiler / Dead code elimination / Strength reduction |
