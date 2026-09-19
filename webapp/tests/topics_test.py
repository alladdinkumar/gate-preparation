"""Checks the topic catalogue that the planner hangs off every session.

    python webapp/tests/topics_test.py

The catalogue is assembled from three files that are edited by hand at different
times - the syllabus, the curriculum tables and topic-lectures.md - so the failure
mode is not a crash, it is a topic quietly losing its links. These assertions are
about that: every syllabus row is present, every topic has somewhere to go, and no
link is a placeholder. Runs in CI with the parity test.
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
WEBAPP = HERE.parent
ROOT = WEBAPP.parent
sys.path.insert(0, str(WEBAPP))

import server  # noqa: E402
import topics  # noqa: E402

failures = []


def check(name, condition, detail=""):
    if condition:
        print(f"  ok    {name}")
    else:
        failures.append(name)
        print(f"  FAIL  {name}{' - ' + detail if detail else ''}")


def syllabus_ids():
    text = (ROOT / "plan" / "syllabus.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\| ([A-Z]{2}-\d+) \|", text, re.M))


print("\ntopic catalogue")
catalogue = topics.build_catalogue(server.SUBJECTS)
sources = topics.load_sources()
allowed_hosts = {urlsplit(url).netloc for _, url in sources.values()}

# ---- 1. every syllabus row is covered -------------------------------------
missing = sorted(syllabus_ids() - set(catalogue))
check("every syllabus topic is in the catalogue", not missing, f"missing {missing}")
check("catalogue is not padded with unknown ids",
      not sorted(set(catalogue) - syllabus_ids()),
      f"extra {sorted(set(catalogue) - syllabus_ids())}")

# ---- 2. every topic has somewhere to go -----------------------------------
thin = [t for t, e in catalogue.items()
        if len(e["lectures"]) + len(e.get("search", [])) < 3]
check("every topic has three ways into the lecture", not thin, f"thin: {thin}")

# The whole point of topic-videos.md is that a session opens a lecture, not a
# channel. Report how many topics got real videos, and fail only if the file has
# gone missing entirely - a handful of thin topics is a content problem, not a build one.
named_videos = {t: [l for l in e["lectures"] if l.get("video")] for t, e in catalogue.items()}
with_video = [t for t, v in named_videos.items() if v]
print(f"        ({len(with_video)}/{len(catalogue)} topics have named videos, "
      f"{sum(1 for v in named_videos.values() if len(v) >= 3)} have three)")
check("named videos are wired up at all", len(with_video) > 0,
      "plan/topic-videos.md is missing or unparsable")

bad_watch = [(t, l["url"]) for t, ls in named_videos.items() for l in ls
             if not re.fullmatch(r"https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}", l["url"])]
check("every named video is a watch?v= link", not bad_watch, f"{bad_watch[:3]}")

playlisty = [(t, l["url"]) for t, ls in named_videos.items() for l in ls
             if "list=" in l["url"] or "/@" in l["url"] or "/channel/" in l["url"]]
check("no playlist or channel links among the named videos", not playlisty, f"{playlisty[:3]}")

dupe_vid = [t for t, ls in named_videos.items() if len({l["url"] for l in ls}) != len(ls)]
check("a topic does not list the same video twice", not dupe_vid, f"{dupe_vid}")

no_practice = [t for t, e in catalogue.items() if not e["practice"]]
check("every topic has at least one practice link", not no_practice, f"{no_practice}")

no_notes = [t for t, e in catalogue.items() if not e["notes"]]
check("every topic names a note file", not no_notes, f"{no_notes}")

# ---- 3. links are real links ----------------------------------------------
bad_url, bad_host, placeholder = [], [], []
for tid, entry in catalogue.items():
    for item in entry["lectures"] + entry.get("search", []) + entry["practice"]:
        url = item["url"]
        if not url.startswith("https://"):
            bad_url.append((tid, url))
        if "{q}" in url or "{}" in url:
            placeholder.append((tid, url))
        host = urlsplit(url).netloc
        if host not in allowed_hosts and host not in ("gateoverflow.in", "www.youtube.com"):
            bad_host.append((tid, host))
check("every link is https", not bad_url, f"{bad_url[:3]}")
check("no placeholder survived interpolation", not placeholder, f"{placeholder[:3]}")
check("links only point at sources named in topic-lectures.md", not bad_host,
      f"{sorted(set(h for _, h in bad_host))}")

dupes = [t for t, e in catalogue.items()
         if len({i["url"] for i in e["lectures"]}) != len(e["lectures"])]
check("the three alternatives are three different places", not dupes, f"{dupes}")

# ---- 4. short labels stay short -------------------------------------------
long_short = [(t, e["short"]) for t, e in catalogue.items() if len(e["short"]) > 48]
check("collapsed labels fit on one line", not long_short, f"{long_short[:3]}")

# ---- 5. id parsing --------------------------------------------------------
check("a range expands", topics.find_ids("PYQs, PD-1 … PD-4, negative marking")
      == ["PD-1", "PD-2", "PD-3", "PD-4"])
check("a slashed pair is found", topics.find_ids("unseen PYQs on PD-1/PD-2")
      == ["PD-1", "PD-2"])
check("a plain list is found", topics.find_ids("Topics: AL-7, AL-8") == ["AL-7", "AL-8"])
check("prose is not mistaken for an id", topics.find_ids("Revise CO and OS") == [])

# ---- 6. the plan actually uses it -----------------------------------------
plan = server.parse_plan()
tasks = [t for d in plan["days"] for t in d["tasks"]]
with_topics = [t for t in tasks if t["topics"]]
ratio = len(with_topics) / len(tasks)
check("most sessions resolve to a topic", ratio >= 0.75,
      f"{len(with_topics)}/{len(tasks)} = {ratio:.0%}")

unknown = sorted({tid for t in tasks for tid in t["topics"] if tid not in plan["topics"]})
check("every session topic is shipped in plan.json", not unknown, f"{unknown}")

reviews = [t for t in tasks if t["slot"] == "Sunday review" and t["topics"]]
check("Sunday reviews carry no topic", not reviews, f"{len(reviews)} do")

# A session that names its topics must get exactly those, not a keyword guess.
named = next(t for t in tasks if t["id"] == "w2-Sat-09001100")
check("an explicit id list wins over keyword matching",
      named["topics"] == ["PD-1", "PD-2", "PD-3", "PD-4"], f"{named['topics']}")

lecture = next(t for t in tasks if t["id"] == "w2-Tue-PM")
check("a lecture row matches the topic it is about",
      lecture["topics"][0] == "PD-3", f"{lecture['topics']}")

aptitude = next(t for t in tasks if t["id"] == "w2-Sat-11001200")
check("the aptitude hour matches a GA topic, not the week's subject",
      aptitude["topics"] == ["GA-1"], f"{aptitude['topics']}")

# ---- 7. prompts ship once --------------------------------------------------
check("Gemini prompts ship as templates, not per topic",
      all("gemini" not in e for e in plan["topics"].values()))
check("the prompt head states the goal, not a topic",
      "GATE 2028" in plan["geminiHead"] and "{" not in plan["geminiHead"])
check("there are five prompts", len(plan["geminiPrompts"]) == 5)
check("one of them is open-ended",
      any(p["label"] == "Ask anything" for p in plan["geminiPrompts"]))
check("the questions prompt still withholds the answers",
      any("Print no answers" in p["text"] for p in plan["geminiPrompts"]))

# Every prompt must dictate the shape of the reply. Without it the answer comes
# back as an essay, which cannot be pasted into a note file or marked against a key.
shapeless = [p["label"] for p in plan["geminiPrompts"] if "exactly" not in p["text"]]
check("every prompt states a required answer format", not shapeless, f"{shapeless}")

# gemini.google.com ignores ?q= and ?prompt=; AI Mode reads the URL. If this ever
# goes back to a bare chat URL the buttons silently stop prefilling again.
check("the Gemini link carries the prompt", "{q}" in plan.get("geminiUrl", ""),
      plan.get("geminiUrl", "(missing)"))
check("the link is AI Mode, not the empty chat app",
      "udm=50" in plan.get("geminiUrl", ""), plan.get("geminiUrl", "(missing)"))

# A prompt that overflows the URL gets trimmed in the browser, so keep the shipped
# text comfortably under budget for a realistic context block.
budget = plan["geminiUrlMax"]
context = len(plan["geminiHead"]) + 760      # a long real session context, measured
over = [(p["label"], context + len(p["text"]))
        for p in plan["geminiPrompts"] if context + len(p["text"]) > budget]
check(f"every prompt fits the {budget}-char URL budget", not over, f"{over}")

print(f"\n{len(failures)} check(s) failed" if failures else "\nall topic checks passed")
sys.exit(1 if failures else 0)
