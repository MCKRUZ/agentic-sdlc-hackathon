# Agentic SDLC Hackathon
## Participant Workbook

---

## Welcome

Today is a hands-on introduction to agentic coding tools -- the class of developer tools that can read your codebase, plan multi-step changes, and execute them with you in the loop. By the end of the day you will have a working context file committed to a real project, at least one custom skill you built yourself, and a live MCP server giving your agent access to up-to-date documentation. You will also have a mental model that separates what these tools actually do from the noise around them. Expect to make mistakes, get unexpected outputs, and iterate -- that is the point. There is no lecture-only stretch longer than 40 minutes today.

---

## Pre-Work Checklist

Complete these before you arrive. If something is not working, flag it at registration.

**Required installs:**
- [ ] Agentic coding tool installed and authenticated
  - Claude Code: `npm install -g @anthropic-ai/claude-code` (needs Anthropic API key)
  - Cursor: download at cursor.com (needs account)
  - GitHub Copilot Workspace: needs GitHub subscription
- [ ] Node.js 20 or later -- verify: `node --version`
- [ ] Git -- verify: `git --version`
- [ ] VS Code or another editor you know well

**Required before arriving:**
- [ ] DevBoard sample project cloned: `git clone https://github.com/[your-org]/devboard-sample`
  - OR your own project open and ready (must have real code in it)
- [ ] Confirmed tool works: open your project, start the tool, type "What files are in this directory?" and get a response

**Nice to have:**
- [ ] 15 minutes reading your tool's getting started page
- [ ] This workbook open on your laptop or printed

---

## Workshop Agenda

| Time | Block | Type |
|------|-------|------|
| 09:00 | Welcome and Introductions | Facilitated |
| 09:15 | M01: Agentic Mental Shift | Instruction |
| 09:45 | M02: Out-of-the-Box Tool Usage + Demo | Instruction + Demo |
| 10:15 | LAB 01: First Interaction | Lab |
| 10:45 | Break | -- |
| 11:00 | M03: Context Files + Demo | Instruction + Demo |
| 11:20 | LAB 02: Writing Your Context File | Lab |
| 12:00 | Lunch | -- |
| 13:00 | M04: Skills and Custom Commands + Demo | Instruction + Demo |
| 13:40 | LAB 03: Building a Skill | Lab |
| 14:15 | Break | -- |
| 14:30 | M05: MCP Servers + Demo | Instruction + Demo |
| 15:00 | LAB 04: Adding an MCP Server | Lab |
| 15:30 | M06: Token Management | Instruction |
| 15:45 | M07: Agentic SDLC + Wrap-up | Instruction |

---

## Module Reference Summaries

---

### M01: Agentic Mental Shift

**Key concept:** An agentic coding tool is not autocomplete or a chatbot -- it is a tool that reads your codebase, plans sequences of actions, and executes them.

- Traditional AI coding tools predict the next token. Agentic tools take action sequences: read files, run commands, write changes, ask clarifying questions.
- The "agent loop" is the cycle of: observe (read context), plan (decide what to do), act (execute), observe again.
- The context window is the tool's working memory. Everything the agent knows about your project in a given conversation fits inside it.
- Your job is not to type less -- it is to provide enough context for the agent to make good decisions, and to review what it produces.
- Treating the tool like a search engine produces search-engine-quality results. Treating it like a collaborator that needs context produces useful work.

> **Remember this:** The quality of the agent's output is directly proportional to the quality of context you give it. Vague prompts produce generic code.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

### M02: Out-of-the-Box Tool Usage

**Key concept:** Without any configuration, the tool can already read your project, answer questions about it, and make targeted changes -- but it will make assumptions about your conventions.

- Cold start: open a project, start the tool, ask a navigation question. It will read real files and give grounded answers.
- The tool can explain code it has never seen before -- useful for onboarding onto unfamiliar projects.
- It can make changes based on natural language descriptions, but the changes reflect generic best practices, not your specific standards.
- Always review the proposed diff before accepting. The tool shows you what it intends to change.
- The gap between "works" and "fits our project" is exactly what context files (M03) solve.

> **Remember this:** Every change the agent proposes is a diff you must review. This is not optional. It is how you stay in control.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

### M03: Context Files

**Key concept:** A context file is a markdown document that the agent reads at the start of every conversation, giving it persistent knowledge about your project's stack, conventions, and constraints.

- The file lives in your project root. The name depends on the tool: `CLAUDE.md` for Claude Code, `.cursor/rules` for Cursor.
- It is committed to the repo. Everyone on your team benefits from it.
- What belongs in it: stack and version info, naming conventions, error handling patterns, things the agent should never do, links to architectural decisions.
- What does not belong in it: secrets, long prose explanations, generic advice that applies to any project.
- The context file is not magic -- it is instruction. If you write vague instructions, you get vague results.

