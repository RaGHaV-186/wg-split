# ADR-0003: wg-split is a CLI, not a web app

## Context

Split shared-flat expenses from a CSV and print who pays whom.
3 flatmates, used about once a month. Today's learning goals:
CLAUDE.md, plan mode, tests.

## Options

- A. CLI: ~1 session, €0, runs locally, only the runner needs a terminal
- B. Web app: ~3–5 sessions (UI, upload, hosting), anyone with a link can use it

## Decision

CLI. All 3 flatmates need the _result_, not the tool: one person
runs it and posts the output to the WG group. A web app would spend
most of the time on UI instead of the money logic. (YAGNI)

## Consequences

- Pro: small scope, fast to test, matches today's goals
- Con: flatmates can't enter expenses themselves
- Two-way door: the split logic can get a web UI later
- Revisit when: flatmates want to add expenses themselves
- Future (not scheduled): per-item splits → web app with bill upload
- Rejected for now: in-app bank payments (PSD2 licensing, real
  financial data). If needed, use a payment QR code / PayPal.me link
