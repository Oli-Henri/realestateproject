---
name: feature
description: Scaffold a new feature with full TDD workflow (user story → interface → tests → cycles → commit)
argument-hint: <feature-name>
---

Start a new feature: $ARGUMENTS

This command scaffolds a complete TDD-driven feature following project conventions.

## STEP 1 — Define the Feature

Confirm or clarify:
1. **Feature name**: what it's called (used for file naming)
2. **User story**: "As a [contractor], I want to [action] so that [value]"
3. **Acceptance criteria**: list of testable conditions that define "done"
4. **Layer(s) involved**: API endpoint / Service / Repository / Frontend component

## STEP 2 — Design the Interface First

Before writing any code, define:
- Function signatures with type hints
- Request/Response Pydantic models (if API)
- Expected inputs and outputs for each layer

Show the interface design and wait for confirmation.

## STEP 3 — Scaffold Test Files

Create the test file(s) in `backend/tests/` mirroring the app structure:
- One test file per module being tested
- Use descriptive class grouping if multiple scenarios
- Write test stubs (function names only, with `pass`) for all acceptance criteria

## STEP 4 — Run TDD Cycle

For each acceptance criterion, run `/tdd-cycle` to:
1. Implement the test (RED)
2. Write minimum code (GREEN)
3. Refactor (REFACTOR)

## STEP 5 — Integration Check

Once all unit tests pass:
1. Write an integration test if the feature touches an API endpoint
2. Confirm the full test suite passes: `pytest backend/tests/`
3. Run `/clean-check` on all new files

## STEP 6 — Update Memory

After the feature is complete, update:
- `memory/MEMORY.md` — current project state
- `memory/iterations.md` — log the completed feature

## STEP 7 — Commit

Stage and commit following conventions:
```
feat: <short description of what the feature does>
```
