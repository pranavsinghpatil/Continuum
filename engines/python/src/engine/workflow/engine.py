import uuid
from typing import List, Dict

class Workflow:
    def __init__(self, protocol_name: str, prompt: str):
        self.id = str(uuid.uuid4())
        self.protocol_name = protocol_name
        self.prompt = prompt
        self.tasks: List[str] = []
        self.status = "INITIALIZED"
        
class WorkflowEngine:
    def __init__(self):
        self.workflows: Dict[str, Workflow] = {}
        
    def start_workflow(self, protocol_name: str, prompt: str) -> Workflow:
        wf = Workflow(protocol_name, prompt)
        self.workflows[wf.id] = wf
        wf.status = "RUNNING"
        return wf
