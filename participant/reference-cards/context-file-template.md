# Context File Template (CLAUDE.md / .cursorrules / copilot-instructions.md)

<!--
  HOW TO USE THIS FILE
  ====================
  This is a fill-in-the-blank context file. Copy it to the root of your project
  (or to ~/.claude/CLAUDE.md for global settings) and fill in every section.

  Why this matters: the agent reads this file at the start of every session.
  A good context file cuts hallucinations, prevents unwanted changes, and saves
  you from repeating yourself on every prompt.

  Tool-specific filenames:
    Claude Code   →  CLAUDE.md  (project root or ~/.claude/CLAUDE.md for global)
    Cursor        →  .cursorrules  (project root)
    GitHub Copilot→  .github/copilot-instructions.md
    Continue.dev  →  .continuerc.json  (use "systemMessage" field)

  Delete all comment blocks (HTML comments like this one) before committing.
-->

---

## Project Overview

<!--
  2–4 sentences. What does this project do, who uses it, and what problem does it solve?
  The agent uses this to understand intent — it will make better decisions on ambiguous
  tasks if it understands the "why" behind the project.
-->

This is {{ PROJECT_NAME }}, a {{ TYPE_OF_PROJECT }} that {{ WHAT_IT_DOES }}.

The primary users are {{ TARGET_USERS }}. The core problem it solves is {{ PROBLEM }}.

Current status: {{ alpha | beta | production }} — {{ any_relevant_context_about_stability }}.

---

## Tech Stack

<!--
  List every technology the agent might encounter. Be specific about versions where
  they affect API behavior (e.g., .NET 8 vs .NET 9, React 18 vs 19).
  The agent will use this to choose the right APIs and avoid deprecated patterns.
-->

**Language(s):** {{ e.g., TypeScript 5.4, C# 12 }}
**Runtime / Framework:** {{ e.g., Node 22, ASP.NET Core 8, Angular 18 }}
**Database:** {{ e.g., PostgreSQL 16 via Entity Framework Core 8 }}
**Infrastructure:** {{ e.g., Azure App Service, GitHub Actions }}
**Key Libraries:**
- {{ LIBRARY_1 }} — {{ what it's used for }}
- {{ LIBRARY_2 }} — {{ what it's used for }}
- {{ LIBRARY_3 }} — {{ what it's used for }}

**Package Manager:** {{ npm | pnpm | yarn | NuGet | pip }}
**Test Framework:** {{ xUnit | pytest | Jasmine | Playwright }}

---

## Coding Conventions

<!--
  Document the patterns the agent must follow. Be explicit — do not assume the
  agent will infer your conventions from existing code. The more specific, the better.
-->

**Naming:**
- {{ e.g., "PascalCase for classes and methods. _camelCase for private fields." }}
- {{ e.g., "kebab-case for file names in TypeScript." }}

**File Organization:**
- {{ e.g., "One class per file. Files live in the layer they belong to (Services/, Controllers/, etc.)." }}
- {{ e.g., "Max 400 lines per file. Split before you hit the limit." }}

**Error Handling:**
- {{ e.g., "Use Result<T> for expected failures. Throw exceptions only for truly exceptional conditions." }}

**Immutability:**
- {{ e.g., "No mutation of objects or arrays. Use spread operators in TypeScript." }}

**Code Style:**
- {{ e.g., "No console.log. Use the logger service." }}
- {{ e.g., "Max function length: 50 lines. Extract if it grows beyond that." }}
- {{ e.g., "No deep nesting. Max 4 levels." }}

---

## What NOT To Do

<!--
  This is the most important section for preventing unwanted behavior.
  Be explicit about anti-patterns, off-limits areas, and things the agent
  tends to do that you don't want.
-->

- **Never** hardcode secrets, API keys, or connection strings.
- **Never** use `{{ BANNED_PATTERN_1 }}` — use `{{ PREFERRED_ALTERNATIVE_1 }}` instead.
- **Never** modify `{{ OFF_LIMITS_FILE_OR_DIRECTORY }}` without explicit instruction.
- **Never** add dependencies without asking first.
- **Do not** refactor code that is not related to the current task.
- **Do not** add comments that restate what the code obviously does.
- **Do not** create wrapper abstractions for one-time operations.
- {{ ADD_YOUR_OWN_RULES }}

---

## Preferred Patterns

<!--
  Show the agent the patterns you want it to copy. Short examples are more
  effective than long prose descriptions.
-->

**Preferred: {{ PATTERN_NAME_1 }}**
```{{ LANGUAGE }}
{{ GOOD_EXAMPLE_1 }}
```

**Avoid: {{ ANTI_PATTERN_NAME_1 }}**
```{{ LANGUAGE }}
{{ BAD_EXAMPLE_1 }}
```

---

**Preferred: {{ PATTERN_NAME_2 }}**
```{{ LANGUAGE }}
{{ GOOD_EXAMPLE_2 }}
```

---

## Autonomy Rules

<!--
  Tell the agent exactly how much authority it has. This is the single biggest
  factor in preventing unwanted large changes. Three tiers work well:

  GREEN  — Do it without asking.
  YELLOW — Propose a plan first, then execute after I confirm.
  RED    — Always ask. Never assume. Stop and wait.
-->

### Green — Just Do It

- Fix lint errors, type errors, and broken imports
- Run tests and report results
- Single-function bug fixes with an obvious cause
- Reading files to understand context
- {{ ADD_YOUR_OWN_GREEN_RULES }}

### Yellow — Propose First, Then Execute

- Changes that touch more than 2 files
- Adding new files or directories
- Adding or upgrading dependencies
- Changes to build or CI configuration
- {{ ADD_YOUR_OWN_YELLOW_RULES }}

### Red — Always Ask, Never Assume

- Deleting any file, record, or data
- Changes to `{{ CRITICAL_CONFIG_OR_INFRA }}`
- Anything touching authentication, payments, or user PII
- Rewriting working code that is not broken
- Expanding scope beyond what was explicitly requested
- {{ ADD_YOUR_OWN_RED_RULES }}

---

## Testing Standards

<!--
  Tell the agent what a passing test looks like in this project.
  The more specific you are, the less it will make up test patterns.
-->

**Framework:** {{ xUnit | pytest | Jasmine | Playwright }}
**Minimum coverage:** {{ 80 }}% on new code
**Naming convention:** {{ e.g., "MethodName_Scenario_ExpectedResult for C#" }}
**Test file location:** {{ e.g., "tests/ directory mirroring src/ structure" }}

**What to mock:**
- External HTTP calls — always mock
- The system clock — always mock via `TimeProvider` or equivalent
- Database — prefer in-memory / test database over mocking the ORM

**What NOT to mock:**
- The class or function under test
- Value objects and DTOs
- Internal services you control

**Before a bug fix is done:**
1. Write a failing test that reproduces the bug
2. Fix the code until the test passes
3. The fix is not done until the test passes

---

## Additional Notes

<!--
  Anything else the agent needs to know: team conventions, architecture decisions,
  known tech debt to avoid, external system quirks, etc.
-->

- {{ ADDITIONAL_NOTE_1 }}
- {{ ADDITIONAL_NOTE_2 }}
