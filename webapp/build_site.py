"""Build the static site that GitHub Pages serves.

The hosted planner has no server, so the plan has to be parsed ahead of time.
This imports server.py's own parser rather than reimplementing it, so the
hosted page and the local planner can never disagree about what the plan says.

Output (all under site/):

    index.html          the planner, unchanged
    lib/*.js            backend + template modules
    data/plan.json      parse_plan() plus the templates the browser needs
    data/config.json    which repository to read and write
    manifest.webmanifest, icon.svg, .nojekyll

Run locally with `python webapp/build_site.py`; CI runs the same command.
"""

import json
import os
import shutil
import sys
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent
ROOT = WEBAPP.parent
OUT = ROOT / "site"

sys.path.insert(0, str(WEBAPP))

import server  # noqa: E402  (needs WEBAPP on the path first)


def repo_config():
    """Repository coordinates, from CI or from the local git remote."""
    slug = os.environ.get("GITHUB_REPOSITORY")
    if not slug:
        import subprocess
        try:
            url = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=ROOT, capture_output=True, text=True, check=True,
            ).stdout.strip()
            slug = url.removesuffix(".git").split("github.com")[-1].lstrip(":/")
        except Exception:
            slug = ""
    if "/" not in slug:
        raise SystemExit(
            "Can't tell which repository to target. Set GITHUB_REPOSITORY, "
            "or add an origin remote pointing at GitHub."
        )
    owner, name = slug.split("/", 1)
    return {"repo": {"owner": owner, "name": name,
                     "branch": os.environ.get("GITHUB_REF_NAME", "main")}}


def templates():
    """Template text and lookup tables the browser needs to create files.

    Everything here is read from server.py's constants or the on-disk
    TEMPLATE.md files, so no skeleton is ever retyped in JavaScript.
    """
    read = lambda rel: (ROOT / rel).read_text(encoding="utf-8")  # noqa: E731
    return {
        "start": server.START.isoformat(),
        "note": server.NOTE_SKELETON,
        "dailyLog": read("daily-logs/TEMPLATE.md"),
        "reviewWeekly": read("reviews/weekly/TEMPLATE.md"),
        "reviewMonthly": read("reviews/monthly/TEMPLATE.md"),
        "phaseSlugs": {str(k): v for k, v in server.PHASE_SLUGS.items()},
        "phaseStartWeek": {str(k): v for k, v in server.PHASE_START_WEEK.items()},
        "subjectSlugs": server.SUBJECT_SLUGS,
        "weekSubjects": {str(k): v for k, v in server.WEEK_SUBJECTS.items()},
        "allowedDirs": list(server.ALLOWED_DIRS),
        "progressStart": server.PROGRESS_START,
        "progressEnd": server.PROGRESS_END,
    }


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "data").mkdir(parents=True)
    (OUT / "lib").mkdir()

    plan = server.parse_plan()
    plan["templates"] = templates()
    (OUT / "data" / "plan.json").write_text(
        json.dumps(plan, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (OUT / "data" / "config.json").write_text(
        json.dumps(repo_config(), ensure_ascii=False, indent=2), encoding="utf-8")

    shutil.copy2(WEBAPP / "index.html", OUT / "index.html")
    for js in sorted((WEBAPP / "lib").glob("*.js")):
        shutil.copy2(js, OUT / "lib" / js.name)
    for extra in ("manifest.webmanifest", "icon.svg"):
        source = WEBAPP / extra
        if source.exists():
            shutil.copy2(source, OUT / extra)

    # Stops Pages from running Jekyll over the output, which would drop any
    # file or folder whose name starts with an underscore.
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    weeks = sum(len(p["weeks"]) for p in plan["phases"])
    size = (OUT / "data" / "plan.json").stat().st_size
    print(f"site/ built: {len(plan['phases'])} phases, {weeks} weeks, "
          f"{len(plan['days'])} days, plan.json {size // 1024} KB")


if __name__ == "__main__":
    main()
