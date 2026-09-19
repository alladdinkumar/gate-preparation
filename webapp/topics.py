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
WATCH = "https://www.youtube.com/watch?v={}"
YOUTUBE_SEARCH = "https://www.youtube.com/results?search_query={}"
# A topic row offers individual lectures. A channel page, a channel-scoped search
# and a playlist all fail that in the same way: they hand over a list to sift
# instead of the video that teaches this topic. Course playlists still appear as
# subject links and in resources.md, which is where a whole course belongs.
CHANNEL_PAGE = re.compile(r"youtube\.com/(@|channel/)|[?&]list=")

VIDEO_RE = re.compile(
    r"^\|\s*([A-Z]{2}-\d+)\s*\|\s*([A-Za-z0-9_-]{11})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")

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
        # British and American spellings both turn up in these titles: the syllabus
        # says "synchronization", GO Classes titles a lecture "Synchronisation".
        for a, b in (("isation", "ization"), ("ise", "ize"), ("yse", "yze"),
                     ("our", "or"), ("ll", "l")):
            if a in raw:
                out.add(raw.replace(a, b))
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


def load_pyq_videos():
    """Topic id -> [{id, channel, title}] from plan/topic-pyq-videos.md.

    Videos of someone working through GATE questions on the topic, as opposed to
    teaching it. Same provenance as the lecture file - written by build_videos.py
    --pyq, every id confirmed against YouTube before it lands.
    """
    return _read_video_file(PLAN / "topic-pyq-videos.md")


def load_videos():
    """Topic id -> [{id, channel, title}] from plan/topic-videos.md.

    Written by webapp/tools/build_videos.py, which verifies every id against
    YouTube's oEmbed endpoint before it is allowed into the file. Missing file or
    missing topic is not an error - the channel searches cover it.
    """
    return _read_video_file(PLAN / "topic-videos.md")


def _read_video_file(path):
    videos = {}
    if not path.exists():
        return videos
    for line in path.read_text(encoding="utf-8").splitlines():
        m = VIDEO_RE.match(line)
        if not m:
            continue
        tid, vid, channel, title = m.group(1), m.group(2), m.group(3), m.group(4)
        videos.setdefault(tid, []).append(
            {"id": vid, "channel": channel.strip(), "title": title.strip()})
    for tid in videos:
        videos[tid] = in_order(videos[tid])
    return videos


SEQ_RE = re.compile(
    r"(?:^|[\s|(\[])(?:lec(?:ture)?[\s.-]*|part[\s.-]*|chapter[\s.-]*|#)(\d+)|^(\d+)[.\s]",
    re.I)


def sequence(title):
    """The lecture number a title announces, if it announces one."""
    m = SEQ_RE.search(title)
    if not m:
        return None
    return int(m.group(1) or m.group(2))


def in_order(videos):
    """Group a topic's videos by teacher, and put each teacher's in lecture order.

    Left alone, these come back ranked by search score, so "Part 2" can sit above
    "Part 1" and two teachers interleave. Watching order is what matters at 21:00:
    one teacher's videos together, lowest lecture number first. Channels keep the
    order they were ranked in, so the strongest match is still the first thing shown.
    """
    order, seen = [], {}
    for v in videos:
        if v["channel"] not in seen:
            seen[v["channel"]] = len(seen)
        order.append(v)
    return sorted(
        order,
        key=lambda v: (seen[v["channel"]],
                       sequence(v["title"]) if sequence(v["title"]) is not None else 10 ** 6),
    )


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
# Two rules learned the hard way:
#
# 1. Gemini's web app ignores ?q= and ?prompt= - both were tested and the input box
#    stays empty. Google's AI Mode (udm=50) is the same model and does take the
#    prompt in the URL, so that is what the buttons open. Its query survives to at
#    least 2044 characters, hence PROMPT_URL_MAX below.
# 2. An ask without a required answer shape gets an essay. Every prompt states the
#    exact structure the reply must take, because a wall of prose at 21:00 is worse
#    than no answer - it cannot be pasted into a note file or marked against a key.
#
# These ship once and are interpolated in the browser: written out per topic they
# cost 187 KB of the plan payload to say the same thing 124 times. The browser
# prepends a context block naming the day, week, phase, subject, syllabus topic, the
# session's focus and what was already ticked off today.

