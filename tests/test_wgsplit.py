import pytest
from wg_split import parse_amount, split_expenses


@pytest.mark.parametrize(
    "amount_str, expected_cents",
    [
        ("12.50", 1250),
        ("0.01", 1),
        ("100.00", 10000),
        ("33.33", 3333),
    ],
)
def test_parse_amount(amount_str, expected_cents):
    assert parse_amount(amount_str) == expected_cents


@pytest.mark.parametrize(
    "amount_str, error_match",
    [
        ("-50", "negative"),
        ("12.500", "decimal"),
        ("abc", "invalid"),
    ],
)
def test_parse_amount_errors(amount_str, error_match):
    with pytest.raises(ValueError, match=error_match):
        parse_amount(amount_str)


def test_split_one_payer():
    # anna 100, chris 0, lucia 0
    # → chris pays anna €33.33 / lucia pays anna €33.33
    rows = [("anna", 10000), ("chris", 0), ("lucia", 0)]
    result = split_expenses(rows)
    assert ("chris", "anna", 3333) in result
    assert ("lucia", "anna", 3333) in result


def test_split_two_payers():
    # anna 50, lucia 50, chris 0
    # → chris pays anna €16.66 / chris pays lucia €16.66
    rows = [("anna", 5000), ("lucia", 5000), ("chris", 0)]
    result = split_expenses(rows)
    assert ("chris", "anna", 1666) in result
    assert ("chris", "lucia", 1666) in result


def test_split_even():
    # anna 30, chris 30, lucia 30 → nobody owes anything
    rows = [("anna", 3000), ("chris", 3000), ("lucia", 3000)]
    result = split_expenses(rows)
    assert result == []


def test_empty_raises():
    with pytest.raises(ValueError, match="no expenses"):
        split_expenses([])


def test_names_case_insensitive():
    # ANNA and anna are the same person → 2 people: anna, chris
    # anna total = 10000, share = 10000 // 2 = 5000
    rows = [("ANNA", 6000), ("anna", 4000), ("chris", 0)]
    result = split_expenses(rows)
    assert ("chris", "anna", 5000) in result


def test_output_lowercase():
    # ANNA 50, Chris 50 → output uses lowercase
    rows = [("ANNA", 5000), ("Chris", 5000), ("lucia", 0)]
    result = split_expenses(rows)
    for payer, payee, _ in result:
        assert payer == payer.lower()
        assert payee == payee.lower()
