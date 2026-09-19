# -*- coding: utf-8 -*-
"""Check every named video against its own description, not against a search result.

    python webapp/tools/verify_videos.py            # report only
    python webapp/tools/verify_videos.py --prune    # also delete the failures

build_videos.py picks videos by how well a *search result title* matches a topic.
That is a guess made by YouTube's ranker plus a keyword overlap. This asks the
video itself: it pulls the uploader's title, keywords, description and duration
from YouTube's player endpoint and decides whether the evidence supports the topic
it has been filed under.

A video passes when the topic's own vocabulary shows up in its metadata often
enough, and fails when the description reveals it is a different course entirely -
a C++ lecture filed under a C topic, an AI lecture filed under Discrete Maths, or
a fifteen-second short. Results are cached, so re-running is cheap.
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
CACHE = HERE / "details-cache.json"

# A description mentioning one of these is teaching a different course. Checked
# against the description as well as the title, which is the point of this pass.
OFF_DOMAIN = build_videos.OFF_DOMAIN
WRONG_LANG = build_videos.WRONG_LANG
C_SUBJECTS = build_videos.C_SUBJECTS

PASS, WEAK, FAIL = "pass", "weak", "fail"


def load_cache():
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return {}


# Every big channel ends its description with the same block: course links, an app
# download, a social list, then thirty hashtags. It mentions Android, Machine
# Learning and Web Development on a video about spanning trees. Cut it off before
# reading anything into the words.
BOILERPLATE = re.compile(
    r"(^|\n)\s*(?:https?://|#\w|download\b|subscribe\b|follow us|join (?:our|us)|"
    r"telegram|instagram|facebook|linkedin|whatsapp|playlist link|"
    r"for more|our courses|check out our)", re.I)


def body(description):
    """The part of a description the uploader actually wrote about this video."""
    m = BOILERPLATE.search(description)
    return description[:m.start()] if m else description[:1200]


def evidence(det):
    """What the uploader said about this video, boilerplate removed."""
    return " ".join([det["title"], " ".join(det["keywords"][:40]), body(det["description"])])


def judge(entry, det):
    """(verdict, score, reason) for one video under one topic.

    The description is positive evidence only. It cannot be used to rule a video
    out by domain keywords, because the promotional tail on almost every channel
    lists their other courses - checking it there failed 92 of 389 videos,
    including GO Classes' own lecture on minimum spanning trees.
    """
    if det is None:
        return FAIL, 0, "no metadata (removed, private, or region locked)"

    hits = topic_mod._words(evidence(det)) & entry["_words"]
    score = sum(2 if w in entry["_rare"] else 1 for w in hits)
    title_hits = topic_mod._words(det["title"]) & entry["_words"]
    rare_hits = hits & entry["_rare"]

    # Domain and language are judged from the title, which no one pads.
    if OFF_DOMAIN.search(det["title"]):
        return FAIL, score, "title says a different course"
    if entry["subject"] in C_SUBJECTS and WRONG_LANG.search(det["title"]) \
            and not re.search(r"\bC programming\b|\bin C\b", det["title"], re.I):
        return FAIL, score, "taught in a different language"
    if det["seconds"] and det["seconds"] < 150:
        return FAIL, score, f"only {det['seconds']}s long"

    # A rare word belongs to at most two topics in the whole syllabus, so one of
    # those is stronger evidence than several generic hits.
    if rare_hits or score >= 5 or len(title_hits) >= 2:
        return PASS, score, ",".join(sorted(rare_hits)[:4]) or f"{len(hits)} topic words"
    if score >= 2:
        return WEAK, score, f"{len(hits)} topic words, none distinctive"
    return FAIL, score, "nothing in title, keywords or description matches this topic"


def main():
    prune = "--prune" in sys.argv
    catalogue = topic_mod.build_catalogue(server.SUBJECTS)
    videos = topic_mod.load_videos()
    cache = load_cache()

    rows = [(tid, v) for tid, vs in videos.items() for v in vs]
    print(f"verifying {len(rows)} videos against their own descriptions\n")

    verdicts = {}
    fetched = 0
    for n, (tid, v) in enumerate(rows, 1):
        vid = v["id"]
        if vid not in cache:
            det = yt.details(vid)
            cache[vid] = det
            fetched += 1
            if fetched % 10 == 0:
                CACHE.write_text(json.dumps(cache, indent=1), encoding="utf-8")
                print(f"  ... {n}/{len(rows)}", flush=True)
            time.sleep(0.35)
        det = cache[vid]
        verdict, score, reason = judge(catalogue[tid], det)
        verdicts[(tid, vid)] = (verdict, score, reason)
    CACHE.write_text(json.dumps(cache, indent=1), encoding="utf-8")

    counts = {PASS: 0, WEAK: 0, FAIL: 0}
    for verdict, _, _ in verdicts.values():
        counts[verdict] += 1

    print(f"\npass {counts[PASS]}   weak {counts[WEAK]}   fail {counts[FAIL]}\n")

    for want, label in ((FAIL, "FAILED"), (WEAK, "WEAK")):
        listed = [(t, v) for (t, v), (verdict, _, _) in verdicts.items() if verdict == want]
        if not listed:
            continue
        print(f"--- {label} ({len(listed)})")
        for tid, vid in sorted(listed):
            det = cache.get(vid) or {}
            _, score, reason = verdicts[(tid, vid)]
            print(f"  {tid:<7} {det.get('channel', '?')[:22]:<22} "
                  f"{det.get('title', vid)[:46]:<46} score {score:>2}  {reason}")
        print()

    if prune:
        removed = {(t, v) for (t, v), (verdict, _, _) in verdicts.items() if verdict == FAIL}
        if not removed:
            print("nothing to prune")
            return 0
        kept = []
        for line in VIDEOS.read_text(encoding="utf-8").splitlines():
            m = topic_mod.VIDEO_RE.match(line)
            if m and (m.group(1), m.group(2)) in removed:
                continue
            kept.append(line)
        VIDEOS.write_text("\n".join(kept) + "\n", encoding="utf-8")
        print(f"pruned {len(removed)} row(s) from {VIDEOS.name}; "
              f"re-run build_videos.py for the topics left short")
    return 0


if __name__ == "__main__":
    sys.exit(main())
