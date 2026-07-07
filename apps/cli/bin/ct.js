#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
const pythonScript = path.resolve(__dirname, '../../../engines/python/src/engine/cli/ct.py');

const result = spawnSync('python', [pythonScript, ...args], { stdio: 'inherit' });
process.exit(result.status);
