/* Walk all 504 days in a real browser and check what each session renders.
 *
 * Paste this into the browser console on the planner - localhost or the hosted
 * copy - and wait a few seconds. It clicks through every day and inspects the DOM
 * that actually came out.
 *
 * Why this exists: videos_audit.py checks plan.json, which is the input to
 * rendering. Twice that passed while the page itself showed the wrong thing - a
 * subject with no playlist fell through to a channel page, and the fallback row
 * linked channel-scoped searches. Neither was visible in the data being audited.
 * If it renders, this is what sees it.
 */
(async () => {
  const WATCH = /^https:\/\/www\.youtube\.com\/watch\?v=[A-Za-z0-9_-]{11}$/;
  const CHANNEL = /youtube\.com\/(@|channel\/)/;

  const next = document.getElementById("nextBtn");
  const jump = document.getElementById("jumpInput");
  if (!next || !jump) return console.error("Not the planner page.");

  const total = Number(jump.max);
  const problems = [];
  const ids = new Set();
  let days = 0, sessions = 0, withTopics = 0, withVideo = 0, chips = 0, blocks = 0;

  for (let i = 0; i < total; i++) {
    const day = jump.value;
    const list = [...document.querySelectorAll("#sessions .session")];
    if (!list.length) problems.push(`day ${day}: no sessions rendered`);
    days++;

    for (const s of list) {
      sessions++;
      const topics = [...s.querySelectorAll(".topic")];
      blocks += topics.length;
      if (topics.length) withTopics++;

      const vids = [...s.querySelectorAll(".links.vids .chip")];
      // Every .vids chip is a lecture or a solved-question video; both must be
      // real watch links, which the loop below enforces.
      if (vids.length) withVideo++;
      for (const a of vids) {
        chips++;
        const href = a.getAttribute("href") || "";
        if (!WATCH.test(href)) problems.push(`day ${day}: bad video href "${href}"`);
        else ids.add(href.slice(-11));
        if (!a.textContent.trim()) problems.push(`day ${day}: empty video label`);
      }

      for (const a of s.querySelectorAll("a[href]")) {
        const h = a.getAttribute("href") || "";
        if (CHANNEL.test(h)) problems.push(`day ${day}: channel page ${h}`);
        if (!h || h === "undefined" || h === "null") problems.push(`day ${day}: broken href`);
      }
      for (const t of topics) {
        if (!t.querySelector(".links.vids .chip")) {
          const id = t.querySelector(".tid")?.textContent;
          problems.push(`day ${day}: topic ${id} renders no video`);
        }
      }
      if (topics.length && !vids.length) problems.push(`day ${day}: topics but no video chip`);
    }
    if (i < total - 1) next.click();
  }

  console.log({ days, sessions, sessionsWithTopics: withTopics, sessionsWithVideo: withVideo,
                topicBlocks: blocks, videoChips: chips, distinctVideos: ids.size,
                problems: problems.length });
  if (problems.length) console.warn(problems.slice(0, 40));
  else console.log("every day renders a watchable lecture for every topic it carries");
})();
