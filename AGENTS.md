# Working on GD Project (for people and coding agents)

GD Project is the home site of the owner's open-source desktop tools made with Godot: Second Brain GD, Agent Manager GD,
and what they do together. Decided by the owner on 2026-11-08: the name « GD Project », MIT for every repository, a
site of its own (not PYF Studio, which is a separate site and project).

## Context lives in the Second Brain

The project's vision, decisions, problems, ideas, third parties and market are kept in the owner's Second Brain, in the
place « GD Project ». Read it over the second-brain MCP before working: start with « GD Project — main card », which
links the six detailed notes. When something significant changes (a decision, a solved problem, a new idea, a
dependency), propose an update there through the archivist (`propose_item`), following the directive « Directive de
capitalisation des connaissances projet via Second Brain MCP ». Never put source code, secrets, keys or tokens in it.

## Where things stand (2026-11-08)

- Plain HTML and CSS in `docs/` (no build step), ready for GitHub Pages (Settings → Pages → main, /docs). One page:
  hero (both apps, joined by a « signal » wire), why Godot, one « scene » per app, « Better together » (the session →
  Brain key → search → propose → wrap-up → next session flow), open source.
- On GitHub: `origin` is github.com/sonixz/gd-project (private for now), `main` pushed on 2026-11-08 and tracking
  `origin/main`. Push only on the owner's word. Sessions get the repository's deploy key through `GIT_SSH_COMMAND`
  (git commands only: check access with `git ls-remote origin`, never `ssh -T`).
- First owner review pending. A preview was published as a private Artifact (claude.ai/artifact/T2Vk5QZnaGtzkPipw1BaU2).

## Rules for the content

- Every claim must be true of the real apps today: check the apps' DEVLOG.md / README.md before writing a feature.
  Things that only exist as proposals stay off the site.
- Screenshots are the apps' own captures converted to WebP: Agent Manager's from `agent-manager-gd/docs/screens/`
  (converted with the Second Brain's `tools/web_images.gd`: `godot --headless --path ../second-brain-gd --script
  res://tools/web_images.gd -- in.png=out.webp@1440`), Second Brain's from `second-brain-gd/public/assets/showcase/`.
- The Second Brain keeps its own product site (product page, docs, how-to guides in `second-brain-gd/public`); GD
  Project links to it rather than replacing it.
- Godot is a trademark of the Godot Foundation: no Godot logo, the footer says GD Project is independent.
- Light and dark themes are both designed (tokens in `:root`); the page must work at phone width.
