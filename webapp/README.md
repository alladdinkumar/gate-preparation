# Study Planner (local web page)

A day-by-day view of the plan with checkboxes, direct lecture / PYQ / material links, daily-progress saving, and a built-in Markdown editor for notes and trackers. Runs on your machine only; no install beyond Python.

## Start it

- **Windows:** double-click `webapp\start.bat`
- **Any OS:** `python webapp/server.py`

It opens http://127.0.0.1:8765 in your browser. Keep the terminal window open while you use it; close it (or press Ctrl+C) to stop.

Opening `index.html` directly does not work because the page needs the server to read the plan and save progress.

## What's on the page

- **Day view:** today's sessions (morning, evening, Saturday block, Sunday review), each with a checkbox. Every session shows its focus and required study record from the plan table.
- **Links on every session:**
  - red play icon: the relevant lecture video or course
  - green tick icon: the matching GATE Overflow PYQs
  - blue page icon: the requested material or tool
  - pencil icon: edit your Markdown files inside the planner. Notes and weekly/monthly reviews are created from a template if they do not exist yet.
- **Edit daily log:** creates `daily-logs/YYYY-MM-DD.md` from the template with phase, week, and subject frontmatter, then opens it in the built-in editor.
- **Save daily progress:** writes a checklist snapshot of planned sessions to the selected daily log. It also runs automatically when every session for the day is marked complete.
- **Day palette:** every day of the current phase as a numbered square: green completed, amber partly done, red missed, grey upcoming, and a violet ring for today. Tabs 1-7 switch phases.
- **Catch-up notice:** unfinished earlier sessions, with a jump to the first one.
- **Week strip and subject links** under the sessions.

Keyboard: left/right arrow moves days; T jumps to today. Each day has its own address (`#day-42`) that you can bookmark.

## Where things are stored

| What | Where |
|---|---|
| The plan (read on every page load) | `plan/phase-*.md` |
| Checkbox progress | `webapp/progress.json` (task id to completion time) |
| Daily checklist snapshots | `daily-logs/YYYY-MM-DD.md` |

Task ids look like `w12-Wed-PM` (week, day, slot), so progress survives wording edits to the plan. If a phase table's day or slot changes, that one checkbox resets.

The planner is a convenience layer: trackers and reviews remain the source of truth for accuracy, errors, and mock scores.

## Links

Link targets live in the `SUBJECTS` and `NAMED_LINKS` tables at the top of `server.py`, mirroring `plan/resources.md`. If a playlist moves, update both.

## Safety

The server listens on 127.0.0.1 only, rejects write requests without its own header, and only reads, creates, or saves `.md` files inside `notes/`, `trackers/`, `reviews/`, `daily-logs/`, `plan/`, and `docs/`.
