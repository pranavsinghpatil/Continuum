# The Continuum Cookbook

This cookbook provides practical, step-by-step guides on how to build and extend Continuum AI Organizations.

## Recipe 1: Extending the Global Layer

The Global Layer (`/packs/global/`) provides the standard primitives. When you build a new pack, you should inherit from it.

### Step 1: Examine the Global Role
Let's look at the `base-engineer.yaml` in the global layer:
```yaml
# /packs/global/roles/base-engineer.yaml
name: Base Engineer
description: A standard software engineer capable of writing syntactically correct code.
traits:
  - meticulous
  - test-driven
knowledge:
  - global.git-flow
  - global.clean-code
```

### Step 2: Create your Specialized Role
In your new pack (e.g., `frontend-force`), you don't need to redefine clean code. You just inherit the base role and add your specific capabilities.

```yaml
# /packs/frontend-force/roles/chief-design-officer.yaml
name: Chief Design Officer
inherits: global.base-engineer
description: Elite UI/UX architect and frontend engineer.
traits:
  - pixel-perfect
  - accessibility-obsessed
knowledge:
  - frontend-force.design-systems
  - frontend-force.wcag-standards
capabilities:
  - FF.UX.DESIGN
```

## Recipe 2: Writing a Protocol (The Workflow)

A protocol defines the sequence of events and debates that occur between roles.

```yaml
# /packs/frontend-force/protocols/landing-page.yaml
name: landing-page
description: Generates a high-converting landing page.
steps:
  - role: Product Strategist
    action: INTERVIEW_USER
    output: PRD_STATE

  - role: UX Architect
    action: DRAFT_WIREFRAME
    input: PRD_STATE
    output: WIREFRAME_STATE

  - role: Chief Design Officer
    action: REVIEW_AND_CRITIQUE
    input: WIREFRAME_STATE
    # The CDO can loop the UX Architect if the standard isn't met
    on_reject: return to UX Architect
```

By defining the `on_reject` hook, you create the "multi-agent debate" that makes Continuum superior to single-shot LLM generation.
