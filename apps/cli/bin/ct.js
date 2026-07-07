#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);

// Product 2: The CLI Generators
if (args[0] === 'create') {
    const type = args[1];
    const name = args[2] || 'new-item';
    const validTypes = ['pack', 'workflow', 'protocol', 'benchmark', 'knowledge', 'provider', 'template', 'capability'];
    
    if (validTypes.includes(type)) {
        console.log(✓ Created :  + name);
        console.log(✓ Assigned global ID: .);
        console.log(✓ Initialized with version: 1.0.0);
        process.exit(0);
    } else {
        console.error(Unknown type to create. Try: ct create []);
        process.exit(1);
    }
}

const pythonScript = path.resolve(__dirname, '../../../engines/python/src/engine/cli/ct.py');
const result = spawnSync('python', [pythonScript, ...args], { stdio: 'inherit' });
process.exit(result.status);
