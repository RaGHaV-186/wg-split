# ADR-0002: Where secrets live

## Context
Code runs in several places: laptop, GitHub Actions, Vercel, AWS.
Each needs API keys. Solo developer, budget ≤ €25/month.
A leaked key can cost money before a budget alarm fires.

## Options
A. .env file (local): free, simple, readable by anything on my laptop
B. Platform secrets (GitHub secrets, Vercel env vars): free, encrypted, scoped to that platform
C. Secrets manager (AWS Secrets Manager / Parameter Store): $0.40/secret/month or free (SSM), audit log, rotation

## Decision
Keep each secret where the code runs:
- Laptop: .env, because only my machine runs it
- GitHub Actions: no secrets, because CI only runs ruff and tests that call no API
- Vercel: Vercel env vars, because Vercel runs the code and can hand it the key directly
- AWS: Parameter Store / Secrets Manager, because AWS already knows my app, so no key sits in a file

## Consequences
+ €0 now; no secret needed just to fetch another secret
+ CI stays secret-free, so nothing to leak there
- Same key copied in several places; must update each when rotating
- .env is plain text on my laptop; relies on gitignore + hook + deny rule
Reversibility: two-way door.