> **Remember this:** Write your context file as if you are onboarding a contractor who is technically skilled but knows nothing about your specific project.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

### M04: Skills and Custom Commands

**Key concept:** A skill is a reusable, parameterized prompt stored as a file in your project that you can invoke by name to perform a repeatable task.

- Skills live in a specific directory: `.claude/commands/` for Claude Code. They are markdown files with instructions.
- When you invoke a skill (e.g. `/commit-message`), the tool reads the skill file and executes its instructions against your current project state.
- Skills can reference your context file and combine it with task-specific instructions.
- Good candidates for skills: generating commit messages, writing test stubs from a function signature, creating pull request descriptions, checking code against your conventions.
- Skills are plain files. You can version-control them, share them with your team, and iterate on them like code.

> **Remember this:** If you find yourself writing the same long prompt more than twice, that is a skill waiting to be written.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

### M05: MCP Servers

**Key concept:** The Model Context Protocol (MCP) lets you connect external data sources and tools to the agent, extending what it can access during a conversation.

- MCP servers are separate processes that the agent can query: for documentation, database records, issue tracker items, and more.
- You register an MCP server once (via CLI or config file) and it is available in every conversation.
- context7 is a documentation server: it fetches up-to-date library docs so the agent is not relying on training data that may be outdated.
- Other common MCP servers: filesystem access, web search, GitHub issues, SQL databases.
- The agent tells you when it is calling an MCP server and what it retrieved. You can see the source of information.

> **Remember this:** MCP servers do not add new AI capability -- they add current, accurate data. Think of them as the agent's ability to look things up rather than rely on memory.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

### M06: Token Management

**Key concept:** The context window is finite. As a conversation grows, older content is pushed out or the cost increases. Managing token usage is a practical habit, not a technical detail.

- Every message, every file the agent reads, and every response consumes tokens. The window fills up.
- When the context window is near full, the agent's quality drops because it can no longer see earlier parts of the conversation.
- Practical habits: use `/compact` or `/clear` when a conversation task is done. Start a new conversation for a new task. Put permanent context in files, not chat history.
- Large files cost proportionally. If you ask the agent to read a 5,000-line file, that is expensive and often unnecessary. Ask it to read the specific function instead.
- Watch for the agent re-reading the same files repeatedly in one conversation -- that is a sign of context confusion.

> **Remember this:** A new conversation is free. Starting fresh when you change tasks is better than dragging a bloated context into new work.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

### M07: Agentic SDLC

**Key concept:** Agentic tools are not just for writing new code -- they have a role in every phase of the development lifecycle.

- Planning: use the agent to draft technical specs, break down tickets, and identify edge cases before writing code.
- Coding: the core use case most people start with. Writing, refactoring, debugging.
- Review: ask the agent to review a diff for logic errors, security issues, or convention violations before you open a PR.
- Testing: generate test stubs from function signatures, identify untested branches, write edge case tests.
- Documentation: generate changelogs from git history, update README sections, write inline comments for complex logic.
- The 6-week sprint model: weeks 1-2 for strategy and context file setup, weeks 3-4 for skills and MCP integration, weeks 5-6 for team-wide adoption and habit building.

> **Remember this:** Start with one phase and one workflow. Get one thing working well before expanding to the rest of the lifecycle.

**Personal notes:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## Lab Worksheets

---

### LAB 01: First Interaction

**Duration:** 30 minutes
**Tools needed:** Your project, agent tool running

**What I'll do:**
Ask the agent three types of questions against a real project -- navigation, explanation, and change. The goal is to see what the tool can do with zero configuration.

**Key steps:**

1. Open your project root in the terminal. Start the agent.

2. Ask a navigation question:
   ```
   What are the main entry points for this application?
   ```
   Read the response. Did it cite actual files? Were the files correct?

3. Ask an explanation question:
   ```
   Pick the most complex function in this project and explain what it does.
   ```
   Check the explanation against the actual code. Is it accurate?

4. Ask for a small change:
   ```
   Add a comment block to the [specific function] explaining what it does and what parameters it expects.
   ```
   Review the diff before accepting. Does it look right? Accept it.

5. Run your project or tests to confirm nothing broke.

**Notes / scratch:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**Done?**
- [ ] Ran all three prompt types
- [ ] Reviewed the diff before accepting the change
- [ ] Ran the project or tests after the change
- [ ] Noted one thing that surprised you (good or bad)

---

### LAB 02: Writing Your Context File

**Duration:** 40 minutes
**Tools needed:** Your project, agent tool running, text editor

**What I'll do:**
Write a CLAUDE.md (or equivalent) for my project and confirm it changes the agent's behavior.

