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

Preview locally, with the three repositories side by side:

    python3 tools/assemble.py
    python3 -m http.server -d _site 8800      # then open http://localhost:8800

Publication: `.github/workflows/pages.yml` runs the same assembly on GitHub Actions and deploys to GitHub Pages. The
steps to turn it on are at the top of that file.

A new blog post is one HTML file in `docs/blog/` (copy the last one), plus a card in `docs/blog/index.html` and in the
« From the lab » section of `docs/index.html`.

Licence: MIT. Godot is a trademark of the Godot Foundation; GD Project is an independent project.
