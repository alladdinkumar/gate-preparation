"""GATE study planner — local web server.

Reads the day-by-day tables in plan/phase-*.md, serves a single-page planner,
and stores checkbox progress in webapp/progress.json. Standard library only.

Run:  python webapp/server.py        (or double-click webapp/start.bat)
Open: http://127.0.0.1:8765
"""

import datetime as dt
import json
import os
import re
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HOST = "127.0.0.1"
PORT = int(os.environ.get("GATE_PLANNER_PORT", "8765"))
WEBAPP = Path(__file__).resolve().parent
ROOT = WEBAPP.parent
PLAN = ROOT / "plan"
PROGRESS_FILE = WEBAPP / "progress.json"
START = dt.date(2026, 9, 14)
DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
WRITE_LOCK = threading.Lock()

import gitsync  # noqa: E402  (needs nothing from this module, kept beside it)

# ---------------------------------------------------------------------------
# Link table (mirrors plan/resources.md)
# ---------------------------------------------------------------------------

GO_PDF = "https://github.com/GATEOverflow/GO-PDFs/releases"
GO_EXAMS = "https://gateoverflow.in/exams/gate"
CALCULATOR = "https://www.tcsion.com/OnlineAssessment/ScientificCalculator/Calculator.html"
GO_CLASSES_COURSES = "https://www.goclasses.in/s/store/courses"
OFFICIAL_SITE = "https://gate2027.iitm.ac.in"

