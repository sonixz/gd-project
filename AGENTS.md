# Working on GD Project (for people and coding agents)

GD Project is the home site of the owner's open-source desktop tools made with Godot: Second Brain GD, Agent Manager GD,
and what they do together. Decided by the owner on 2026-11-08: the name « GD Project », MIT for every repository, a
site of its own (not PYF Studio, which is a separate site and project).

## Where things stand (2026-11-08)

- Plain HTML and CSS in `docs/` (no build step), ready for GitHub Pages (Settings → Pages → main, /docs). One page:
  hero (both apps, joined by a « signal » wire), why Godot, one « scene » per app, « Better together » (the session →
  Brain key → search → propose → wrap-up → next session flow), open source.
- Local git only, nothing uncommitted. The owner created github.com/sonixz/gd-project (empty); no remote is set here
  yet and nothing was pushed: push only on his word. The repository can also be connected in Agent Manager
  (⎇ Repos → « I already have it on this computer » → this folder → « Add it as origin »).
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
