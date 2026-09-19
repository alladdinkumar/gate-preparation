# -*- coding: utf-8 -*-
"""Pick three real, verified YouTube videos for each of the 124 syllabus topics.

For every topic: search YouTube for its phrase, score the results by channel and
by how well the title matches the topic, take the best three from three different
channels, and confirm each id against oEmbed before writing it down. Anything that
fails verification is dropped and the next candidate takes its place.

Writes plan/topic-videos.md. Re-runnable; existing rows are reused unless --refresh.
"""
import json
import re
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))              # yt.py, beside this file
sys.path.insert(0, str(HERE.parent))       # server.py, topics.py

import yt                       # noqa: E402
import server                   # noqa: E402
import topics as topic_mod      # noqa: E402

ROOT = HERE.parent.parent
OUT = ROOT / "plan" / "topic-videos.md"
CACHE = HERE / "video-cache.json"          # gitignored; delete it to start clean

# Channels worth sending Sandeep to, best first. Tier 1 are the ones resources.md
# already vouches for; tier 2 are large free GATE/CS teaching channels used only
# when tier 1 has nothing on the topic.
TIER1 = {
    "go classes": 9, "goclasses": 9,
    "gate smashers": 8,
    "neso academy": 8,
    "ravindrababu ravula": 7, "gate lectures by ravindrababu ravula": 7,
    "abdul bari": 7,
}
TIER2 = {
    "knowledge gate": 5, "knowledgegate": 5,
    "jenny's lectures cs it": 5, "jennys lectures cs it": 5,
    "nptel": 5, "nptel-noc iitm": 5, "iit madras - nptel": 5,
    "unacademy computer science": 4,
    "cse classroom": 4,
    "education 4u": 4,
    "sudhakar atchala": 4,
    "thegatehub": 4, "gate hub": 4,
    "byju's exam prep gate & es": 3,
    "last moment tuitions": 3,
    "mysirg.com": 3, "mysirg": 3,
}

BAD_TITLE = re.compile(r"\b(shorts?|#shorts|motivation|strategy|time table|cut ?off|"
                       r"vacancy|result|admit card|counselling|salary|job|placement|"
                       r"live class|doubt session|orientation|demo|webinar|"
                       # Whole-subject marathons: relevant, but they are exactly the
                       # generic link that naming individual videos exists to replace.
                       r"one shot|all in one|complete course|full course|crash course|"
                       r"in one video|marathon|entire syllabus)\b", re.I)

# GATE code questions are C. A video teaching the same concept in Python or C++ is
# the wrong video however well its title matches - "Operators in Python" outscored
# everything for "C operators precedence" until this existed.
WRONG_LANG = re.compile(r"(python|\bjava\b|javascript|c\+\+|\bcpp\b|c#|kotlin|golang)", re.I)
RIGHT_LANG = re.compile(r"(\bin c\b|\bc program|\bc language|\bc\b(?!\+\+))", re.I)
C_SUBJECTS = {"c", "ds"}


def seconds(text):
    if not text:
        return 0
    parts = [p for p in text.split(":") if p.strip().isdigit()]
    if not parts:
        return 0
    s = 0
    for p in parts:
        s = s * 60 + int(p)
    return s


def score(video, words, rare, subject=None):
    ch = video["channel"].lower().strip()
    base = TIER1.get(ch) or TIER2.get(ch) or 0
    if base == 0:
        for name, pts in {**TIER1, **TIER2}.items():
            if name in ch:
                base = pts
                break
    title_words = topic_mod._words(video["title"])
    hits = title_words & words
    overlap = sum(2 if w in rare else 1 for w in hits)

    dur = seconds(video["duration"])
    if dur and dur < 180:
        overlap -= 4                      # too short to teach anything
    elif dur and dur > 9000:
        overlap -= 2                      # a whole marathon, not a topic
    if BAD_TITLE.search(video["title"]):
        overlap -= 8
    if re.search(r"\bGATE\b", video["title"], re.I):
        overlap += 1
    if subject in C_SUBJECTS:
        if WRONG_LANG.search(video["title"]):
            overlap -= 12                 # right concept, wrong language
        elif RIGHT_LANG.search(video["title"]):
            overlap += 2
    return base * 2 + overlap, base


