# Lab 02: Write Your Context File

**Duration:** 40 minutes
**Track:** All tools

## Objectives

- Establish a baseline for agent output quality on your project without any context
- Write a project context file that shapes agent behavior for your specific codebase
- Measure the improvement by running the same prompt before and after

## What You'll Do

- Run a feature request prompt against your project with no context file and save the output
- Fill out a context file template with your project's conventions and constraints
- Re-run the same prompt and document what changed

## Prerequisites

- Lab 01 complete (you have a working agent session against your project)
- Your project has enough code that a "small new feature" prompt is meaningful (at least a few files)
- A text editor to write and save the context file

---

## Background

AI agents produce dramatically different output depending on what they know about your project upfront. Without guidance, an agent defaults to community conventions: it might use `var` when your team bans it, or write a REST endpoint without the auth middleware your architecture requires. The context file (called `CLAUDE.md` in Claude Code, `.cursorrules` in Cursor, `.github/copilot-instructions.md` in Copilot, and so on) is how you tell the agent what "correct" means for your project.

The goal is not to write a novel. Two pages of specific, opinionated instructions beats ten pages of vague preferences. Focus on what the agent consistently gets wrong, what patterns are non-negotiable, and what it should never do. You will iterate on this file throughout the hackathon as you discover gaps.

---

## Steps

### 1. Run a baseline prompt (no context file)

Make sure there is no context file in your project root. If one exists, move it temporarily:
```bash
mv CLAUDE.md CLAUDE.md.bak   # or whatever your tool uses
```

Start a fresh agent session and run this prompt:
```
Implement a small new feature: add a way for users to export their data as a CSV file.
Implement it following the patterns already in this project.
```

Copy the full agent response to a scratch file or your notes. You'll compare against this later.

**Expected output:** Some amount of code -- probably a new function, route, or component. Note specifically:
- Does it follow your naming conventions?
- Does it use your error handling pattern?
- Does it put files in the right directories?
- Does it add auth/validation where your project requires it?

---

### 2. Create your context file

Create a new file in your project root. The filename depends on your tool -- see your track file for the exact name. If you're unsure, use `CLAUDE.md` (works for Claude Code and is a reasonable default).

Use the template below as your starting point. Fill in every section -- leave none blank. It is better to write "not applicable" than to leave a section empty and have the agent guess.

---

**Context File Template**

```markdown
# Project Context

## What This Project Does
<!-- 2-3 sentences. What problem does it solve? Who uses it? -->


## Tech Stack
<!-- List languages, frameworks, databases, and key libraries. Be specific about versions if they matter. -->
- Language:
- Framework:
- Database:
- Testing:
- Other:

## Project Structure
<!-- Describe the folder layout. Where do routes live? Services? Models? Tests? -->


## Coding Conventions

### Naming
<!-- e.g., "camelCase for variables, PascalCase for classes, kebab-case for files" -->

### File Organization
<!-- e.g., "One class per file. Feature folders, not type folders." -->

### Formatting
<!-- e.g., "2-space indentation, single quotes, no trailing commas" -->

### Error Handling
<!-- e.g., "Use Result<T> for expected failures. Throw only for truly exceptional conditions." -->

## What NOT to Do
<!-- This section is critical. List things the agent should never do in this project. -->
- Never:
- Never:
- Never:
- Never:

## Required Patterns
<!-- List patterns the agent MUST follow, even if not obvious from the code. -->
- All new endpoints must:
- All new functions must:
- All database queries must:

## Autonomy Rules
<!-- Tell the agent what it can do without asking vs. what requires confirmation. -->

### Do without asking:
- Fix lint errors and type errors
- Write tests for code you just wrote
- Add missing imports

### Always ask before:
- Deleting files
- Changing database schemas
- Modifying authentication or authorization logic
- Adding new dependencies

## Out of Scope
<!-- List things that are out of scope for this project entirely. -->
- Do not add:
- Do not change:
```

---

