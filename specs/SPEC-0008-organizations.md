# SPEC-0008: Organizations

## Overview
The structure and payload that runs on top of Continuum.

## Requirements
- Defined via YAML (Roles, Capabilities, Protocols).
- Roles have strict boundaries and guidelines.

## Interfaces
- OrganizationLoader.load_org_manifest()

## Invariants
- Validates against a strict JSON/YAML schema.

## Acceptance Criteria
- Frontend Force alpha parses completely without errors.