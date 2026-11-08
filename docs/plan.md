# Final plan: wg-split (code only; user writes tests on Day 4)

## Scope and approvals
- Approved: `pytest` as dev dependency, `[project.scripts]` entry point, rename project to `wg-split`.
- User writes all tests on Day 4. I write code only, until their tests pass. No test files in this plan.
- Money: integer cents, parsed with `Decimal`. No floats anywhere, including formatting.
- In scope beyond SPEC: same person on several rows nets correctly; amounts with more than 2 decimals are rejected.
- Not handled (deliberately): non-numeric amounts, wrong column count, blank names, missing file. These may still traceback.

## Files
- `pyproject.toml`: name `wg-split`; `[project.scripts] wg-split = "wg_split.cli:main"`; `[build-system]` uv_build; `uv add --dev pytest`.
- `src/wg_split/__init__.py`: empty.
- `src/wg_split/core.py`: pure logic, no I/O: `parse_expenses`, `balances`, `settle`.
- `src/wg_split/cli.py`: `main(argv=None) -> int`.

## Interface for the Day 4 tests
- `wg_split.cli.main(["path/to/expenses.csv"])` returns the exit code.
- Normal output to stdout (`capsys.readouterr().out`). Errors: one line on stderr, exit code 1. Success, including `Nobody owes anything.`, returns 0.

## Parsing and validation
- Header is line 1; rows read in file order; first error stops the run.
- Names: `.strip().lower()`. "Anna" and "anna" are the same person; output uses lowercase names.
- Amount: `Decimal(text)`. Decimals judged as written: more than 2 digits after the point is rejected, so `12.500` is rejected. Error: `Error: line N has more than 2 decimals`.
- Otherwise cents = `int(amount.scaleb(2))` (exact, no floats).
- Check order per row: negative first (`Error: line N has a negative amount`), then decimals.
- No data rows, including a completely empty file: `Error: no expenses in file`.

## Split and rounding
- People = distinct (lowercased) names, n of them. A person with several rows counts once.
- Per row, payer p, `a` cents: `share = a // n`, `leftover = a - share*n`. Everyone else owes p `share`; p's own share is `share + leftover`.
- Balances accumulate per name across all rows (this is what nets repeated people): `net[p] += share*(n-1)`, `net[other] -= share`.
- Nets always sum to 0, so payments add up to the exact cent.

## Settling and output
- Debtors (net < 0) and creditors (net > 0), each sorted by name. Each debtor pays the current creditor `min(debt, credit)` until cleared. Deterministic, not minimal-transaction.
- Nobody owes anything: print `Nobody owes anything.`
- Line: `f"{debtor} pays {creditor} €{c // 100}.{c % 100:02d}"` (integer division and modulo only).

## Done check
- Throwaway CSVs for the 5 SPEC cases plus the two extras, in the scratchpad (not the repo), run through the CLI by hand.
- `uv run ruff check .` and `uv run ruff format .`.
- `uv run pytest` only once the Day 4 tests exist. Don't claim done before they pass.
