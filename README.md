# GD Project

An open lab of AI-native apps with rich interfaces, made with the Godot engine. We drop apps in, run their back-ends,
plug APIs into Godot, build interfaces and integrations, and see how far it goes. Everyone is welcome to suggest an
idea or build an app.

Apps in the lab today:

- [Second Brain GD](https://github.com/sonixz/second-brain-gd): your second brain, every AI agent, your rules.
- [Agent Manager GD](https://github.com/sonixz/agent-manager-gd): every coding agent, one control room.

## The site

One site, assembled from several repositories:

| Path | Source |
|---|---|
| `/` and `/blog/` | `docs/` in this repository (plain HTML and CSS, shared styles in `docs/assets/lab.css`) |
| `/second-brain/` | `public/` in second-brain-gd |
| `/agent-manager/` | `public/` in agent-manager-gd |

Each app keeps its site in its own repository. `tools/assemble.py` (Python standard library only) copies everything
into `_site/` and adds the thin GD Project bar (`tools/lab-bar.html`) at the top of every app page, unless the page
already has one.

Work on it locally, with the three repositories side by side (`../second-brain-gd`, `../agent-manager-gd`):

    python3 tools/site.py serve     # build, check the links, serve on http://localhost:8800, rebuild on every change
    python3 tools/site.py check     # build and check every internal link and image (non-zero exit if one is broken)
    python3 tools/site.py build     # just build _site/

Publication: the repositories stay private for now (owner, 2026-11-09), so the site is built and checked locally.
`.github/workflows/pages.yml` (GitHub Pages, parked: manual runs only) is kept for when the site goes online.

A new blog post is one HTML file in `docs/blog/` (copy the last one), plus a card in `docs/blog/index.html` and in the
« From the lab » section of `docs/index.html`.

Licence: MIT. Godot is a trademark of the Godot Foundation; GD Project is an independent project.
