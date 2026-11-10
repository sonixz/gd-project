# Working on GD Project (for people and coding agents)

GD Project is an open lab of AI-native apps with rich interfaces, made with Godot (owner, 2026-11-09): apps are dropped
in, back-ends run, APIs get plugged into Godot, interfaces and integrations are pushed as far as they go, and anyone may
suggest or build an app. Second Brain GD and Agent Manager GD are its first two apps. This repository is the lab's
public showcase: its index, its blog, and the assembly of every app's site. Decided by the owner on 2026-11-08: the name
« GD Project », MIT for every repository, a site of its own (not PYF Studio, which is a separate site and project).

## Context lives in the Second Brain

The project's vision, decisions, problems, ideas, third parties and market are kept in the owner's Second Brain, in the
place « GD Project ». Read it over the second-brain MCP before working: start with « GD Project — main card », which
links the six detailed notes. When something significant changes (a decision, a solved problem, a new idea, a
dependency), propose an update there through the archivist (`propose_item`), following the directive « Directive de
capitalisation des connaissances projet via Second Brain MCP ». Never put source code, secrets, keys or tokens in it.

## Where things stand (2026-11-09)

- One site assembled from three repositories (see README): the lab's index and blog in `docs/`, each app's own
  `public/` under `/second-brain/` and `/agent-manager/`, with the GD Project bar added by `tools/assemble.py`.
  Local work: `python3 tools/site.py serve` (build, link check, http://localhost:8800, rebuild on change);
  `python3 tools/site.py check` before every commit that touches the site.
- Not online yet. Owner, 2026-11-09: this repository may be made public; the apps' repositories are being cleaned
  up first (Second Brain's checklist is in its `docs/audit-before-public.md`). The site is built and checked locally,
  and going online comes next. `.github/workflows/pages.yml` (GitHub Pages) is parked, manual runs only: Pages on a private
  repository needs a paid plan, and the workflow would need an `APPS_READ_TOKEN` secret to read the apps.
- On GitHub: `origin` is github.com/sonixz/gd-project (private for now). Push only on the owner's word. Sessions get
  the repository's deploy key through `GIT_SSH_COMMAND` (git commands only: check access with `git ls-remote origin`,
  never `ssh -T`).

## Rules for the content

- Tone and shape of the index (owner, 2026-11-09): humble, a portfolio of projects made with Godot. Simple, concise,
  visually beautiful. The apps' sites carry the detail; do not grow the index into a long page.
- The lab's vision (owner, 2026-11-10): apps that share one brain, the Second Brain at the centre. The index shows the
  whole lab: the constellation (the Brain at the centre, solid lines for what is connected today, dotted for what is
  planned), the apps in use (one big card each), « Connected over MCP », « Next in the lab », the stack, open source
  and the latest post.
- GitHub links stay even while the repositories are private (owner, 2026-11-09): they will work once published.

- Every claim must be true of the real apps today: check the apps' DEVLOG.md / README.md before writing a feature.
- Planned projects may appear (owner, 2026-11-10), always with their status written on them (« Prototype · not built
  yet », « In planning »), never described as if they existed. Their status changes on the site the day it changes.
- Screenshots are the apps' own captures converted to WebP: Agent Manager's from `agent-manager-gd/docs/screens/`
  (converted with the Second Brain's `tools/web_images.gd`: `godot --headless --path ../second-brain-gd --script
  res://tools/web_images.gd -- in.png=out.webp@1440`), Second Brain's from `second-brain-gd/public/assets/showcase/`.
- Each app owns its site (`public/` in its repository: product page, how-to guides, docs). GD Project never edits a
  copy: it assembles them. Changes to an app's site go to that app's session. An app may adopt the lab bar itself
  (`data-gd-lab-bar` on its root element), then the assembly leaves its pages alone.
- The blog tells the story across the apps; facts in a post follow the same rule as the site (true today).
- Godot is a trademark of the Godot Foundation: no Godot logo, the footer says GD Project is independent.
- Light and dark themes are both designed (tokens in `:root`); the page must work at phone width.
