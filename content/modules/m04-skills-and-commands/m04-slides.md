# M04: Skills & Custom Commands — Slide Outline

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

## Slide 8: Tool Differences — Same Concept, Different Syntax

| Tool | File Location | Trigger Model |
|---|---|---|
| Claude Code | `.claude/commands/*.md` | Manual: `/command-name` |
| Cursor | `.cursor/rules/*.mdc` | Automatic: injected by file type/glob |
| Factory / Devin | YAML or visual editor | Workflow invocation |

- The underlying idea is identical across all tools
- Skills learned in one tool transfer in under an hour

Speaker note: Some people in the room use Cursor. Acknowledge that Cursor's model is slightly different (ambient vs. on-demand) but the skill-writing discipline is the same.

---

## Slide 9: What Good Skills Have in Common

- Specific output format ("return a numbered list with file:line references")
- Explicit constraints ("under 72 characters", "no explanation — just the output")
- Team standards baked in, not personal preferences
- Tested against at least three real inputs before committing

Speaker note: This is the "quality bar" slide. It's brief but it sets the expectation that a skill worth sharing is a skill worth polishing.

---

## Slide 10: Your First Skill — Right Now

Think of the one prompt you type most often.

- What task does it handle?
- What does good output look like?
- What constraints matter to your team?

Write that down. You'll build it in the exercise.

Speaker note: Give them 90 seconds of quiet to actually write something down. Don't skip this — people who write it down are the ones who build it during the exercise.

---

*10 slides total. Estimated deck time: 35 minutes with demo, 5 minutes buffer.*