SUBJECTS = {
    "c": {"name": "C Programming", "notes": "programming-ds", "sheet": "programming-ds",
          "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHgzQutUHGzqMjA1z7XJ_Uya",
          "pyq": "https://gateoverflow.in/questions/programming-in-c/programming/programming-in-c?sort=gate",
          "backup": [("NPTEL courses (search: Programming in C)", "https://nptel.ac.in/courses")]},
    "ds": {"name": "Data Structures", "notes": "programming-ds", "sheet": "programming-ds",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHi_0QW5bavzLyAJZ0ozFTJ3",
           "pyq": "https://gateoverflow.in/questions/programming-in-c/data-structures?sort=gate",
           "backup": [("Gate Smashers Data Structure", "https://www.youtube.com/playlist?list=PLxCzCOWd7aiEwaANNt3OqJPVIxwp2ebiT")]},
    "dm": {"name": "Discrete Maths", "notes": "maths", "sheet": "engineering-maths",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHgjPQN2GtCVOCgrkH2zCkSU",
           "pyq": "https://gateoverflow.in/questions/mathematics/discrete-mathematics?sort=gate",
           "backup": [("GO Classes Graph Theory", "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjQoj0k-BlI9zXE0QKdl-lI"),
                      ("MIT 6.042J", "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/")]},
    "algo": {"name": "Algorithms", "notes": "algorithms", "sheet": "algorithms",
             "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjUCHdJp-_soSSmhgmO4i0T",
             "pyq": "https://gateoverflow.in/questions/algorithms?sort=gate",
             "backup": [("NPTEL DAA (Mukund)", "https://nptel.ac.in/courses/106106131"),
                        ("Abdul Bari", "https://www.youtube.com/@abdul_bari")]},
    "la": {"name": "Linear Algebra", "notes": "maths", "sheet": "engineering-maths",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHhGLQ1ZT37KLpBMAD90CM4_",
           "pyq": "https://gateoverflow.in/questions/mathematics/linear-algebra?sort=gate",
           "backup": [("MIT 18.06", "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/")]},
    "calc": {"name": "Calculus", "notes": "maths", "sheet": "engineering-maths",
             "video": GO_CLASSES_COURSES,
             "pyq": "https://gateoverflow.in/questions/mathematics/calculus?sort=gate",
             "backup": [("3Blue1Brown Essence of Calculus", "https://www.3blue1brown.com/topics/calculus")]},
    "prob": {"name": "Probability", "notes": "maths", "sheet": "engineering-maths",
             "video": GO_CLASSES_COURSES,
             "pyq": "https://gateoverflow.in/questions/mathematics/probability?sort=gate",
             "backup": [("MIT RES.6-012 (Tsitsiklis)", "https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/")]},
    "dl": {"name": "Digital Logic", "notes": "digital-logic", "sheet": "digital-logic",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHiwFGR4fqKlj9C_eo8R6hbY",
           "pyq": "https://gateoverflow.in/questions/digital-logic?sort=gate",
           "backup": [("Neso Academy", "https://www.youtube.com/channel/UCQYMhOMi_Cdj1CEAU-fv80A")]},
    "coa": {"name": "COA", "notes": "coa", "sheet": "coa",
            "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjMdZR3GYQ2KZio0NKczrik",
            "pyq": "https://gateoverflow.in/questions/co-and-architecture?sort=gate",
            "backup": [("NPTEL COA (Sengupta)", "https://nptel.ac.in/courses/106105163")]},
    "os": {"name": "Operating Systems", "notes": "os", "sheet": "os",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHixlIaarIXGPy-eggJQMxd_",
           "pyq": "https://gateoverflow.in/questions/operating-system?sort=gate",
           "backup": [("NPTEL Intro to OS (Rebeiro)", "https://nptel.ac.in/courses/106106144"),
                      ("Gate Smashers", "https://www.youtube.com/@GateSmashers/playlists")]},
    "dbms": {"name": "DBMS", "notes": "dbms", "sheet": "dbms",
             "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHhUXFx03wy3uFeCXRw6qlm8",
             "pyq": "https://gateoverflow.in/questions/databases?sort=gate",
             "backup": [("NPTEL DBMS (Das)", "https://nptel.ac.in/courses/106105175")]},
    "cn": {"name": "Computer Networks", "notes": "cn", "sheet": "cn",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHim3NUSNOb7ffyhaE5MSkmE",
           "pyq": "https://gateoverflow.in/questions/computer-networks?sort=gate",
           "backup": [("NPTEL CN & IP", "https://nptel.ac.in/courses/106105183")]},
    "toc": {"name": "Theory of Computation", "notes": "toc", "sheet": "toc",
            "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHhXeEdbXsi34ePvUjL8I-Q9",
            "pyq": "https://gateoverflow.in/questions/theory-of-computation?sort=gate",
            "backup": [("Neso Academy TOC", "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev"),
                       ("NPTEL TOC (Tewari)", "https://onlinecourses.nptel.ac.in/noc21_cs83/preview")]},
    "cd": {"name": "Compiler Design", "notes": "compiler", "sheet": "compiler",
           "video": "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjy3eH_qRImIs5dVUTpr9ga",
           "pyq": "https://gateoverflow.in/questions/compiler-design?sort=gate",
           "backup": [("NPTEL Compiler Design", "https://nptel.ac.in/courses/106105190"),
                      ("Ravindrababu Ravula", "https://www.youtube.com/channel/UCJjC1hn78yZqTf0vdTC6wAQ")]},
    "ga": {"name": "General Aptitude", "notes": "aptitude", "sheet": None,
           "video": None,
           "pyq": "https://gateoverflow.in/questions/general-aptitude?sort=gate",
           "backup": [("IndiaBix", "https://www.indiabix.com")]},
    "mixed": {"name": "Mixed / mocks", "notes": "formula-sheets", "sheet": None, "video": None,
              "pyq": GO_EXAMS, "backup": []},
}

# Week -> subject key(s). Revision weeks can cover two or three subjects.
WEEK_SUBJECTS = {}
for _a, _b, _k in [(1, 3, "c"), (4, 6, "ds"), (7, 10, "dm"), (11, 14, "algo"), (15, 15, "la"), (16, 16, "calc"),
                   (17, 18, "prob"), (19, 22, "dl"), (23, 27, "coa"), (28, 32, "os"), (33, 36, "dbms"),
                   (37, 41, "cn"), (42, 46, "toc"), (47, 49, "cd")]:
    for _w in range(_a, _b + 1):
        WEEK_SUBJECTS[_w] = [_k]
WEEK_SUBJECTS.update({50: ["c", "ds"], 51: ["algo"], 52: ["dm"], 53: ["la", "calc", "prob"], 54: ["dl"], 55: ["coa"],
                      56: ["os"], 57: ["dbms"], 58: ["cn"], 59: ["toc"], 60: ["cd"]})
for _w in range(61, 73):
    WEEK_SUBJECTS[_w] = ["mixed"]

