# SPEC-0004: Provider Interface

## Overview
Abstraction layer for language models.

## Requirements
- Standardized prompt/response format for all LLM backends (OpenAI, Anthropic, etc).
- Support Mock provider for unit tests.

## Interfaces
- Provider.generate(prompt: str) -> str

## Invariants
- Must return predictable text structures.

## Acceptance Criteria
- Mock provider handles requests without network calls.