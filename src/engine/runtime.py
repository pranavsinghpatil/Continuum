from organization.loader import OrganizationLoader
from organization.graph import ExecutionGraph
from engine.event.bus import EventBus, Event
from engine.task.engine import TaskEngine

class Runtime:
    def __init__(self, workspace_dir: str = "."):
        self.workspace_dir = workspace_dir
        self.loader = OrganizationLoader(workspace_dir)
        self.bus = EventBus()
        self.task_engine = TaskEngine()
        self.org_cache = {}

    def load_org(self, org_name: str, version: str = "v1"):
        org = self.loader.load_organization(org_name, version)
        self.org_cache[f"{org_name}@{version}"] = org
        return org

    def execute_protocol(self, org_name: str, version: str, protocol_id: str):
        org_key = f"{org_name}@{version}"
        if org_key not in self.org_cache:
            self.load_org(org_name, version)
            
        org = self.org_cache[org_key]
        graph = ExecutionGraph(org)
        
        steps = graph.build_graph(protocol_id)
        
        print(f"\n[Runtime] Executing Protocol: {protocol_id}")
        for step in steps:
            print(f" -> [Step] Executing Capability: {step}")
            task = self.task_engine.create_task(f"Task for {step}", f"Executing {step} capability", step)
            print(f"    [TaskEngine] Dispatched task {task.id}")
            self.bus.dispatch(Event("TaskCreated", {"task_id": task.id}))
