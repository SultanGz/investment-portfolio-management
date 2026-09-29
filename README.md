# Investment Portfolio Management (Phase 1)

This repository is the beginning of an MLOps-friendly investment portfolio management project. Phase 1 establishes a reproducible Python package skeleton, automated linting and testing, and project conventions.

## Project purpose

Provide a maintainable foundation for portfolio analytics and (in later phases) machine-learning experiments. This phase intentionally contains only small, pure-Python utilities and does not include financial data, trained models, deployment pipelines, or production configuration.

## Setup

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -e ".[dev]"
```

## Run checks

```bash
ruff check .
ruff format --check .
pytest
```

## Project structure

```
src/investment_portfolio/   # Source package
tests/                      # pytest suite
.github/workflows/ci.yml    # GitHub Actions CI
pyproject.toml              # Project metadata and tool config
AGENTS.md                   # Agent conventions and safety boundaries
```

## CI

GitHub Actions runs Ruff and pytest on every push and pull request to `main`.
