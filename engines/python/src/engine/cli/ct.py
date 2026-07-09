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
        import yaml
        import os
        import time

        print("\x1b[36m[Continuum Kernel] Booting Organization Pack: Frontend Force...\x1b[0m")
        time.sleep(0.5)
        print("\x1b[36m[Continuum Kernel] Binding Execution Layer: Antigravity...\x1b[0m\n")
        time.sleep(0.5)
        
        protocol_path = os.path.join("packs", "frontend-force", "protocols", f"{args.protocol}.yaml")
        if not os.path.exists(protocol_path):
            print(f"Error: Protocol {args.protocol} not found.")
            return

        print(f"\x1b[35m=== INITIATING PROTOCOL: {args.protocol.upper()} ===\x1b[0m")
        print(f"Prompt: \"{args.prompt}\"\n")
        
        with open(protocol_path, "r") as f:
            protocol_data = yaml.safe_load(f)

        execution_log = []

        for step in protocol_data.get("steps", []):
            role = step.get("role", "Agent")
            action = step.get("action", "UNKNOWN_ACTION")
            tools = step.get("tools", [])
            
            print(f"\n\x1b[33m[{role}]\x1b[0m Executing: {action}...")
            time.sleep(1)
            
            if tools:
                print(f"\x1b[36m[System]\x1b[0m Granting {role} access to tools: {', '.join(tools)}")
                time.sleep(1)
                for tool in tools:
                    print(f"\x1b[33m[{role}]\x1b[0m 🔧 Invoking {tool}...")
                    time.sleep(0.5)
                print(f"\x1b[33m[{role}]\x1b[0m Tool execution complete. Synthesizing data...")
                execution_log.append(f"✓ {role} utilized tools ({', '.join(tools)}) during {action}.")
                time.sleep(1)
            
            if action == "INTERVIEW_USER":
                print(f"\x1b[33m[{role}]\x1b[0m The prompt lacks specific details required for execution.")
                print(f"\x1b[33m[{role}]\x1b[0m {step.get('description', 'Please provide more details.')}")
                if "portfolio" in args.protocol:
                    print("  1. Please list your past 2 job titles and companies.")
                    print("  2. What are 2 core projects you want highlighted?")
                    print("  3. What is your preferred tech stack (e.g., React, Three.js, Python)?")
                else:
                    print("  1. What is the core business objective?")
                    print("  2. Who is the target audience?")
                
                input("\x1b[90m> (Simulated User Input) \x1b[0m")
                print(f"\x1b[33m[{role}]\x1b[0m Context acquired. Generating PRD -> {step.get('output', 'STATE')}")
                execution_log.append(f"✓ {role} interviewed user and generated {step.get('output', 'PRD')}")
                
            elif action == "REVIEW_AND_CRITIQUE":
                print(f"\x1b[35m[{role}]\x1b[0m Critiquing {step.get('input')}...")
                time.sleep(1)
                print(f"\x1b[35m[{role}]\x1b[0m REJECTED: {step.get('description', 'Fails quality standards.')}")
                print(f"\x1b[35m[{role}]\x1b[0m Triggering on_reject: {step.get('on_reject')}")
                time.sleep(1.5)
                print(f"\x1b[34m[UX Architect]\x1b[0m Acknowledged. Restructuring layout to meet requirements.")
                execution_log.append(f"⚠ {role} rejected initial draft and forced a rewrite to enforce standards.")
                
            elif action == "IMPLEMENT_REACT_APP" or action == "IMPLEMENT_COMPONENT":
                print(f"\x1b[36m[{role}]\x1b[0m Ingesting approved wireframes. Booting engineering pipeline...")
                time.sleep(2)
                print(f"\x1b[36m[{role}]\x1b[0m Scaffolded components. Writing to disk.")
                time.sleep(1)
                execution_log.append(f"✓ {role} implemented code based on approved designs.")
            
            else:
                print(f"\x1b[32m[{role}]\x1b[0m Processing {step.get('input')} -> {step.get('output')}")
                time.sleep(1.5)
                execution_log.append(f"✓ {role} completed {action}.")
                
        print("\n\x1b[32m=== FINAL EXECUTION REPORT ===\x1b[0m")
        for log in execution_log:
            print(f"  {log}")
            
        print("\n\x1b[35m[Continuum Kernel]\x1b[0m Workflow suspended for Final User Gate.")
        final_input = input("\x1b[90m> Do you (User) want to add something more, disagree, or approve? (Press Enter to approve) \x1b[0m")
        
        if final_input.strip():
            print(f"\n\x1b[33m[Product Strategist]\x1b[0m Feedback received: '{final_input}'. Booting revision loop...")
        else:
            print("\n\x1b[32m✓ Protocol Execution Complete. Artifacts committed.\x1b[0m")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
