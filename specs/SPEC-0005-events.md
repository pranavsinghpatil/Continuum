# SPEC-0005: Events

## Overview
The EventBus decoupling layer.

## Requirements
- Subsystems communicate via asynchronous-style events.
- Central event dispatcher.

## Interfaces
- EventBus.subscribe(event_name, callback)
- EventBus.dispatch(Event)

## Invariants
- Publishers do not know their subscribers.

## Acceptance Criteria
- Event delivery is guaranteed across the local process.