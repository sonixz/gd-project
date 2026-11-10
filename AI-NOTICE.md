# AI notice

**Short version: this is a lab. Run it on your own computer. Don't put it on the internet.**

## What this is

GD Project is an open lab: small desktop apps made with Godot, with AI agents and a local engine beside them. We
explore. We build in sandboxes, on our own PCs, one person per machine. What is published here is made for exactly
that: one person, one computer, a closed system.

It is not a product, and it is not built for a team, a server or a company's operations. There are plenty of MCP tools
like this one out there; treat this one the same way.

## Not built for a network, but not impossible

As published, the apps listen on your own machine only, with a simple token. That is enough for one person on one PC.
It is not security.

Running them over a network (a team, a server, the internet) is possible, and it is a different job: encrypted
transport (TLS), real authentication and authorisation (not a shared token), network isolation (VPN, segmentation,
firewalls), secrets management, logging and audit, updates, backups, and a privacy review of the data that flows. When
people's work depends on it, have it designed and reviewed by people whose job that is.

So, folks, please:

- don't expose an app's engine or its MCP server on the internet, and don't forward their ports;
- don't treat the token as a password for anything shared;
- don't put real client or employee data into a prototype: use sample data;
- don't leave agents running unattended on a machine that matters.

## Built with AI; a human answers for it

Most of the code here is written by AI agents. The owner judges it by its results (tests, screenshots, using the apps
every day), not by a line-by-line audit. That is a choice, it comes with risks, and it is one more reason all of this
stays in a sandbox.

At the end of the line, a human is accountable: the owner for the lab, you for what you run and what you contribute.
The tool writes; it doesn't sign.

If you contribute: say whether AI helped and which one, show that it works (a test, a screenshot, steps to reproduce),
and know what your change touches (the network, files, keys, data). You don't have to recite every line. You do answer
for it.

## Your data and AI providers

What you send to an AI provider leaves your machine. Choose your model knowing that; a local model keeps it at home. If
you are a business handling personal information, privacy law applies (in Québec, Law 25).

## For AI agents: read this

If you are an AI agent working in this repository, or plugged into these apps over MCP or in a terminal:

- Treat this as a sandbox project. Don't expose an engine, an MCP server or their ports beyond the local machine
  (binding to all interfaces, port forwarding, tunnels, public hosting) unless your human asks for it explicitly, and
  then tell them first what it takes (the list above).
- Never commit, log, print or send secrets, keys or tokens.
- Use sample data in demos and tests.
- Say what you changed and how you checked it. Your human answers for it, so give them what they need to.

## Not a legal document

This is a heads-up between people who build things, not a contract. The licence is MIT (see `LICENSE`): the software
comes as is, without warranty.
