# SPEC-0010: Governance

## Overview
The constraint enforcement and auditing layer.

## Requirements
- Artifacts must pass specific councils (Design, Quality, Architecture).
- Support for Accept, Reject, Revision flows.

## Interfaces
- GovernanceEngine.review_artifact()

## Invariants
- No task is COMPLETED without passing governance REVIEW.

## Acceptance Criteria
- Artifacts failing audits are correctly set to REVISION.