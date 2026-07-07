<p align="center">
  <img src="./assets/favicons/continuum.ico" alt="Continuum Logo" width="120" />
</p>
<h1 align="center">Continuum</h1>
<p align="center">
  <strong>The Operating Kernel for AI Organizations</strong><br>
  Install reusable AI organizations. Run them on any execution provider.
</p>
<p align="center">
  <a href="https://github.com/pranavsinghpatil/Continuum/releases">
    <img src="https://img.shields.io/github/v/release/pranavsinghpatil/Continuum?color=blue" alt="Release">
  </a>
  <a href="https://github.com/pranavsinghpatil/Continuum/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

<br/>

## What is Continuum?

Most developers use AI to generate code. **Continuum uses AI to generate organizations.**

Continuum is not another LLM wrapper, prompt chain, or LangChain alternative. It is an operating kernel and package manager for autonomous, multi-agent workflows. 

Instead of writing complex custom scripts, you install a **Pack** (like `frontend-force`), which contains the specialized knowledge, capabilities, and protocols to simulate an entire virtual engineering department.

```bash
# 1. Install the Continuum CLI
git clone https://github.com/pranavsinghpatil/Continuum.git
cd Continuum

# Link the CLI globally
cd apps/cli && npm link

# 2. Initialize a new workspace
ct init acme

# 3. Add an intelligence pack
ct add frontend-force

# 4. Execute a specialized protocol
ct run landing-page --prompt "Build an AI startup landing page"
```

## Why Continuum?

| Feature | Raw Agent | Continuum |
| ------- | --------- | --------- |
| **End-to-end Execution** | âŒ | âœ… |
| **Accessibility Compliance** | âš ï¸ | âœ… |
| **Design Consistency** | âš ï¸ | âœ… |
| **Governance & Auditing** | âŒ | âœ… |
| **Knowledge Reuse** | âŒ | âœ… |

### The Power of Packs
When you run `ct add frontend-force`, you aren't just downloading scripts. You're downloading an entire organizational structure:
- ðŸ“Š A **Product Strategist** that understands requirements gathering and user flows.
- ðŸ“ A **UX Architect** that builds component taxonomies and wireframes.
- ðŸ’» A **Frontend Engineer** that translates design tokens into pixel-perfect React.
- â™¿ An **Accessibility Auditor** that guarantees strict WCAG compliance.

## Architecture

Continuum is built on three robust pillars:

1. **The Kernel (The OS)**
   Orchestrates Tasks, Events, Artifacts, and Workflows across the distributed execution layer.
   
2. **The Package Manager (The App Store)**
   Resolves and installs Intelligence Packs using manifest-driven architecture, ensuring zero duplication of knowledge.

3. **Execution Engines (The CPU)**
   Pluggable execution providers (like Claude Code, Gemini CLI, or Antigravity). Switching from Claude to Gemini does not require changing your organization. Your company's logic and workflows survive model updates.

## Deep Dive into Packs

Packs are semantically versioned and globally identified. A single Pack manifest looks like this:

```yaml
pack:
  id: pack.frontend-force
  version: 1.0.0

dependencies:
  knowledge.design-core: ^1.0.0
  knowledge.accessibility-core: ^1.0.0
  protocol.landing-page: ^2.1.0

capabilities:
  - id: ff.capability.layout
  - id: ff.capability.typography
  - id: ff.capability.accessibility
```
*When you install a pack, Continuum automatically resolves its entire dependency tree.*

## Getting Started

To learn more about the Continuum architecture, developing your own packs, or contributing to the core kernel, check out our [Documentation](./docs/).

---
<div align="center">
  <sub>Built with precision and developer delight. Welcome to the future of AI workflows.</sub>
</div>

