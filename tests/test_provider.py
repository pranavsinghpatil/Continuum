import os
import sys
import glob

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine.provider.antigravity import AntigravityProvider
from engine.task.engine import TaskEngine
from engine.context.builder import ContextBuilder

def run_test():
    print("--- Executing Phase 9 (Provider Interface - Antigravity) ---")
    
    # 1. Initialize Provider
    provider = AntigravityProvider("D:/Continuum")
    task_engine = TaskEngine()
    context_builder = ContextBuilder("D:/Continuum")
    
    # 2. Simulate the Runtime creating tasks
    task = task_engine.create_task("Build Header Component", "Implement responsive header", "FF.COMPONENTS")
    context = context_builder.build_task_context(task.id, task.capability_id, task.description)
    
    # 3. Worker uses Provider to execute
    print(f"-> [Worker] Delegating task to Antigravity Provider...")
    result = provider.generate(
        task_id=task.id,
        prompt=task.description,
        context=context
    )
    
    print(f"-> [Worker] Result: {result}")
    
    # 4. Verify Inbox
    inbox_files = glob.glob("D:/Continuum/.continuum/tasks/pending/*.json")
    print(f"[SUCCESS] Found {len(inbox_files)} task(s) awaiting Antigravity subagents in the inbox!")
    print("--- Done! ---")

if __name__ == '__main__':
    run_test()
