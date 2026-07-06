# SPEC-0009: Knowledge

## Overview
The RAG and contextual retrieval system.

## Requirements
- Roles retrieve relevant Markdown knowledge instead of long context windows.
- Injects directly into context prior to task execution.

## Interfaces
- KnowledgeEngine.retrieve()
- ContextBuilder.build_task_context()

## Invariants
- Knowledge files must be in Markdown.

## Acceptance Criteria
- RAG successfully intersects task keywords with file contents.