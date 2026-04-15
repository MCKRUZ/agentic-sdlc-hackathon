# M02: OOB Tool Usage — Presenter Script
**Duration:** 30 minutes (including live demo)
**Format:** Lecture + live demo of DevBoard sample project

---

## 1. Getting It Running (5 min)

[SLIDE]

Before you can delegate anything, you need the tool running. Let's cover what that actually looks like across the main options, because "installation" varies more than it should.

For Claude Code, which is what we're using today, you need Node installed and then it's a single npm install command. It runs in your terminal and operates on whatever directory you point it at. There's no IDE plugin to configure.

For Cursor, you're installing a full editor fork. It replaces VS Code for the session. If you're already a VS Code user, the transition is almost invisible, but it is a different binary.

For GitHub Copilot Workspace, there's nothing to install. It lives in your browser, inside GitHub. The tradeoff is that it's more sandboxed: it can't run arbitrary shell commands the way a local agent can.

[SLIDE]

Three things you need regardless of which tool you use:

**An API key or authentication.** The agent calls a model under the hood. That call costs money or uses a quota. Know which account it's billing before you run a long task.

**A working project.** The agent isn't useful on an empty directory. It needs existing code to read, patterns to follow, tests to run. Today's sample project, DevBoard, gives you all of that.

**A configured permissions boundary.** We'll spend most of M03 on this. For now, start with the defaults and tighten them once you see what the tool does.

[PAUSE] Anyone not yet have the tool installed from the pre-work? Let's resolve that now before we go further. Installation issues mid-demo are painful.

---

## 2. Your First Prompt (8 min)

[SLIDE]

Most people's first instinct with an agentic tool is to ask it to build something. That's the wrong starting point.

Your first prompt should always be a question. Before you ask it to change anything, ask it to tell you what's there.

"Walk me through the structure of this project. What does each top-level directory contain? Where does a request come in and how does it get handled?"

This does two things. First, it tells you whether the agent has accurately understood your codebase. If it describes something wrong, you want to know that before it starts making changes. Second, it builds shared context between you and the agent. The response it gives you is a snapshot of its understanding, which you'll reference when you give it tasks.

[SLIDE]

The sequence that works reliably for onboarding to a new codebase:

**Step 1: Understand the structure.** "Describe the project layout and how the main pieces connect."

**Step 2: Understand a specific flow.** "Trace what happens from when a user submits the login form to when they get a session token."

**Step 3: Ask about conventions.** "What patterns does this codebase use for error handling? How are tests structured?"

**Step 4: Now modify.** Once you're confident the agent has an accurate model of the codebase, you can give it tasks with confidence.

Skipping to step 4 is tempting and often works, but when it doesn't, the failure is harder to diagnose because you don't know what the agent thought it was working with.

[PAUSE] This is the "understand before modify" principle. It applies to you as a developer too: you wouldn't modify a system you've never read. Don't expect the agent to do better than that.

---

## 3. What the Agent Sees (7 min)

[SLIDE]

Let's be concrete about what context the agent actually has when you give it a task.

By default, when you run Claude Code in a directory, it has access to:

- Everything in that directory and all subdirectories, recursively
- Your git history (it can read commit messages, diffs, branches)
- Your shell environment (the commands available on your PATH, environment variables)
- Any tools you've explicitly given it access to (web search, external APIs)

It does not have access to files outside the project directory unless you explicitly tell it to look there. It does not know what's in your browser, your Slack, or your head.

[SLIDE]

What gets read when is determined by the task. The agent doesn't read every file upfront. It reads files on demand as it plans and executes. When it needs to understand how you handle errors, it searches for error handling patterns and reads the relevant files. When it needs to write a test, it reads the existing test files first to understand the structure.

This has a practical implication: **the agent's behavior is sensitive to what's in your codebase.** If your existing tests are well-structured and consistent, the agent will write tests that match. If your codebase is inconsistent, the agent will make choices you might not like because it has no single pattern to follow.

[SLIDE]

Two things that shape what the agent can see beyond the raw files:

