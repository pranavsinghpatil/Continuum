import os
import json
from typing import Dict, Any
from engine.execution.interface import ExecutionProvider
from engine.artifact.store import ArtifactStore

class DemoExecutionProvider(ExecutionProvider):
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.artifact_store = ArtifactStore(workspace_dir)
        
    def submit(self, task_id: str, txf_payload: Dict[str, Any]) -> str:
        role = txf_payload.get("role", "Worker")
        capability = txf_payload.get("capability", "Task")
        
        print(f"\n→ {role}")
        
        # Fake Artifact Generation based on capability
        artifact_name = f"{capability}_output.md"
        if "layout" in capability.lower() or "page" in capability.lower():
            artifact_name = "page.tsx"
        elif "req" in capability.lower() or "strategist" in role.lower():
            artifact_name = "Requirements.md"
        elif "ux" in role.lower():
            artifact_name = "UserFlow.md"
        elif "design" in role.lower():
            artifact_name = "DesignSpec.md"
        elif "audit" in role.lower():
            artifact_name = "audit.md"
            
        content = f"Mock generated content for {capability} by {role}."
        
        artifact_id = self.artifact_store.save_artifact(
            name=artifact_name,
            content=content,
            metadata={"task_id": task_id, "provenance": txf_payload}
        )
        
        print(f"  ✓ {artifact_name}")
        return "COMPLETED"
        
    def status(self, task_id: str) -> str:
        return "COMPLETED"
