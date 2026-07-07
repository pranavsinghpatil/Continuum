#!/bin/bash
export PYTHONPATH="$(dirname "$0")/engines/python/src"
python "$(dirname "$0")/engines/python/src/engine/cli/ct.py" "$@"