### 3. Fill in every section

Work through the template deliberately. Some tips:

- **"What NOT to Do"** is the most valuable section. Think about the last 3 times a code review caught something. Those items belong here.
- **"Required Patterns"** should cover your authentication middleware, validation approach, logging format, and any other non-obvious structural requirement.
- **"Autonomy Rules"** prevent the agent from either asking too many questions or making dangerous changes silently.

Aim for 1-2 pages total. If a section genuinely doesn't apply to your project, say so explicitly rather than leaving it blank.

---

### 4. Run the same prompt again

Save the context file. Start a fresh agent session (some tools pick up the context file automatically on launch; others require a restart). Run the exact same prompt you used in step 1:

```
Implement a small new feature: add a way for users to export their data as a CSV file.
Implement it following the patterns already in this project.
```

**Expected output:** The same general feature, but now aligned with your conventions. The agent should:
- Use your naming style
- Place files in the correct directories
- Include auth/validation if your context file requires it
- Avoid patterns you listed under "What NOT to Do"

---

### 5. Compare and iterate

Put the two outputs side by side (your scratch notes from step 1 vs. the new output).

For each thing the agent still got wrong, add a rule to your context file. Be specific:

- Wrong: "Write clean code"
- Right: "All service methods must return a Result type, never throw exceptions for validation failures"

Add at least 2 new rules based on what you observed. Save the file.

---

### 6. Confirm the improvement

Run one more prompt to verify your new rules are being respected:

```
Add input validation to the CSV export feature you just built.
```

**Expected output:** Validation that matches your project's validation pattern (the one you described in the context file). If the agent uses a different approach, your rule wasn't specific enough -- refine it.

---

## Done?

- [ ] Baseline output is saved and you noted at least 3 specific things it got wrong
- [ ] Context file exists in your project root with all sections filled in
- [ ] Second run of the same prompt produced output that is measurably closer to your conventions
- [ ] At least 2 new rules were added after the comparison
- [ ] Third prompt (validation) respected the pattern you described in the context file
- [ ] The context file is committed to git (`git add CLAUDE.md && git commit -m "chore: add agent context file"`)

---

## Troubleshooting

**The second run looks almost identical to the first.**
Either the agent isn't reading the context file, or your rules aren't specific enough. First, confirm the file is in the right location for your tool (check your track file). Then ask the agent directly: "What instructions are you following from my context file?" If it can't answer, it isn't finding the file.

**The agent is ignoring a specific rule.**
Vague rules get ignored. "Write clean code" means nothing. "Never use `any` as a TypeScript type -- use explicit types or `unknown`" is enforceable. Rewrite vague rules as concrete prohibitions or requirements, then re-test.

**The context file is getting too long.**
If you're past 3 pages, you're probably writing documentation instead of instructions. Cut anything that describes how the code works (the agent can read that itself) and keep only rules that constrain agent behavior. "We use PostgreSQL" is documentation. "Never use raw SQL strings -- use the ORM query builder only" is an instruction.

**Freshly started session still ignores the context file.**
Some tools require the context file to be in a specific location (project root vs. home directory vs. `.agent/` folder). Check your track file. Also verify there are no syntax errors in the file that might cause it to be silently skipped.

---

## Stretch Goals

1. **Test a hard constraint.** Pick the rule you care most about (the one that would cause the most pain if violated). Deliberately prompt the agent to break it: "Use raw SQL for this query." Does it refuse or warn you? If it complies, your rule needs to be stronger.

2. **Add a "preferred patterns" section.** Beyond what NOT to do, add 3-5 examples of ideal code from your project. Paste actual snippets. Agents that can see examples of good code reproduce that style more reliably than agents that only have prose descriptions.

3. **Write a second context file for a different scope.** Most tools support layered context files (project root + subdirectory). Create a context file inside your `tests/` or `__tests__/` folder with test-specific rules (naming conventions, what to mock, coverage requirements). Verify it applies when you ask the agent to work on test files.
