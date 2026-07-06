# The Continuum Cookbook (The "Bible")

Welcome to the definitive guide to **Continuum**—the world's first Event-Driven Knowledge Operating System for AI Organizations.

## What is Continuum?

Most agent frameworks look like this: `Agent -> Memory -> Tools`
Continuum flips the paradigm entirely: `Organization -> Knowledge -> Tasks -> Artifacts -> Governance`

Continuum is **not** just a multi-agent chat wrapper. It is a system that models enduring enterprise capabilities. If you swap out Claude for GPT-5 tomorrow, the organization doesn't die. The **Knowledge Vault** (standards, rules, audits, research) persists, and the new models just execute against it.

---

## 1. Core Architecture

The Continuum runtime is powered by four specialized engines. Notice that LLMs exist in only ONE engine:

1. **Reasoning Engine:** Interfaces with LLM APIs (Claude, OpenAI, Gemini) to generate output.
2. **Knowledge Engine:** Retrieves principles, standards, and playbooks via Semantic Search (RAG for Organizations).
3. **Workflow Engine:** Routes events, queues tasks, and moves artifacts between roles (e.g. from Designer to QA).
4. **Governance Engine:** Assesses artifacts against standards to approve or reject them.

---

## 2. The Organizational Taxonomy

Everything in Continuum is an object in a Knowledge Graph, classified via the **Universal Classification Code (CCC)**:

`Organization` > `Division` > `Domain` > `Capability` > `Role`

Example CCC: `FF.DES.LAY.GRID` (Frontend Force -> Design Division -> Layout Domain -> Grid Systems).

### The Capability Contract
Capabilities don't just "do stuff". They are modular packages with strict contracts that define what they require, what they provide, and how success is measured.

```yaml
id: FF.DES.LAYOUT
contract:
  provides:
  - reusable_layouts
  requires:
  - spacing_standard
  success:
  - layouts_are_consistent
```

---

## 3. The CLI (`ct`) Quickstart

The Continuum CLI (`ct`) is your entry point to managing and executing the operating system.

### Step 1: Initialize a Workspace
```bash
ct init my-company
```
**What it does:** Scaffolds the `.continuum/`, `organizations/`, `knowledge/`, and `.artifacts/` folders, and generates the `continuum.yaml` file.

### Step 2: Install an Organization Pack (Coming Soon)
```bash
ct add frontend-force
```
**What it does:** Downloads the `frontend-force` organization blueprint, including its Divisions, Capabilities, and Roles.

### Step 3: Run the Runtime (Coming Soon)
```bash
ct run
```
**What it does:** Boots up the four engines (Reasoning, Knowledge, Workflow, Governance). It asks for your AI Provider (e.g., Claude), connects to the task queue, and starts listening for events (like a new PR, a Slack message, or a design file update).

---

## 4. Developing for Continuum (The Codebase)

The runtime is built in Python inside the `src/` directory, following a modular engine architecture:

### `src/config/parser.py`
Parses the `continuum.yaml` workspace file into a Python object `ContinuumConfig`. Ensures structural integrity.

### `src/providers/base.py`
The **Provider Interface**. This enforces a strict API (`chat`, `stream`, `embeddings`) that any AI model must adhere to. The Reasoning Engine uses this base class, meaning Continuum can switch from OpenAI to Anthropic with zero workflow changes.

### `src/organization/loader.py`
The **Organization Loader**. Parses the massive physical directory structure (`organizations/frontend-force/v1`) into a dynamic, in-memory graph by loading `registry/index.yaml` and recursively compiling `capability.yaml` definitions.

### `src/engine/task/engine.py`
The **Task Engine**. Orchestrates the event-driven queue. It makes Roles completely **stateless**. Tasks are emitted, placed in a queue, claimed by a Role, processed using injected contextual memory, and finally completed.

### `src/engine/artifact/store.py`
The **Artifact Store**. Artifacts are the true measure of organizational value (what was produced, rather than who produced it). This engine persists all outputs (Code, Markdown, Audits) as JSON files in `.artifacts/`, tagged with unique UUIDs and metadata (author, timestamp, task ID).

---

## 5. Event-Driven Workflows (The Magic)

Because Continuum is event-driven, tasks are emitted rather than directly called.

1. `Product Brief Submitted` (Event)
2. **Workflow Engine** creates `Requirements Task` and puts it in the Queue.
3. The `Product Manager Role` claims the task.
4. **Knowledge Engine** injects the `Product Brief Playbook` into the context.
5. **Reasoning Engine** (LLM) writes the Requirements Document.
6. The Document is passed to the **Artifact Store** and **Governance Engine** for approval.
7. Upon approval, `Requirements Generated` (Event) is emitted, starting the next step.

---

*This document will continuously evolve as we implement further milestones in Continuum.*
