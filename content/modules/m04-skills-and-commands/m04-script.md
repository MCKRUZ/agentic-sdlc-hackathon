# M04: Skills & Custom Commands
## Presenter Script — 40 minutes including demo

---

### Section 1: The Problem It Solves (5 min)

[SLIDE 1]

Let me ask you something. How many of you have typed a prompt like "review this code for security issues and suggest improvements" more than once this week? More than five times? More than ten?

That's the problem we're solving in this module.

Right now, every time you want the agent to do something specific, you have to describe what you want from scratch. Maybe you have a notes file with your favorite prompts. Maybe you just retype it and hope you remember the details you included last time. Neither of those scales.

[PAUSE — 3 seconds]

The other issue is consistency. If you're on a team, the person next to you has a completely different set of prompts for the same tasks. Their code reviews look different from yours. Their commit messages follow a different pattern. That inconsistency compounds over time.

Skills and custom commands are how you fix this. They're how you stop being a prompt typist and start being someone who builds tools.

---

### Section 2: What Skills and Slash Commands Are (8 min)

[SLIDE 2]

A skill — sometimes called a slash command depending on the tool — is a reusable prompt stored in a file and triggered by a short command.

Instead of typing a paragraph every time you want a code review, you type `/review-pr` and the agent runs your pre-written, carefully structured prompt against the current context.

[SLIDE 3]

Let's look at the anatomy of a skill file. They're simpler than you'd expect.

A skill file is typically a Markdown file. It lives in a known directory your agent tool watches — for Claude Code, that's the `.claude/commands/` folder in your project or in your home config directory. For Cursor, it's rules files. We'll cover the tool differences at the end.

The file has a few parts:

First, a name. This becomes the command you type. A file called `commit-message.md` becomes `/commit-message`.

Second, optionally, a description. One sentence that shows up in the command picker so you remember what it does.

Third, the prompt body. This is the actual instruction the agent will execute. You write it exactly like you'd write a prompt, except you can use a placeholder — typically `$ARGUMENTS` or `{{input}}` depending on the tool — to pass in whatever the user provides after the command name.

[SLIDE 4]

Here's what a minimal skill file looks like:

```
---
description: Generate a conventional commit message from staged changes
---

Look at the staged changes in this repo. Write a git commit message following
the Conventional Commits spec: type(scope): description in imperative mood,
under 72 characters. If the scope isn't obvious, omit it. Output only the
commit message, no explanation.
```

That's it. No code, no configuration beyond the frontmatter. The agent already knows the context — your repo, your staged files — so the prompt just needs to tell it what to do with that context.

[PAUSE — 2 seconds]

One thing worth noting: the best skill files are specific. "Review my code" is a bad skill. "Check this function for SQL injection vulnerabilities, missing input validation, and unhandled exceptions — output findings as a numbered list with file:line references" is a good skill. The more specific, the more consistent the output.

---

### Section 3: When to Build One vs. Inline Prompt (5 min)

[SLIDE 5]

Here's the heuristic: if you've typed the same prompt more than three times, make it a skill.

That's not a hard rule but it'll serve you well. Three times is enough to know the prompt is stable and useful. It's also enough to know you're going to type it a fourth time, and a tenth.

[PAUSE — 2 seconds]

The flip side: don't over-abstract. Not everything needs to be a skill. A one-off "explain why this specific async deadlock is happening" prompt belongs inline. It's contextual, it's ad hoc, you'll never need it again in that exact form.

Skills are for:
- Repeated workflows. Code review, commit messages, changelogs, test generation.
- Team standards. Things everyone should do the same way.
- Complex prompts you don't want to reconstruct from memory.
- Tasks with consistent inputs and outputs.

Inline prompts are for:
- Exploratory or debugging conversations.
- One-time analysis.
- Anything highly specific to a single piece of code.

If you're unsure, ask yourself: would a teammate benefit from running this exact prompt? If yes, make it a skill.

---

### Section 4: Building Your First Skill — /commit-message (12 min)

[SLIDE 6]

[DEMO CUE — open terminal and VS Code side by side]

Let's build the `/commit-message` skill from scratch. I'm going to walk through every step.

Step one: find or create your commands directory.

In Claude Code, skills live in `.claude/commands/` relative to your project root, or in `~/.claude/commands/` for skills you want available everywhere. Let's put this one in the project so we can commit it and share it with the team.

```
mkdir -p .claude/commands
```

Step two: create the file.

