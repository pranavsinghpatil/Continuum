from typing import Dict, Any

class ContextBuilder:
    def __init__(self, workspace_dir: str):
        self.workspace_dir = workspace_dir
        
    def build_task_context(self, task_id: str, capability_id: str) -> Dict[str, Any]:
        return {
            "task_id": task_id,
            "capability_id": capability_id,
            "knowledge": f"Loaded standards and playbooks for {capability_id}",
            "workspace": self.workspace_dir
        }