**Context files.** Files like CLAUDE.md or .cursorrules are read at the start of every session. They're where you put project-level instructions that override the agent's defaults. We cover these in detail in M03.

**Conversation history.** Within a session, the agent remembers everything you've said and done. If you told it in message 3 to use the logger service instead of console.log, it should still be doing that in message 15. Sessions don't persist by default, so starting a new session resets this.

[PAUSE] Any questions about the context model before we talk about when the agent acts vs. asks?

---

## 4. The Autonomy Spectrum (5 min)

[SLIDE]

Not every action the agent considers is equal, and a well-designed tool treats them differently. We covered the green/yellow/red model in M01. Here's what that looks like in practice.

When the agent reads a file, it just does it. No prompt, no confirmation. Same with running your test suite to check if something works, analyzing a stack trace, or searching for a pattern across your codebase. These are read-only or low-risk operations.

When the agent wants to install a package, create a new file, or modify a config it hasn't touched before, it should pause and tell you what it's about to do. "I'm going to install express-rate-limit and add a middleware file at src/middleware/rateLimit.ts. Should I proceed?" You say yes or no. It's not asking you to make the decision for it; it's confirming scope.

When something is genuinely destructive, a well-configured agent won't do it even if your prompt implies it. Deleting a folder. Dropping a table. Resetting the main branch. If the agent you're using will do these things without resistance, that's a configuration problem.

[SLIDE]

The practical takeaway: when you're first using a tool, give it low-stakes tasks and watch where it asks for confirmation and where it acts immediately. That tells you what its defaults are. If it's too quiet (acting on things you'd want to approve), add explicit escalation hints to your prompts. If it's too chatty (asking about obvious low-stakes reads), tighten your context file to tell it what's green.

You're calibrating trust, the same way you would with a new team member.

[PAUSE] That's a good segue into the live portion.

---

## 5. Demo Transition (5 min)

[SLIDE]

We're going to switch to live demo now using the DevBoard sample project. DevBoard is a minimal task management app with a Node/Express backend and a plain JavaScript frontend. It has intentional issues that we'll use throughout today.

[DEMO CUE] Switch to terminal. Show the DevBoard directory open in Claude Code. Share screen if presenting remotely.

Here's what we're going to do in sequence:

First, I'll run the "understand the structure" prompt so you can see what a good codebase exploration response looks like. Pay attention to what the agent gets right and what it might miss or approximate.

Second, I'll ask it to trace a specific request through the codebase. This shows how it reads files on demand rather than all upfront.

Third, I'll give it a modification task with a scope constraint and show you what the confirmation flow looks like before it changes anything.

[DEMO CUE] Run: "Walk me through the structure of this project. What does each top-level directory contain, and where does an incoming API request get handled?"

While the agent responds, point out:
- Which files it's reading (shown in the tool output)
- How it builds up its understanding incrementally
- The difference between what it read and what it inferred

[DEMO CUE] Follow up with: "Trace what happens when a user creates a new task. Start from the fetch call in the frontend and end at the database write."

After the trace, show one modification prompt:

[DEMO CUE] Run: "Add input validation to the POST /tasks endpoint. The title field is required and must be between 1 and 200 characters. Return a 400 with a clear error message if validation fails. Don't modify any other endpoint."

Show the confirmation step before it writes files. Show the resulting diff.

[SLIDE]

That's the workflow in practice: **Explore → Plan → Code → Commit**. Start by exploring the codebase until you understand what's there. Plan what you'll do — for larger changes, use Plan Mode: type `/plan` in Claude Code to get an explicit step-by-step plan the agent will wait for you to approve before touching any file. Code the changes with tight scope. Then commit.

The Explore and Plan steps are what most people skip, and that's exactly where the surprises come from. Spend the time upfront.

In the hands-on section after lunch, you'll do this yourself with DevBoard. The exercises will walk you through progressively more complex tasks, starting with read-only exploration and ending with a feature addition that requires the agent to make decisions about scope.

Any questions before we break?

---

*End of M02 script. Total estimated time: 28-32 minutes with pauses and demo.*
