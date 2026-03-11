# RealEstate Investment Assistant

An AI-powered assistant that helps general contractors discover and evaluate real estate investment opportunities in Quebec, Canada.

## What It Does

- Search and filter Quebec property listings (Centris / MLS)
- Estimate renovation scope and cost from listing data
- Model investment returns: cap rate, cash-on-cash, GRM, flip vs. hold scenarios
- Provide AI-driven analysis tailored for general contractors

## Stack

| Layer      | Technology                     |
|------------|-------------------------------|
| Backend    | Python 3.12 + FastAPI          |
| Frontend   | React + Vite (TypeScript)      |
| AI Engine  | Claude API (claude-sonnet-4-6) |
| Database   | PostgreSQL                     |
| Listings   | Centris / Quebec MLS           |

## Development Principles

- **Strict TDD**: Red → Green → Refactor. No production code without a test.
- **Clean Code**: Single responsibility, descriptive names, no magic values, max 20 lines per function.
- **Layered architecture**: API → Service → Repository.

See [CLAUDE.md](CLAUDE.md) for full AI governance rules and development workflow.

## Custom Skills

| Command        | Purpose                                      |
|---------------|----------------------------------------------|
| `/tdd-cycle`  | Walk through Red → Green → Refactor          |
| `/clean-check`| Review code for clean code violations        |
| `/feature`    | Scaffold a new feature with full TDD workflow |

## Getting Started

> Backend and frontend scaffolding coming in Iteration 1.

## Project Status

See `memory/iterations.md` for the feature log and current iteration status.