# Names that appear inside resource / focus cells -> subject key. Longest first.
NAME_TO_SUBJECT = [
    ("theory of computation", "toc"), ("computer networks", "cn"), ("operating systems", "os"),
    ("compiler design", "cd"), ("discrete mathematics", "dm"), ("discrete maths", "dm"), ("data structures", "ds"),
    ("digital logic", "dl"), ("linear algebra", "la"), ("engineering mathematics", "prob"), ("engg maths", "prob"),
    ("engineering maths", "prob"), ("maths", "prob"), ("c programming", "c"), ("algorithms", "algo"),
    ("graph theory", "dm"), ("probability", "prob"), ("calculus", "calc"), ("dbms", "dbms"), ("coa", "coa"),
    ("toc", "toc"), ("pds", "ds"), ("algo", "algo"), ("cd", "cd"), ("cn", "cn"), ("os", "os"), ("dl", "dl"),
    ("dm", "dm"), ("ds", "ds"), ("c", "c"),
]

NAMED_LINKS = [
    ("tcs ion", "Virtual calculator", CALCULATOR, "tool"),
    ("indiabix", "IndiaBix", "https://www.indiabix.com", "practice"),
    ("mit 18.06", "MIT 18.06", "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/", "video"),
    ("mit 6.042j", "MIT 6.042J", "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/", "video"),
    ("res.6-012", "MIT RES.6-012", "https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/", "video"),
    ("tsitsiklis", "MIT RES.6-012", "https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/", "video"),
    ("3blue1brown", "3Blue1Brown Essence of Calculus", "https://www.3blue1brown.com/topics/calculus", "video"),
    ("abdul bari", "Abdul Bari", "https://www.youtube.com/@abdul_bari", "video"),
    ("nptel daa", "NPTEL DAA (Mukund)", "https://nptel.ac.in/courses/106106131", "video"),
    ("nptel coa", "NPTEL COA (Sengupta)", "https://nptel.ac.in/courses/106105163", "video"),
    ("nptel intro to os", "NPTEL Intro to OS", "https://nptel.ac.in/courses/106106144", "video"),
    ("nptel dbms", "NPTEL DBMS (Das)", "https://nptel.ac.in/courses/106105175", "video"),
    ("nptel cn", "NPTEL CN & IP", "https://nptel.ac.in/courses/106105183", "video"),
    ("nptel toc", "NPTEL TOC (Tewari)", "https://onlinecourses.nptel.ac.in/noc21_cs83/preview", "video"),
    ("nptel compiler", "NPTEL Compiler Design", "https://nptel.ac.in/courses/106105190", "video"),
    ("nptel c", "NPTEL courses", "https://nptel.ac.in/courses", "video"),
    ("neso academy toc", "Neso Academy TOC", "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgp46KUv4ZY69yXmpwKOIev", "video"),
    ("neso academy", "Neso Academy", "https://www.youtube.com/channel/UCQYMhOMi_Cdj1CEAU-fv80A", "video"),
    ("gate smashers ds", "Gate Smashers Data Structure", "https://www.youtube.com/playlist?list=PLxCzCOWd7aiEwaANNt3OqJPVIxwp2ebiT", "video"),
    ("gate smashers", "Gate Smashers playlists", "https://www.youtube.com/@GateSmashers/playlists", "video"),
    ("official gate 2028 site", "Official GATE site", OFFICIAL_SITE, "material"),
    ("go graph theory", "GO Classes Graph Theory", "https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjQoj0k-BlI9zXE0QKdl-lI", "video"),
    ("go exams page", "GO exams (test mode)", GO_EXAMS, "practice"),
]

TRACKER_FILES = {"error-log.md", "mocks.md", "subjects.md", "revision.md", "aptitude.md", "pyq.md",
                 "weak-areas.md", "progress.md"}
SHEET_FILES = {"programming-ds.md", "engineering-maths.md", "algorithms.md", "digital-logic.md", "coa.md", "os.md",
               "dbms.md", "cn.md", "toc.md", "compiler.md", "top-30-traps.md"}


def subject_from_text(text):
    low = " " + re.sub(r"[^a-z0-9.+ ]", " ", text.lower()) + " "
    for name, key in NAME_TO_SUBJECT:
        if f" {name} " in low:
            return key
    return None


def link(label, url, kind):
    return {"label": label, "url": url, "kind": kind}


def file_link(label, path):
    return {"label": label, "path": path, "kind": "file"}


