# SPEC-0007: Artifacts

## Overview
The tangible outputs produced by tasks.

## Requirements
- Stored reliably in the .artifacts directory.
- Versioned and immutable once completed.

## Interfaces
- ArtifactStore.save_artifact()
- ArtifactStore.get_artifact()

## Invariants
- Artifacts cannot be modified once in COMPLETED state.

## Acceptance Criteria
- Content and metadata are persisted securely.