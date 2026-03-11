---
name: tdd-cycle
description: Walk through Red → Green → Refactor for a specific feature or function
argument-hint: <feature or function to test>
---

Walk me through a strict TDD cycle for the following feature: $ARGUMENTS

Follow this exact sequence and do not skip steps:

## STEP 1 — RED (Write the failing test)

1. Ask me to describe the expected behavior in plain language if not already clear
2. Identify the unit under test (function, class, or endpoint)
3. Write a test in `backend/tests/` that:
   - Has a descriptive name: `test_<what_it_does>_<expected_result>`
   - Tests one behavior only
   - Uses `pytest` conventions
   - Will FAIL because the implementation does not exist yet
4. Show me the test and confirm it fails before writing any production code

## STEP 2 — GREEN (Minimum implementation)

1. Write the minimum production code in `backend/app/` to make the test pass
2. Do not over-engineer — only what the test requires
3. Run the test and confirm it is GREEN
4. Do not refactor yet

## STEP 3 — REFACTOR (Improve without breaking)

1. Review the production code for:
   - Functions longer than 20 lines → extract
   - Magic numbers/strings → extract to constants
   - Duplicated logic → extract to shared function
   - Naming clarity → rename if needed
2. Apply changes while keeping tests GREEN
3. Run the full test suite to confirm nothing is broken

## STEP 4 — CHECKPOINT

- [ ] Test written before code (RED confirmed)
- [ ] Test passes (GREEN confirmed)
- [ ] Code is clean (REFACTOR done)
- [ ] No hardcoded values
- [ ] Type hints present
- [ ] Ready for next cycle or commit