def resolve_resources(cell, week_subjects):
    """Turn a Resource cell into link objects."""
    links = []
    default = SUBJECTS[week_subjects[0]]
    parts = [p.strip() for p in re.split(r";|\s/\s|\s\+\s", cell) if p.strip()]
    for part in parts:
        low = part.lower().replace("backup:", "").strip()
        if low in ("—", "-", ""):
            continue
        named = next((n for n in NAMED_LINKS if n[0] in low), None)
        if named:
            links.append(link(named[1], named[2], named[3]))
            continue
        if low.startswith("go tag"):
            for tag in [t.strip() for t in part[6:].split(",") if t.strip()]:
                links.append(link(f"PYQs: {tag}", f"https://gateoverflow.in/tag/{tag}", "practice"))
            continue
        if low.startswith("go classes"):
            key = subject_from_text(part[10:]) or week_subjects[0]
            subj = SUBJECTS[key]
            if "practice" in low or "course" in low or "engineering mathematics" in low or "engg maths" in low:
                if subj["video"] and "youtube" in subj["video"] and "practice" not in low:
                    links.append(link(f"GO Classes {subj['name']}", subj["video"], "video"))
                else:
                    links.append(link("GO Classes courses (free)", GO_CLASSES_COURSES, "video"))
            elif subj["video"]:
                label = f"GO Classes {subj['name']}" + (" (segment)" if "segment" in low else "")
                links.append(link(label, subj["video"], "video"))
            else:
                # Mock phases: the subject is whatever the last mock exposed.
                links.append(link("GO Classes playlists", "https://www.youtube.com/@GOClassesforGATECS/playlists", "video"))
                links.append(file_link("Weak-areas tracker", "trackers/weak-areas.md"))
            if "notes" in low:
                links.append(file_link(f"{subj['name']} notes", f"notes/{subj['notes']}/_index.md"))
            continue
        if low.startswith("quiz:") or low.startswith("pre-2000"):
            key = subject_from_text(part.replace("PYQs", "")) or week_subjects[0]
            subj = SUBJECTS[key]
            links.append(link(f"Older {subj['name']} PYQs", subj["pyq"], "practice"))
            continue
        if "ga pyqs" in low or "go pdf vol 1 ga" in low:
            links.append(link("GA PYQs", SUBJECTS["ga"]["pyq"], "practice"))
            links.append(link("GO PDF (Vol 1)", GO_PDF, "material"))
            continue
        if low.startswith("go pyqs") or low.startswith("go pdf"):
            inner = re.search(r"\(([^)]+)\)", part)
            key = subject_from_text(inner.group(1)) if inner else None
            keys = [key] if key else week_subjects
            for k in keys:
                subj = SUBJECTS[k]
                if k != "mixed":
                    links.append(link(f"{subj['name']} PYQs", subj["pyq"], "practice"))
            if low.startswith("go pdf"):
                subject_names = ", ".join(SUBJECTS[k]["name"] for k in keys if k != "mixed")
                label = f"GO PDF releases — {subject_names}" if subject_names else "GATE Overflow PDF releases"
                links.append(link(label, GO_PDF, "material"))
            continue
        if low.startswith("programming-in-c"):
            links.append(link("PYQs: programming-in-c", "https://gateoverflow.in/tag/programming-in-c", "practice"))
            continue
        if "own notes" in low:
            links.append(file_link(f"{default['name']} notes", f"notes/{default['notes']}/_index.md"))
            continue
        if "formula sheet" in low:
            for k in week_subjects:
                if SUBJECTS[k]["sheet"]:
                    links.append(file_link(f"{SUBJECTS[k]['sheet']}.md sheet", f"notes/formula-sheets/{SUBJECTS[k]['sheet']}.md"))
            if not any(SUBJECTS[k]["sheet"] for k in week_subjects):
                links.append(file_link("Formula sheets", "notes/formula-sheets/_index.md"))
            continue
        if "traps list" in low:
            links.append(file_link("top-30-traps.md", "notes/formula-sheets/top-30-traps.md"))
            continue
        if low == "error log":
            links.append(file_link("error-log.md", "trackers/error-log.md"))
            continue
        code = re.findall(r"`([^`]+)`", part)
        if code:
            for c in code:
                path = resolve_md_ref(c, week_subjects)
                if path:
                    links.append(file_link(Path(path).name, path))
            continue
        if low == "notes":
            links.append(file_link(f"{default['name']} notes", f"notes/{default['notes']}/_index.md"))
            continue
        if low in ("key", "go key", "go answer key"):
            links.append(link("GO exams (answer keys)", GO_EXAMS, "practice"))
            continue
        links.append({"label": part, "kind": "text"})
    # de-duplicate while preserving order
    seen, out = set(), []
    for item in links:
        sig = (item.get("url") or item.get("path") or item["label"], item["kind"])
        if sig not in seen:
            seen.add(sig)
            out.append(item)
    return out


