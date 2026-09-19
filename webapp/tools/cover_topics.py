# -*- coding: utf-8 -*-
"""Is every concept named in a topic actually covered by one of its videos?

    python webapp/tools/cover_topics.py            # report the gaps
    python webapp/tools/cover_topics.py --fill     # search for videos to close them
    python webapp/tools/cover_topics.py --fill PD-1 OS-3

A syllabus topic is not one idea. OS-3 is "CPU scheduling - FCFS, SJF, SRTF, RR,
priority, multilevel queue/feedback, Gantt charts, waiting/turnaround time,
starvation": ten things. Three videos on "CPU scheduling" can easily leave SRTF and
starvation untouched, and the topic still looks fully covered from the outside.

This splits each topic name into the concepts it lists, then asks whether any of
that topic's videos actually mentions each one - using the uploader's title,
keywords and description, cached by verify_videos.py. What is missing gets its own
search, and any video found is held to the same acceptance checks as the rest.
"""

import json
import re
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import yt                        # noqa: E402
import server                    # noqa: E402
import topics as topic_mod       # noqa: E402
import build_videos              # noqa: E402

ROOT = HERE.parent.parent
VIDEOS = ROOT / "plan" / "topic-videos.md"
DETAILS = HERE / "details-cache.json"

# Concepts too generic to be worth checking on their own: every video in the subject
# "covers" them, so a miss means nothing.
SKIP = {"basics", "introduction", "concepts", "properties", "types", "examples",
        "applications", "operations", "problems", "questions", "idea", "etc"}


def concepts(name):
    """The individual things a topic name lists."""
    # "control flow (switch fall-through, loops)" is three concepts, not one.
    text = re.sub(r"\(([^)]*)\)", r", \1", name)
    out = []
    for part in re.split(r"[,;·]|—| and (?=[a-z])", text):
        part = part.strip(" -–—.")
        if not part:
            continue
        words = topic_mod._words(part)
        if not words or all(w in SKIP for w in words):
            continue
        out.append({"text": part, "words": words})
    return out


def video_text(det):
    if not det:
        return ""
    return " ".join([det.get("title", ""), " ".join(det.get("keywords", [])[:40]),
                     det.get("description", "")[:900]])


def covers(concept, blobs):
    """True when some video's own metadata mentions this concept.

    A concept is matched when its distinctive words appear. One-word concepts
    ("starvation", "SRTF") need that word; multi-word ones need most of them, so
    "carry-lookahead" is not satisfied by a video that merely says "carry".
    """
    words = concept["words"]
    need = 1 if len(words) == 1 else max(1, round(len(words) * 0.6))
    for blob in blobs:
        got = topic_mod._words(blob) & words
        if len(got) >= need:
            return True
    return False


def main():
    fill = "--fill" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]

    catalogue = topic_mod.build_catalogue(server.SUBJECTS)
    videos = topic_mod.load_videos()
    details = json.loads(DETAILS.read_text(encoding="utf-8")) if DETAILS.exists() else {}

    ids = only or list(catalogue)
    total_concepts = covered_concepts = 0
    gaps = {}

    for tid in ids:
        entry = catalogue[tid]
        blobs = [video_text(details.get(v["id"])) or v["title"]
                 for v in videos.get(tid, [])]
        missing = []
        for c in concepts(entry["name"]):
            total_concepts += 1
            if covers(c, blobs):
                covered_concepts += 1
            else:
                missing.append(c)
        if missing:
            gaps[tid] = missing

    pct = covered_concepts / total_concepts * 100 if total_concepts else 0
    print(f"concepts named across {len(ids)} topics: {total_concepts}")
    print(f"  covered by an existing video: {covered_concepts} ({pct:.0f}%)")
    print(f"  not covered                 : {total_concepts - covered_concepts}")
    print(f"  topics with a gap           : {len(gaps)}\n")

    for tid, missing in sorted(gaps.items())[:40]:
        print(f"  {tid:<7} {', '.join(c['text'][:28] for c in missing)}")
    if len(gaps) > 40:
        print(f"  ... and {len(gaps) - 40} more topics")

    if not fill:
        return 0

    print("\nfilling gaps\n")
    added_rows = []
    for n, (tid, missing) in enumerate(sorted(gaps.items()), 1):
        entry = catalogue[tid]
        have = {v["id"] for v in videos.get(tid, [])}
        print(f"[{n}/{len(gaps)}] {tid}: {len(missing)} missing", flush=True)
        for c in missing:
            found = search_for(c, entry, have)
            if found:
                have.add(found["id"])
                added_rows.append((tid, found, c["text"]))
                print(f"      + {c['text'][:30]:<30} {found['channel'][:18]:<18} "
                      f"{found['title'][:44]}", flush=True)
            else:
                print(f"      - {c['text'][:30]:<30} (nothing passed)", flush=True)
            time.sleep(1.2)

    if added_rows:
        append_rows(added_rows)
    print(f"\nadded {len(added_rows)} video(s) to {VIDEOS.name}")
    return 0


def search_for(concept, entry, have):
    """One video for one concept, held to the usual acceptance checks."""
    queries = [
        f"{concept['text']} {entry['subjectName']} GATE",
        f"{concept['text']} {entry['short']} explained",
    ]
    # Match against the concept, not the whole topic - that is the point here.
    probe = dict(entry)
    probe["_words"] = concept["words"] | entry["_words"]
    probe["_rare"] = concept["words"]

    best = []
    for q in queries:
        try:
            results = yt.search(q, limit=12)
        except Exception:
            results = []
        for v in results:
            if v["id"] in have:
                continue
            if entry["subject"] in build_videos.C_SUBJECTS and \
                    build_videos.WRONG_LANG.search(v["title"]):
                continue
            if build_videos.BAD_TITLE.search(v["title"]) or \
                    build_videos.OFF_DOMAIN.search(v["title"]):
                continue
            # The title must speak to this concept, or the search drifted back to
            # the topic at large and we would add a fourth video about nothing new.
            if not (topic_mod._words(v["title"]) & concept["words"]):
                continue
            s, _ = build_videos.score(v, probe["_words"], probe["_rare"], entry["subject"])
            v["score"] = s
            best.append(v)
        if best:
            break
        time.sleep(1.5)

    best.sort(key=lambda v: -v["score"])
    for v in best[:6]:
        ok = build_videos.accept(v, probe)
        if ok:
            return ok
        time.sleep(0.3)
    return None


def append_rows(rows):
    """Add rows under the right topic, keeping the file grouped by topic id."""
    lines = VIDEOS.read_text(encoding="utf-8").splitlines()
    by_topic = {}
    for tid, v, why in rows:
        title = v["title"].replace("|", "/").strip()
        chan = v["channel"].replace("|", "/").strip()
        by_topic.setdefault(tid, []).append(f"| {tid} | {v['id']} | {chan} | {title} |")

    out, inserted = [], set()
    for i, line in enumerate(lines):
        m = topic_mod.VIDEO_RE.match(line)
        out.append(line)
        if not m:
            continue
        tid = m.group(1)
        nxt = topic_mod.VIDEO_RE.match(lines[i + 1]) if i + 1 < len(lines) else None
        if tid in by_topic and tid not in inserted and (not nxt or nxt.group(1) != tid):
            out.extend(by_topic[tid])
            inserted.add(tid)

    for tid, extra in by_topic.items():          # topics that had no rows at all
        if tid not in inserted:
            out.extend(extra)
    VIDEOS.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
