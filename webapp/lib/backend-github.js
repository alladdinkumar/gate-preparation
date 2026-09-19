// Backend used when the page is served from GitHub Pages.
//
// There is no server here: the repository *is* the database. Reads and writes
// go through the GitHub Contents API with a fine-grained token the user pastes
// once and that lives only in this browser's localStorage.
(() => {
  const API = "https://api.github.com";
  const TOKEN_KEY = "gate.planner.token";
  const OPS_KEY = "gate.planner.pendingOps";
  const DEBOUNCE_MS = 4000;

  // ---- base64 over UTF-8 --------------------------------------------------
  // btoa() alone throws on anything outside Latin-1, and these files are full
  // of em dashes and arrows, so every byte goes through TextEncoder first.
  function b64encode(str) {
    const bytes = new TextEncoder().encode(str);
    let binary = "";
    const CHUNK = 0x8000;
    for (let i = 0; i < bytes.length; i += CHUNK) {
      binary += String.fromCharCode.apply(null, bytes.subarray(i, i + CHUNK));
    }
    return btoa(binary);
  }

  function b64decode(b64) {
    const binary = atob(String(b64).replace(/\s/g, ""));
    const bytes = Uint8Array.from(binary, (c) => c.charCodeAt(0));
    return new TextDecoder().decode(bytes);
  }

  function loadOps() {
    try {
      const raw = localStorage.getItem(OPS_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch {
      return [];
    }
  }

  function storeOps(ops) {
    try {
      localStorage.setItem(OPS_KEY, JSON.stringify(ops));
    } catch {
      /* private mode, quota — the in-memory queue still works this session */
    }
  }

  window.createGitHubBackend = (config) => {
    const T = window.GateTemplates;
    const repo = config.repo;
    const base = `${API}/repos/${repo.owner}/${repo.name}/contents`;
    const ref = repo.branch || "main";

    let token = "";
    try {
      token = localStorage.getItem(TOKEN_KEY) || "";
    } catch {
      token = "";
    }

    let templates = null;              // filled by getPlan()
    let progress = { version: 1, done: {} };
    let progressSha = null;
    const shas = new Map();            // path -> last known blob sha
    let pendingOps = loadOps();
    let flushTimer = null;
    let flushing = false;
    const listeners = [];

    function emit(text, kind) {
      for (const cb of listeners) cb(text, kind);
    }

    function headers(extra) {
      const h = Object.assign({ Accept: "application/vnd.github+json" }, extra || {});
      if (token) h.Authorization = `Bearer ${token}`;
      return h;
    }

    async function ghFetch(path, opts) {
      const res = await fetch(path, opts);
      if (res.status === 401) throw new Error("Token rejected. Re-paste it in Settings.");
      if (res.status === 403) {
        const body = await res.json().catch(() => ({}));
        const msg = body.message || "";
        if (/rate limit/i.test(msg)) {
          throw new Error(token ? "GitHub rate limit hit. Wait a few minutes." : "Rate limited. Add your token in Settings.");
        }
        throw new Error(msg || "GitHub refused the request (403).");
      }
      return res;
    }

    // Returns { content, sha } or null when the file does not exist yet.
    async function getContents(path) {
      const url = `${base}/${encodeURI(path)}?ref=${encodeURIComponent(ref)}&t=${Date.now()}`;
      const res = await ghFetch(url, { headers: headers(), cache: "no-store" });
      if (res.status === 404) return null;
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.message || `Couldn't read ${path} (${res.status})`);
      }
      const data = await res.json();
      shas.set(path, data.sha);
      return { content: b64decode(data.content || ""), sha: data.sha };
    }

    async function putContents(path, content, message, sha) {
      if (!token) throw new Error("Add your GitHub token in Settings before saving.");
      const body = { message, content: b64encode(content), branch: ref };
      if (sha) body.sha = sha;
      const res = await ghFetch(`${base}/${encodeURI(path)}`, {
        method: "PUT",
        headers: headers({ "Content-Type": "application/json" }),
        body: JSON.stringify(body),
      });
      if (res.status === 409 || res.status === 422) return { conflict: true };
      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.message || `Couldn't save ${path} (${res.status})`);
      }
      const data = await res.json();
      shas.set(path, data.content.sha);
      return { sha: data.content.sha };
    }

    // ---- progress: replay ops, never merge states -------------------------
    // done[] is a map where *unticking removes a key*, so unioning two states
    // would resurrect anything unticked elsewhere. Replaying the ordered op
    // log onto whatever the repo currently holds keeps the last action winning.
    function applyOps(done, ops) {
      for (const op of ops) {
        if (op.done) done[op.id] = op.at;
        else delete done[op.id];
      }
      return done;
    }

    function localView() {
      return applyOps(Object.assign({}, progress.done), pendingOps);
    }

    function commitMessage(ops) {
      const marked = ops.filter((o) => o.done).length;
      const cleared = ops.length - marked;
      const parts = [];
      if (marked) parts.push(`+${marked}`);
      if (cleared) parts.push(`-${cleared}`);
      const ids = [...new Set(ops.map((o) => o.id))];
      const tail = ids.length <= 3 ? ids.join(", ") : `${ids.slice(0, 3).join(", ")} +${ids.length - 3} more`;
      return `progress: ${parts.join(" ")} (${tail})`;
    }

    async function flush() {
      clearTimeout(flushTimer);
      flushTimer = null;
      if (flushing || pendingOps.length === 0) return;
      if (!token) {
        emit("Not saved — add your token", "error");
        return;
      }
      if (!navigator.onLine) {
        emit(`Offline — ${pendingOps.length} queued`, "warn");
        return;
      }
      flushing = true;
      emit("Syncing…", "busy");
      try {
        for (let attempt = 0; attempt < 2; attempt++) {
          const taking = pendingOps.slice();      // snapshot; more may arrive mid-flight
          const remote = await getContents("webapp/progress.json");
          const state = remote ? JSON.parse(remote.content) : { version: 1, done: {} };
          state.done = applyOps(state.done || {}, taking);
          const text = `${JSON.stringify(state, null, 2)}\n`;
          const result = await putContents(
            "webapp/progress.json", text, commitMessage(taking), remote ? remote.sha : progressSha
          );
          if (result.conflict) continue;          // someone else wrote; re-read and replay
          progress = state;
          progressSha = result.sha;
          pendingOps = pendingOps.slice(taking.length);
          storeOps(pendingOps);
          emit(pendingOps.length ? `${pendingOps.length} queued` : "Synced", "ok");
          flushing = false;
          if (pendingOps.length) schedule();
          return;
        }
        emit("Sync conflict — retrying", "warn");
        flushing = false;
        schedule();
      } catch (err) {
        flushing = false;
        emit(`Not synced: ${err.message}`, "error");
      }
    }

    function schedule() {
      clearTimeout(flushTimer);
      flushTimer = setTimeout(flush, DEBOUNCE_MS);
    }

    window.addEventListener("online", () => { if (pendingOps.length) flush(); });
    window.addEventListener("beforeunload", (e) => {
      if (pendingOps.length) {
        e.preventDefault();
        e.returnValue = "";
      }
    });

    // ---- file helpers -----------------------------------------------------
    function guard(path) {
      const safe = T.safePath(templates, path);
      if (!safe) throw new Error("That file isn't inside the prep folders.");
      return safe;
    }

    async function writeFile(path, content) {
      const safe = guard(path);
      let sha = shas.get(safe);
      if (sha === undefined) {
        const existing = await getContents(safe);
        sha = existing ? existing.sha : null;
      }
      let result = await putContents(safe, content, `planner: update ${safe}`, sha);
      if (result.conflict) {
        const fresh = await getContents(safe);
        result = await putContents(safe, content, `planner: update ${safe}`, fresh ? fresh.sha : null);
        if (result.conflict) throw new Error(`${safe} changed elsewhere. Reload and try again.`);
      }
      return { ok: true, path: safe, created: !sha };
    }

    async function readFile(path) {
      const safe = guard(path);
      const existing = await getContents(safe);
      if (existing) return { ok: true, path: safe, content: existing.content, created: false };
      // Not in the repo yet. Hand back the template unsaved rather than
      // committing an empty skeleton — the first Save creates the file.
      const skeleton = T.skeletonFor(templates, safe);
      if (skeleton === null) throw new Error(`${safe.split("/").pop()} doesn't exist yet.`);
      return { ok: true, path: safe, content: skeleton, created: true };
    }

    async function createDailyLog(date) {
      const path = `daily-logs/${date}.md`;
      const existing = await getContents(path);
      if (existing) return { ok: true, path, content: existing.content, created: false };
      return { ok: true, path, content: T.dailyLog(templates, date), created: true };
    }

    async function saveDailyProgress(date, ctx) {
      const path = `daily-logs/${date}.md`;
      const existing = await getContents(path);
      const current = existing ? existing.content : T.dailyLog(templates, date);
      const { block, completed, total } = T.progressBlock(templates, ctx.day, ctx.done);
      const updated = T.applyProgressBlock(current, templates, block);
      await writeFile(path, updated);
      return { ok: true, path, content: updated, completed, total, created: !existing };
    }

    // ---- public interface -------------------------------------------------
    return {
      kind: "github",
      repo,
      canWrite: () => Boolean(token),
      needsSetup: () => !token,
      onStatus: (cb) => listeners.push(cb),

      async setToken(value) {
        const candidate = String(value || "").trim();
        if (!candidate) throw new Error("Paste a token first.");
        const res = await fetch(`${base}/webapp/progress.json?ref=${encodeURIComponent(ref)}`, {
          headers: { Accept: "application/vnd.github+json", Authorization: `Bearer ${candidate}` },
        });
        if (!res.ok) {
          throw new Error(
            res.status === 401 ? "GitHub rejected that token."
              : res.status === 404 ? "That token can't see this repository. Check its repository access."
                : `GitHub returned ${res.status}.`
          );
        }
        token = candidate;
        try { localStorage.setItem(TOKEN_KEY, token); } catch { /* private mode */ }
        if (pendingOps.length) flush();
        return true;
      },

      clearToken() {
        token = "";
        try { localStorage.removeItem(TOKEN_KEY); } catch { /* ignore */ }
      },

      async getPlan() {
        const res = await fetch(`data/plan.json?t=${Date.now()}`, { cache: "no-store" });
        if (!res.ok) throw new Error(`Couldn't load the plan (${res.status}). The site build may still be running.`);
        const plan = await res.json();
        templates = plan.templates;
        return plan;
      },

      async getProgress() {
        const remote = await getContents("webapp/progress.json");
        progress = remote ? JSON.parse(remote.content) : { version: 1, done: {} };
        progressSha = remote ? remote.sha : null;
        if (pendingOps.length) schedule();
        return { version: progress.version, done: localView() };
      },

      async setTask(id, done) {
        pendingOps.push({ id, done: Boolean(done), at: new Date().toISOString() });
        storeOps(pendingOps);
        emit(`${pendingOps.length} queued`, "busy");
        schedule();
        // Optimistic: the UI reflects the tick now, the commit lands shortly.
        return { ok: true, done: localView() };
      },

      readFile,
      writeFile,
      createDailyLog,
      saveDailyProgress,

      offlineCount: () => pendingOps.length,
      flush,
      describe: () => `${repo.owner}/${repo.name}`,
    };
  };
})();
