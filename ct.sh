#!/bin/bash
export PYTHONPATH="$(dirname "$0")/sdks/python/src"
python "$(dirname "$0")/sdks/python/src/engine/cli/ct.py" "$@"
