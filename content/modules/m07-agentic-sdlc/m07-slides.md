# M07: Agentic SDLC & Wrap-up — Slide Outline

---

## Slide 1: Today Mapped to the SDLC

| SDLC Phase | Module | What You Learned |
|---|---|---|
| Plan | M01 | Agent as thinking partner: requirements, task breakdown, risk |
| Build | M02, M03 | Code generation, refactoring, debugging, test generation |
| Automate | M04 | Skills, subagents, and hooks: reusable tools and deterministic control |
| Extend | M05 | MCP servers: connect agent to live systems and current docs |
| Manage | M06 | Context and tokens: work within the limits of the tool |

Agentic tools don't replace the SDLC. They plug into every stage of it.

Speaker note: This is the connective tissue slide. Give the room a moment to see their day reflected back. Don't rush it.

---

## Slide 2: Multi-Agent Patterns

Single agent today. Multi-agent next.

```
Orchestrator Agent
    |
    +-- Worker: Write implementation
    +-- Worker: Write tests
    +-- Worker: Code review
    |
[Human checkpoint]
    |
Orchestrator: Collect, resolve, output
```

- Parallel execution: tasks that took 30 min sequentially run concurrently
- Focused workers produce better output than one agent doing everything
- Human-in-the-loop checkpoints for decisions that require judgment

The goal is not to remove humans. It's to remove humans from the parts of the loop where they aren't adding value.

Speaker note: Draw this on the whiteboard if it helps. The key concepts are: decomposition, parallelism, and deliberate human checkpoints. Don't let this become a demo — keep it conceptual.

---

## Slide 3: Where This Is Going

- **More autonomous agents:** better handling of ambiguous tasks, less hand-holding required
- **Agentic CI/CD:** agents that write, test, review, and PR without manual initiation — already in use for routine maintenance
- **Tooling convergence:** MCP, skills, agent frameworks are stabilizing — patterns you learn now transfer as tools evolve

Honest framing: early phase. Tools work today. Improving fast.

Developers who build fluency now have a meaningful head start.

Speaker note: No hype here. Be measured. The "honest framing" line is important — say it out loud.

---

## Slide 4: One Thing to Do Tomorrow

Pick the task you do most repetitively in your current project.

Build a skill for it.

- Write the file
- Test it against three real inputs
- Commit it to your repo

If it takes more than 30 minutes, the scope is too large.

Speaker note: Say "one thing" with emphasis. People leave workshops with lists of ten things and do none of them. One thing, tomorrow morning. Land this clearly.

---

## Slide 5: Resources

**Go deeper on what we covered today:**
- **Anthropic SkillJar** (anthropic.skilljar.com) — free courses:
  - *Claude Code 101* — hooks, subagents, Plan Mode in full depth
  - *Claude Code in Action* — GitHub integration, automated workflows, visual inputs

**Reference:**
- Anthropic Claude Code docs — skills, MCP config, agent settings
- MCP server registry — full list of available servers
- Claude Discord — developer channel, shared skills and workflows
- Model Context Protocol spec — if you want to build a custom server

The most common mistake after a day like this: over-engineering before you've done the basics in anger.

Start small. Use the tools for real work. Let the patterns emerge.

Speaker note: Call out SkillJar specifically — "If you want to go deeper on hooks or GitHub integration, those are the two courses to start with, and they're free." Close on the "start small" line. Don't add more after it.

---

*5 slides total. Estimated deck time: 13 minutes, 2 minutes buffer.*
