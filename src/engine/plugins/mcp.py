from typing import Dict, Any, Callable

class MCPServer:
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
        
    def register_tool(self, name: str, description: str, handler: Callable):
        print(f"[MCP] Registered external tool: {name}")
        self.tools[name] = {
            "description": description,
            "handler": handler
        }
        
    def call_tool(self, name: str, params: Dict[str, Any]) -> Any:
        print(f"[MCP] Executing tool: {name} with params {params}")
        if name not in self.tools:
            raise ValueError(f"Tool {name} not found.")
        return self.tools[name]["handler"](params)
