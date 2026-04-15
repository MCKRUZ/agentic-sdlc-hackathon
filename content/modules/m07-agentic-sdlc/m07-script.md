# M07: Agentic SDLC & Wrap-up
## Presenter Script — 15 minutes

---

### Section 1: The Full Picture (5 min)

[SLIDE 1]

We've covered a lot today. Before we close out, I want to step back and show you how it all connects.

Think about the software development lifecycle: plan, build, review, ship, maintain. Agentic tools don't replace that process. They plug into it at every stage.

Planning — that's where we started. Using the agent to break down requirements, generate task lists, identify risks before you write a line of code. The agent as a thinking partner before the work begins.

Building — the bulk of what most people use agents for. Code generation, refactoring, debugging. But also test generation, documentation, and the exploratory work of understanding an unfamiliar codebase.

Automating — that's what skills and commands do. You've now seen how to stop doing repetitive prompt work manually and encode it into reusable tools your whole team can use.

Extending — that's MCP. Connecting the agent to your live systems so it's working from real data instead of approximations.

Managing — that's context and tokens. Knowing the limits of the tool you're working with and designing your workflow around those limits.

[PAUSE — 2 seconds]

None of these modules is optional. They're each solving a different part of the same problem: how do you use agentic tools effectively across the whole lifecycle, not just during the part where you're typing code?

---

### Section 2: Multi-Agent Patterns (4 min)

[SLIDE 2]

The sessions today have mostly been about a single agent working with you. But the direction the industry is heading is multi-agent: multiple specialized agents working in parallel, coordinated by an orchestrator.

Here's the basic pattern. An orchestrator agent takes a high-level task — "implement this feature" — and decomposes it into subtasks. It then dispatches those subtasks to worker agents. One worker writes the implementation. Another writes the tests. Another does the code review. The orchestrator collects results, resolves conflicts, and produces a coherent output.

[PAUSE — 2 seconds]

The parallel execution is the key benefit. Tasks that would take a developer thirty minutes sequentially can run concurrently in a few minutes. And because each worker agent has a focused, narrower context, they tend to produce better output than a single agent trying to do everything in one session.

The critical design decision in any multi-agent system is where to put the human. Fully autonomous pipelines work for well-defined, low-risk tasks. For anything that touches production data, customer-facing behavior, or security, you want human-in-the-loop checkpoints. The orchestrator pauses and surfaces decisions that require human judgment rather than proceeding autonomously.

That's not a limitation — that's good system design. The goal isn't to remove humans from the loop. It's to remove humans from the parts of the loop where they aren't adding value.

---

### Section 3: What's Next (3 min)

[SLIDE 3]

A quick look at where this is going, without the hype.

Fully autonomous agents are becoming more capable. The current generation handles well-defined tasks with high reliability. The next generation will handle more ambiguous tasks, recover from more failures, and require less hand-holding. That's already happening in research and early production systems.

Agentic CI/CD is starting to show up in real pipelines. Agents that write code, run tests, review output, and open pull requests without a human initiating each step. Some teams are already using this for routine maintenance tasks: dependency updates, test fixes, documentation updates.

The tooling is converging. MCP, skills, agent frameworks — these are stabilizing. The investments you make today in learning these patterns will transfer as the tools evolve, because the underlying concepts are durable even as the specific implementations change.

[PAUSE — 2 seconds]

The honest framing: we're in the early phase. The tools work, they're useful today, and they're improving fast. The developers who build fluency now will have a meaningful advantage over those who wait for the tools to mature.

---

### Section 4: Call to Action (3 min)

[SLIDE 4]

One thing. Not a list of ten things, not a reading curriculum. One thing to do tomorrow morning.

Pick the task you do most repetitively in your current project — the one that takes ten minutes every time and follows the same pattern. Build a skill for it. Write the file, test it against three real inputs, commit it to your repo.

That's it. One skill, tomorrow morning. If it takes you more than thirty minutes, the scope is too large.

[PAUSE — 2 seconds]

If you want to go further, here's where to look.

Anthropic's SkillJar platform (anthropic.skilljar.com) has two courses worth doing next week. **Claude Code 101** covers hooks, subagents, and Plan Mode in depth — the material we introduced today. **Claude Code in Action** goes deeper into GitHub integration, automated code review workflows, and visual inputs. Both are free.

The Anthropic documentation for Claude Code covers skills, MCP configuration, and agent settings in detail. The MCP server registry has the full list of available servers. The Claude Discord has a developer channel where people share skills and workflows.

For multi-agent patterns, look at the Claude Code documentation on subagents and the broader literature on agentic systems — there's good practical writing appearing now from teams who are doing this in production.

[SLIDE 5]

One last thing before you leave.

The most common mistake people make after a day like this is over-engineering. They try to build a full agent system before they've built one skill. They configure five MCP servers before they've used one in anger.

Start small. Use the tools for real work. Let the patterns emerge from actual problems you're solving.

The developers who get the most out of agentic tools are the ones who treat them as colleagues, not magic. They give clear instructions, they check the output, and they course-correct when something's off. That relationship gets better over time as you learn what the tools are good at and where they need guidance.

Thanks for spending the day on this. Go build something.

---

*End of M07 script. Total estimated time: 15 minutes.*
