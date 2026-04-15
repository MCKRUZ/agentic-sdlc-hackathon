# Top 10 Agent Prompts That Actually Work

> A field reference for the Agentic SDLC Hackathon. Each pattern is tool-agnostic
> (Claude Code, Cursor, Copilot Chat, etc.) — adapt the phrasing to your tool of choice.

---

## 1. Codebase Exploration

**Pattern:** Orient me before I ask you to change anything.

**What it's for:** Getting an accurate mental model of an unfamiliar repo before making changes. Prevents the agent from hallucinating structure.

**Example:**

```
Give me a map of this codebase. For each top-level directory, one sentence on what lives
there and why. Then identify the entry point(s) for the main application flow and trace
the request path from HTTP in to database out — just the key files and function names,
no code yet.
```

---

## 2. Feature Planning

**Pattern:** Plan before you code. Show your work.

**What it's for:** Generating an implementation plan you can review and correct before any files are touched. Saves you from a large diff that goes the wrong direction.

**Example:**

```
I want to add {{ feature }}. Before writing any code, give me:
1. Which existing files will change and why
2. Any new files needed
3. External dependencies required
4. The order of implementation (what unblocks what)
5. Any design decisions I should weigh in on before you start

Do not write code yet.
```

---

## 3. Code Review

**Pattern:** Review this like a senior engineer on my team, not a polite assistant.

**What it's for:** Getting substantive feedback, not just style nits. The explicit tone instruction suppresses sycophantic softening.

**Example:**

```
Review the diff below. Flag: security issues, logic bugs, missing edge cases, naming that
will confuse future readers, and anything that will break under load. For each finding,
give: file:line, the problem, and a concrete fix. Do not mention things that are fine.

{{ paste diff or @file reference }}
```

---

## 4. Test Generation

**Pattern:** Tests first, then ask me what's missing.

**What it's for:** Generating a full test suite for a function or module, then surfacing coverage gaps the agent itself isn't confident about.

**Example:**

```
Write unit tests for {{ function/class }}. Cover: happy path, all documented edge cases,
invalid inputs, and boundary conditions. Use {{ xUnit | pytest | Jasmine }} with
Arrange-Act-Assert layout. After writing the tests, list any scenarios you weren't sure
how to test and explain why.
```

---

## 5. Refactoring

**Pattern:** Improve the code, explain each change, leave behavior identical.

**What it's for:** Getting clean, reviewable refactors with an audit trail — especially useful when you need to justify the changes to a teammate.

**Example:**

```
Refactor {{ file or function }} to improve readability and reduce complexity. Rules:
- Do not change observable behavior
- Do not add new features
- Each change must have a one-line comment explaining why (remove comments after I approve)
- If you see something broken that is out of scope, flag it but do not fix it
```

---

## 6. Debugging

**Pattern:** Reproduce first, fix second.

**What it's for:** Forcing the agent to reason about root cause before touching code. Prevents "fix the symptom" patches.

**Example:**

```
Here is the bug: {{ description }}
Here is the error / unexpected output: {{ paste }}
Here is the relevant code: {{ @file or paste }}

Step 1: Explain what you think is causing this and why.
Step 2: Identify the minimal reproduction case.
Step 3: Propose a fix. Do not implement it yet — wait for my confirmation.
```

---

## 7. Documentation

**Pattern:** Write for the next developer, not for completeness.

**What it's for:** Getting docs that explain the "why" and "gotchas" rather than restating what the code obviously does.

**Example:**

```
Write documentation for {{ module/function/API }}. Target audience: a mid-level developer
who has never seen this codebase. Include: purpose, key assumptions, parameters with types
and constraints, return values, error conditions, and one realistic usage example. Skip
anything self-evident from the function signature.
```

---

## 8. Commit Messages

**Pattern:** Conventional commits, imperative mood, explain the why in the body.

**What it's for:** Generating commit messages that are useful in `git log` six months from now, not just "fixed stuff".

**Example:**

```
Write a conventional commit message for this diff. Format:
  type: short imperative summary (under 72 chars)

  Body: what changed and WHY (not what — the diff shows what). If there is a trade-off
  or a decision that isn't obvious, explain it here.

{{ paste diff }}
```

---

## 9. PR Descriptions

**Pattern:** Summary + test plan + reviewer hints.

**What it's for:** PRs that reviewers can actually evaluate without reading every line of the diff.

**Example:**

```
Write a pull request description for these changes. Include:
1. What this PR does (2–3 sentences, non-technical enough for a PM to follow)
2. Why it was done this way (key design decisions)
3. What to look at carefully in review (the riskiest parts)
4. Test plan: what was tested, how to verify manually
5. Any follow-up work intentionally left out of scope

Diff: {{ paste or @branch }}
```

---

## 10. Explaining Unfamiliar Code

**Pattern:** Explain, then give me a mental model I can hold in my head.

**What it's for:** Understanding complex code fast without having to read every line yourself. The "mental model" request forces the agent past surface description.

**Example:**

```
Explain {{ file or function }} to me. First, a plain-English summary of what it does and
why it exists. Then walk through the non-obvious parts line by line. Finally, give me a
one-paragraph mental model I can use to reason about this code without re-reading it —
what are the key invariants and the one thing I must not break?
```

---

## Quick Tips

- **Be specific about what NOT to do.** Agents are eager. "Do not change X" prevents surprises.
- **Ask for a plan before code** on anything touching more than two files.
- **Request confidence levels.** "If you're not sure about any part, say so" surfaces hallucinations.
- **Iterate in small steps.** One concern per prompt is faster than one giant prompt that goes sideways.
