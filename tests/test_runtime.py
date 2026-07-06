import os
import sys

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine.event.bus import EventBus, Event
from engine.task.engine import TaskEngine, TaskStatus
from engine.artifact.store import ArtifactStore
from engine.context.builder import ContextBuilder

def run_test():
    print("[START] Booting Continuum Runtime Kernel...")
    
    # Initialize Core Engines
    bus = EventBus()
    task_engine = TaskEngine()
    artifact_store = ArtifactStore(".")
    context_builder = ContextBuilder(".")
    
    # Define Event Handlers
    def on_task_created(event):
        task_id = event.payload["task_id"]
        print(f"-> [Worker] Claiming task {task_id}")
        task = task_engine.claim_task(task_id, "test_role")
        
        # Build Context
        context = context_builder.build_task_context(task.id, task.capability_id)
        print(f"-> [Worker] Built Context: {context['knowledge']}")
        
        # Execute Task (Mocking LLM Reasoning Engine for now)
        print("-> [ReasoningEngine] Generating output...")
        output_content = f"Draft Requirements for {task.name}"
        
        # Save Artifact
        artifact_id = artifact_store.save_artifact(
            name=f"{task.name}_draft", 
            content=output_content, 
            metadata={"task_id": task.id}
        )
        print(f"-> [ArtifactStore] Saved artifact {artifact_id}")
        
        # Complete Task
        task_engine.complete_task(task.id, [artifact_id])
        print(f"-> [Worker] Task completed.")
        
        # Emit Task Completed Event
        bus.dispatch(Event("TaskCompleted", {"task_id": task.id, "artifact_id": artifact_id}))

    def on_task_completed(event):
        print("[SUCCESS] Runtime successfully executed one task end-to-end!")

    # Subscribe to Events
    bus.subscribe("TaskCreated", on_task_created)
    bus.subscribe("TaskCompleted", on_task_completed)
    
    # Trigger the first event
    print("\n--- Starting Execution ---")
    task = task_engine.create_task("Draft Feature Requirements", "Write requirements for authentication.", "FF.PROD.REQ")
    bus.dispatch(Event("TaskCreated", {"task_id": task.id}))

if __name__ == '__main__':
    run_test()
