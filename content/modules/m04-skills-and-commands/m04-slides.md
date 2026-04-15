# M04: Skills, Subagents & Hooks — Slide Outline

---

## Slide 1: The Prompt You've Typed 20 Times This Week

- Show of hands: how many times did you write "review this code" this week?
- Every repeated prompt is a skill waiting to be built
- Right now your prompts are inconsistent, private, and disposable
- Skills make them reusable, shareable, and reliable

Speaker note: Open with the show of hands. Don't rush past it — let the room feel the recognition. The goal is "yes, this is my actual problem."

---

## Slide 2: What a Skill Is

- A Markdown file containing a reusable prompt
- Triggered by a short command: `/commit-message`, `/review-pr`
- Lives in a directory your agent watches
- Accepts optional arguments via a placeholder

Speaker note: Keep this definition tight. Resist the urge to go deeper here — the anatomy slide is next.

---

## Slide 3: Anatomy of a Skill File

```
---
description: One-line description shown in the command picker
---

The actual prompt you want the agent to run.
Reference $ARGUMENTS for anything the user types after the command name.
```

- Frontmatter (optional YAML) at the top
- Prompt body below the separator
- File name becomes the command name
- `.claude/commands/commit-message.md` → `/commit-message`

Speaker note: Show this as a code block, not a diagram. It's simpler than people expect and you want them to see that immediately.

---

## Slide 4: When to Build a Skill vs. Inline Prompt

| Situation | Use |
|---|---|
| Typed the same prompt 3+ times | Skill |
| Team needs consistent output | Skill |
| Task has a fixed structure | Skill |
| One-off exploration or debugging | Inline |
| Highly contextual, won't repeat | Inline |

- Heuristic: would a teammate benefit from running this exact prompt?
- If yes, make it a skill

Speaker note: The table does the work here. Walk through each row, then land on the heuristic. Don't overexplain.

---

## Slide 5: Building /commit-message — Step by Step

```bash
mkdir -p .claude/commands
```

```markdown
---
description: Generate a conventional commit message from staged changes
---

Review staged changes. Write a commit message following Conventional Commits:
type(scope): description — imperative mood, under 72 chars.
Output only the message.
```

```bash
git add .claude/commands/commit-message.md
git commit -m "chore: add commit-message skill"
```

- The file lives in version control — your whole team gets it on pull

Speaker note: This is the demo slide. The audience is watching you type, not reading this slide. Flip to this for reference if you lose your place.

---

## Slide 6: Advanced Skill Patterns

- **Arguments:** `/commit-message feat` passes "feat" as `$ARGUMENTS`
- **Project context:** Reference `CONTRIBUTING.md` or style guides inside the prompt
- **Multi-step prompts:** "First summarize. Then write." — better output than single-shot
- **Commit the skill:** `.claude/commands/` belongs in your repo

Speaker note: Quick slide, two minutes max. The hands-on exercise is where they'll experiment with these.

---

## Slide 7: Skills You'll Actually Use

| Command | What It Does |
|---|---|
| `/commit-message` | Conventional commit from staged diff |
| `/review-pr` | Structured review: security, perf, tests, naming |
| `/write-tests` | Unit tests from a function or class |
| `/explain-this` | Plain-language explanation with assumptions |
| `/daily-standup` | Standup summary from git log + open PRs |

Speaker note: Ask the room which of these they'd use first. Gets people engaged and gives you signal on what to emphasize.

---

## Slide 8: Subagents — Delegating Without Bloating Your Context

The problem: a long session fills your context window. Research and investigation make it worse.

The solution: spawn a subagent — a separate Claude instance with its own context — to handle focused work.

```
Use a subagent to analyze the authentication module and report back:
where are session tokens stored, in what format, and who accesses them?
```

- The subagent works in isolation, summarizes its findings, then terminates
- Your main context sees only the result, not all the steps that got there
- Think of it as delegating to a colleague: they go figure it out, you get the answer

Speaker note: The analogy that lands best is "you don't sit next to them while they do the research." Emphasize that the main context only gets the summary — that's the whole point.

---

## Slide 9: When to Use a Subagent vs. Inline

| Use a subagent | Keep it inline |
|---|---|
| Investigation you don't need in your main thread | You'll iterate on the output in conversation |
| Well-defined task with a clear deliverable | Task is short — overhead not worth it |
| Parallel work: two agents at once | The agent needs your current session context |
| You're near your context limit | Exploratory or back-and-forth work |

Subagents and skills are complementary — you'll often use both in the same session.

Skills: reusable prompt templates for known tasks.
Subagents: isolated workers for investigation or parallel execution.

Speaker note: Quick slide. The table does the work. Emphasize that these are complementary, not competing.

---

## Slide 10: Hooks — Deterministic Control

**The problem with prompts:** "always run prettier after editing" is a suggestion. The agent might miss it.

**Hooks:** shell commands that run at specific lifecycle events — outside the model, guaranteed to execute.

| Trigger | When It Fires | Example Use |
|---|---|---|
| PreToolUse | Before a tool runs | Block `rm -rf` before it executes |
| PostToolUse | After a tool completes | Run formatter after every file write |
| Notification | When Claude wants to notify you | Play a sound / send Slack DM |
| Stop | When Claude finishes and waits | Log session summary |

```json
"PostToolUse": [{ "matcher": "Write", "hooks": [{ "type": "command",
  "command": "prettier --write \"$CLAUDE_TOOL_OUTPUT_FILE\"" }] }]
```

Demo-only today. Full reference: Claude Code 101 on anthropic.skilljar.com.

Speaker note: The hook example on this slide is real and runnable. Make sure to show it working — the "after every Write, prettier runs automatically" moment is the one that clicks for people.

---

## Slide 11: Tool Differences — Same Concept, Different Syntax

| Tool | File Location | Trigger Model |
|---|---|---|
| Claude Code | `.claude/commands/*.md` | Manual: `/command-name` |
| Cursor | `.cursor/rules/*.mdc` | Automatic: injected by file type/glob |
| Factory / Devin | YAML or visual editor | Workflow invocation |

- The underlying idea is identical across all tools
- Skills learned in one tool transfer in under an hour

Speaker note: Some people in the room use Cursor. Acknowledge that Cursor's model is slightly different (ambient vs. on-demand) but the skill-writing discipline is the same.

---

## Slide 12: What Good Skills Have in Common

- Specific output format ("return a numbered list with file:line references")
- Explicit constraints ("under 72 characters", "no explanation — just the output")
- Team standards baked in, not personal preferences
- Tested against at least three real inputs before committing

Speaker note: This is the "quality bar" slide. It's brief but it sets the expectation that a skill worth sharing is a skill worth polishing.

---

## Slide 13: Your First Skill — Right Now

Think of the one prompt you type most often.

- What task does it handle?
- What does good output look like?
- What constraints matter to your team?

Write that down. You'll build it in the exercise.

Speaker note: Give them 90 seconds of quiet to actually write something down. Don't skip this — people who write it down are the ones who build it during the exercise.

---

*13 slides total. Estimated deck time: 45 minutes with demo, 5 minutes buffer.*