GEMINI_URL = "https://www.google.com/search?udm=50&q={q}"
PROMPT_URL_MAX = 1900

GEMINI_HEAD = (
    "I am preparing for GATE 2028 Computer Science (CS paper; the target is a PSU "
    "shortlist, so accuracy matters more than volume). Answer in GATE terms: exam "
    "style, terse, no encouragement, no analogies."
)

GEMINI_PROMPTS = [
    {"label": "Make notes", "icon": "notes", "text":
        "Write revision notes on this topic in exactly this structure and nothing else:\n"
        "\n"
        "## <topic>\n"
        "### Must know\n"
        "- one bullet per definition, rule or formula; define every symbol; no prose\n"
        "### Worked example\n"
        "one GATE-style question, then the solution line by line with the arithmetic shown\n"
        "### Traps\n"
        "- the exact misreading GATE exploits, and the wrong answer it produces\n"
        "### Formula-sheet lines\n"
        "- at most 5 lines, the ones worth copying verbatim\n"
        "\n"
        "Plain markdown, no preamble, no closing remarks. Leave out anything outside "
        "the GATE CS syllabus."},

    {"label": "Give me questions", "icon": "practice", "text":
        "Set me 5 questions on this topic at real GATE difficulty. Use this format "
        "exactly:\n"
        "\n"
        "Q1. [MCQ | 1 mark] <question>\n"
        "(A) ...  (B) ...  (C) ...  (D) ...\n"
        "\n"
        "Mix MCQ, MSQ and NAT, and mix 1-mark and 2-mark. State the type and marks on "
        "every question. NAT questions take a number and get no options.\n"
        "\n"
        "Then stop. Print no answers, no hints, no method, no explanation. End with "
        "exactly this line: Reply Q1:<ans> Q2:<ans> Q3:<ans> Q4:<ans> Q5:<ans>\n"
        "\n"
        "When I send my answers, reply with one table - Q | my answer | correct answer "
        "| right or wrong | one line on what I got wrong - and then a single line "
        "naming the one concept to revise. Nothing else."},

    {"label": "Explain it", "icon": "video", "text":
        "Explain this topic in exactly these four sections:\n"
        "\n"
        "1. Core idea - 5 lines maximum\n"
        "2. How it works - the derivation or mechanism, with the assumptions stated\n"
        "3. The three hardest GATE variations - for each: what is asked, why it is "
        "hard, and the one move that cracks it\n"
        "4. Formula-sheet lines - at most 5\n"
        "\n"
        "I write code for a living but have not touched the theory in five years. Skip "
        "the history and the motivation."},

    {"label": "Where did I go wrong", "icon": "error", "text":
        "I will paste a previous-year question, my answer, and the official answer. "
        "Reply in exactly this form:\n"
        "\n"
        "1. What the question actually asks - one line\n"
        "2. Where my reasoning broke - quote the step\n"
        "3. The concept I am missing - name it in three words\n"
        "4. The rule for next time - one general line\n"
        "5. One similar question to retry now - no answer\n"
        "\n"
        "Do not give a full worked solution unless I ask. If I was right for the wrong "
        "reason, say so. Wait for me to paste it."},

    {"label": "Ask anything", "icon": "gem", "text":
        "That is what I am working on right now. I will ask you questions about it - "
        "follow-ups, things I half-remember, tangents I am unsure matter for the exam.\n"
        "\n"
        "Answer every one in exactly this shape:\n"
        "- the direct answer first, in one line\n"
        "- then at most 5 lines of why\n"
        "- show the arithmetic for anything numerical\n"
        "- if it is outside the GATE CS syllabus, open with \"Out of syllabus\" and say "
        "so in one line\n"
        "- no preamble, no encouragement, no summary at the end\n"
        "\n"
        "Wait for my first question."},
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
    videos = load_videos()
    pyq_videos = load_pyq_videos()
    catalogue = {}

    for tid, topic in curriculum.items():
        prefix = tid.split("-")[0]
        key = "c" if tid in C_TOPICS else PREFIX_SUBJECT.get(prefix, "mixed")
        phrase, alt_keys = lectures.get(tid, (topic["name"], []))

        entry = dict(topic)
        entry["subject"] = key
        entry["subjectName"] = subjects[key]["name"]
        entry["phrase"] = phrase

        # Named videos first - these are the actual lecture, verified to exist.
        # The channel searches from topic-lectures.md follow as a fallback, because
        # a video can be pulled down and a search cannot.
        entry["lectures"] = [
            {"label": f"{v['channel']} — {v['title']}",
             "url": WATCH.format(v["id"]), "kind": "video", "video": True}
            for v in videos.get(tid, [])
        ]
        # Fallback row, for when one of the named videos is taken down. A search
        # scoped to a channel lands on a channel page, which is the thing this whole
        # file exists to avoid, so those are dropped: what is left is course pages
        # (NPTEL, MIT, goclasses.in) plus one plain topic search on YouTube.
        entry["search"] = []
        for k in alt_keys:
            if k not in sources:
                continue
            label, template = sources[k]
            if CHANNEL_PAGE.search(template):
                continue
            url = template.replace("{q}", quote_plus(phrase))
            entry["search"].append({"label": f"Search {label}", "url": url, "kind": "video"})
        entry["search"].append({
            "label": f'YouTube: "{phrase}"',
            "url": YOUTUBE_SEARCH.format(quote_plus(phrase + " GATE")),
            "kind": "video",
        })
        if not entry["lectures"]:
            # No video survived verification for this topic; the searches are all
            # there is, so promote them rather than show an empty row.
            entry["lectures"] = entry["search"]
            entry["search"] = []

        # Questions on this topic, worked through on video. Shown beside the GATE
        # Overflow links, not among the lectures: these are for after an attempt.
        entry["pyqVideos"] = [
            {"label": f"{v['channel']} — {v['title']}",
             "url": WATCH.format(v["id"]), "kind": "practice", "video": True}
            for v in pyq_videos.get(tid, [])
        ]

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
# The Saturday aptitude hour is written "GA rotation 2 - Grammar". Matching on a
# bare "rotation" caught it, and also caught "AVL rotations" and "Booth's shifting
# rotation", handing BST and COA sessions a pool of English-grammar topics.
APTITUDE = re.compile(r"\bGA\b|\baptitude\b|GA rotation", re.I)


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


# A topic recurs across many sessions - PD-3 appears in 22, GA-1 in 29 - so showing
# all of its videos on each one repeats the same links for weeks. Deal them out
# instead: each video is offered on exactly one day, and a session that has run out
# says where the rest were listed. Practice links still repeat, because a question
# bank is a reference, not something you finish.
FIRST_SESSION_LECTURES = 2


def deal_videos(ordered_days, catalogue):
    """Give each topic's videos to the sessions that carry it, once each.

    Two topics can legitimately share a video - one lecture covering both arrays
    and pointers - so a URL already handed out anywhere is skipped rather than
    offered again under the second topic.
    """
    cursor = {}
    given = set()

    def take(items, start, limit):
        """Next `limit` items from `start` that have not been shown anywhere."""
        picked, i = [], start
        while i < len(items) and len(picked) < limit:
            url = items[i].get("url")
            if url not in given:
                given.add(url)
                picked.append(i)
            i += 1
        return picked, i

    for day in ordered_days:
        for task in day["tasks"]:
            cut = {}
            for tid in task["topics"]:
                entry = catalogue.get(tid)
                if not entry:
                    continue
                seen = cursor.setdefault(tid, {"l": 0, "p": 0, "days": []})
                first = not seen["days"]

                lec_idx, seen["l"] = take(entry["lectures"], seen["l"],
                                          FIRST_SESSION_LECTURES if first else 1)
                pyq_idx, seen["p"] = take(entry.get("pyqVideos", []), seen["p"], 1)
                if lec_idx or pyq_idx:
                    seen["days"].append(day["dayNumber"])

                cut[tid] = {"lidx": lec_idx, "pidx": pyq_idx,
                            "listed": seen["days"][0] if seen["days"] else None,
                            "lastListed": seen["days"][-1] if seen["days"] else None}
            task["videoCut"] = cut
