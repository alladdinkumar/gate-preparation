# -*- coding: utf-8 -*-
"""Judge every session against what it actually offers, one day at a time.

    python webapp/tests/relevance_report.py              # summary + suspects
    python webapp/tests/relevance_report.py --all        # every session, one line
    python webapp/tests/relevance_report.py --day 42     # one day in full

Other checks ask "is this video about its topic". This asks the sharper question:
now that videos are dealt out to individual days, is the video this session hands
you about *this session*? A pointer-arithmetic lecture is a fine PD-3 video and
the wrong thing to open on the day the plan says "strings".

Three judgements per session:
  TOPIC   does the assigned topic match the focus text
  VIDEO   does each dealt video match the focus, or at least the topic
  LINKS   is every link well-formed and not a channel or playlist page
"""

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
WEBAPP = HERE.parent
sys.path.insert(0, str(WEBAPP))
sys.path.insert(0, str(WEBAPP / "tools"))

import server   # noqa: E402
import topics   # noqa: E402

DETAILS = WEBAPP / "tools" / "details-cache.json"
WATCH = re.compile(r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$")
CHANNEL_OR_LIST = re.compile(r"youtube\.com/(@|channel/)|[?&]list=")


def blob(det, fallback):
    if not det:
        return fallback
    body = det.get("description", "")[:700]
    return " ".join([det.get("title", ""), " ".join(det.get("keywords", [])[:30]), body])


def overlap(a_words, b_words, rare):
    hit = a_words & b_words
    return sum(2 if w in rare else 1 for w in hit), hit


def main():
    show_all = "--all" in sys.argv
    one_day = None
    if "--day" in sys.argv:
        one_day = int(sys.argv[sys.argv.index("--day") + 1])

    plan = server.parse_plan()
    catalogue = topics.build_catalogue(server.SUBJECTS)
    details = json.loads(DETAILS.read_text(encoding="utf-8")) if DETAILS.exists() else {}

    counts = {"ok": 0, "weak": 0, "bad": 0}
    suspects = []
    link_problems = []

    for day in plan["days"]:
        if one_day and day["dayNumber"] != one_day:
            continue
        for task in day["tasks"]:
            focus_words = topics._words(task["focus"] + " " + task.get("outputText", ""))
            cut = task.get("videoCut") or {}

            # ---- links -------------------------------------------------
            for link in task["links"]:
                url = link.get("url", "")
                if url and CHANNEL_OR_LIST.search(url) and "list=" not in url:
                    link_problems.append((day["dayNumber"], task["id"], url))

            for tid in task["topics"]:
                entry = catalogue.get(tid)
                if not entry:
                    continue
                t_score, _ = overlap(focus_words, entry["_words"], entry["_rare"])

                dealt = []
                for i in cut.get(tid, {}).get("lidx", []):
                    dealt.append(("lecture", entry["lectures"][i]))
                for i in cut.get(tid, {}).get("pidx", []):
                    dealt.append(("solved", entry.get("pyqVideos", [])[i]))

                for kind, link in dealt:
                    url = link["url"]
                    if not WATCH.match(url):
                        link_problems.append((day["dayNumber"], task["id"], url))
                    vid = url[-11:]
                    text = blob(details.get(vid), link["label"])
                    v_words = topics._words(text)
                    f_score, _ = overlap(focus_words, v_words, entry["_rare"])
                    t_vid, _ = overlap(entry["_words"], v_words, entry["_rare"])

                    if f_score >= 2:
                        verdict = "ok"
                    elif t_vid >= 3:
                        verdict = "weak"       # right topic, not this session's slice
                    else:
                        verdict = "bad"
                    counts[verdict] += 1
                    if verdict == "bad":
                        suspects.append((day["dayNumber"], day["date"], task["id"], tid,
                                         task["focus"][:44], kind, link["label"][:52],
                                         f_score, t_vid))
                    if show_all:
                        print(f"{verdict:<4} day {day['dayNumber']:>3} {task['id']:<16} "
                              f"{tid:<6} f{f_score:<2} t{t_vid:<2} {link['label'][:56]}")

    total = sum(counts.values())
    print(f"\nvideo placements judged   {total}")
    print(f"  match the session focus {counts['ok']}")
    print(f"  match only the topic    {counts['weak']}")
    print(f"  match neither           {counts['bad']}")
    print(f"link problems             {len(link_problems)}")
    for p in link_problems[:10]:
        print("   ", p)

    if suspects:
        print(f"\nsuspect placements ({len(suspects)}), worst first:")
        for s in sorted(suspects, key=lambda x: (x[7], x[8]))[:45]:
            print(f"  day {s[0]:>3} {s[2]:<16} {s[3]:<6} [{s[5]}] f{s[7]} t{s[8]}")
            print(f"        focus: {s[4]}")
            print(f"        video: {s[6]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
