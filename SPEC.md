# wg-split spec

Split shared-flat expenses from a CSV and print who pays whom.

## Done when

1. Running `wg-split expenses.csv` prints one line per payment,
   like `chris pays anna €20.00`.
2. The CSV has a header row and 3 columns: name, category, amount.
   Everyone who shares costs appears at least once; a 0 row is allowed.
3. Each expense is split equally among everyone; leftover cents
   go to the payer's own share. All payments add up to the exact cent.
4. An empty CSV or a negative amount prints a clear error naming the
   problem and line instead of crashing.
5. All tests pass with `uv run pytest`.

## Test cases

1. anna 100, chris 0, lucia 0
   → chris pays anna €33.33 / lucia pays anna €33.33
2. anna -50, chris 29, lucia 25
   → Error: line 2 has a negative amount
3. anna 50, lucia 50, chris 0
   → chris pays anna €16.66 / chris pays lucia €16.66
4. header only, no rows
   → Error: no expenses in file
5. anna 30, chris 30, lucia 30
   → Nobody owes anything.

## Non-goals

- Does not track who has already paid back.
- No web app (see ADR-0003).
- No in-app bank payments.
