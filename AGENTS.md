# Working on GD Project (for people and coding agents)

GD Project is an open lab of AI-native apps with rich interfaces, made with Godot (owner, 2026-11-09): apps are dropped
in, back-ends run, APIs get plugged into Godot, interfaces and integrations are pushed as far as they go, and anyone may
suggest or build an app. Second Brain GD and Agent Manager GD are its first two apps. This repository is the lab's
public showcase: its index, its blog, and the assembly of every app's site. Decided by the owner on 2026-11-08: the name
« GD Project », MIT for every repository, a site of its own (not PYF Studio, which is a separate site and project).

Read [`AI-NOTICE.md`](AI-NOTICE.md) first: this is a lab, run on one person's computer. Never expose an engine, an
MCP server or their ports beyond the local machine unless the owner asks for it explicitly (owner, 2026-11-10).

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
- Online since 2026-11-11: https://sonixz.github.io/gd-project/ (the lab) with the apps under `/second-brain/` and
  `/agent-manager/`. The three repositories are public. Pages' source is « GitHub Actions »: `.github/workflows/pages.yml`
  assembles and publishes on every push to `main` (and by hand). Never switch the source back to « Deploy from a branch »:
  it would republish the branch alone and erase the apps' pages (it happened once, 2026-11-11).
- An app's site does not go online when the app pushes: it goes online the next time this workflow runs. A push to
  `main` here does it; so does « Run workflow » on GitHub. The workflow also listens to `repository_dispatch`
  (`app-site-updated`), but no app sends it yet (it needs a token the owner creates). So after an app's session
  pushes a new `public/`, the owner asks this repository's session to publish (it happened on 2026-11-13).
- On GitHub: `origin` is github.com/sonixz/gd-project (public). Push only on the owner's word. Sessions get
  the repository's deploy key through `GIT_SSH_COMMAND` (git commands only: check access with `git ls-remote origin`,
  never `ssh -T`).

## Rules for the content

- Tone and shape of the index (owner, 2026-11-09): humble, a portfolio of projects made with Godot. Simple, concise,
  visually beautiful. The apps' sites carry the detail; do not grow the index into a long page.
- The lab's vision (owner, 2026-11-10): each app stands alone; together they share one brain. The index shows it with
  « The lab »: app windows side by side as equals (Second Brain is one of them, not the centre) and a switch « Alone ·
  Together ». Alone: what each app does on its own, with its own data. Together: cables to the Second Brain (solid for
  what is connected today, dotted for what is planned) and what each app gains. Prototypes are dashed « blueprint »
  windows with a sketch. Then « Together, up close » (the same windows and cables in detail: a key per session,
  reads, proposals waiting for your approval, the timeline; its three steps play in turn), the stack, open source and
  the latest post.
- GitHub links stay (owner, 2026-11-09); the repositories are public now, so they work.

- Every claim must be true of the real apps today: check the apps' DEVLOG.md / README.md before writing a feature.
- Planned projects may appear (owner, 2026-11-10), always with their status written on them (« Prototype · not built
  yet », « In planning »), never described as if they existed. Their status changes on the site the day it changes.
- Screenshots are the apps' own captures, already WebP, copied as they are: Agent Manager's from
  `agent-manager-gd/public/assets/showcase/` (1920×1200; its old `docs/screens/` folder is gone since 2026-11-09),
  Second Brain's from `second-brain-gd/public/assets/showcase/`. When an app's look changes, copy them again: the
  lab's pages must show the app as it is today (the home page's captures were renewed on 2026-11-13).
- Each app owns its site (`public/` in its repository: product page, how-to guides, docs). GD Project never edits a
  copy: it assembles them. Changes to an app's site go to that app's session. An app may adopt the lab bar itself
  (`data-gd-lab-bar` on its root element), then the assembly leaves its pages alone.
- The blog tells the story across the apps; facts in a post follow the same rule as the site (true today).
- Godot is a trademark of the Godot Foundation: no Godot logo, the footer says GD Project is independent.
- Light and dark themes are both designed (tokens in `:root`); the page must work at phone width.
