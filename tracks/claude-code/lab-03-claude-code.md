# Lab 03 — Claude Code: Build a Skill

This is the Claude Code variant of Lab 03. Skills are reusable prompt templates stored as files. You invoke them with a slash command inside Claude Code. This lab walks you through creating two working skills.

---

## Where Skills Live

Skills are markdown files stored in the `.claude/commands/` directory inside your project:

```
your-project/
  .claude/
    commands/
      commit.md
      review.md
```

The filename (without `.md`) becomes the slash command. A file named `commit.md` is invoked with `/commit`.

**Global skills** (available in every project):

- Windows: `C:\Users\<you>\.claude\commands\`
- macOS/Linux: `~/.claude/commands/`

Put skills you want everywhere (like `/commit`) in the global directory. Put project-specific skills in the project `.claude/commands/` directory.

---

## Skill File Format

A skill file is a markdown file. The content is the prompt that Claude Code runs when you invoke the command.

**Minimal format:**

```markdown
# Skill Name

Brief description of what this skill does.

---

[The prompt instructions go here. Write them as if you are telling Claude Code exactly what to do.]
```

**With argument support:**

Use `$ARGUMENTS` anywhere in the file as a placeholder. When you type `/skill-name some text`, Claude Code substitutes `some text` wherever `$ARGUMENTS` appears.

```markdown
# My Skill

Does something with the provided input.

---

Process the following: $ARGUMENTS
```

---

## How to Invoke a Skill

At the Claude Code prompt, type a forward slash followed by the skill name:

```
/commit
```

```
/review
```

```
/review src/api/users.js
```

Claude Code reads the skill file and executes the prompt. If the skill uses `$ARGUMENTS`, whatever you typed after the command name is substituted in.

---

## Complete Example: /commit Skill

Create this file at `.claude/commands/commit.md` (or `~/.claude/commands/commit.md` for global use):

```markdown
# Commit

Stages changes and creates a conventional commit with an appropriate message.

---

Look at all uncommitted changes in this repository using `git diff` and `git status`.

Then do the following:

1. Identify what changed and why the change was made based on the code diff.
2. Choose the correct conventional commit type:
   - feat: a new feature
   - fix: a bug fix
   - refactor: code restructuring with no behavior change
   - test: adding or updating tests
   - docs: documentation changes
   - chore: build, config, or tooling changes
   - perf: performance improvement
3. Write a commit message in this format:
   - First line: `type: short description` (under 72 characters, imperative mood, no period)
   - If the change needs explanation, add a blank line and a brief body paragraph
4. Stage the relevant files with `git add` (do not use `git add -A` or `git add .`)
5. Run the commit

If there is nothing to commit, say so and stop.

If any staged file looks like it could contain secrets (e.g., .env, credentials, private keys), stop and warn me before committing.
```

---

## Complete Example: /review Skill

Create this file at `.claude/commands/review.md`:

```markdown
# Review

Reviews code for correctness, security, and maintainability.

---

Review the following for code quality: $ARGUMENTS

If no specific file or path was provided, review all files changed since the last git commit.

For each file you review, check the following and report issues with file path and line number:

**Correctness**
- Logic errors or off-by-one mistakes
- Unhandled edge cases (null, empty, zero, negative)
- Missing error handling

**Security**
- Unvalidated or unsanitized user input
- Hardcoded secrets, tokens, or credentials
- SQL or command injection risks
- Overly permissive access controls

**Maintainability**
- Functions longer than 50 lines
- Files longer than 400 lines
- Deeply nested logic (more than 4 levels)
- Duplicated code that should be extracted
- Unclear variable or function names

**Test coverage**
- Public functions with no corresponding test
- Branches that are not exercised by any test

Format your response as a list of findings grouped by severity: Critical, Warning, Suggestion.
End with a one-line overall assessment.
```

---

## How to Pass Arguments to a Skill

In the skill file, place `$ARGUMENTS` wherever you want the user's input inserted.

Invocation:

```
/review src/api/auth.js
```

Claude Code substitutes `src/api/auth.js` for `$ARGUMENTS` in the prompt before running it.

You can use `$ARGUMENTS` multiple times in a single skill file. The same substitution is applied to every occurrence.

If the user does not provide arguments, `$ARGUMENTS` becomes an empty string. Write your skill to handle this gracefully (as the /review example does by falling back to git-changed files).

---

## Sharing Skills Across Projects

Any skill file placed in the global commands directory is available in every project:

- Windows: `C:\Users\<you>\.claude\commands\`
- macOS/Linux: `~/.claude/commands\`

Good candidates for global skills: `/commit`, `/review`, `/standup`, `/explain`.

Good candidates for project-level skills: anything that references project-specific paths, commands, or conventions.

Project-level skills override global skills with the same name. If you have `/commit` globally and `/commit` in your project, the project version wins.

---

## Verify Your Skills Loaded

After creating skill files, either restart Claude Code or type:

```
/help
```

Your custom skills appear in the command list. If they do not appear, check:

1. The file is in `.claude/commands/` (not `.claude/skills/` or any other path)
2. The file extension is `.md`
3. The filename has no spaces (use hyphens: `code-review.md` not `code review.md`)

---

## Stretch Goal: Try a Subagent

Once your skill is working, try delegating a research task to a subagent. Subagents run in their own context window and return a summary — they're useful when you want to investigate something without consuming your main session's context.

**How to spawn a subagent in Claude Code:**

At the Claude Code prompt, ask the agent to use a subagent for a focused task:

```
Use a subagent to explore the tests directory in this project and report back:
- What test files exist?
- What is being tested?
- What are the biggest coverage gaps you can identify?

Summarize the findings when done.
```

Claude Code will spawn the subagent, run the investigation in isolation, and return a summary to your main session.

**What to observe:**
- Your main conversation only receives the summary, not the full exploration transcript
- The subagent's work does not consume your main context window
- The quality of the summary depends on how clearly you scoped the task

**When subagents are useful:**
- Investigating a part of the codebase unrelated to your current task
- Running two independent investigations in parallel ("use a subagent for X, and separately use a subagent for Y")
- Any well-defined research task where you want the answer without the exploration overhead

**Global vs. project subagents:** Like skills, you can define reusable subagent configurations for common delegation patterns. These are covered in the Claude Code 101 course on Anthropic's SkillJar platform.
