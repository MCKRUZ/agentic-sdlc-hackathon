# M01: The Agentic Mental Shift — Slide Outline
**Module duration:** 30 minutes
**Slide count:** 10

---

## Slide 1: Two Scenarios

- **Copilot model:** You type, it suggests the next line. You're driving.
- **Agent model:** You describe a goal. It reads, plans, acts, and reports back.
- The shift is from steering to delegating.
- Today is about learning to delegate effectively.

Speaker note: Open with the contrast. Don't rush past it. This reframe is the whole point of the module. Ask the room which model they've actually used.

---

## Slide 2: The Agent Loop

Four stages, always in order:

1. **Observe** — reads your codebase, files, context
2. **Plan** — sequences the steps needed
3. **Act** — writes files, runs commands, calls tools
4. **Verify** — checks whether the outcome matched expectations, then loops

Speaker note: Draw this on a whiteboard if the room is engaged. The loop concept is more important than the terminology. Emphasize that it repeats until the task is done or it gets stuck.

---

## Slide 3: A Concrete Example

Task given: "The checkout page throws a 500 when the cart is empty."

What the agent does:
1. Reads the error log / stack trace
2. Locates the route handler and template
3. Identifies the null reference
4. Writes the fix
5. Runs the test suite
6. Reports back

One sentence in. Six steps out.

Speaker note: Walk through each step slowly. This makes the abstract loop concrete. Ask: "What would you have done manually?" Same steps, just slower.

---

## Slide 4: Agent vs. Copilot

| | Copilot | Agent |
|---|---|---|
| Unit of work | One suggestion | One task |
| Memory | None | Persistent within session |
| Tool access | None | File system, shell, APIs |
| Autonomy | Zero | Configurable |
| Failure mode | Bad suggestion | Bad action |

Speaker note: The failure mode row is the important one. Spend time on it. A bad suggestion costs 1 keystroke to reject. A bad action may have already modified files. This motivates the permissions model.

---

## Slide 5: Context Window vs. Working Memory

- **Copilot:** Only knows what's visible in the current editor tab
- **Agent:** Actively reads your project, indexes files, holds relevant pieces across the full task
- Result: the agent can answer questions about code you haven't opened
- Also means: what you give it as context shapes everything it does

Speaker note: This is why the agent can find the AuthService on its own vs. why the copilot can't. Leads naturally into context files in M03.

---

## Slide 6: The Permissions Model — Three Tiers

**Green — act without asking**
- Read files, run tests, fix lint, format code

**Yellow — ask before acting**
- Install packages, create files, modify build config, touch auth/payments

**Red — never without explicit instruction**
- Delete files, force push, change production config, destructive migrations

Speaker note: This is a mental model, not a specific UI. Every tool implements it differently. The point is that you should know which tier an action falls into before you give the agent a task.

---

## Slide 7: Why the Tiers Matter to You

- Too conservative = agent asks about everything, becomes friction
- Too permissive = agent takes actions you didn't intend
- Right setting: liberal on reads, cautious on writes, strict on destructive
- You configure this. It doesn't guess your preferences.

Speaker note: Transition: "We'll configure this in M03. For now, just hold the three-tier model in your head." Don't go down a rabbit hole on specific tool settings here.

---

## Slide 8: Prompting an Agent vs. Asking a Chatbot

**Chatbot:** You ask questions. It explains. You do the work.

**Agent:** You write instructions. It does the work.

The difference is scope, constraints, and acceptance criteria:
- "Implement rate limiting on all public endpoints using express-rate-limit, 100 req/15 min per IP, with integration tests, following the existing middleware pattern."

Speaker note: Read the example prompt aloud slowly. Ask the room: "What would you have typed into ChatGPT for the same task?" Compare the two. The agent prompt has scope, a specific library, limits, and a test requirement.

---

## Slide 9: The Four Elements of an Effective Agent Prompt

1. **Scope** — what's in, what's out ("only modify src/api")
2. **Constraints** — your conventions ("use the logger service, not console.log")
3. **Acceptance criteria** — what done looks like ("all existing tests must pass")
4. **Escalation hints** — when to stop ("if unsure about schema changes, ask first")

You don't need all four every time. The more you include, the less cleanup you do.

Speaker note: These four are a checklist, not a formula. Quick exercise: have the room rephrase "make the login page better" using this framework. Takes 2 minutes and makes the point immediately.

---

## Slide 10: Mental Model Summary

- An agent holds a goal and works toward it across multiple steps
- It uses tools (file system, shell, APIs) to take real actions
- Its failure modes have real consequences, so permissions matter
- You write instructions, not questions
- Specificity beats length every time

**Next up: M02 — getting your hands on the actual tools**

Speaker note: This is a recap slide. Don't read it verbatim. Just pause, let people absorb it, and ask if there are questions before transitioning to M02.
