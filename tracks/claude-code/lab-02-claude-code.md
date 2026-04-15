# Lab 02 — Claude Code: Write Your Context File

This is the Claude Code variant of Lab 02. CLAUDE.md is Claude Code's native mechanism for persistent instructions. This lab walks you through creating one that actually changes Claude Code's behavior.

---

## Where CLAUDE.md Lives

Claude Code looks for CLAUDE.md files in three places. All three can exist at the same time.

**Global** (`~/.claude/CLAUDE.md`):
- Windows: `C:\Users\<you>\.claude\CLAUDE.md`
- macOS/Linux: `~/.claude/CLAUDE.md`
- Applies to every project on your machine
- Use this for personal preferences, your preferred tools, and conventions you want everywhere

**Project root** (`.claude/CLAUDE.md` or `CLAUDE.md` in the repo root):
- Applies to everyone who works on the project
- Commit this file to git so your whole team gets it
- Use this for project-specific conventions, architecture notes, and required commands

**Subdirectory** (e.g., `src/api/CLAUDE.md`):
- Applies only when Claude Code is working in that subdirectory
- Useful for monorepos where different parts have different conventions

---

## How Claude Code Reads and Prioritizes Them

Claude Code loads all three levels at startup and merges them. The priority order is:

1. Subdirectory CLAUDE.md (most specific, wins on conflicts)
2. Project root CLAUDE.md
3. Global CLAUDE.md (least specific)

If your global file says "use 2-space indentation" but your project file says "use 4-space indentation," Claude Code uses 4 spaces for that project.

Claude Code re-reads CLAUDE.md files when you start a new session. Changes to CLAUDE.md take effect the next time you run `claude`.

---

## Verify Claude Code Is Using Your CLAUDE.md

After creating or editing your CLAUDE.md, restart Claude Code and ask:

```
What do your instructions say about coding conventions?
```

or

```
What tools and frameworks should you use for this project?
```

Claude Code will recite the relevant sections from your CLAUDE.md. If it says "I don't have specific instructions about that," either the file is in the wrong location or it was not loaded. Run `/status` to see which CLAUDE.md files are active.

---

## The Template

Create `.claude/CLAUDE.md` in your project root. Copy this template and fill in the sections for your project:

```markdown
# Project: [Your Project Name]

## What This Project Is
[One paragraph. What does it do? Who uses it? What problem does it solve?]

## Tech Stack
- Runtime: [e.g., Node.js 20, Python 3.12, .NET 8]
- Framework: [e.g., Express, FastAPI, ASP.NET Core]
- Database: [e.g., PostgreSQL, MongoDB, SQLite]
- Test framework: [e.g., Jest, pytest, xUnit]
- Other key libraries: [list them]

## Project Structure
[Describe the top-level directories and what lives in each]
- `src/` — application source code
- `tests/` — unit and integration tests
- `docs/` — documentation
- `scripts/` — build and deployment scripts

## Coding Conventions
- Language: [language and version]
- Indentation: [spaces or tabs, how many]
- Naming: [camelCase, snake_case, PascalCase for what]
- File naming: [kebab-case, camelCase, etc.]
- Max function length: [e.g., 50 lines]
- Max file length: [e.g., 400 lines]

## Key Commands
- Install dependencies: `[command]`
- Run in development: `[command]`
- Run tests: `[command]`
- Build for production: `[command]`
- Lint: `[command]`

## Autonomy Framework
### Do without asking
- Fix lint errors and type errors
- Add missing imports
- Write tests for new code

### Ask before doing
- Adding new dependencies
- Creating new directories or files
- Changing the database schema

### Always ask, never assume
- Deleting files or data
- Changing authentication logic
- Modifying production configuration

## What Good Code Looks Like Here
[2-3 bullet points describing the style you want. Examples:]
- Prefer explicit over clever. A readable 10-line function beats a 2-line one nobody understands.
- Every public function has a unit test.
- Errors surface immediately. No swallowing exceptions.

## Things to Avoid
[Anti-patterns specific to this project]
- Do not use [pattern] because [reason]
- Do not modify [file/area] without discussing it first
```

---

## Claude Code-Specific Sections to Add

Beyond the generic template, add these sections to get more out of Claude Code specifically:

**Preferred tools** (Claude Code will use these when there are options):

```markdown
## Preferred Tools
- Package manager: npm (not yarn, not pnpm)
- Test runner: jest
- Linter: eslint with the project .eslintrc
- Git: use conventional commits format (feat/fix/chore/etc.)
```

**Response style** (controls how Claude Code talks to you):

```markdown
## Response Style
- Be direct. Skip preamble.
- Reference file paths and line numbers when pointing to code.
- When something is wrong, say what is wrong before suggesting a fix.
```

---

## Reference CLAUDE.md in a Prompt with @filename

You can point Claude Code to a specific file using the `@` syntax in your prompt:

```
Review @.claude/CLAUDE.md and tell me if there are any contradictions or gaps before we start working.
```

```
I updated @.claude/CLAUDE.md with new conventions. Apply them to the files in src/api/.
```

The `@filename` syntax works with any file in the project, not just CLAUDE.md. Use it when you want Claude Code to focus on a specific file as part of its instructions for the current prompt.

---

## Checklist Before Moving to the Next Lab

- [ ] Created `.claude/CLAUDE.md` in the project root
- [ ] Filled in the tech stack, commands, and conventions sections
- [ ] Restarted Claude Code (`/exit`, then `claude` again)
- [ ] Asked "what do your instructions say about coding conventions?" and got a correct answer
- [ ] Ran `/status` and confirmed the project CLAUDE.md is listed