NOTE_INDEX = {}


def load_note_index():
    NOTE_INDEX.clear()
    for idx in (ROOT / "notes").glob("*/_index.md"):
        folder = idx.parent.name
        for name in re.findall(r"`([a-z0-9-]+\.md)`", idx.read_text(encoding="utf-8")):
            prefix = "-".join(name.split("-")[:2])
            NOTE_INDEX[prefix] = f"notes/{folder}/{name}"
            NOTE_INDEX[name] = f"notes/{folder}/{name}"


def resolve_md_ref(ref, week_subjects):
    ref = ref.strip()
    if ref.startswith(("notes/", "trackers/", "reviews/", "daily-logs/", "plan/")):
        return ref if ref.endswith(".md") else None
    if ref in TRACKER_FILES:
        return f"trackers/{ref}"
    if ref in SHEET_FILES:
        return f"notes/formula-sheets/{ref}"
    if ref in NOTE_INDEX:
        return NOTE_INDEX[ref]
    return None


def resolve_outputs(cell, week_subjects):
    links = []
    for ref in re.findall(r"`([^`]+)`", cell):
        path = resolve_md_ref(ref, week_subjects)
        if path:
            label = Path(path).name
            links.append(file_link(label, path))
    return links


# ---------------------------------------------------------------------------
# Plan parser
# ---------------------------------------------------------------------------

ROW_RE = re.compile(r"^\| (Mon|Tue|Wed|Thu|Fri|Sat|Sun) \| ([^|]+) \| (.+) \| ([^|]+) \| ([^|]+) \|\s*$")
WEEK_RE = re.compile(r"^### Week (\d+)\b(.*)$")
DATES_RE = re.compile(r"\((\d{4}-\d{2}-\d{2}) → (\d{4}-\d{2}-\d{2})\)")


def slot_label(day, slot):
    slot = slot.strip()
    if slot == "AM":
        return "Morning", "08:30–10:00"
    if slot == "PM":
        return "Evening", "20:00–21:30"
    if day == "Sun":
        return "Sunday review", "30–45 min"
    return "Saturday block", slot


