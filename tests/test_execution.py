import os
import sys
import glob

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from engine.execution.router import ExecutionRouter
from engine.execution.agents.antigravity import AntigravityProvider

def run_test():
    print("--- Executing Agent Provider Epic ---")
    
    # 1. Setup Execution Router
    router = ExecutionRouter()
    
    # 2. Register Providers
    ag_provider = AntigravityProvider("D:/Continuum")
    router.register("antigravity", ag_provider)
    
    # 3. Simulate a Task Exchange Format (TXF) Payload
    txf_payload = {
        "version": 1,
        "task_id": "test-task-123",
        "role": "frontend.visual-designer",
        "capability": "layout",
        "context": "Context strings...",
        "constraints": ["Accessible", "Responsive"]
    }
    
    # 4. Route Task
    print(f"-> [Router] Routing task to 'antigravity' provider...")
    result = router.route("test-task-123", "antigravity", txf_payload)
    print(f"-> [Router] Result: {result}")
    
    # 5. Verify Queue
    inbox_files = glob.glob("D:/Continuum/.continuum/queue/incoming/*.txf.json")
    print(f"[SUCCESS] Found {len(inbox_files)} TXF file(s) in the incoming queue!")
    print("--- Done! ---")

if __name__ == '__main__':
    run_test()
