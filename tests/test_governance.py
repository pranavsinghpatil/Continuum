import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine.event.bus import EventBus, Event
from engine.task.engine import TaskEngine, TaskStatus
from engine.artifact.store import ArtifactStore
from engine.context.builder import ContextBuilder
from engine.governance.engine import GovernanceEngine

def run_test():
    print("--- Executing Phase 7 (Governance) ---")
    
    bus = EventBus()
    task_engine = TaskEngine()
    artifact_store = ArtifactStore(".")
    context_builder = ContextBuilder(".")
    governance_engine = GovernanceEngine(".")
    
    def on_task_created(event):
        task_id = event.payload["task_id"]
        task = task_engine.claim_task(task_id, "FrontendEngineer")
        
        # 1. Execute task
        print("-> [Worker] Generating output...")
        output_content = f"Draft Component Code"
        
        artifact_id = artifact_store.save_artifact(
            name=f"{task.name}_draft", 
            content=output_content, 
            metadata={"task_id": task.id}
        )
        
        # 2. Phase 7: Governance Review
        task.status = TaskStatus.REVIEW
        review_result = governance_engine.review_artifact(task.id, output_content)
        
        if review_result["status"] == "ACCEPT":
            task_engine.complete_task(task.id, [artifact_id])
            print("-> [Worker] Task completed.")
            bus.dispatch(Event("TaskCompleted", {"task_id": task.id, "artifact_id": artifact_id}))
        else:
            task.status = TaskStatus.REVISION
            print(f"-> [Worker] Task sent back for revision: {review_result['feedback']}")

    def on_task_completed(event):
        print("[SUCCESS] Artifacts were reviewed before completion!")

    bus.subscribe("TaskCreated", on_task_created)
    bus.subscribe("TaskCompleted", on_task_completed)
    
    task = task_engine.create_task("Build Button Component", "Write standard button", "FF.COMPONENTS")
    bus.dispatch(Event("TaskCreated", {"task_id": task.id}))
    print("--- Done! ---")

if __name__ == '__main__':
    run_test()
