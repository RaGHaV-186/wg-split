# ai-dev-workflow

A template repo that every new project starts from, with guardrails built in:

- **uv** project on Python 3.14
- **ruff** (lint + format) and **gitleaks** (secret scanning) run by **pre-commit** on every commit
- `.env` is gitignored, and Claude Code is denied from reading it (`.claude/settings.json`)
- `.env.example` documents the required variables with fake placeholders
- Decisions are recorded as ADRs in `docs/adr/`

## Start a new project from it

1. Create the project from this template:
   ```
  gh repo create my-project --template RaGHaV-186/ai-dev-workflow --public --clone
   cd my-project
   ```
   (or click **Use this template** on GitHub)
2. Install dependencies and the git hooks:
   ```
   uv sync
   uv run pre-commit install
   ```
3. Create your local env file and fill in real values (never commit it):
   ```
   cp .env.example .env
   ```
4. Check everything works:
   ```
   uv run ruff check
   uv run pre-commit run --all-files
   ```
