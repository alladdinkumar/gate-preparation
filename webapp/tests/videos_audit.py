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
# A channel home page or a channel-scoped search. Never acceptable anywhere: both
# land you on a list of a channel's output instead of a lecture.
CHANNEL_PAGE = re.compile(r"youtube\.com/(@|channel/)")
# A playlist is fine as a *subject* link when the playlist really is that subject's
# course - Discrete Maths has 71 videos, DBMS 90. It is not fine as a *topic* link,
# where the whole point is to name the one video that teaches this topic.
PLAYLIST = re.compile(r"[?&]list=")


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
            for link in entry["lectures"] + entry.get("pyqVideos", []):
                if link.get("video") and not WATCH.match(link["url"]):
                    problems.append((d["date"], t["id"], f"not a watch link: {link['url']}"))
            # Everything the session renders, not just the videos. The chips built by
            # resolve_resources and the topic fallback row are what actually broke
            # twice: a subject with no playlist fell back to a channel page, and the
            # fallback row linked channel-scoped searches. Checking the catalogue
            # alone missed both, because neither lives in the catalogue's videos.
            for link in (entry["lectures"] + entry.get("search", [])
                         + entry.get("pyqVideos", []) + entry["practice"]):
                url = link.get("url", "")
                if CHANNEL_PAGE.search(url) or PLAYLIST.search(url):
                    problems.append((d["date"], t["id"],
                                     f"{tid} topic row links a channel or playlist: {url}"))
        for link in t["links"]:
            if CHANNEL_PAGE.search(link.get("url", "")):
                problems.append((d["date"], t["id"],
                                 f"session chip links a channel page: {link['url']}"))
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
    # Videos are dealt out, not repeated: count how many days each one appears on.
    from collections import Counter as _C
    shown = _C()
    for d in days:
        for t in d["tasks"]:
            for tid, c in (t.get("videoCut") or {}).items():
                e = catalogue.get(tid) or {}
                for i in c.get("lidx", []):
                    shown[e["lectures"][i]["url"]] += 1
                for i in c.get("pidx", []):
                    shown[e.get("pyqVideos", [])[i]["url"]] += 1
    repeats = [u for u, n in shown.items() if n > 1]
    print(f"videos dealt to a day      {len(shown)}")
    print(f"  shown on more than one   {len(repeats)}")
    if repeats:
        problems.append(("-", "-", f"{len(repeats)} video(s) repeat across days"))
    print(f"topics                     {len(catalogue)}")
    print(f"  with videos              {sum(1 for t in catalogue if cat_videos.get(t))}")
    print(f"  with 3 or more           {sum(1 for t in catalogue if len(cat_videos.get(t, [])) >= 3)}")
    pyq = topics.load_pyq_videos()
    print(f"  with solved-question vids {sum(1 for t in catalogue if pyq.get(t))}")
    print(f"solved-question videos     {sum(len(v) for v in pyq.values())}")

    # A topic is a list of concepts, not one idea. Report how many of those concepts
    # a video actually mentions, because "every topic has three videos" hides the
    # case where all three are about the first item in the list.
    try:
        import cover_topics
        named = covered = 0
        for tid, entry in catalogue.items():
            blobs = [v["title"] for v in cat_videos.get(tid, [])]
            for c in cover_topics.concepts(entry["name"]):
                named += 1
                covered += 1 if cover_topics.covers(c, blobs) else 0
        pct = covered / named * 100 if named else 0
        print(f"concepts named by topics   {named}")
        print(f"  mentioned by a video     {covered} ({pct:.0f}%, titles only)")
    except Exception as exc:
        print(f"concept coverage           (not computed: {exc})")
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