def parse_plan():
    load_note_index()
    phases, days = [], {}
    for pf in sorted(PLAN.glob("phase-*.md")):
        lines = pf.read_text(encoding="utf-8").splitlines()
        title_m = re.match(r"^# Phase (\d+) — (.+?)(?: \(Weeks.*)?$", lines[0])
        phase_no = int(title_m.group(1))
        phase = {"number": phase_no, "title": title_m.group(2).strip(), "file": f"plan/{pf.name}", "weeks": []}
        phases.append(phase)
        current = None
        for line in lines:
            wm = WEEK_RE.match(line)
            if wm:
                n = int(wm.group(1))
                rest = wm.group(2)
                dm_ = DATES_RE.search(rest)
                start = dt.date.fromisoformat(dm_.group(1)) if dm_ else START + dt.timedelta(weeks=n - 1)
                title = DATES_RE.sub("", rest).strip(" —-")
                title = re.sub(r"\s+—\s+—\s+", " — ", title).strip(" —")
                current = {"number": n, "title": title, "start": start.isoformat(), "meta": "", "notes": [],
                           "subjects": WEEK_SUBJECTS.get(n, ["mixed"])}
                phase["weeks"].append(current)
                continue
            if current is None:
                continue
            if line.startswith(("## ", "### ")):
                current = None
                continue
            if line.startswith("**Hours"):
                current["meta"] = line.strip()
                continue
            rm = ROW_RE.match(line)
            if rm:
                day, slot, focus, resource, output = [g.strip() for g in rm.groups()]
                if day == "Day":
                    continue
                offset = DAY_NAMES.index(day)
                date = dt.date.fromisoformat(current["start"]) + dt.timedelta(days=offset)
                label, time = slot_label(day, slot)
                slot_id = re.sub(r"[^0-9A-Za-z]", "", slot) or "review"
                outputs = resolve_outputs(output, current["subjects"])
                if re.search(r"error analysis|error log|error-log", focus + " " + output, re.I) and \
                        not any(o["path"] == "trackers/error-log.md" for o in outputs):
                    outputs.append(file_link("error-log.md", "trackers/error-log.md"))
                task = {
                    "id": f"w{current['number']}-{day}-{slot_id}",
                    "slot": label, "time": time, "focus": focus,
                    "links": resolve_resources(resource, current["subjects"]),
                    "outputs": outputs,
                    "outputText": output if output not in ("—",) else "",
                }
                key = date.isoformat()
                if key not in days:
                    days[key] = {"date": key, "dayNumber": (date - START).days + 1, "weekday": day,
                                 "week": current["number"], "phase": phase_no, "tasks": []}
                days[key]["tasks"].append(task)
                continue
            stripped = line.strip()
            # Paragraphs between the "**Hours" line and the table are week notes (holidays, exam reminders).
            if stripped and current["meta"] and not current.get("_table") and not stripped.startswith(("|", "---", "- ")):
                current["notes"].append(stripped)
            if stripped.startswith("|"):
                current["_table"] = True
    for phase in phases:
        for week in phase["weeks"]:
            week.pop("_table", None)
    subjects = {k: {"name": v["name"], "video": v["video"], "pyq": v["pyq"], "backup": v["backup"],
                    "notes": f"notes/{v['notes']}/_index.md",
                    "sheet": f"notes/formula-sheets/{v['sheet']}.md" if v["sheet"] else None}
                for k, v in SUBJECTS.items()}
    return {"start": START.isoformat(), "phases": phases, "days": sorted(days.values(), key=lambda d: d["date"]),
            "subjects": subjects,
            "common": [link("GO PDFs", GO_PDF, "material"), link("GO exams (test mode)", GO_EXAMS, "practice"),
                       link("Virtual calculator", CALCULATOR, "tool"), link("Official GATE site", OFFICIAL_SITE, "material")]}


# ---------------------------------------------------------------------------
# Progress + local files
# ---------------------------------------------------------------------------

def read_progress():
    if not PROGRESS_FILE.exists():
        return {"version": 1, "done": {}}
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        data.setdefault("done", {})
        return data
    except (ValueError, OSError):
        return {"version": 1, "done": {}}


def write_progress(data):
    tmp = PROGRESS_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    os.replace(tmp, PROGRESS_FILE)


ALLOWED_DIRS = ("notes", "trackers", "reviews", "daily-logs", "plan", "docs")

NOTE_SKELETON = """# {title}

## Core idea

## Definitions / formulas

## Worked example (one PYQ, your own solution)

## Traps

## Related
"""


def safe_path(rel):
    rel = rel.replace("\\", "/").lstrip("/")
    target = (ROOT / rel).resolve()
    if ROOT not in target.parents or target.suffix != ".md":
        return None
    if target.relative_to(ROOT).parts[0] not in ALLOWED_DIRS:
        return None
    return target


def create_if_missing(target):
    if target.exists():
        return False
    rel = target.relative_to(ROOT).as_posix()
    target.parent.mkdir(parents=True, exist_ok=True)
    if rel.startswith("notes/"):
        title = target.stem.split("-", 2)[-1].replace("-", " ").capitalize()
        target.write_text(NOTE_SKELETON.format(title=title), encoding="utf-8")
    elif rel.startswith("reviews/weekly/"):
        target.write_text((ROOT / "reviews/weekly/TEMPLATE.md").read_text(encoding="utf-8"), encoding="utf-8")
    elif rel.startswith("reviews/monthly/"):
        target.write_text((ROOT / "reviews/monthly/TEMPLATE.md").read_text(encoding="utf-8"), encoding="utf-8")
    else:
        return None
    return True


PHASE_SLUGS = {1: "foundations", 2: "algo-maths-digital", 3: "systems", 4: "networks-theory", 5: "revision",
               6: "test-series", 7: "final-sprint"}
PHASE_START_WEEK = {1: 1, 2: 11, 3: 23, 4: 37, 5: 50, 6: 61, 7: 71}
SUBJECT_SLUGS = {"c": "c-programming", "ds": "data-structures", "dm": "discrete-maths", "algo": "algorithms",
                 "la": "linear-algebra", "calc": "calculus", "prob": "probability", "dl": "digital-logic", "coa": "coa",
                 "os": "os", "dbms": "dbms", "cn": "cn", "toc": "toc", "cd": "compiler-design", "mixed": "mixed"}


