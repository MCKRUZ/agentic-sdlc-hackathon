# M03: Project Context Files — Slide Outline
**Module duration:** 20 minutes (includes live demo)
**Slide count:** 8

---

## Slide 1: The Generic Output Problem

The agent writes code that works but doesn't match your codebase:
- Wrong error handling pattern
- console.log instead of your logger
- Route files structured differently from everything else

This isn't a bug. The agent is using general knowledge, not your conventions.
The fix: write your conventions down where the agent reads them.

Speaker note: Ask if anyone hit this during the exercises. If yes, use their specific example. Real friction makes the point better than a hypothetical.

---

## Slide 2: Context Files by Tool

| Tool | File name | Where it lives |
|---|---|---|
| Claude Code | CLAUDE.md | Project root or ~/.claude/ |
| Cursor | .cursorrules | Project root |
| Custom / API | System prompt | Injected at session start |

Same concept, different names. One file. Read every session. Applies to everything.

Think of it as your onboarding doc for a contractor with no memory between visits.

Speaker note: Emphasize "no memory between visits." That's the reason the file needs to be complete enough to stand alone without prior conversation context.

---

## Slide 3: What Context Files Are Not

- Not a chat message (you're giving instructions, not asking questions)
- Not a one-time setup (every session reads it fresh)
- Not a replacement for good task prompts (defaults vs. per-task overrides)

They set the floor. Individual prompts raise or restrict within that floor for a specific task.

Speaker note: The "every session reads it fresh" point prevents a common mistake: people write the file once and forget about it. If your conventions evolve, so should the file.

---

## Slide 4: What to Put In — Foundations

Start with these three sections:

**1. Tech stack** — exact versions, actual libraries in use
- "Node 20, Express 4, TypeScript 5, Prisma + Postgres, Jest, Pino"

**2. Persona / role** — how the agent should behave
- "You are a backend engineer on this team. Match the existing code style."

**3. Error handling pattern** — the single most common source of inconsistency
- Name the specific pattern and where it lives in the codebase

Speaker note: Don't skip the tech stack. "Guess the ORM" failures are common and frustrating. List the exact packages you use.

---

## Slide 5: What to Put In — Conventions and Prohibitions

**Coding conventions** — specific beats vague:
- Bad: "Follow clean code principles."
- Good: "Handle all errors via Result<T> in src/types/result.ts. Never throw from service functions. Use src/services/logger.ts, not console.log."

**Explicit prohibitions** — often more valuable than positive instructions:
- "Do not add npm dependencies without asking."
- "Do not modify src/auth."
- "Do not create utility files outside src/utils."

Speaker note: Ask the room: "What's the last thing you corrected in a code review?" That's what goes in prohibitions. The agent can't infer what you don't want from what you have.

---

## Slide 6: What to Put In — Workflow and Autonomy

**Workflow rules:**
- "Run the test suite after every change."
- "Fix failing tests before reporting done."
- "Write tests for all new public functions."

**Autonomy config:**
- Green (act freely): read files, run tests, fix lint
- Yellow (ask first): install packages, create directories, modify config
- Red (never): delete files, destructive operations

Speaker note: Workflow rules are acceptance criteria baked in at project level. You write them once instead of putting them in every prompt. This is high leverage.

---

## Slide 7: Three Levels of Scope

**Global** — applies to every project
- Your personal preferences, communication style
- Lives in your home directory / user config

**Project** — applies to one repo
- Tech stack, conventions, workflow rules
- Committed to version control, shared with the team

**Folder** — applies to a specific subdirectory
- Useful in monorepos with divergent conventions per package

Start with project-level. Get it right before adding the others.

Speaker note: Emphasize that the project context file should be in version control. It's code. Review it in PRs. A silent change to the context file can degrade an entire team's agent output.

---

## Slide 8: Live Demo — DevBoard CLAUDE.md

[DEMO CUE] Open DevBoard's CLAUDE.md. Walk through each section.

Then:
1. Run a prompt with CLAUDE.md in place
2. Temporarily rename the file so the agent can't find it
3. Run the same prompt again
4. Show the diff in output quality

The contrast is the point. No narration needed.

**Exercise:** Write a CLAUDE.md for DevBoard from scratch, then compare with the shipped version.

Speaker note: The exercise works best if people do it before seeing the shipped file. If they write it first, the comparison reveals what they missed. If they read it first, they just copy it.