**Key steps:**

1. Create the file:
   ```bash
   touch CLAUDE.md
   ```
   (Windows: create it in your editor)

2. Fill in the minimum viable structure (use the Context File Template in the Reference Cards section):
   - Project name and one-sentence purpose
   - Tech stack with versions
   - At least 3 coding conventions specific to your project
   - At least 1 "never do this" rule

3. Run a prompt WITHOUT the context file first (delete or rename it temporarily) and note the response.

4. Re-add the context file and run the same prompt. Note the difference.

5. Iterate: the first version will be imperfect. Edit based on what you observed.

6. Commit the file:
   ```bash
   git add CLAUDE.md
   git commit -m "docs: add agent context file"
   ```

**Notes / scratch:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**Done?**
- [ ] CLAUDE.md (or equivalent) created and committed
- [ ] Contains stack information
- [ ] Contains at least 3 project-specific conventions
- [ ] Ran a before/after comparison and saw a difference

---

### LAB 03: Building a Skill

**Duration:** 35 minutes
**Tools needed:** Your project, agent tool running, text editor

**What I'll do:**
Create at least one reusable skill file and invoke it.

**Key steps:**

1. Create the skills directory:
   ```bash
   mkdir -p .claude/commands
   ```

2. Think of a task you run repeatedly: writing commit messages, generating test stubs, drafting PR descriptions, checking for convention violations.

3. Create a new `.md` file in `.claude/commands/` named after the task (e.g. `commit-message.md`, `test-stub.md`).

4. Write the skill (use the Skill File Template in the Reference Cards section):
   - What the skill does (1 sentence)
   - Step-by-step instructions for the agent
   - Output format

5. Invoke the skill:
   - Claude Code: `/your-skill-name`
   - Cursor: reference the file with `@`

6. Review the output. Does it do what you wanted? Edit the skill file and try again.

7. Commit the skill:
   ```bash
   git add .claude/commands/
   git commit -m "feat: add [skill-name] skill"
   ```

**Notes / scratch:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**Done?**
- [ ] Skills directory created
- [ ] At least one skill file written
- [ ] Skill invoked and produced output
- [ ] Output reviewed and skill iterated at least once
- [ ] Skill committed to the repo

---

### LAB 04: Adding an MCP Server

**Duration:** 30 minutes
**Tools needed:** Your project, agent tool running, terminal with internet access

**What I'll do:**
Install and connect the context7 MCP server, verify it is live, and use it to answer a documentation question.

**Key steps:**

1. Install context7 (Claude Code):
   ```bash
   claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
   ```
   For other tools, see the MCP Server Quick Reference in the Reference Cards section.

2. Restart the agent:
   ```
   /exit
   claude
   ```

3. Verify the connection:
   ```
   /mcp
   ```
   context7 should appear as connected.

4. Ask a documentation question for a library your project uses:
   ```
   Using the context7 docs, how do I [specific thing] with [library name]? Show me the exact API.
   ```

5. Review the response. Compare it to the library's official docs -- is it accurate?

6. Try a second question for a different library or a different aspect of the same one.

**Notes / scratch:**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**Done?**
- [ ] context7 installed without errors
- [ ] Shows as connected in `/mcp`
- [ ] Used it to answer at least one real documentation question
- [ ] Confirmed the answer is accurate against the library docs

---

## Reference Cards

---

### Context File Template

Copy this into your `CLAUDE.md` (Claude Code) or `.cursor/rules` (Cursor) and fill in the blanks.

```markdown
# [Project Name] -- Agent Context

## Project Overview
[One sentence: what this project does and who it's for.]

## Tech Stack
- Language: [e.g. TypeScript 5.4]
- Framework: [e.g. Express 4.x / Next.js 14]
- Database: [e.g. PostgreSQL via Prisma]
- Testing: [e.g. Jest + React Testing Library]
- Other: [e.g. Redis for sessions, Zod for validation]

## Architecture
[2-3 sentences: how the code is organized. Where is the entry point? How are layers separated?]

## Coding Conventions
- [Convention 1: e.g. All errors are returned as Result<T>, never thrown for expected failures]
- [Convention 2: e.g. All API routes live in src/routes/, one file per resource]
- [Convention 3: e.g. Tests live next to the code they test, named *.test.ts]
- [Convention 4: e.g. No inline styles -- use Tailwind utility classes only]
- [Convention 5: e.g. All database queries go through the repository layer, never direct in routes]

## Never Do This
- [Rule 1: e.g. Do not add npm packages without asking]
- [Rule 2: e.g. Do not modify the database schema directly -- use migrations]
- [Rule 3: e.g. Do not use any -- use unknown and narrow the type]

## Current Focus
[Optional: what part of the system is being actively worked on right now.]
```

