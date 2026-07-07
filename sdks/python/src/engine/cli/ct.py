import argparse
import sys
sys.stdout.reconfigure(encoding="utf-8")
from engine.runtime import Runtime
from engine.execution.router import ExecutionRouter
from engine.execution.agents.demo import DemoExecutionProvider
from engine.context.builder import ContextBuilder

def main():
    parser = argparse.ArgumentParser(description="Continuum OS CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    init_parser = subparsers.add_parser("init", help="Initialize a new Continuum workspace")
    init_parser.add_argument("template", nargs='?', default="default", help="Template to use (e.g. demo)")
    
    run_parser = subparsers.add_parser("run", help="Execute a protocol workflow")
    run_parser.add_argument("protocol", help="Protocol to execute (e.g. landing-page)")
    run_parser.add_argument("--prompt", required=True, help="User prompt driving the protocol")

    args = parser.parse_args()

    if args.command == "init":
        print(f"Initialized Continuum workspace using template: {args.template}")
        
    elif args.command == "run":
        print("✓ Loaded Frontend Force")
        print("✓ Loaded Knowledge Packs")
        print(f"✓ Loaded {args.protocol.replace('-', ' ').title()} Protocol\n")
        
        # Execute the vertical slice pipeline
        runtime = Runtime(".")
        
        router = ExecutionRouter()
        router.register("demo", DemoExecutionProvider("."))
        context_builder = ContextBuilder(".")
        
        # Hardcoded simulation of the protocol steps for the Alpha Demo
        steps = [
            ("Product Strategist", "FF.PROD.REQ"),
            ("UX Architect", "FF.UX.DESIGN"),
            ("Visual Designer", "FF.VISUAL.DESIGN"),
            ("Frontend Engineer", "FF.COMPONENTS"),
            ("Accessibility Auditor", "FF.ACCESSIBILITY")
        ]
        
        for role, cap in steps:
            task = runtime.task_engine.create_task(f"Task for {cap}", f"Execute {cap}", cap)
            
            txf_payload = {
                "version": 1,
                "task_id": task.id,
                "role": role,
                "capability": cap,
                "context": context_builder.build_task_context(task.id, cap, ""),
                "prompt": args.prompt
            }
            
            router.route(task.id, "demo", txf_payload)
            
        print("\n✓ Workflow completed")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
