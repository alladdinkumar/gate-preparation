"""Topic catalogue — joins the curriculum tables with plan/topic-lectures.md.

`curriculum-*.md` already carries, per syllabus topic: the topic text, its week, its
note file and its GATE Overflow tags. `topic-lectures.md` adds a search phrase and
three teachers. Neither file repeats the other, and neither is repeated here — this
module only reads them and works out which topics a given session is about.

Nothing in here talks to the network or the filesystem beyond plan/.
"""

import re
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "plan"

# Subject key (matching server.SUBJECTS) for each topic-id prefix.
PREFIX_SUBJECT = {
    "PD": "ds", "AL": "algo", "DM": "dm", "LA": "la", "CA": "calc", "PS": "prob",
    "DL": "dl", "CO": "coa", "OS": "os", "DB": "dbms", "CN": "cn", "TC": "toc",
    "CD": "cd", "GA": "ga",
}
# PD covers both C and Data Structures; PD-1..PD-6 are C.
C_TOPICS = {f"PD-{n}" for n in range(1, 7)}

GO_TAG = "https://gateoverflow.in/tag/{}"
GO_SEARCH = "https://gateoverflow.in/search?q={}"

ROW_RE = re.compile(r"^\|\s*([A-Z]{2})-(\d+)\s*\|(.+)\|\s*$")
SOURCE_RE = re.compile(r"^\|\s*([a-z0-9-]+)\s*\|\s*([^|]+?)\s*\|\s*(\S+)\s*\|\s*$")

STOPWORDS = {
    "a", "an", "and", "the", "of", "to", "in", "on", "for", "with", "vs", "or", "by",
    "from", "its", "it", "as", "at", "into", "via", "per", "that", "this", "these",
    "then", "than", "not", "no", "is", "are", "be", "using", "use", "used", "each",
    "one", "two", "three", "more", "most", "all", "any", "only", "also", "up", "out",
    "lecture", "lectures", "pyq", "pyqs", "practice", "revise", "revision", "review",
    "notes", "note", "daily", "log", "error", "week", "day", "min", "mins", "hour",
    "hours", "gate", "go", "cs", "write", "start", "complete", "finish", "test",
    "paper", "question", "questions", "concept", "topic", "topics", "basic", "basics",
    "problem", "problems", "time", "table", "tables", "list", "set", "sheet", "own",
    "new", "old", "full", "mixed", "mock", "score", "marks", "mark", "analysis",
    "rotation", "slot", "block", "session", "sessions",
}


def _words(text):
    """Lowercase significant words, singularised crudely (traps -> trap)."""
    out = set()
    for raw in re.split(r"[^a-z0-9+]+", text.lower()):
        if len(raw) < 3 or raw in STOPWORDS:
            continue
        out.add(raw)
        if raw.endswith("ies") and len(raw) > 4:
            out.add(raw[:-3] + "y")
        elif raw.endswith("es") and len(raw) > 4:
            out.add(raw[:-2])
        if raw.endswith("s") and not raw.endswith("ss"):
            out.add(raw[:-1])
    return out


def _cells(body):
    return [c.strip() for c in body.split("|")]


def load_sources():
    """Key -> (name, url template) from the Sources table in topic-lectures.md."""
    sources = {}
    path = PLAN / "topic-lectures.md"
    if not path.exists():
        return sources
    for line in path.read_text(encoding="utf-8").splitlines():
        m = SOURCE_RE.match(line)
        if m and m.group(3).startswith("http"):
            sources[m.group(1)] = (m.group(2), m.group(3))
    return sources


def load_lectures():
    """Topic id -> (search phrase, [source keys])."""
    lectures = {}
    path = PLAN / "topic-lectures.md"
    if not path.exists():
        return lectures
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = _cells(m.group(3))
        if len(cells) < 2:
            continue
        phrase, alts = cells[0], cells[1]
        keys = [k.strip() for k in alts.split(",") if k.strip()]
        if phrase and keys:
            lectures[f"{m.group(1)}-{m.group(2)}"] = (phrase, keys)
    return lectures


