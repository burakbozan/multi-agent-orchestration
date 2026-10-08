import json
import os
import sys

PROMPTS_DIR = "prompts"
WORKFLOWS_DIR = "workflows"

def load_prompt(agent_name):
    """Load prompt text from the /prompts folder."""
    filename = os.path.join(PROMPTS_DIR, f"{agent_name.lower()}.md")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    return f"No prompt found for {agent_name}"

def load_workflow(workflow_name):
    """Load workflow JSON by name."""
    filename = os.path.join(WORKFLOWS_DIR, f"{workflow_name}.json")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    raise FileNotFoundError(f"Workflow {workflow_name} not found in {WORKFLOWS_DIR}")

# Simulated agent functions (replace with Copilot/LLM calls later)
def planner(user_request, prompt):
    print(f"\n[Planner Prompt]\n{prompt}")
    return ["Set up project scaffold", "Implement CRUD operations", "Add authentication"]

def researcher(tasks, prompt):
    print(f"\n[Researcher Prompt]\n{prompt}")
    return {"Spring Boot": "Robust framework", "JWT": "Secure authentication"}

def coder(tasks, recommendations, prompt):
    print(f"\n[Coder Prompt]\n{prompt}")
    return {"Task.java": "Entity class", "TaskController.java": "REST endpoints"}

def reviewer(code_output, prompt):
    print(f"\n[Reviewer Prompt]\n{prompt}")
    return {"Entity": "✅ Correct", "Controller": "⚠️ Missing error handling"}

def orchestrator(outputs, prompt):
    print(f"\n[Orchestrator Prompt]\n{prompt}")
    print("\n=== Final Integrated Solution ===")
    for agent, output in outputs.items():
        print(f"\n[{agent} Output]\n{output}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py <workflow_name>")
        sys.exit(1)

    workflow_name = sys.argv[1]
    workflow = load_workflow(workflow_name)

    user_request = "Build a Task Manager API"
    outputs = {}

    # Run workflow steps dynamically
    for step in workflow["orchestration"]["workflow"]["steps"]:
        agents = step.split("→")
        current_agent = agents[0].strip()
        next_agent = agents[-1].strip()

        if current_agent == "Planner":
            outputs["Planner"] = planner(user_request, load_prompt("planner"))
        elif current_agent == "Researcher":
            outputs["Researcher"] = researcher(outputs["Planner"], load_prompt("researcher"))
        elif current_agent == "Coder":
            outputs["Coder"] = coder(outputs["Planner"], outputs["Researcher"], load_prompt("coder"))
        elif current_agent == "Reviewer":
            outputs["Reviewer"] = reviewer(outputs["Coder"], load_prompt("reviewer"))
        elif current_agent == "Orchestrator":
            orchestrator(outputs, load_prompt("orchestrator"))
