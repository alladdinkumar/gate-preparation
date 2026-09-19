# -*- coding: utf-8 -*-
"""YouTube harvesting helpers: playlist contents, search results, id verification.

No API key. Reads ytInitialData out of the served HTML, which is the same data the
page renders from. Every id that survives here is then checked against the oEmbed
endpoint, which 400s on anything that does not exist - so no id can be invented.
"""
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")


def get(url, timeout=45, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "en-US,en;q=0.9"})
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError:
            raise
        except Exception as e:      # connection reset: YouTube throttling, back off
            last = e
            time.sleep(2 + 3 * attempt)
    raise last


def initial_data(html):
    marker = "var ytInitialData = "
    if marker not in html:
        return None
    i = html.index(marker) + len(marker)
    depth = 0
    for j in range(i, len(html)):
        c = html[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return json.loads(html[i:j + 1])
    return None


def _walk(node, key, out):
    if isinstance(node, dict):
        if key in node:
            out.append(node[key])
        for v in node.values():
            _walk(v, key, out)
    elif isinstance(node, list):
        for v in node:
            _walk(v, key, out)


def _text(t):
    if not isinstance(t, dict):
        return ""
    if "runs" in t:
        return "".join(r.get("text", "") for r in t["runs"])
    return t.get("simpleText") or t.get("content") or ""


def playlist(list_id):
    """[{id, title}] for a playlist, in order."""
    data = initial_data(get(f"https://www.youtube.com/playlist?list={list_id}"))
    if not data:
        return []
    out, seen = [], set()

    lockups = []
    _walk(data, "lockupViewModel", lockups)
    for lk in lockups:
        vid = lk.get("contentId")
        md = lk.get("metadata", {}).get("lockupMetadataViewModel", {})
        title = _text(md.get("title", {}))
        if vid and title and vid not in seen:
            seen.add(vid)
            out.append({"id": vid, "title": title.strip()})

    # Older renderer, still served in some regions.
    olds = []
    _walk(data, "playlistVideoRenderer", olds)
    for v in olds:
        vid = v.get("videoId")
        title = _text(v.get("title", {}))
        if vid and title and vid not in seen:
            seen.add(vid)
            out.append({"id": vid, "title": title.strip()})
    return out


def search(query, limit=20):
    """[{id, title, channel, duration}] from a YouTube search, videos only."""
    q = urllib.parse.quote_plus(query)
    # sp=EgIQAQ%3D%3D restricts results to videos (no channels, playlists, shorts mixes).
    data = initial_data(get(f"https://www.youtube.com/results?search_query={q}&sp=EgIQAQ%3D%3D"))
    if not data:
        return []
    out, seen = [], set()

    vids = []
    _walk(data, "videoRenderer", vids)
    for v in vids:
        vid = v.get("videoId")
        if not vid or vid in seen:
            continue
        title = _text(v.get("title", {}))
        channel = _text(v.get("ownerText", {})) or _text(v.get("longBylineText", {}))
        length = _text(v.get("lengthText", {}))
        if title:
            seen.add(vid)
            out.append({"id": vid, "title": title.strip(),
                        "channel": channel.strip(), "duration": length.strip()})
        if len(out) >= limit:
            break

    if not out:
        lockups = []
        _walk(data, "lockupViewModel", lockups)
        for lk in lockups:
            vid = lk.get("contentId")
            md = lk.get("metadata", {}).get("lockupMetadataViewModel", {})
            title = _text(md.get("title", {}))
            if vid and title and vid not in seen:
                seen.add(vid)
                out.append({"id": vid, "title": title.strip(), "channel": "", "duration": ""})
            if len(out) >= limit:
                break
    return out


def verify(video_id, retries=2):
    """(ok, title, channel) straight from YouTube's oEmbed endpoint."""
    url = ("https://www.youtube.com/oembed?url="
           + urllib.parse.quote(f"https://www.youtube.com/watch?v={video_id}", safe="")
           + "&format=json")
    for attempt in range(retries + 1):
        try:
            d = json.loads(get(url, timeout=25))
            return True, d.get("title", ""), d.get("author_name", "")
        except urllib.error.HTTPError as e:
            if e.code in (400, 401, 403, 404):
                return False, "", ""       # does not exist, private, or embedding blocked
            time.sleep(1 + attempt)
        except Exception:
            time.sleep(1 + attempt)
    return False, "", ""
