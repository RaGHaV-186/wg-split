# ADR-0004: Store money as integer cents

## Context

wg-split reads euro amounts from CSV, splits them among flatmates, and prints who pays whom.

## Options

1. float — fast but inexact; binary rounding causes drift
2. Decimal — exact; more verbose; requires string construction
3. Integer cents — store €12.50 as 1250; all arithmetic on whole numbers

## Decision

Integer cents. All splitting math stays on integers (no drift). Convert only at boundaries: parse on input, format on output.

## Consequences

- No rounding errors in arithmetic
- Same approach as Stripe, PayPal
  − Must parse and format at boundaries
