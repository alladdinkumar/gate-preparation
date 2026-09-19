"""Walk every day of the plan and report what each session actually links to.

    python webapp/tests/videos_audit.py            # summary
    python webapp/tests/videos_audit.py --days     # every day, one line each
    python webapp/tests/videos_audit.py --bad      # only the sessions worth fixing

The topic tests check the catalogue. This checks the thing that matters on the day:
open any of the 504 days, and does the session in front of you link to a lecture on
what it is about? It re-derives that from plan.json rather than trusting the
catalogue, so a matching bug shows up here as a day with the wrong videos.
"""

import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
WEBAPP = HERE.parent
sys.path.insert(0, str(WEBAPP))
sys.path.insert(0, str(WEBAPP / "tools"))

import server   # noqa: E402
import topics   # noqa: E402

try:
    import build_videos            # noqa: E402
    TRUSTED = {**build_videos.TIER1, **build_videos.TIER2}
except Exception:                  # the tool needs no deps, but don't die if it moves
    TRUSTED = {}

WATCH = re.compile(r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$")


def trusted(channel):
    c = channel.lower()
    return any(name in c for name in TRUSTED)


def main():
    show_days = "--days" in sys.argv
    only_bad = "--bad" in sys.argv

    plan = server.parse_plan()
    catalogue = topics.build_catalogue(server.SUBJECTS)
    cat_videos = topics.load_videos()

    days = plan["days"]
    sessions = [(d, t) for d in days for t in d["tasks"]]
    studied = [(d, t) for d, t in sessions if t["topics"]]

    problems = []
    day_rows = []
    video_sessions = 0
    channel_counts = Counter()

    for d, t in studied:
        vids, off_topic, untrusted = [], [], []
        for tid in t["topics"]:
            entry = catalogue.get(tid)
            if not entry:
                problems.append((d["date"], t["id"], f"unknown topic {tid}"))
                continue
            for v in cat_videos.get(tid, []):
                vids.append(v)
                channel_counts[v["channel"]] += 1
                # On-topic means the title shares vocabulary with the topic it is
                # filed under - the cheap version of "does this video match".
                if not (topics._words(v["title"]) & entry["_words"]):
                    off_topic.append((tid, v["channel"], v["title"]))
                if TRUSTED and not trusted(v["channel"]):
                    untrusted.append((tid, v["channel"], v["title"]))
            for link in entry["lectures"]:
                if link.get("video") and not WATCH.match(link["url"]):
                    problems.append((d["date"], t["id"], f"not a watch link: {link['url']}"))
        if vids:
            video_sessions += 1
        for tid, ch, title in off_topic:
            problems.append((d["date"], t["id"], f"{tid} off-topic: {ch} - {title[:54]}"))
        day_rows.append((d, t, len(vids), len(off_topic), len(untrusted)))

    if show_days or only_bad:
        for d, t, n, off, unt in day_rows:
            flag = "BAD " if off else ("weak" if unt else "ok  ")
            if only_bad and not off and not unt:
                continue
            print(f"{flag} day {d['dayNumber']:>3} {d['date']} {t['id']:<16} "
                  f"{','.join(t['topics']):<18} {n} videos"
                  + (f"  off-topic:{off}" if off else "")
                  + (f"  untrusted:{unt}" if unt else ""))

    print(f"\ndays                       {len(days)}")
    print(f"sessions                   {len(sessions)}")
    print(f"  with a topic             {len(studied)}")
    print(f"  with at least one video  {video_sessions}")
    print(f"topics                     {len(catalogue)}")
    print(f"  with videos              {sum(1 for t in catalogue if cat_videos.get(t))}")
    print(f"  with 3 or more           {sum(1 for t in catalogue if len(cat_videos.get(t, [])) >= 3)}")
    # Count the rows in topic-videos.md, not the times a row is shown: a video on a
    # topic that recurs across twenty sessions is still one video.
    rows = [(t, v) for t, vs in cat_videos.items() for v in vs]
    row_channels = Counter(v["channel"] for _, v in rows)
    print(f"videos                     {len(rows)}")
    print(f"  distinct channels        {len(row_channels)}")
    if TRUSTED:
        untrusted_rows = [(t, v["channel"]) for t, v in rows if not trusted(v["channel"])]
        print(f"  from untrusted channels  {len(untrusted_rows)}")
        if untrusted_rows:
            for ch, n in Counter(c for _, c in untrusted_rows).most_common(8):
                print(f"      {n:>3}  {ch}")
    print(f"  shown across sessions    {sum(channel_counts.values())}")

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems[:40]:
            print("   ", p[0], p[1], "-", p[2])
        if len(problems) > 40:
            print(f"    ... and {len(problems) - 40} more")
    else:
        print("\nno session links to a video that is off-topic for it")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
