# ADR-0005: Branching workflow for wg-split

## Context

I push straight to main today (e.g. 84291eb on Day 4). Nothing stands
between a commit and main except the pre-commit hook, which can be
skipped with --no-verify and doesn't run tests. Most of wg-split's
code is written by an AI agent, so I need a fixed point where I review
its changes before they land.

## Options

- A. Straight to main: fastest, no gate, nobody checks.
- B. Trunk-based: short-lived branch → small PR → CI → merge the same day.
- C. Long-lived branches (GitFlow): branches live weeks, big merges,
  conflicts; only worth it for scheduled releases.

## Decision

B. Every change goes through a small PR. I read the full diff before
merging, and CI must be green. Short branches also avoid the merge
conflicts that long-lived branches cause. It is also the workflow
most companies use, so I practise it now.

## Consequences

Good:

- CI can't be skipped and runs on a clean machine (catches
  "works on my machine" bugs, e.g. a dependency missing from pyproject.toml).
- Every AI change is reviewed before it reaches main.

Cost:

- ~2–5 min extra per change (branch, PR, wait for CI).

Door: two-way. I can go back to pushing to main any time.
