import json

# Load workflow definition
with open("workflows/generic-orchestration.json", "r") as f:
    workflow = json.load(f)

# Simulated agent functions
def planner(user_request):
    return [
        "Set up project scaffold",
        "Implement CRUD operations",
        "Add authentication",
        "Document API with Swagger"
    ]

def researcher(tasks):
    return {
        "Spring Boot": "Robust framework, easy integration",
        "JWT": "Secure authentication, widely used",
        "Swagger": "Interactive API docs, developer-friendly"
    }

def coder(tasks, recommendations):
    return {
        "Task.java": "Entity with id, title, description, completed",
        "TaskController.java": "REST endpoints for CRUD",
        "SecurityConfig.java": "JWT filter applied"
    }

def reviewer(code_output):
    return {
        "Entity": "✅ Correct fields",
        "Controller": "⚠️ Missing error handling",
        "Security": "✅ JWT implemented"
    }

def orchestrator(outputs):
    print("\n=== Final Integrated Solution ===")
    for agent, output in outputs.items():
        print(f"\n[{agent} Output]")
        print(output)

# Simulate workflow
if __name__ == "__main__":
    user_request = "Build a Task Manager API"
    outputs = {}

    outputs["Planner"] = planner(user_request)
    outputs["Researcher"] = researcher(outputs["Planner"])
    outputs["Coder"] = coder(outputs["Planner"], outputs["Researcher"])
    outputs["Reviewer"] = reviewer(outputs["Coder"])
    orchestrator(outputs)
