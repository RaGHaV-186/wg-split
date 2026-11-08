# CLAUDE.md

## Project

wg-split: reads expenses.csv and prints who owes whom how much.
Read SPEC.md before any task. It defines "done", test cases and non-goals.

## Stack

Python 3.14, uv, pytest, ruff.

## Commands

- Tests: `uv run pytest`
- Lint: `uv run ruff check .`
- Format: `uv run ruff format .`

## Rules

1. Plan first: show a plan and wait for my approval before writing code.
2. Tests first: I (Raghav) write the tests. You write code until they pass.
   Propose extra tests in the plan; don't add them unasked.
3. Stay in scope: nothing outside SPEC.md. Respect the non-goals.
4. Ask before adding any dependency.
5. Never read, print or create .env files. No secrets in code.
6. Keep changes small; run tests + lint before saying you're done.
