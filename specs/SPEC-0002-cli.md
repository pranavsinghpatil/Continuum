# SPEC-0002: CLI

## Overview
The ct command-line interface.

## Requirements
- Commands: init, doctor, alidate, ersion, config, 
un.
- Output must be structured and readable.

## Interfaces
- Terminal arguments mapping to Python rgparse.

## Invariants
- Commands must not mutate global system state unexpectedly.

## Acceptance Criteria
- ct doctor verifies the environment properly.