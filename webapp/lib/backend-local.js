// Backend used when the page is served by webapp/server.py on localhost.
// Every method is the original fetch call, moved here unchanged so the local
// planner keeps behaving exactly as it did before the split.
(() => {
  async function api(path, body) {
    const opts = body === undefined
      ? { cache: "no-store" }
      : {
          method: "POST",
          headers: { "Content-Type": "application/json", "X-Gate-Planner": "1" },
          body: JSON.stringify(body),
        };
    const res = await fetch(path, opts);
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.error || `Request failed (${res.status})`);
    return data;
  }

  window.createLocalBackend = () => ({
    kind: "local",
    // The local server always has write access to the filesystem.
    canWrite: () => true,
    needsSetup: () => false,

    getPlan: () => api("/api/plan"),
    getProgress: () => api("/api/progress"),
    setTask: (id, done) => api("/api/progress", { id, done }),
    readFile: (path) => api(`/api/file?path=${encodeURIComponent(path)}`),
    writeFile: (path, content) => api("/api/file", { path, content }),
    createDailyLog: (date) => api("/api/daily-log", { date }),
    // ctx (day + done map) is only needed by the GitHub backend, which has no
    // server to rebuild the checklist for it.
    saveDailyProgress: (date) => api("/api/daily-progress", { date }),

    offlineCount: () => 0,
    flush: async () => {},
    describe: () => "Local planner server",
  });
})();
