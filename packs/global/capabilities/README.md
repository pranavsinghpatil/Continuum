# Global Capabilities

This directory contains generic action handlers (capabilities) that any organization can use.

## Purpose
A capability represents a concrete skill or tool an agent can use (e.g., "Run a terminal command", "Search the web", "Write to a file"). 
By keeping generic capabilities here, specialized packs only need to define niche capabilities (e.g., `frontend-force` might define `GENERATE_FIGMA_TOKENS`).

## Usage
Define capabilities using YAML manifests that link to the underlying execution functions in the Kernel.