def daily_log_text(date_str):
    """The Markdown a new daily log starts from. Pure: reads only the template."""
    date = dt.date.fromisoformat(date_str)
    week = (date - START).days // 7 + 1
    phase = max(p for p, w in PHASE_START_WEEK.items() if week >= w) if week >= 1 else 1
    subj = WEEK_SUBJECTS.get(week, ["mixed"])[0]
    weekday = date.strftime("%A")
    hours = "0" if weekday == "Sunday" else "4.0" if weekday == "Saturday" else "3.0"
    text = (ROOT / "daily-logs" / "TEMPLATE.md").read_text(encoding="utf-8")
    repl = {
        r"^date: .*$": f"date: {date.isoformat()}",
        r"^day_of_week: .*$": f"day_of_week: {weekday}",
        r"^phase: .*$": f"phase: {PHASE_SLUGS[phase]}",
        r"^phase_week: .*$": f"phase_week: {week - PHASE_START_WEEK[phase] + 1}",
        r"^overall_week: .*$": f"overall_week: {week}",
        r"^target_hours: .*$": f"target_hours: {hours}",
        r"^subject: .*$": f"subject: {SUBJECT_SLUGS[subj]}",
        r"^focus_topic: .*$": "focus_topic: ",
    }
    for pattern, value in repl.items():
        text = re.sub(pattern, value, text, count=1, flags=re.M)
    return text


def daily_log(date_str):
    target = ROOT / "daily-logs" / f"{dt.date.fromisoformat(date_str).isoformat()}.md"
    created = False
    if not target.exists():
        target.write_text(daily_log_text(date_str), encoding="utf-8")
        created = True
    return target, created


PROGRESS_START = "<!-- planner-progress:start -->"
PROGRESS_END = "<!-- planner-progress:end -->"


def read_markdown(target):
    """Return one permitted Markdown file without launching a local editor."""
    if not target.exists():
        created = create_if_missing(target)
        if created is None:
            return None, False
        return target.read_text(encoding="utf-8"), bool(created)
    return target.read_text(encoding="utf-8"), False


def save_daily_progress(date_str):
    """Write the planner's current checklist to the day's Markdown log."""
    target, created = daily_log(date_str)
    day = next((item for item in parse_plan()["days"] if item["date"] == date_str), None)
    if day is None:
        raise ValueError("That date is not in the study plan")
    done = read_progress().get("done", {})
    block, completed = progress_block(day, done)
    current = target.read_text(encoding="utf-8")
    updated = apply_progress_block(current, block)
    target.write_text(updated, encoding="utf-8")
    return target, created, completed, len(day["tasks"]), updated


def progress_block(day, done):
    """The planner checklist snapshot for one day. Pure."""
    completed = sum(bool(done.get(task["id"])) for task in day["tasks"])
    timestamp = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")
    lines = [
        PROGRESS_START,
        "## Planner progress",
        f"Saved from the study planner: {timestamp}. **{completed}/{len(day['tasks'])} planned sessions completed.**",
        "",
    ]
    for task in day["tasks"]:
        mark = "x" if done.get(task["id"]) else " "
        focus = re.sub(r"`([^`]+)`", r"\1", task["focus"])
        lines.append(f"- [{mark}] **{task['slot']} ({task['time']})** — {focus}")
        if task["outputText"]:
            lines.append(f"  - Required record: {task['outputText']}")
    lines.extend(["", PROGRESS_END])
    return "\n".join(lines), completed


def apply_progress_block(text, block):
    pattern = re.compile(re.escape(PROGRESS_START) + r".*?" + re.escape(PROGRESS_END), re.S)
    if pattern.search(text):
        return pattern.sub(lambda _: block, text)
    return text.rstrip() + "\n\n" + block + "\n"


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