```
touch .claude/commands/commit-message.md
```

[DEMO CUE — open the file in the editor]

Step three: write the frontmatter. This is YAML between triple-dashed lines at the top.

```yaml
---
description: Generate a conventional commit message from staged changes
---
```

Step four: write the prompt. Here's what I actually use:

```
Review the currently staged git changes. Write a commit message following
the Conventional Commits specification:

  type(scope): short description

Rules:
- type must be one of: feat, fix, refactor, docs, test, chore, perf, ci
- Use imperative mood (e.g. "add" not "added")
- Keep the first line under 72 characters
- Omit scope if it isn't clear from the diff
- If the change is non-trivial, add a blank line then a short body paragraph
  explaining WHY the change was made, not what

Output only the commit message. Do not explain your reasoning.
```

[DEMO CUE — save the file, switch to terminal]

Step five: use it.

```
/commit-message
```

[PAUSE — let it run, show output]

Notice a few things. The agent read the staged diff without us telling it to — it understood that from context. The message follows our spec. And if we don't like it, we can iterate: "make the scope more specific" or "this is actually a fix, not a feat."

[DEMO CUE — show a second iteration]

Step six — and this is important — commit the skill file itself.

```
git add .claude/commands/commit-message.md
git commit -m "chore: add commit-message skill"
```

Now everyone on your team has it. When they pull this repo, the skill is there.

[SLIDE 7]

A few advanced features worth knowing:

You can accept arguments. If you type `/commit-message feat` the text "feat" gets passed in as `$ARGUMENTS`. You can reference that in your prompt to pre-fill the type.

You can chain context. Reference other files in your project. "Read our CONTRIBUTING.md and use those commit conventions" makes the skill aware of project-specific rules.

You can write multi-step prompts. "First summarize the diff in one sentence. Then write the commit message based on that summary." Breaking into steps often produces better output.

---

### Section 5: Real Examples (5 min)

[SLIDE 8]

Let me show you a handful of skills that are genuinely useful in day-to-day development.

**/review-pr**
Runs a structured code review: security, performance, test coverage, naming, and SOLID violations — each as a separate section. Because the structure is fixed, every review looks the same and nothing gets skipped.

**/write-tests**
Given a function or class in context, generates unit tests covering the happy path, edge cases, and known failure modes. You can extend this with your specific test framework and naming conventions so the output drops straight into your test file.

**/explain-this**
Takes the selected code and explains it in plain language: what it does, what assumptions it makes, and what breaks if those assumptions are violated. Useful when you're onboarding to an unfamiliar codebase.

**/daily-standup**
Looks at your git log for the past 24 hours, your open PRs, and any TODO comments you've added, then writes a standup summary. Takes about three seconds. Saves you the mental overhead of reconstructing what you did.

[PAUSE — 2 seconds]

The pattern you'll notice: each of these is a task you do repeatedly, has a consistent structure, and benefits from being done the same way every time. That's the target profile for a skill.

---

### Section 6: Tool Differences (5 min)

[SLIDE 9]

The concept is the same across tools but the syntax and file locations differ. Let's map it out quickly.

**Claude Code** — Skills are Markdown files in `.claude/commands/`. Triggered with `/command-name`. The `$ARGUMENTS` placeholder captures text after the command name. Global skills live in `~/.claude/commands/`.

**Cursor** — Uses "rules files" in `.cursor/rules/`. These are always-on context rather than triggered commands, which is a different model. You don't invoke them manually; Cursor injects them automatically based on the file type or glob patterns you configure. Think of Cursor rules as ambient instructions, not on-demand tools.

**Factory / Devin / similar agent platforms** — Often called "workflows" or "playbooks." Stored in their own config formats, sometimes YAML, sometimes a visual editor. The underlying idea is identical: a reusable, parameterized instruction set the agent can execute.

[SLIDE 10]

The key insight is that this is a converging pattern. Every serious agentic tool is building some version of it because the need is universal. When you learn to write good skills for one tool, you can adapt that knowledge to any other tool in under an hour.

What transfers across all of them:
- Specificity beats generality
- Structured output prompts produce consistent results
- Team-shared skill libraries are a force multiplier
- Skills should encode your team's standards, not just your personal preferences

[PAUSE — 3 seconds]

Before we move to the next module, take two minutes and think about the one prompt you type most often. That's your first skill. Write it down — we'll have time during the hands-on exercise to actually build it.

---

*End of M04 script. Total estimated time: 40 minutes.*
