// Picks the data layer for however this page is being served.
//
//   localhost           -> webapp/server.py, reading and writing the D: drive
//   anything else       -> GitHub Pages, reading and writing the repo via API
//
// index.html talks only to the object this returns and never knows which one
// it got.
(() => {
  const LOCAL_HOSTS = ["127.0.0.1", "localhost", "[::1]", ""];

  window.selectBackend = async () => {
    if (LOCAL_HOSTS.includes(location.hostname) && location.protocol !== "file:") {
      return window.createLocalBackend();
    }
    // Served statically. build_site.py writes config.json next to plan.json so
    // the repo coordinates are explicit rather than guessed from the URL.
    const res = await fetch(`data/config.json?t=${Date.now()}`, { cache: "no-store" });
    if (!res.ok) {
      throw new Error(
        "This page needs to be served by the planner. Run webapp\\start.bat locally, " +
        "or open the hosted version on GitHub Pages."
      );
    }
    const config = await res.json();
    return window.createGitHubBackend(config);
  };
})();
