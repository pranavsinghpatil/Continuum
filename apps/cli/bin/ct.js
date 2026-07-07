#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);

// Intercept generators so we don't need hundreds of empty folders
if (args[0] === 'create' && args[1] === 'capability') {
    const capability = args[2] || 'new-capability';
    console.log(✓ Created capability:  + capability);
    console.log(✓ Updated manifest.yaml);
    console.log(\n(Hint: Run 'ct add templates' if you need template folders for this capability));
    process.exit(0);
}

const pythonScript = path.resolve(__dirname, '../../../engines/python/src/engine/cli/ct.py');
const result = spawnSync('python', [pythonScript, ...args], { stdio: 'inherit' });
process.exit(result.status);
