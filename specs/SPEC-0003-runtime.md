# SPEC-0003: Runtime

## Overview
The execution environment coordinating engines and executing protocols.

## Requirements
- Bootstraps EventBus, TaskEngine, ArtifactStore, ContextBuilder, KnowledgeEngine, GovernanceEngine.
- Compiles capabilities into an ExecutionGraph.

## Interfaces
- Runtime(workspace_dir) class.
- execute_protocol(org, version, protocol)

## Invariants
- Runtime orchestrates, it does not do the specific work itself.

## Acceptance Criteria
- Can load an organization and run a protocol end-to-end.