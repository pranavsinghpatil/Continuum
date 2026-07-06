import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from engine.runtime import Runtime
from engine.context.builder import ContextBuilder

def run():
    print("--- Executing Phase 6 (Knowledge Engine) ---")
    runtime = Runtime(".")
    
    # Intercept tasks to prove Context Builder uses RAG
    context_builder = ContextBuilder(".")
    
    def on_task_created(event):
        task_id = event.payload["task_id"]
        task = runtime.task_engine.claim_task(task_id, "test_role")
        
        # Test Knowledge Retrieval
        context = context_builder.build_task_context(task.id, task.capability_id, task.description)
        print(f"    [Worker] {context['knowledge']}")
        
    runtime.bus.subscribe("TaskCreated", on_task_created)
    
    runtime.load_org("FrontendForce", "v1")
    runtime.execute_protocol("FrontendForce", "v1", "LandingPage")
    print("--- Done! ---")

if __name__ == '__main__':
    run()
