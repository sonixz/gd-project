#!/usr/bin/env python3
"""Assemble the GD Project site: the lab's own pages plus each app's site under its own path.

    python3 tools/assemble.py [--out _site] [--apps-root ..]

- docs/                      -> <out>/            (the lab: index, blog)
- <apps-root>/<repo>/public  -> <out>/<path>/     (each app keeps its site in its own repository)
- every app page gets the thin GD Project lab bar right after <body> (and after the skip link), unless the page
  already carries one (data-gd-lab-bar), so an app can adopt the bar itself later without a double.

Standard library only: it runs the same on a laptop and in the GitHub Pages workflow.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The lab's apps. `path` is where the app's site lives on the GD Project site.
APPS = [
    {"repo": "second-brain-gd", "path": "second-brain", "name": "Second Brain GD"},
    {"repo": "agent-manager-gd", "path": "agent-manager", "name": "Agent Manager GD"},
]

BAR_TEMPLATE = (ROOT / "tools" / "lab-bar.html").read_text(encoding="utf-8")


def lab_bar(current: dict, root: str) -> str:
    """The bar for one page; `root` is the relative way back to the site's root from that page (e.g. "../")."""
    links = []
    for app in APPS:
        here = ' aria-current="page"' if app is current else ""
        links.append(f'<a href="{root}{app["path"]}/"{here}>{app["name"]}</a>')
    return BAR_TEMPLATE.replace("{{APPS}}", "".join(links)).replace("{{ROOT}}", root)


def inject(html: str, bar: str) -> str:
    if "data-gd-lab-bar" in html:
        return html
    skip = re.search(r'<a class="skip"[^>]*>.*?</a>', html, re.S)
    if skip:
        return html[: skip.end()] + "\n" + bar + html[skip.end():]
    body = re.search(r"<body[^>]*>", html)
    if not body:
        return html
    return html[: body.end()] + "\n" + bar + html[body.end():]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--apps-root", default=str(ROOT.parent), help="folder holding the apps' repositories")
    args = ap.parse_args()
    out = Path(args.out).resolve()
    apps_root = Path(args.apps_root).resolve()

    if out in (ROOT, ROOT / "docs", ROOT / "tools", apps_root):
        print(f"refusing to write into {out}", file=sys.stderr)
        return 2
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / "docs", out)

    for app in APPS:
        src = apps_root / app["repo"] / "public"
        if not (src / "index.html").is_file():
            print(f"missing: {src}/index.html", file=sys.stderr)
            return 1
        dest = out / app["path"]
        shutil.copytree(src, dest)
        pages = 0
        for page in dest.rglob("*.html"):
            root = "../" * len(page.relative_to(out).parts[:-1])
            page.write_text(inject(page.read_text(encoding="utf-8"), lab_bar(app, root)), encoding="utf-8")
            pages += 1
        print(f"{app['repo']}/public -> /{app['path']}/ ({pages} pages)")

    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"site assembled in {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
