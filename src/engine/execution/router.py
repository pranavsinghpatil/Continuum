from typing import Dict, Any
from engine.execution.interface import ExecutionProvider

class ExecutionRouter:
    """
    Routes Tasks to the appropriate ExecutionProvider.
    """
    def __init__(self):
        self.providers: Dict[str, ExecutionProvider] = {}
        
    def register(self, name: str, provider: ExecutionProvider):
        self.providers[name] = provider
        
    def route(self, task_id: str, provider_name: str, txf_payload: Dict[str, Any]) -> str:
        if provider_name not in self.providers:
            raise ValueError(f"Unknown Execution Provider: {provider_name}")
        return self.providers[provider_name].submit(task_id, txf_payload)
