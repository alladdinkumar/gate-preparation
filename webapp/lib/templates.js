// Client-side twins of the file-creation logic in server.py.
//
// The GitHub backend writes straight to the repo, so it has to build the same
// Markdown the local server builds: daily logs from the template, note
// skeletons, and the planner checklist block. Only the *interpolation* lives
// here. Every template string and lookup table comes from plan.json, which
// build_site.py emits from server.py's own constants, so nothing is retyped in
// two languages and left to drift.
(() => {
  const DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  const WEEKDAY_LONG = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  const pad = (n) => String(n).padStart(2, "0");

  // Parse an ISO date as a *local* midnight so day arithmetic never shifts a
  // timezone. new Date("2026-09-14") would be UTC and can land on the 13th.
  function parseIso(iso) {
    const [y, m, d] = iso.split("-").map(Number);
    return new Date(y, m - 1, d);
  }

  function isoOf(date) {
    return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
  }

  function daysBetween(fromIso, toIso) {
    return Math.round((parseIso(toIso) - parseIso(fromIso)) / 86400000);
  }

  // Python's Monday=0 ordering, not JavaScript's Sunday=0.
  function weekdayIndex(iso) {
    return (parseIso(iso).getDay() + 6) % 7;
  }

  // server.py: week = (date - START).days // 7 + 1
  function weekOf(templates, dateIso) {
    return Math.floor(daysBetween(templates.start, dateIso) / 7) + 1;
  }

  // server.py: max(p for p, w in PHASE_START_WEEK.items() if week >= w)
  function phaseOf(templates, week) {
    if (week < 1) return 1;
    let phase = 1;
    for (const [p, w] of Object.entries(templates.phaseStartWeek)) {
      if (week >= w && Number(p) > phase) phase = Number(p);
    }
    return phase;
  }

  // server.py daily_log(): fill the frontmatter of daily-logs/TEMPLATE.md.
  function dailyLog(templates, dateIso) {
    const week = weekOf(templates, dateIso);
    const phase = phaseOf(templates, week);
    const subject = (templates.weekSubjects[week] || ["mixed"])[0];
    const dayIdx = weekdayIndex(dateIso);
    const weekday = WEEKDAY_LONG[dayIdx];
    const hours = dayIdx === 6 ? "0" : dayIdx === 5 ? "4.0" : "3.0";

    const fields = {
      date: dateIso,
      day_of_week: weekday,
      phase: templates.phaseSlugs[phase],
      phase_week: String(week - templates.phaseStartWeek[phase] + 1),
      overall_week: String(week),
      target_hours: hours,
      subject: templates.subjectSlugs[subject] || subject,
      focus_topic: "",
    };

    let text = templates.dailyLog;
    for (const [key, value] of Object.entries(fields)) {
      // count=1 and multiline, matching the Python re.sub calls.
      text = text.replace(new RegExp(`^${key}: .*$`, "m"), `${key}: ${value}`);
    }
    return text;
  }

  // server.py create_if_missing(): notes get a skeleton, reviews get their
  // template, anything else is not created from thin air.
  function skeletonFor(templates, path) {
    if (path.startsWith("notes/")) {
      const stem = path.slice(path.lastIndexOf("/") + 1).replace(/\.md$/, "");
      // Python's stem.split("-", 2)[-1]: at most three parts, keep the last.
      const parts = stem.split("-");
      const tail = parts.length > 2 ? parts.slice(2).join("-") : parts[parts.length - 1];
      const words = tail.replace(/-/g, " ");
      const title = words.charAt(0).toUpperCase() + words.slice(1).toLowerCase();
      return templates.note.replace("{title}", title);
    }
    if (path.startsWith("reviews/weekly/")) return templates.reviewWeekly;
    if (path.startsWith("reviews/monthly/")) return templates.reviewMonthly;
    return null;
  }

  // server.py save_daily_progress(): the checklist snapshot written into the
  // day's log between the two HTML-comment markers.
  function progressBlock(templates, day, done) {
    const tasks = day.tasks;
    const completed = tasks.filter((t) => done[t.id]).length;
    const now = new Date();
    const stamp = `${isoOf(now)} ${pad(now.getHours())}:${pad(now.getMinutes())}`;

    const lines = [
      templates.progressStart,
      "## Planner progress",
      `Saved from the study planner: ${stamp}. **${completed}/${tasks.length} planned sessions completed.**`,
      "",
    ];
    for (const task of tasks) {
      const mark = done[task.id] ? "x" : " ";
      const focus = task.focus.replace(/`([^`]+)`/g, "$1");
      lines.push(`- [${mark}] **${task.slot} (${task.time})** — ${focus}`);
      if (task.outputText) lines.push(`  - Required record: ${task.outputText}`);
    }
    lines.push("", templates.progressEnd);
    return { block: lines.join("\n"), completed, total: tasks.length };
  }

  function escapeRe(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  // Replace an existing snapshot in place, or append one to the end.
  function applyProgressBlock(text, templates, block) {
    const between = new RegExp(
      `${escapeRe(templates.progressStart)}[\\s\\S]*?${escapeRe(templates.progressEnd)}`
    );
    if (between.test(text)) return text.replace(between, block);
    return `${text.replace(/\s+$/, "")}\n\n${block}\n`;
  }

  // server.py safe_path(): the same allow-list the local server enforces, so a
  // bug in the UI cannot write outside the prep folders or to a non-Markdown
  // file.
  function safePath(templates, rel) {
    const path = String(rel || "").replace(/\\/g, "/").replace(/^\/+/, "");
    if (!path.endsWith(".md")) return null;
    if (path.includes("..")) return null;
    const top = path.split("/")[0];
    if (!templates.allowedDirs.includes(top)) return null;
    return path;
  }

  window.GateTemplates = {
    DAY_NAMES, WEEKDAY_LONG, parseIso, isoOf, daysBetween, weekdayIndex,
    weekOf, phaseOf, dailyLog, skeletonFor, progressBlock, applyProgressBlock, safePath,
  };
})();
