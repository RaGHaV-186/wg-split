import csv
import sys

from wg_split.core import parse_amount, split_expenses


def _format(cents: int) -> str:
    return f"€{cents // 100}.{cents % 100:02d}"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("Usage: wg-split expenses.csv", file=sys.stderr)
        return 2

    rows = []
    with open(args[0], newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # header
        for line_no, row in enumerate(reader, start=2):
            name, _category, amount = row
            try:
                rows.append((name, parse_amount(amount)))
            except ValueError as e:
                print(f"Error: line {line_no} has {_describe(e)}", file=sys.stderr)
                return 1

    try:
        payments = split_expenses(rows)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not payments:
        print("Nobody owes anything.")
    for debtor, creditor, cents in payments:
        print(f"{debtor} pays {creditor} {_format(cents)}")
    return 0


def _describe(e: ValueError) -> str:
    msg = str(e)
    if msg.startswith("negative"):
        return "a negative amount"
    return f"an {msg}"


if __name__ == "__main__":
    sys.exit(main())