def pick(topic, entry, want=4):
    """Search, score, verify. Returns up to `want` confirmed videos."""
    words = entry["_words"]
    rare = entry["_rare"]
    phrase = entry["phrase"]

    # Three angles on the same topic. The long phrase is precise but skews results
    # toward its tail words; the short name plus the subject finds the canonical
    # lecture that every channel has; the bare phrase catches the rest.
    queries = [
        f"{phrase} GATE",
        f"{entry['short'].rstrip('.')} {entry['subjectName']} GATE",
        phrase,
    ]
    candidates, seen = [], set()
    for query in queries:
        try:
            results = yt.search(query, limit=20)
        except Exception as e:
            print(f"    search failed ({e})", flush=True)
            results = []
        for v in results:
            if v["id"] in seen:
                continue
            seen.add(v["id"])
            # A Python or C++ video is never the right answer for a C topic, no
            # matter how good the channel - so exclude, do not merely penalise.
            if entry["subject"] in C_SUBJECTS and WRONG_LANG.search(v["title"]):
                continue
            if BAD_TITLE.search(v["title"]):
                continue                  # marathons and non-teaching uploads, never
            s, tier = score(v, words, rare, entry["subject"])
            # An unrecognised channel has to be an overwhelming title match: at 6
            # this let in a lecture in Indonesian that happened to say "delay",
            # "throughput" and "packet switching". General Aptitude is the exception
            # - no GATE CS channel teaches English grammar, so holding it to the CS
            # bar leaves those topics with nothing at all.
            if tier == 0 and s < (7 if entry["subject"] == "ga" else 10):
                continue
            v["score"] = s
            candidates.append(v)
        if len(candidates) >= 18:
            break
        time.sleep(2.0)

    candidates.sort(key=lambda v: -v["score"])

    chosen, used_channels = [], set()
    for v in candidates:
        if len(chosen) >= want:
            break
        ch = v["channel"].lower()
        if ch and ch in used_channels:
            continue                      # three teachers, not one teacher three times
        ok, real_title, real_channel = yt.verify(v["id"])
        if not ok:
            continue
        used_channels.add(ch)
        chosen.append({"id": v["id"],
                       "title": (real_title or v["title"]).strip(),
                       "channel": (real_channel or v["channel"]).strip(),
                       "duration": v["duration"]})
        time.sleep(0.25)

    # If three distinct channels was too strict, allow repeats to fill the gap.
    if len(chosen) < want:
        have = {c["id"] for c in chosen}
        for v in candidates:
            if len(chosen) >= want:
                break
            if v["id"] in have:
                continue
            ok, real_title, real_channel = yt.verify(v["id"])
            if not ok:
                continue
            chosen.append({"id": v["id"],
                           "title": (real_title or v["title"]).strip(),
                           "channel": (real_channel or v["channel"]).strip(),
                           "duration": v["duration"]})
            time.sleep(0.25)
    return chosen


def main():
    refresh = "--refresh" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]

    catalogue = topic_mod.build_catalogue(server.SUBJECTS)
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() and not refresh else {}

    ids = only or list(catalogue)
    for n, tid in enumerate(ids, 1):
        if tid in cache and cache[tid]:
            continue
        entry = catalogue[tid]
        print(f"[{n}/{len(ids)}] {tid} {entry['phrase'][:52]}", flush=True)
        got = pick(tid, entry)
        cache[tid] = got
        for g in got:
            print(f"      {g['channel'][:22]:<22} {g['title'][:60]}", flush=True)
        if not got:
            print("      (nothing passed)", flush=True)
        CACHE.write_text(json.dumps(cache, indent=1), encoding="utf-8")
        time.sleep(2.0)

    write(catalogue, cache)


def write(catalogue, cache):
    lines = [
        "# Topic Videos — the actual lecture for each topic",
        "",
        "One row per video: **the video itself**, not a playlist and not a channel.",
        "`topic-lectures.md` said *where* to look; this file says *what to watch*, because",
        "\"open the C playlist\" is not an answer when the C playlist turns out to be nine",
        "videos about structs.",
        "",
        "**How these were chosen.** For each topic, YouTube was searched for the topic's",
        "phrase, results were ranked by channel and by title match, and the best three from",
        "three different teachers were kept. **Every id below was then confirmed against",
        "YouTube's oEmbed endpoint**, which rejects anything that does not exist or cannot",
        "be embedded — the title and channel columns are the ones YouTube returned, not the",
        "ones the search page claimed. Nothing here was typed from memory.",
        "",
        "**What this does not do:** it matches on titles, not on full video descriptions.",
        "A title that lies will get through. If a link is wrong, delete the row — the",
        "planner falls back to the channel search in `topic-lectures.md` for that topic.",
        "",
        "Regenerate with `python webapp/tools/build_videos.py` (all topics) or pass topic",
        "ids to redo only those.",
        "",
        "| # | Video ID | Channel | Title |",
        "|---|----------|---------|-------|",
    ]
    total = 0
    for tid in catalogue:
        for v in cache.get(tid, []):
            title = v["title"].replace("|", "/").strip()
            chan = v["channel"].replace("|", "/").strip()
            lines.append(f"| {tid} | {v['id']} | {chan} | {title} |")
            total += 1
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")

    covered = sum(1 for t in catalogue if cache.get(t))
    three = sum(1 for t in catalogue if len(cache.get(t, [])) >= 3)
    print(f"\nwrote {OUT.name}: {total} videos, {covered}/{len(catalogue)} topics covered, "
          f"{three} with three")


if __name__ == "__main__":
    main()
