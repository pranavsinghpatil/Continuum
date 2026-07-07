# Continuum

**The Operating Kernel for AI Organizations.**

Continuum is not just another LLM prompt wrapper. It is a distributed execution layer, a package manager, and a governance kernel for multi-agent workflows.

## Getting Started

\\\ash
npm install -g @continuum/cli

ct init acme
ct add frontend-force
ct run landing-page --prompt "Build an AI startup landing page"
\\\

## Architecture
- **Kernel**: Orchestrates Tasks, Events, Artifacts, and Workflows.
- **Packs**: Installable intelligence (like \rontend-force\).
- **Engines**: Execution providers (Claude Code, Gemini CLI, Python Workers).

See the [ROADMAP.md](./ROADMAP.md) for our path to v1.0.