def load_curriculum():
    """Topic id -> {name, week, notes, tags} from the curriculum tables."""
    topics = {}
    for path in sorted(PLAN.glob("curriculum-*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW_RE.match(line)
            if not m:
                continue
            tid = f"{m.group(1)}-{m.group(2)}"
            cells = _cells(m.group(3))
            # Aptitude: | # | Area | Topic | Note file |
            # Everything else: | # | Topic | Week | Note file | GO tag |
            if path.name.endswith("aptitude.md"):
                if len(cells) < 3:
                    continue
                name, week, notes, tags = cells[1], None, cells[2], ""
            else:
                if len(cells) < 4:
                    continue
                name, week, notes, tags = cells[0], cells[1], cells[2], cells[3]
            notes = notes.strip("`").strip()
            topics[tid] = {
                "id": tid,
                "name": name,
                "week": int(week) if week and week.isdigit() else None,
                "notes": notes if notes.endswith(".md") else None,
                "tags": [t.strip() for t in tags.split(",") if t.strip()],
            }
    return topics


# The five things worth asking an assistant about a topic, in order of use.
#
# These ship once and are interpolated in the browser: written out per topic they
# cost 187 KB of the plan payload to say the same thing 124 times. The browser
# prepends a context block naming the day, week, phase, subject, syllabus topic, the
# session's focus and whatever else was ticked off today - so the assistant is told
# what is being studied and how far in, not just a topic name.
GEMINI_HEAD = (
    "I am preparing for GATE 2028 Computer Science (CS paper; the target is a PSU "
    "shortlist, so accuracy matters more than volume). Answer in GATE terms: exam "
    "style, terse, no encouragement."
)

GEMINI_PROMPTS = [
    {"label": "Make notes", "icon": "notes", "text":
        "Write me one page of revision notes: every definition and formula I must "
        "memorise, one fully worked example, and the traps GATE questions set on this "
        "topic. Be terse - I am a senior software engineer, not a beginner. Use plain "
        "markdown so I can paste it straight into my notes file."},
    {"label": "Give me questions", "icon": "practice", "text":
        "Give me 5 GATE-style questions on this topic - a mix of MCQ, MSQ and NAT, with "
        "the marks stated for each, at real GATE difficulty. Do NOT show the answers. "
        "Wait for me to send my answers, then mark them and explain only what I got wrong."},
    {"label": "Explain it", "icon": "video", "text":
        "Explain this topic from first principles, then show me the three hardest "
        "variations GATE has asked on it and what makes each one hard. Assume I know how "
        "to program but have not touched the theory in five years."},
    {"label": "Where did I go wrong", "icon": "error", "text":
        "I am working through previous-year questions on this topic. I will paste a "
        "question and my attempt. Find the flaw in my reasoning and name the concept I am "
        "missing - do not just give me the correct answer."},
    {"label": "Ask anything", "icon": "gem", "text":
        "That is what I am working on right now. I am going to ask you questions about "
        "it - follow-ups, things I half-remember, tangents I am not sure matter for the "
        "exam. Keep answers short and tied to what GATE actually asks, and say so plainly "
        "when something is out of syllabus. Wait for my question."},
]


SHORT_MAX = 46


def short_name(name):
    """A label for the collapsed row — the topic, not its detail list.

    Curriculum names run long on purpose ("Pointers — declaration, dereferencing,
    pointer arithmetic, arrays vs pointers, ..."): that length is the study
    definition. As the summary line of a collapsed row it wraps to three lines on a
    phone, so cut at the dash, then at the last comma that fits.
    """
    head = name.split("—")[0].split("(")[0].strip().rstrip(",;")
    if len(head) <= SHORT_MAX:
        return head
    cut = head.rfind(",", 0, SHORT_MAX)
    if cut < 12:
        cut = head.rfind(" ", 0, SHORT_MAX)
    head = head[:cut].rstrip(",; ") if cut > 12 else head[:SHORT_MAX].rstrip()
    return head + "…"


def build_catalogue(subjects):
    """Topic id -> full topic record, ready to attach to sessions."""
    curriculum = load_curriculum()
    lectures = load_lectures()
    sources = load_sources()
    catalogue = {}

    for tid, topic in curriculum.items():
        prefix = tid.split("-")[0]
        key = "c" if tid in C_TOPICS else PREFIX_SUBJECT.get(prefix, "mixed")
        phrase, alt_keys = lectures.get(tid, (topic["name"], []))

        entry = dict(topic)
        entry["subject"] = key
        entry["subjectName"] = subjects[key]["name"]
        entry["phrase"] = phrase

        entry["lectures"] = []
        for k in alt_keys:
            if k not in sources:
                continue
            label, template = sources[k]
            url = template.replace("{q}", quote_plus(phrase))
            entry["lectures"].append({"label": label, "url": url, "kind": "video"})

        entry["practice"] = [
            {"label": f"PYQs tagged {tag}", "url": GO_TAG.format(tag), "kind": "practice"}
            for tag in topic["tags"]
        ]
        query = " ".join(w for w in phrase.split() if w.lower() not in STOPWORDS)
        query = " ".join(query.split()[:4]) or phrase
        entry["practice"].append({
            "label": f'Search GO: "{query}"',
            "url": GO_SEARCH.format(quote_plus(query)),
            "kind": "practice",
        })
        if subjects[key].get("pyq") and key != "mixed":
            entry["practice"].append({
                "label": f"All {subjects[key]['name']} PYQs",
                "url": subjects[key]["pyq"], "kind": "practice",
            })

        entry["short"] = short_name(entry["name"])
        catalogue[tid] = entry

    _add_keywords(catalogue)
    return catalogue


def _add_keywords(catalogue):
    """Attach match words, and mark the ones distinctive enough to match on alone."""
    for entry in catalogue.values():
        entry["_words"] = _words(entry["name"] + " " + entry["phrase"] + " " +
                                 " ".join(entry["tags"]).replace("-", " "))
    counts = {}
    for entry in catalogue.values():
        for w in entry["_words"]:
            counts[w] = counts.get(w, 0) + 1
    for entry in catalogue.values():
        entry["_rare"] = {w for w in entry["_words"] if counts[w] <= 2}


def expand_ids(text):
    """'PD-1, PD-2' or 'LA-1 ... LA-5' -> ['PD-1', 'PD-2'] / ['LA-1'..'LA-5']."""
    ids = []
    for part in re.split(r",", text):
        part = part.strip()
        rng = re.match(r"^([A-Z]{2})-(\d+)\s*(?:\.\.\.|…|-|–|—)\s*(?:[A-Z]{2}-)?(\d+)$", part)
        if rng:
            ids.extend(f"{rng.group(1)}-{n}" for n in
                       range(int(rng.group(2)), int(rng.group(3)) + 1))
            continue
        one = re.match(r"^([A-Z]{2}-\d+)$", part)
        if one:
            ids.append(one.group(1))
    return ids


ID_RE = re.compile(r"\b([A-Z]{2})-(\d+)(?:\s*(?:\.\.\.|\u2026|\u2013|\u2014)\s*(?:[A-Z]{2}-)?(\d+))?\b")
NON_STUDY = re.compile(r"weekly review|monthly review|rest day|score with|record section", re.I)
APTITUDE = re.compile(r"\bGA\b|aptitude|rotation", re.I)


def find_ids(text):
    """Syllabus ids written anywhere in a cell.

    Handles the three ways the phase tables write them: a list ("AL-7, AL-8"), a
    slashed pair ("PYQs on PD-1/PD-2"), and a range ("PD-1 ... PD-4"), which is
    expanded because the range endpoints alone would hide the topics in between.
    """
    found = []
    for prefix, first, last in ID_RE.findall(text):
        lo = int(first)
        hi = int(last) if last else lo
        for n in range(lo, max(lo, hi) + 1):
            found.append(f"{prefix}-{n}")
    return found


def match_topics(focus, output, candidates, catalogue, limit=3):
    """Pick the topics a session is about, best first.

    `candidates` is the week's declared topic list. A session matches a candidate by
    word overlap with its name, search phrase and GO tags; a word that belongs to at
    most two topics in the whole syllabus counts double, so "pigeonhole" is decisive
    where "graph" is not. With no overlap the week's own topics are used, because a
    lecture row that says "continue yesterday" is still about this week's subject.
    """
    text = f"{focus} {output}"
    seen, explicit = set(), []
    for t in find_ids(text):
        if t in catalogue and t not in seen:
            seen.add(t)
            explicit.append(t)
    if explicit:
        return explicit
    if NON_STUDY.search(focus):
        return []
    # The Saturday aptitude hour sits inside a subject week, so its topics are never
    # in the week's candidate list. Swap the pool rather than widen it.
    if APTITUDE.search(focus):
        pool = [tid for tid, e in catalogue.items() if e["subject"] == "ga"]
    else:
        pool = [c for c in candidates if c in catalogue]
    if not pool:
        return []

    words = _words(text)
    scored = []
    for tid in pool:
        entry = catalogue[tid]
        hits = words & entry["_words"]
        if not hits:
            continue
        score = sum(2 if w in entry["_rare"] else 1 for w in hits)
        if score >= 2:
            scored.append((score, pool.index(tid), tid))
    if scored:
        scored.sort(key=lambda s: (-s[0], s[1]))
        # Keep only what is in the same league as the best match, so "pointers" does
        # not drag in every topic that happens to say "array".
        cutoff = scored[0][0] / 2
        return [tid for score, _, tid in scored[:limit] if score >= cutoff]
    return pool[:limit]


def public(entry):
    """The topic record as the planner sees it - without the matching internals."""
    return {k: v for k, v in entry.items() if not k.startswith("_")}
