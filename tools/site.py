#!/usr/bin/env python3
"""The GD Project site, locally: build, check, serve.

    python3 tools/site.py build            # assemble _site/ from docs/ and each app's public/
    python3 tools/site.py check            # build, then check every internal link and image
    python3 tools/site.py serve [--port 8800]
                                           # build, serve _site/, and rebuild when docs/, tools/ or an app's
                                           # public/ changes (refresh the browser to see it)

Standard library only. The apps' repositories are expected next to this one (../second-brain-gd, ...), or
pass --apps-root.
"""
import argparse
import functools
import http.server
import re
import shutil
import sys
import threading
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assemble  # noqa: E402

ROOT = assemble.ROOT


def build(out: Path, apps_root: Path) -> bool:
    """Assemble next to `out`, then swap, so a page being served is never half-built."""
    fresh = out.with_name(out.name + ".new")
    argv = sys.argv
    sys.argv = ["assemble.py", "--out", str(fresh), "--apps-root", str(apps_root)]
    try:
        if assemble.main() != 0:
            return False
    finally:
        sys.argv = argv
    old = out.with_name(out.name + ".old")
    if old.exists():
        shutil.rmtree(old)
    if out.exists():
        out.rename(old)
    fresh.rename(out)
    shutil.rmtree(old, ignore_errors=True)
    return True


def check(out: Path) -> int:
    """Every href/src that points inside the site must exist. Returns the number of broken links."""
    broken = checked = 0
    for page in sorted(out.rglob("*.html")):
        html = page.read_text(encoding="utf-8")
        for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
            if re.match(r"(https?:|mailto:|#|data:|javascript:)", ref) or "{" in ref or "&lt;" in ref:
                continue
            target = (page.parent / urllib.parse.unquote(urllib.parse.urlparse(ref).path)).resolve()
            if target.is_dir():
                target = target / "index.html"
            checked += 1
            if not target.exists():
                broken += 1
                print(f"BROKEN  {page.relative_to(out)} -> {ref}")
    print(f"{checked} internal links checked, {broken} broken")
    return broken


def sources(apps_root: Path):
    yield ROOT / "docs"
    yield ROOT / "tools"
    for app in assemble.APPS:
        yield apps_root / app["repo"] / "public"


def snapshot(apps_root: Path) -> dict:
    state = {}
    for folder in sources(apps_root):
        for f in folder.rglob("*"):
            if f.is_file():
                try:
                    state[f] = f.stat().st_mtime_ns
                except OSError:
                    pass
    return state


def watch(out: Path, apps_root: Path, every: float = 1.5) -> None:
    last = snapshot(apps_root)
    while True:
        time.sleep(every)
        now = snapshot(apps_root)
        if now != last:
            last = now
            print(time.strftime("%H:%M:%S"), "change seen, rebuilding")
            build(out, apps_root)


def serve(out: Path, apps_root: Path, port: int) -> None:
    threading.Thread(target=watch, args=(out, apps_root), daemon=True).start()

    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):  # quiet
            pass

        def end_headers(self):
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

    handler = functools.partial(Handler, directory=str(out))
    with http.server.ThreadingHTTPServer(("", port), handler) as httpd:
        print(f"GD Project site on http://localhost:{port}  (Ctrl+C to stop)")
        httpd.serve_forever()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["build", "check", "serve"])
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--apps-root", default=str(ROOT.parent))
    ap.add_argument("--port", type=int, default=8800)
    args = ap.parse_args()
    out, apps_root = Path(args.out).resolve(), Path(args.apps_root).resolve()

    if not build(out, apps_root):
        return 1
    if args.command == "check":
        return 1 if check(out) else 0
    if args.command == "serve":
        check(out)
        serve(out, apps_root, args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