class Handler(BaseHTTPRequestHandler):
    server_version = "GatePlanner/1.0"

    def log_message(self, fmt, *args):
        pass

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_static(self, target, content_type):
        if not target.exists():
            self.send_json({"error": "Not found"}, 404)
            return
        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > 1_000_000:
            raise ValueError("payload too large")
        return json.loads(self.rfile.read(length) or b"{}")

    def do_GET(self):
        request = urlparse(self.path)
        path = request.path
        if path in ("/", "/index.html"):
            self.send_static(WEBAPP / "index.html", "text/html; charset=utf-8")
        elif re.fullmatch(r"/lib/[a-z0-9-]+\.js", path):
            self.send_static(WEBAPP / path.lstrip("/"), "text/javascript; charset=utf-8")
        elif path == "/manifest.webmanifest":
            self.send_static(WEBAPP / "manifest.webmanifest", "application/manifest+json")
        elif path == "/icon.svg":
            self.send_static(WEBAPP / "icon.svg", "image/svg+xml")
        elif path == "/api/plan":
            try:
                self.send_json(parse_plan())
            except Exception as exc:  # surface parse errors in the UI
                self.send_json({"error": f"Couldn't read the plan files: {exc}"}, 500)
        elif path == "/api/progress":
            self.send_json(read_progress())
        elif path == "/api/file":
            rel = parse_qs(request.query).get("path", [""])[0]
            target = safe_path(rel)
            if target is None:
                self.send_json({"error": "That file isn't inside the prep folders."}, 400)
                return
            with WRITE_LOCK:
                content, created = read_markdown(target)
            if content is None:
                self.send_json({"error": f"{target.name} doesn't exist yet."}, 404)
                return
            self.send_json({"ok": True, "created": created,
                            "path": target.relative_to(ROOT).as_posix(), "content": content})
        else:
            self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        # Custom header forces a CORS preflight, so other websites can't post to this server.
        if self.headers.get("X-Gate-Planner") != "1":
            self.send_json({"error": "Missing X-Gate-Planner header"}, 403)
            return
        path = urlparse(self.path).path
        try:
            payload = self.read_json()
        except ValueError as exc:
            self.send_json({"error": str(exc)}, 400)
            return
        if path == "/api/progress":
            task_id, done = payload.get("id"), payload.get("done")
            if not isinstance(task_id, str) or not re.fullmatch(r"w\d+-[A-Za-z]{3}-[0-9A-Za-z]+", task_id):
                self.send_json({"error": "Invalid task id"}, 400)
                return
            with WRITE_LOCK:
                data = read_progress()
                if done:
                    data["done"][task_id] = dt.datetime.now().isoformat(timespec="seconds")
                else:
                    data["done"].pop(task_id, None)
                write_progress(data)
            gitsync.touch()
            self.send_json({"ok": True, "done": data["done"]})
        elif path == "/api/file":
            target = safe_path(str(payload.get("path", "")))
            content = payload.get("content")
            if target is None or not isinstance(content, str):
                self.send_json({"error": "That file isn't inside the prep folders."}, 400)
                return
            if len(content.encode("utf-8")) > 1_000_000:
                self.send_json({"error": "Markdown file is too large."}, 400)
                return
            with WRITE_LOCK:
                created = create_if_missing(target)
                if created is None and not target.exists():
                    self.send_json({"error": f"{target.name} doesn't exist yet."}, 404)
                    return
                target.write_text(content, encoding="utf-8")
            gitsync.touch()
            self.send_json({"ok": True, "created": bool(created), "path": target.relative_to(ROOT).as_posix()})
        elif path == "/api/daily-log":
            try:
                target, created = daily_log(str(payload.get("date", "")))
            except ValueError:
                self.send_json({"error": "Invalid date"}, 400)
                return
            if created:
                gitsync.touch()
            self.send_json({"ok": True, "created": created, "path": target.relative_to(ROOT).as_posix(),
                            "content": target.read_text(encoding="utf-8")})
        elif path == "/api/daily-progress":
            try:
                target, created, completed, total, content = save_daily_progress(str(payload.get("date", "")))
            except ValueError as exc:
                self.send_json({"error": str(exc)}, 400)
                return
            gitsync.touch()
            self.send_json({"ok": True, "created": created, "completed": completed, "total": total,
                            "path": target.relative_to(ROOT).as_posix(), "content": content})
        else:
            self.send_json({"error": "Not found"}, 404)


def main():
    # Pull before serving: the hosted planner may have been ticking sessions
    # from a phone since the last time this ran.
    print(gitsync.init(ROOT))
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}"
    print(f"GATE study planner running at {url}  (Ctrl+C to stop)")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        # Commit whatever this session produced rather than leaving it behind.
        gitsync.flush()
        print("\nStopped.")


if __name__ == "__main__":
    main()
