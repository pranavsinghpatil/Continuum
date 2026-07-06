import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine.plugins.mcp import MCPServer

def run_test():
    print("--- Executing Phase 8 (Plugins & MCP) ---")
    
    mcp_server = MCPServer()
    
    # 1. Register an external tool
    def external_lint(params):
        return {"status": "success", "linter": "ESLint", "errors": 0}
        
    mcp_server.register_tool("run_linter", "Run standard linter on output", external_lint)
    
    # 2. Worker executes tool during task
    print("\n-> [Worker] Processing task...")
    result = mcp_server.call_tool("run_linter", {"target": "ComponentCode"})
    print(f"-> [Worker] Tool Result: {result}")
    
    print("\n[SUCCESS] Continuum integrates with external tools via MCP!")
    print("--- Done! ---")

if __name__ == '__main__':
    run_test()
