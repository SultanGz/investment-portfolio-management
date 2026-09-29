# Agent conventions and safety boundaries

This file guides automated agents working in this repository.

## Project conventions

- Python code lives under `src/investment_portfolio/`. Tests live under `tests/`.
- Keep runtime dependencies minimal; add new dependencies only after checking `pyproject.toml`.
- Use Ruff for linting/formatting and pytest for tests. Run `ruff check .`, `ruff format --check .`, and `pytest` before opening a PR.
- Prefer pure-Python, deterministic utilities in Phase 1. Do not invent financial data, performance claims, or investment advice.
- Configuration is intentionally minimal; do not add cloud credentials, secrets, or deployment targets unless explicitly requested.

## Safety boundaries

- Do not commit real credentials, API keys, or personally identifiable financial data.
- Do not execute, deserialize, or upload opaque model artifacts or datasets unless requested and the format is understood.
- Keep analysis and changes read-only by default. Permitted writes follow the repo's MLOps lifecycle policy (e.g., MLflow dev runs, feature branches, draft PRs).
- Do not merge pull requests, deploy to production, or modify repository security settings.
- Never disable or weaken CI checks to bypass failures; report failures and propose fixes.
