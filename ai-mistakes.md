# AI Mistakes Log

One entry per mistake. Format: date · category · what happened · how I caught it.

Categories: wrong-diagnosis · unrequested-decision · partial · hallucination · data · agent · other

---

## Day 2 · Wed 28 Oct 2026

**wrong-diagnosis** · Agent blamed a sandbox for a failed download. `/sandbox` showed it was off. Real cause was the phone hotspot. Lesson: an agent's explanation is a hypothesis, not a fact.

**unrequested-decision** · No context given → agent guessed ADR topics wrong and used `ANTHROPIC_API_KEY` in `.env.example` instead of a neutral placeholder.

**unrequested-decision** · README defaulted new projects to `--private` without being asked.

**partial** · Agent planned to run the Judge test itself instead of letting me do it.

**partial** · Refused `.env` by choice at first; only an explicit test proved the hook actually enforces it.

---

## Day 3 · Sat 07 Nov 2026

**partial** · "Revision" reworded the float problem instead of fixing it (`cents/100:.2f` → "formatted from integer cents"). Required an explicit follow-up instruction.

**unrequested-decision** · Picked the money type (Decimal vs float) — that was Day 4's decision to make.

**other** · VS Code formatter on save mangled the ADR Consequences list.

**other** · Template copied `ai-dev-workflow`'s SPEC.md into wg-split unchanged.
