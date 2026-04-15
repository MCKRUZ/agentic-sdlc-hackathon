# M01: The Agentic Mental Shift — Presenter Script
**Duration:** 30 minutes
**Format:** Lecture with room check-ins

---

## 1. Opening Hook (2 min)

[SLIDE]

Let's start with two scenarios.

Scenario one: You're in your editor. You type a function signature and your AI tool suggests the next line. You accept it, keep typing, it suggests more. You're driving, it's helping you steer. That's a copilot. That's what most of you have probably used.

Scenario two: You open a terminal, type "Add user authentication to this app using JWT, follow the existing patterns in the codebase, and write tests," and then you wait. The agent reads your codebase, plans a sequence of steps, creates files, modifies existing ones, runs your test suite, fixes what broke, and comes back to you with a diff.

You didn't steer. You delegated.

That shift, from steering to delegating, is what this module is about. It sounds small. It isn't.

[PAUSE] Show of hands: how many of you have used a copilot-style tool before? GitHub Copilot, Tabnine, anything like that. Good. How many have used something agentic, where it actually went and did multiple things on its own? Smaller group, which is exactly why we're here.

---

## 2. What Is an Agent? (8 min)

[SLIDE]

The word "agent" gets thrown around a lot. Let's pin down what it actually means in this context.

An agent is a system that operates in a loop. That loop has four stages: observe, plan, act, verify.

[SLIDE]

**Observe.** The agent takes in context. In a software development agent, that means reading files, understanding directory structure, looking at your git history, checking what dependencies you have. It builds a model of your current situation before it does anything.

**Plan.** Based on what it observed, it figures out what steps are needed to accomplish your goal. This isn't magic. It's the model reasoning through the problem: "To add authentication, I need to install these packages, create these files, modify this route handler, update these tests."

**Act.** It executes those steps. It writes files. It runs shell commands. It calls tools. This is where it differs from a pure text model: it's not just generating text, it's taking actions with real side effects.

**Verify.** After each action, it checks whether the outcome matched the expectation. If your tests fail after a change, a well-designed agent will notice and either fix it or tell you it got stuck.

Then it loops. Observe the new state, plan the next step, act, verify. Over and over until the task is done or it hits a blocker it can't resolve.

[SLIDE]

Let me make this concrete. You tell an agent: "The checkout page throws a 500 error when the cart is empty."

Here's what happens internally:

1. It reads your error logs or asks you for a stack trace.
2. It finds the relevant route handler and template.
3. It identifies the null reference causing the crash.
4. It writes a fix.
5. It runs your test suite to confirm nothing else broke.
6. It reports back.

You gave it one sentence. It did six things.

[PAUSE] Any questions so far on the loop concept? The terminology matters less than the mental model: it's not responding to prompts, it's executing a plan.

---

## 3. Agent vs. Copilot: The Real Difference (8 min)

[SLIDE]

Let's be precise about the distinction, because "AI coding tool" covers a huge spectrum.

A copilot completes text. You write context, it predicts what comes next. It's useful. It's fast. But it is stateless between suggestions, it doesn't hold a goal across multiple steps, and it doesn't take actions outside the editor. It's pattern-matching with very good taste.

[SLIDE]

An agent holds a goal. It maintains state across a multi-step task. It uses tools, meaning it can actually do things: read and write files, run shell commands, call APIs, search the web, query a database. And it makes decisions about what to do next based on what it observes.

Here's a practical table to keep in your head:

| Dimension | Copilot | Agent |
|---|---|---|
| Unit of work | One suggestion | One task |
| Memory | None between suggestions | Persistent within a session |
| Tool access | None | File system, shell, APIs |
| Autonomy | Zero | Low to high depending on config |
| Failure mode | Bad suggestion | Bad action with real side effects |

That last row matters. A bad autocomplete suggestion is easy to reject. A bad agentic action might have already modified three files and run a migration before you noticed. This is why the trust and permissions model exists, and we'll get to that in a moment.

[SLIDE]

The other thing to understand is context window vs. working memory. A copilot only knows about what's currently visible in your editor. An agent actively builds context by reading files, indexing your project, and holding relevant pieces in its working memory across the full task.

This is why an agent can answer "why does the AuthService behave differently in tests?" even if you haven't opened that file. It found it.

[PAUSE] Let me check: is the distinction between text completion and autonomous task execution landing? This is foundational for the rest of the day.

---

## 4. The Tool Permissions Model (7 min)

[SLIDE]

Every serious agentic tool has some version of a permissions model. The mental model I use is three colors: green, yellow, red.

[SLIDE]

**Green: just do it.** These are actions where the cost of being wrong is low and the cost of asking is higher. Fix a lint error. Run the test suite. Read a file to understand context. Format code. If the agent hesitates on these, it becomes annoying and slow. Good tools default to acting on green tasks without asking.

**Yellow: ask first.** These are actions with real consequences that aren't easily reversed, or actions that might exceed the scope you intended. Installing a new dependency. Creating a new file or directory. Modifying a build configuration. Anything touching authentication or payments. For yellow tasks, the agent should tell you what it wants to do and get confirmation before proceeding. You're still in control, you're just not micromanaging.

**Red: never without explicit instruction.** Deleting files. Force-pushing to main. Changing production configuration. Anything that could cause data loss or outage. A well-configured agent refuses these by default, even if you accidentally phrase a prompt in a way that implies it.

[SLIDE]

Why does this matter to you as a developer? Because you need to configure it, and you need to trust it.

If you haven't set up your permissions model, the agent will use its defaults, which may be more or less conservative than you want. Overly conservative means it asks you about everything and slows you down. Overly permissive means it takes actions you didn't intend.

The right setup is: liberal on reads and analysis, cautious on writes, strict on destructive operations.

[PAUSE] We'll look at exactly how to configure this in M03 when we get into project context files. For now, just internalize the three tiers.

---

## 5. Why Prompting an Agent Differs (5 min)

[SLIDE]

The last thing to cover before we move to the tools themselves: how you communicate with an agent is different from how you talk to a chatbot.

With a chatbot, you ask questions. "How do I implement a rate limiter in Express?" It explains. You take the explanation and do the work.

With an agent, you write instructions. "Implement rate limiting on all public API endpoints using the express-rate-limit package. Limit to 100 requests per 15 minutes per IP. Add integration tests. Follow the existing middleware pattern in src/middleware."

Notice the difference. You're not asking it to explain. You're giving it a job, with constraints, with scope, with acceptance criteria baked in.

[SLIDE]

Four things that make agent prompts effective:

**Scope:** What's in, what's out. "Only modify files in src/api. Don't touch the auth module."

**Constraints:** Your conventions. "Follow the existing error handling pattern. Use the logger service, not console.log."

**Acceptance criteria:** What done looks like. "All existing tests must still pass. The new endpoint needs at least two tests."

**Escalation hints:** When to stop and ask. "If you're not sure whether to modify the schema, stop and ask me."

You don't need all four in every prompt. But the more you include, the fewer interruptions you'll get and the less cleanup you'll do afterward.

[SLIDE]

One more thing: specificity beats length. A 10-word precise instruction beats a 100-word vague one. The agent can't read your mind. If you say "make it better," it will guess what you mean. Sometimes correctly, sometimes not.

Say what you actually want. That's the whole skill.

[PAUSE] Questions before we move to M02? We're about to get hands-on with the actual tools, so this is a good moment to make sure the mental model is solid.

---

*End of M01 script. Total estimated time: 28-32 minutes with pauses.*
