# SPEC-0006: Tasks

## Overview
Units of work executed by Roles.

## Requirements
- Tasks have states: PENDING, IN_PROGRESS, REVIEW, REVISION, COMPLETED.
- Track capabilities being executed.

## Interfaces
- TaskEngine.create_task()
- TaskEngine.claim_task()

## Invariants
- A task can only be claimed by one worker at a time.

## Acceptance Criteria
- Task state transitions correctly log to the history.