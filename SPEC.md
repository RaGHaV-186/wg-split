# ai-dev-workflow — spec

Goal: a template repo every project starts from, with guardrails built in.

## Done when
1. Repo `ai-dev-workflow` exists on GitHub, visibility: public because its part of portfolio
2. uv project, Python version: 3.14 because of using the n-1 rule as 3.15 is the latest release 
3. `ruff check` runs and passes
4. pre-commit runs ruff + gitleaks on every commit
5. `.gitignore` includes `.env`
6. `.env.example` with fake placeholder values is committed
7. Claude Code is not allowed to read `.env`
8. ADR-0001 and ADR-0002 are in `docs/adr/`
9. README.md explains what this repo is for and how to start a new project from it

## Test (the Judge step)
Commit a fake API key on purpose → the commit must be blocked.

## Not in scope today
CI (Day 5), tests (Day 4), CLAUDE.md (Day 3)