---
name: clean-check
description: Review code for clean code violations (size, naming, magic values, DRY, SOLID)
argument-hint: <file path or code to review>
---

Review the following code (or the files I specify) for clean code violations: $ARGUMENTS

Evaluate against the project standards in CLAUDE.md and report findings in this format:

## Clean Code Review

### Functions & Size
- Flag any function exceeding 20 lines
- Flag functions with more than one clear responsibility
- Suggest extraction points if needed

### Naming
- Flag abbreviations or unclear variable/function names
- Suggest descriptive alternatives
- Check that test names follow: `test_<what>_<expected>`

### Magic Values
- Flag any hardcoded numbers or strings that should be constants or config
- Suggest constant names following SCREAMING_SNAKE_CASE

### DRY Violations
- Flag duplicated logic or copy-pasted blocks
- Suggest shared utility or extracted function

### Type Hints (Python)
- Flag any function missing parameter or return type hints

### Complexity
- Flag functions with cyclomatic complexity > 5
- Suggest simplification (early returns, extracted helpers)

### SOLID Violations
- Flag classes with multiple responsibilities
- Flag tight coupling or missing abstractions

---

## Summary

| Category         | Issues Found | Severity |
|-----------------|-------------|---------|
| Function size    |             |         |
| Naming           |             |         |
| Magic values     |             |         |
| DRY              |             |         |
| Type hints       |             |         |
| Complexity       |             |         |
| SOLID            |             |         |

**Overall**: PASS / NEEDS WORK

List specific file paths and line numbers for every finding.
Then ask: "Should I fix these issues now?"
