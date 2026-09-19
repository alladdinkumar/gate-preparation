"""Emit what server.py produces, for the JavaScript twins to be checked against.

The hosted planner rebuilds daily logs, note skeletons and the checklist block
in the browser because it has no server. That is the one place where the same
rule is written twice, so it gets a test: this dumps Python's output and
parity.mjs asserts JavaScript matches it byte for byte.

    python webapp/tests/make_fixtures.py   # writes webapp/tests/fixtures.json
"""

import json
import sys
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WEBAPP))

import server  # noqa: E402

# Dates that exercise every branch: first day, a Saturday, a Sunday, each phase
# boundary, a multi-subject revision week, and the last day of the plan.
DATES = [
    "2026-09-14",  # week 1 Monday, plan start
    "2026-09-19",  # Saturday -> 4.0 target hours
    "2026-09-20",  # Sunday -> 0 target hours
    "2026-11-23",  # week 11, phase 2 begins
    "2027-02-15",  # week 23, phase 3 begins
    "2027-05-24",  # week 37, phase 4 begins
    "2027-08-23",  # week 50, revision: WEEK_SUBJECTS has two entries
    "2027-11-15",  # week 61, test series
    "2028-01-24",  # week 71, final sprint
    "2028-01-30",  # last day of the structured plan
]

NOTE_PATHS = [
    "notes/programming-ds/c-01-operators-control-flow.md",
    "notes/os/deadlock.md",
    "notes/formula-sheets/coa.md",
    "reviews/weekly/2026-09-14-to-2026-09-20.md",
    "reviews/monthly/2026-09.md",
    "trackers/error-log.md",  # not creatable from a template -> null
]


def main():
    plan = server.parse_plan()
    by_date = {d["date"]: d for d in plan["days"]}

    blocks = []
    for date in DATES:
        day = by_date.get(date)
        if day is None:
            continue
        # Tick every other task so both marks appear in the checklist.
        done = {t["id"]: "2026-01-01T00:00:00" for i, t in enumerate(day["tasks"]) if i % 2 == 0}
        block, completed = server.progress_block(day, done)
        base = server.daily_log_text(date)
        blocks.append({
            "date": date,
            "done": done,
            "block": block,
            "completed": completed,
            "total": len(day["tasks"]),
            "appended": server.apply_progress_block(base, block),
            "replaced": server.apply_progress_block(
                server.apply_progress_block(base, block), block),
        })

    fixtures = {
        "dailyLogs": {d: server.daily_log_text(d) for d in DATES},
        "progress": blocks,
        "skeletons": {p: skeleton_for(p) for p in NOTE_PATHS},
        "safePaths": {p: bool(server.safe_path(p)) for p in [
            "notes/os/deadlock.md",
            "trackers/error-log.md",
            "webapp/server.py",
            "../secrets.md",
            "notes/../../escape.md",
            "plan/PLAN.md",
            "notes/os/deadlock.txt",
        ]},
    }
    out = Path(__file__).parent / "fixtures.json"
    out.write_text(json.dumps(fixtures, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out.relative_to(WEBAPP.parent)}: "
          f"{len(fixtures['dailyLogs'])} logs, {len(blocks)} checklists, "
          f"{len(fixtures['skeletons'])} skeletons")


def skeleton_for(rel):
    """What create_if_missing() would write, without writing it."""
    if rel.startswith("notes/"):
        stem = Path(rel).stem
        title = stem.split("-", 2)[-1].replace("-", " ").capitalize()
        return server.NOTE_SKELETON.format(title=title)
    if rel.startswith("reviews/weekly/"):
        return (server.ROOT / "reviews/weekly/TEMPLATE.md").read_text(encoding="utf-8")
    if rel.startswith("reviews/monthly/"):
        return (server.ROOT / "reviews/monthly/TEMPLATE.md").read_text(encoding="utf-8")
    return None


if __name__ == "__main__":
    main()
