# RealEstate Investment Assistant — AI Governance

## Project Overview

An AI-powered assistant that helps general contractors discover and evaluate real estate investment opportunities in Quebec, Canada. The assistant surfaces listings, estimates renovation costs, and models investment returns to support data-driven acquisition decisions.

## Tech Stack

| Layer      | Technology                     | Rationale                                    |
|------------|-------------------------------|----------------------------------------------|
| Backend    | Python 3.12 + FastAPI          | Async, typed, great for AI integrations      |
| Frontend   | React + Vite (TypeScript)      | Simple, mobile-responsive, industry standard |
| AI Engine  | Claude API (claude-sonnet-4-6) | Primary reasoning and assistant layer        |
| Database   | PostgreSQL                     | Relational, good for property/financial data |
| Listings   | Centris / Quebec MLS API       | Primary Quebec real estate data source       |

## Project Structure

```
realestateproject/
├── CLAUDE.md               # This file — AI governance rules
├── README.md
├── backend/
│   ├── app/
│   │   ├── api/            # FastAPI routers (thin layer — delegates to services)
│   │   ├── services/       # Business logic (listings, analysis, financial models)
│   │   ├── models/         # Pydantic models + SQLAlchemy ORM models
│   │   ├── repositories/   # Data access layer (DB + external APIs)
│   │   └── core/           # Config, constants, dependency injection
│   └── tests/              # Mirrors app/ structure: test_<module>.py
└── frontend/
    ├── src/
    │   ├── components/     # Reusable UI components
    │   ├── pages/          # Route-level pages
    │   ├── services/       # API calls to backend
    │   └── hooks/          # Custom React hooks
    └── tests/
```

---

## AI Development Governance

### 1. Test-Driven Development (STRICT — No Exceptions)

Every feature follows Red → Green → Refactor:

1. **RED**: Write a failing test that defines the expected behavior
2. **GREEN**: Write the minimum code required to make the test pass
3. **REFACTOR**: Improve structure and readability — tests must still pass

Rules:
- No production code without a corresponding test
- Tests live in `backend/tests/` mirroring `backend/app/` structure
- Use `pytest` with `pytest-asyncio` for async FastAPI tests
- Use `/tdd-cycle` skill to guide each feature cycle

### 2. Clean Code Standards

**Functions and methods:**
- Max 20 lines per function — if longer, extract smaller functions
- Single Responsibility: one function does one thing
- Descriptive names — no abbreviations (`property_price` not `pp`, `listing_id` not `lid`)
- Type hints on all Python functions and return values

**Structure:**
- SOLID principles enforced throughout
- DRY: extract shared logic — never copy-paste code
- No magic numbers or strings — use constants (`MAX_RESULTS = 20`) or enums
- Max cyclomatic complexity: 5 per function

**Boundaries:**
- Validate external input at system boundaries (API endpoints, external API responses)
- Do not add defensive checks for internal code you control
- Error handling only where recovery is possible

### 3. Commit Conventions

```
feat:      new user-facing feature
fix:       bug fix
test:      add or update tests
refactor:  code improvement with no behavior change
docs:      documentation only
chore:     tooling, config, dependencies
```

Always run tests before committing: `pytest backend/tests/`

### 4. Code Review Checklist

Before considering any task done:
- [ ] Failing test written first (RED phase documented)
- [ ] Tests pass (GREEN confirmed)
- [ ] Code refactored for clarity (REFACTOR done)
- [ ] No hardcoded values — constants or config used
- [ ] Functions are small and focused (< 20 lines)
- [ ] Type hints present on all new functions
- [ ] No copy-pasted logic

---

## Skills (Slash Commands)

Use these custom skills during development:

- `/tdd-cycle` — Walk through Red → Green → Refactor for a new feature
- `/clean-check` — Review staged code for clean code violations
- `/feature` — Start a new feature with full TDD scaffolding

---

## Memory System

Claude maintains persistent memory for this project at:
`.claude/projects/.../memory/`

- `MEMORY.md` — Current project state, active decisions, what was last worked on
- `architecture.md` — Architecture decisions and rationale (ADRs)
- `iterations.md` — Completed feature log with notes

**Protocol:**
- At session start: read MEMORY.md to restore context
- After significant work: update the relevant memory file
- After architectural decisions: log to architecture.md with rationale

---

## Quebec Real Estate Context

- **Primary data source**: Centris (Quebec MLS) — covers all major Quebec markets
- **Currency**: CAD
- **Key investment metrics**:
  - Cap rate (Net Operating Income / Property Value)
  - Cash-on-cash return
  - Gross Rent Multiplier (GRM)
  - Renovation cost estimate (contractor's domain expertise)
- **Target user**: General contractors evaluating properties for investment or flip
- **Key use cases**:
  1. Search and filter listings by investment criteria
  2. Estimate renovation scope and cost from listing data/photos
  3. Model projected returns (flip vs. hold scenarios)
  4. Flag off-market opportunities based on permit/tax data (future)
