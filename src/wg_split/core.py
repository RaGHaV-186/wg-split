from decimal import Decimal, InvalidOperation


def parse_amount(text: str) -> int:
    """Parse a decimal money string into integer cents."""
    try:
        d = Decimal(text.strip())
    except InvalidOperation:
        raise ValueError(f"invalid amount: {text!r}") from None
    if not d.is_finite():
        raise ValueError(f"invalid amount: {text!r}")
    if d < 0:
        raise ValueError("negative amount")
    exponent = d.as_tuple().exponent
    if exponent < -2:
        raise ValueError("invalid amount (too many decimal places)")
    return int(d.scaleb(2))


def split_expenses(rows: list[tuple[str, int]]) -> list[tuple[str, str, int]]:
    """Return (debtor, creditor, cents) payments that settle all expenses."""
    if not rows:
        raise ValueError("no expenses in file")

    rows = [(name.strip().lower(), cents) for name, cents in rows]
    people = sorted({name for name, _ in rows})
    n = len(people)

    net = dict.fromkeys(people, 0)
    for payer, cents in rows:
        share = cents // n
        for person in people:
            if person != payer:
                net[person] -= share
                net[payer] += share

    debtors = [[p, -v] for p, v in sorted(net.items()) if v < 0]
    creditors = [[p, v] for p, v in sorted(net.items()) if v > 0]

    payments = []
    ci = 0
    for debtor in debtors:
        while debtor[1] > 0 and ci < len(creditors):
            creditor = creditors[ci]
            paid = min(debtor[1], creditor[1])
            payments.append((debtor[0], creditor[0], paid))
            debtor[1] -= paid
            creditor[1] -= paid
            if creditor[1] == 0:
                ci += 1
    return payments
