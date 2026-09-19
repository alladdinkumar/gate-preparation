"""Keep the local checkout level with the repo the hosted planner writes to.

The hosted page commits every tick straight to GitHub. Without this the laptop
would drift behind within a day, and a Claude Code session reviewing the week
would read stale logs. So: pull once at startup, and push a debounced commit
after anything is written.

Failures are always non-fatal. A git problem must never stop the planner from
serving the plan - it prints loudly and carries on.

Set GATE_NO_SYNC=1 to turn the whole thing off.
"""

import os
import subprocess
import threading

PUSH_DELAY = 10.0  # seconds of quiet before committing a burst of ticks

_lock = threading.Lock()
_timer = None
_root = None
_enabled = False
_last_error = None


def _git(*args, timeout=60):
    return subprocess.run(
        ["git", *args], cwd=_root, capture_output=True, text=True, timeout=timeout,
    )


def _has_remote():
    return bool(_git("remote").stdout.strip())


def init(root):
    """Enable syncing if this is a git checkout with a remote. Returns a status line."""
    global _root, _enabled
    _root = root
    if os.environ.get("GATE_NO_SYNC") == "1":
        return "git sync off (GATE_NO_SYNC=1)"
    if not (root / ".git").exists():
        return "git sync off (not a git checkout)"
    try:
        if not _has_remote():
            return "git sync off (no remote configured)"
    except (OSError, subprocess.SubprocessError):
        return "git sync off (git not available)"
    _enabled = True
    return pull()


def pull():
    """Fast-forward onto whatever the phone has been writing. Never destructive."""
    if not _enabled:
        return "git sync off"
    try:
        result = _git("pull", "--rebase", "--autostash", timeout=120)
    except subprocess.SubprocessError as exc:
        return f"git pull failed ({exc}) - working offline"
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        # A conflict needs a human; say so plainly rather than guessing.
        return ("git pull failed - resolve it before relying on the hosted page:\n  "
                + "\n  ".join(detail[-3:]))
    if "up to date" in result.stdout.lower():
        return "git: already up to date"
    return "git: pulled changes from the hosted planner"


def _push_now():
    global _last_error
    with _lock:
        try:
            if not _git("status", "--porcelain").stdout.strip():
                return
            _git("add", "-A")
            message = "planner: progress and log updates from the local planner"
            commit = _git("commit", "-m", message)
            if commit.returncode != 0 and "nothing to commit" not in commit.stdout:
                _last_error = (commit.stderr or commit.stdout).strip()
                print(f"[git] commit failed: {_last_error}")
                return
            push = _git("push", timeout=120)
            if push.returncode != 0:
                # Almost always because the phone pushed first. Rebase and retry once.
                rebase = _git("pull", "--rebase", "--autostash", timeout=120)
                if rebase.returncode != 0:
                    _last_error = (rebase.stderr or rebase.stdout).strip()
                    print(f"[git] push rejected and rebase failed. Resolve by hand:\n{_last_error}")
                    return
                push = _git("push", timeout=120)
                if push.returncode != 0:
                    _last_error = (push.stderr or push.stdout).strip()
                    print(f"[git] push failed: {_last_error}")
                    return
            _last_error = None
            print("[git] pushed local changes")
        except (OSError, subprocess.SubprocessError) as exc:
            _last_error = str(exc)
            print(f"[git] sync error: {exc}")


def touch():
    """Called after a write. Debounces a burst of ticks into one commit."""
    global _timer
    if not _enabled:
        return
    if _timer is not None:
        _timer.cancel()
    # daemon=True so a pending push never keeps the server alive after Ctrl+C.
    _timer = threading.Timer(PUSH_DELAY, _push_now)
    _timer.daemon = True
    _timer.start()


def last_error():
    return _last_error


# Public name for the shutdown flush.
flush = _push_now
