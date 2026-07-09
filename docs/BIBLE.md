# The Continuum Bible

Welcome to the definitive guide to Continuum OS. This document explains the **What**, **Why**, **How**, and **What For** of every single concept, folder, and file in the system. It serves as the ultimate source of truth for developers, organization designers, and execution providers.

---

## 1. The Global Layer vs. Organization Packs

Continuum is built on the principle of **Inheritance**. 

### What is the Global Layer?
The Global Layer (`/packs/global/`) acts as the standard library for AI Organizations. It contains foundational Roles (e.g., `Base Engineer`, `Base PM`), universal Knowledge (e.g., standard Git flows, general HTTP principles), and generic Capabilities.

### Why do we need it?
Without a global layer, every single Organization Pack would have to reinvent the wheel. If you are building `frontend-force`, you shouldn't have to teach the AI what an "Engineer" is from scratch. You should just inherit `base-engineer` from the global layer and extend it with frontend-specific skills.

### How does it work?
When the Continuum Kernel executes a protocol, it merges the YAML manifests. It looks for dependencies in the pack's `manifest.yaml` and recursively loads inherited traits from the Global layer.

---

## 2. Directory Architecture (The What, Why, How, For)

### `/apps/`
* **What**: Contains the executable entry points and UI applications.
* **Why**: Separates the interfaces (CLI, Desktop UI, Web Dashboard) from the core logic.
* **How**: Run via standard package managers (e.g., `npm install -g`).
* **For**: The end-user. This is how humans interact with Continuum.
  * `/apps/cli/`: The Node.js command-line interface.

### `/engines/`
* **What**: The core execution routers and state machines.
* **Why**: Decouples the logic of "managing an organization" from the "LLM Provider". 
* **How**: Reads YAML manifests from `/packs/`, converts them into TXF (Task Exchange Format), and sends them to the active Execution Provider (like Anthropic or Antigravity).
* **For**: Managing deterministic state and routing messages between AI agents.
  * `/engines/python/`: The primary runtime engine written in Python.

### `/packs/`
* **What**: The brains and structure of the AI Organizations. 
* **Why**: To make AI workflows installable, versionable, and reusable.
* **How**: Written entirely in declarative YAML. No code. Just definitions.
* **For**: Defining exactly *how* a specific task should be solved.
  * `/packs/global/`: The universal standard library of roles and knowledge.
  * `/packs/frontend-force/`: A specialized organization that builds elite web frontends.

### `/assets/`
* **What**: Static media, branding, and visuals.
* **Why**: To maintain the "Premium Open Source" aesthetic and brand identity.
* **How**: Stored as SVGs, PNGs, and ICOs. Version controlled.
* **For**: READMEs, documentation sites, and UI applications.

### `/docs/`
* **What**: The official documentation (The Bible, Cookbooks, API references).
* **Why**: To make the ecosystem accessible to outside developers.
* **How**: Written in Markdown. Can be deployed to a static site generator (e.g., Docusaurus).
* **For**: Developers learning how to build their own Continuum Packs.

---

## 3. Core Concepts

### TXF (Task Exchange Format)
* **What**: A standardized JSON schema for AI-to-AI communication.
* **Why**: When an AI agent finishes a task, the next agent needs to know exactly what was done without losing context in a massive chat log.
* **How**: Passed as a payload between roles in the Execution Router.

### Capabilities
* **What**: A specific skill an agent possesses (e.g., `FF.ACCESSIBILITY`).
* **Why**: Instead of writing one massive system prompt, you give an agent a specific capability so it focuses on one job at a time.

### Protocols
* **What**: The workflow definition (e.g., `landing-page.yaml`).
* **Why**: To enforce a sequence of events. A protocol guarantees that the UX Architect acts *before* the Visual Designer.
