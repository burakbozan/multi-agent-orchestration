# Copilot instructions

## Build, run, and validate

There is no build system, dependency manifest, test suite, or linter configured. The demo uses only the Python standard library.

- Run the demo from the repository root with `python orchestrator.py`.
- Check Python syntax with `python -m py_compile orchestrator.py`.
- No single-test command is available because the repository currently has no tests.

## Architecture

This repository is a prompt-driven orchestration scaffold, not a live multi-agent/LLM integration. `orchestrator.py` loads role prompts from `prompts/`, calls simulated Planner → Researcher → Coder → Reviewer functions in sequence, then passes their outputs to the Orchestrator for display. The functions return illustrative hard-coded data.

`workflows/generic-orchestration.json` describes the intended sequence, but `orchestrator.py` does not read its `steps` to drive execution; the sequence is hard-coded in the script. Keep both representations aligned when changing the workflow, or explicitly implement workflow-driven execution.

`ARCHITECTURE.md` describes the separation between reusable role prompts, workflow definitions, and project examples. The current example is a short workflow outline in `examples/task-manager-api-orchestration.md`.

## Repository conventions

- Role prompt filenames are lowercase role names (`prompts/planner.md`, `prompts/researcher.md`, `prompts/coder.md`, `prompts/reviewer.md`, `prompts/orchestrator.md`). `load_prompt()` derives the filename from the role name.
- Preserve the role boundaries and output contracts in the prompts: Planner decomposes tasks without code; Researcher gives recommendations without code; Coder implements without changing architecture; Reviewer reports a checklist without writing code; Orchestrator integrates agent outputs.
- Prompt and workflow locations are relative to the process working directory. Run the demo from the repository root; if changing how it is launched, ensure those paths still resolve.
- Treat the Python agent functions as replaceable simulation points. The current sample request, returned tasks/recommendations/code/review, and Java-oriented output are illustrative, not general workflow logic.
