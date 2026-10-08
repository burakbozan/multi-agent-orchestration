import json
import os

PROMPTS_DIR = "prompts"
WORKFLOW_FILE = "workflows/generic-orchestration.json"

def load_prompt(agent_name):
    """Load prompt text from the /prompts folder."""
    filename = os.path.join(PROMPTS_DIR, f"{agent_name.lower()}.md")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    return f"No prompt found for {agent_name}"

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
    # Load workflow
    with open(WORKFLOW_FILE, "r") as f:
        workflow = json.load(f)

    user_request = "Build a Task Manager API"
    outputs = {}

    # Run workflow
    outputs["Planner"] = planner(user_request, load_prompt("planner"))
    outputs["Researcher"] = researcher(outputs["Planner"], load_prompt("researcher"))
    outputs["Coder"] = coder(outputs["Planner"], outputs["Researcher"], load_prompt("coder"))
    outputs["Reviewer"] = reviewer(outputs["Coder"], load_prompt("reviewer"))
    orchestrator(outputs, load_prompt("orchestrator"))