---

### Skill File Template

Save this as `.claude/commands/[skill-name].md` and fill in the blanks.

```markdown
# [skill-name]

[One sentence: what this skill does.]

## When to Use
[One sentence: when to invoke this skill.]

## Instructions
1. [Step 1: what the agent should do first -- e.g. "Run `git diff --staged` to see staged changes."]
2. [Step 2]
3. [Step 3]
4. [Any constraints: e.g. "Do not run git commands that modify history."]

## Output Format
[Describe exactly what the output should look like. The more specific, the better.]

## Example Output
[Optional but useful: show a sample of what a good result looks like.]
```

---

### Top 10 Agent Prompts That Work

These prompt patterns produce consistently better results than vague requests.

| # | Prompt Pattern | Why It Works |
|---|---------------|--------------|
| 1 | "Read [file path] and explain what [specific function] does." | Scopes the read to exactly what you need. |
| 2 | "I want to [goal]. What approach would you take before writing any code?" | Gets a plan you can approve before changes are made. |
| 3 | "Here is the current behavior: [X]. Here is the expected behavior: [Y]. What is wrong?" | Gives the agent a concrete comparison to work from. |
| 4 | "Refactor [function] to [specific goal, e.g. reduce nesting]. Do not change behavior." | Constrains scope so it doesn't over-reach. |
| 5 | "Write a test for [function] that covers [specific scenario]." | More useful than "write tests for this file." |
| 6 | "Review this diff for [specific concern, e.g. security issues, convention violations]." | Focused review beats open-ended review. |
| 7 | "I need to add [feature]. What files should I change and in what order?" | Planning before doing -- use for anything that touches 3+ files. |
| 8 | "Explain this error: [paste error message]. The relevant code is in [file path]." | Gives the agent both symptom and context. |
| 9 | "Generate a commit message for the staged changes. Follow Conventional Commits format." | Specific format constraint improves the output. |
| 10 | "What would break if I deleted [file or function]?" | Impact analysis before risky changes. |

---

### MCP Server Quick Reference

| Server | Purpose | Install Command (Claude Code) |
|--------|---------|-------------------------------|
| context7 | Live library documentation | `claude mcp add context7 -- npx -y @upstash/context7-mcp@latest` |
| filesystem | Expanded file system access | `claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/allow` |
| github | GitHub issues, PRs, and repo data | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` (needs `GITHUB_TOKEN`) |
| postgres | Query a PostgreSQL database | `claude mcp add postgres -- npx -y @modelcontextprotocol/server-postgres postgresql://localhost/mydb` |
| brave-search | Web search from within the agent | `claude mcp add brave-search -- npx -y @modelcontextprotocol/server-brave-search` (needs `BRAVE_API_KEY`) |

**For Cursor:** Add servers in Settings > MCP, or directly in `.cursor/mcp.json`.

**Verify a server is connected:**
```
/mcp
```

**Remove a server:**
```
claude mcp remove [server-name]
```

**List registered servers:**
```
claude mcp list
```

---

## Next Steps

### 3 Things to Do This Week

1. **Commit a context file to your main project.** The one you wrote today was for a sample project. Write one for the real codebase you work in every day. It does not need to be perfect -- a rough first version that you refine over a week is better than a perfect one that never gets written.

2. **Build one skill for a task you do repeatedly.** Look at your last 10 commit messages or PR descriptions. Was there a pattern? That is your first skill. Build it, test it, commit it.

3. **Use the agent for one real task on your actual work.** Not a toy example. Pick something from your backlog, run it through the agent with your new context file, and review what it produces. You will learn more from one real task than from five more tutorials.

### Where to Learn More

**Tool-Agnostic Resources**
- Model Context Protocol specification: modelcontextprotocol.io
- Conventional Commits standard: conventionalcommits.org
- The Pragmatic Engineer newsletter (covers agentic tools regularly): pragmaticengineer.com

**Claude Code**
- Official documentation: docs.anthropic.com/claude-code
- MCP server registry: Browse available servers at the MCP documentation site

**Cursor**
- Official documentation: docs.cursor.com
- Community forum: forum.cursor.com

**GitHub Copilot**
- Official documentation: docs.github.com/en/copilot
- Copilot Workspace docs: githubnext.com/projects/copilot-workspace

**MCP Servers**
- Official server list: github.com/modelcontextprotocol/servers
- context7 documentation: context7.com

### Community Resources

- Ask your teammates who attended today. You now have shared vocabulary and shared tools.
- Most agentic tool communities have Discord servers -- look for the official invite on the tool's documentation site.
- The best way to build skill is to pair with someone who is slightly ahead of you. Find one person at this workshop who is further along and schedule 30 minutes to work through something together next week.
