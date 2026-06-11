# agent-redline-python-demo — greenfield

Bare FastAPI service in hexagonal layout. **No** `agent-policy.yaml`,
**no** `AGENTS.md`, **no** import-linter contracts beyond the inherited
`pyproject.toml` block, **no** CI workflow.

This branch is the starting point for testing **agent-redline bootstrap mode**
on a Python repo. Drop the agent-redline skill into a Claude Code or Codex
session pointed at a checkout of this branch, ask the agent to set up
agent-redline, and observe what it produces.

The expected output is roughly what the `main` branch already has.
