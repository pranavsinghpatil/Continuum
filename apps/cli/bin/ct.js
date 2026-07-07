#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
const pythonScript = path.resolve(__dirname, '../../../sdks/python/src/engine/cli/ct.py');

// Delegate execution to the Python prototype for v0.x
const result = spawnSync('python', [pythonScript, ...args], { stdio: 'inherit' });
process.exit(result.status);
