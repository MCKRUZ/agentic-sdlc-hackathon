# M02: OOB Tool Usage — Slide Outline
**Module duration:** 30 minutes (includes live demo)
**Slide count:** 10

---

## Slide 1: Three Tools, One Mental Model

| Tool | How you run it | Scope |
|---|---|---|
| Claude Code | Terminal, npm install | Full local file system |
| Cursor | IDE fork (replaces VS Code) | Full local file system |
| Copilot Workspace | Browser, inside GitHub | Sandboxed to repo |

- All three follow the same agent loop from M01
- Installation friction varies; capabilities don't differ as much as you'd think
- Pick one and stay consistent for the day

Speaker note: Don't get into a debate about which tool is "best." They're all viable. The mental model transfers. If someone asks, Claude Code has the most transparent tool output, which makes it better for learning.

---

## Slide 2: What You Need Before You Start

Three prerequisites:

1. **API key / auth** — know which account is being billed
2. **A working project** — the agent needs existing code to read and patterns to follow
3. **Default permissions you understand** — you'll tighten them after you see behavior

Today's sample project: **DevBoard** (Node/Express backend, plain JS frontend)

Speaker note: Pause here to confirm everyone has their tool installed. Resolve blockers before moving forward. Five minutes now saves fifteen minutes of lost demo time later.

---

## Slide 3: Your First Prompt Should Be a Question

Wrong first prompt: "Build me a feature."
Right first prompt: "Walk me through this project."

Why: you want to verify the agent's understanding before it acts.
If it misunderstands your codebase, you want to catch that before it writes code.

Ask it to explain structure first. Then trace a specific flow. Then modify.

Speaker note: This "understand before modify" principle is worth stating directly. Ask the room: "Would you modify a codebase you'd never read?" Same rule applies here.

---

## Slide 4: The Exploration Sequence

1. "Describe the project layout and how the main pieces connect."
2. "Trace what happens from [entry point] to [outcome]."
3. "What patterns does this codebase use for error handling / testing / logging?"
4. Now give it a task.

Each step builds shared context. Step 4 is only as reliable as steps 1-3.

Speaker note: This sequence is repeatable. Drill it. The room should be able to recite these four questions before the end of the day.

---

## Slide 5: What the Agent Can See

**Has access to:**
- All files in the project directory (recursive)
- Git history (commits, diffs, branches)
- Shell environment and commands on PATH
- Any tools explicitly enabled (web search, APIs)

**Does not have access to:**
- Anything outside the project directory
- Your browser, Slack, or other apps
- Previous sessions (context resets by default)

Speaker note: The "context resets" point trips people up. If you start a new session, the agent doesn't remember the decisions you made in the last one. That's why context files exist.

---

## Slide 6: How the Agent Reads Files

- It does NOT read every file upfront
- It reads files on demand as it plans and executes
- Example: to write a test, it first reads your existing tests
- Implication: **inconsistent code leads to inconsistent agent output**

If you want the agent to follow your conventions, your codebase needs to demonstrate them consistently.

Speaker note: This is a subtle but important point. The agent learns from what it sees. If half your codebase uses async/await and half uses callbacks, don't be surprised when the agent picks arbitrarily. Consistency pays forward.

---

## Slide 7: The Autonomy Spectrum in Practice

**Acts immediately (green):**
- Read a file, run tests, search for patterns, analyze errors

**Asks before acting (yellow):**
- Install a package, create a new file, modify config

**Resists or refuses (red):**
- Delete directories, reset branches, destructive DB operations

Watch where your tool draws these lines. They tell you its defaults.

Speaker note: Suggest running a low-stakes task first specifically to observe the confirmation behavior. This calibration step is worth 10 minutes at the start of any new project.

---

## Slide 8: Calibrating Trust

Think of it like onboarding a new team member:
- You give them read access before write access
- You confirm their understanding before approving big changes
- You expand autonomy as trust is established

Same with an agent. Start constrained, verify output, loosen grip over time.

The goal is not maximum autonomy. It's calibrated autonomy.

Speaker note: This framing helps people who feel uncomfortable giving the agent "too much" power. You're not surrendering control, you're delegating within boundaries you set.

---

## Slide 9: Live Demo — DevBoard

[DEMO CUE] Switch to terminal with DevBoard open in Claude Code.

We will run three prompts in sequence:
1. Codebase exploration ("walk me through the structure")
2. Request trace ("trace a task creation from frontend to DB")
3. Constrained modification (add validation to POST /tasks, no other endpoints)

Watch for:
- Which files get read and when
- Where the confirmation prompt appears
- What the resulting diff looks like

Speaker note: Narrate what's happening in real time. Point out the tool output lines showing file reads. Make the "observe" phase visible because it's usually the least dramatic but most important part.

---

## Slide 10: The Core Loop, Demonstrated

Explore. Understand. Constrain. Act.

- Explore: ask it what's there before asking it to change anything
- Understand: verify its model matches reality
- Constrain: scope your task explicitly
- Act: let it run, review the diff, iterate

**Hands-on exercises after lunch** start with exploration and build up to a full feature addition.

Speaker note: Land on this as a repeatable pattern they can use outside the workshop. The four words are the takeaway from M02.
