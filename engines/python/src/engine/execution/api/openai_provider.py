import os
import json
from typing import Dict, Any
from engine.execution.interface import ExecutionProvider
from engine.artifact.store import ArtifactStore

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class OpenAIProvider(ExecutionProvider):
    """
    Real execution backend using the OpenAI API.
    Requires OPENAI_API_KEY in environment variables.
    """
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.artifact_store = ArtifactStore(workspace_dir)
        if OpenAI:
            self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        else:
            self.client = None
            
    def submit(self, task_id: str, txf_payload: Dict[str, Any]) -> str:
        if not self.client:
            print("[OpenAIProvider] ERROR: 'openai' package not installed.")
            return "FAILED"
            
        role = txf_payload.get("role", "Worker")
        capability = txf_payload.get("capability", "Task")
        prompt = txf_payload.get("prompt", "")
        context = txf_payload.get("context", {})
        
        system_prompt = f"You are acting as {role}. You are executing the capability {capability}.\n\nContext:\n{json.dumps(context)}"
        
        try:
            print(f"-> [OpenAI] Requesting completion for {capability}...")
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            content = response.choices[0].message.content
            
            artifact_name = f"{capability}_output.md"
            self.artifact_store.save_artifact(
                name=artifact_name,
                content=content,
                metadata={"task_id": task_id, "provider": "openai"}
            )
            print(f"  ✓ Saved real output from OpenAI to {artifact_name}")
            return "COMPLETED"
        except Exception as e:
            print(f"[OpenAIProvider] Execution failed: {e}")
            return "FAILED"

    def status(self, task_id: str) -> str:
        return "COMPLETED"
