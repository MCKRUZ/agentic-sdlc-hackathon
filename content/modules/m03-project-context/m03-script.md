# M03: Project Context Files — Presenter Script
**Duration:** 20 minutes (including live demo)
**Format:** Lecture + brief live demo

---

## 1. The Problem Without Context (4 min)

[SLIDE]

Here's a scenario you'll hit within your first hour of using an agent on a real project.

You ask it to add a new API endpoint. It writes one. The code is technically correct, syntactically fine, and completely inconsistent with everything else in your codebase. It uses a different error handling pattern. It logs with console.log instead of your logger service. It structures the route file differently from every other route file. It works, but merging it creates noise.

This isn't a bug. It's the expected behavior when you haven't told the agent anything about your project. It's working from general knowledge of what good Node code looks like, not from your specific conventions.

The fix is simple: write them down. Put them somewhere the agent reads at the start of every session. That's what context files are.

[SLIDE]

This problem scales with team size. On a solo project, inconsistency is annoying. On a team where three people are each running agents against the same codebase, inconsistency becomes a merge nightmare. Context files are how you give every session, regardless of who runs it, the same baseline instructions.

[PAUSE] Before we talk about what to put in these files, quick check: has anyone already run into the "it works but doesn't match our codebase" problem today in the exercises? That's exactly the symptom.

---

## 2. What Context Files Are (4 min)

[SLIDE]

Different tools use different names. The concept is the same across all of them.

Claude Code reads a file called `CLAUDE.md`. Cursor reads `.cursorrules`. Some tools read a `system_prompt.txt` or similar. If you're using an agent via API and building your own tooling, you inject it as the system prompt.

In every case, the file is read at the start of each session, before any user message, and its contents become standing instructions that apply to the entire conversation.

Think of it as your onboarding document for a contractor who has no memory between visits. Every time they show up, they read it fresh. So it needs to be complete enough to stand alone.

[SLIDE]

Three things these files are not:

**Not a chat message.** You're not asking the agent anything. You're giving it instructions it follows without being asked.

**Not a one-time setup.** Every session reads it. Change it when your conventions change.

**Not a replacement for good prompts.** The context file sets defaults. Individual prompts override or extend those defaults for a specific task. Both matter.

---

## 3. What to Put in Them (8 min)

[SLIDE]

Let's go through the categories of content that belong in a project context file.

**Persona and role.** Tell the agent who it is in your project. "You are a senior backend engineer on this team. You write TypeScript. You follow the conventions in this codebase." This seems obvious but it matters: without it, the agent adopts a generic helpful assistant mode that doesn't match how a developer colleague would behave.

**Tech stack.** List the actual technologies. "Node 20, Express, TypeScript 5, Postgres via Prisma, Jest for testing, Pino for logging." Don't make it guess. A wrong guess about your ORM leads to generated code that doesn't run.

[SLIDE]

**Coding conventions.** This is the most important section and the one most people skip. Document the patterns you actually use, not the ones you aspire to. Specific examples beat vague descriptions.

Bad: "Follow clean code principles."
Good: "All errors are handled via the Result<T> pattern in src/types/result.ts. Never throw from service layer functions. Use the logger service (src/services/logger.ts), not console.log."

The more specific, the less cleanup.

**What NOT to do.** Explicit prohibitions are often more valuable than positive instructions because the agent has no way to infer them from the codebase. "Do not add new npm dependencies without asking first. Do not modify the auth module. Do not create utility functions outside src/utils."

[SLIDE]

**Workflow instructions.** How do you want the agent to work? "Always run the test suite after making changes. If tests fail, fix them before reporting done. Write tests for any new public functions." These are your acceptance criteria baked in at the project level, so you don't have to repeat them in every prompt.

**Autonomy rules.** Which actions should it take immediately, which should it confirm, which should it refuse? "Read files and run tests freely. Ask before installing packages or creating new directories. Never delete files."

[SLIDE]

A complete context file for a real project is usually 50 to 150 lines. It doesn't need to be comprehensive on day one. Start with the three things that, if the agent gets wrong, cause the most pain: tech stack, error handling pattern, test conventions. Add more when you notice recurring corrections.

If you find yourself typing the same correction in multiple sessions, that correction belongs in the context file.

[PAUSE] Quick exercise: think about the last time you reviewed code from a contractor or a new team member and gave feedback. What were the top three things you had to correct? Those belong in your context file.

---

## 4. Scoped Context (4 min)

[SLIDE]

Most tools support multiple levels of context, applied in order from most general to most specific.

**Global context.** Applies to every project you work on. Your personal preferences: preferred language, general coding philosophy, how you want the agent to communicate with you. In Claude Code, this is in your home directory.

**Project context.** Applies to one repository. Your tech stack, conventions, workflow rules. Lives in the root of the repo, typically checked into version control so the whole team shares it.

**Folder context.** Some tools let you put a context file in a specific subdirectory. That context applies only when the agent is working in that folder. Useful for monorepos where a frontend package and a backend package have completely different conventions.

[SLIDE]

The practical recommendation: start with a project-level context file committed to the repo. Get that right before you worry about global or folder-level. Most of the value is at the project level.

One important note on version control: your context file is code. Review it in PRs. If someone changes it, you want to know. An undiscovered change to your context file can cause an entire session worth of agent output to diverge from your standards without any obvious cause.

[DEMO CUE] Open the DevBoard repo. Show the CLAUDE.md file that's already in the project. Walk through each section: tech stack, conventions, workflow rules, autonomy config. Then run a prompt without it and show the difference in output quality.

The difference is immediate and obvious. That's the demo. You don't need anything dramatic. The contrast does the work.

[PAUSE] Any questions before we break for the hands-on block? The exercise for this module is writing your own context file for DevBoard from scratch, then comparing it to the one we ship with the sample project.

---

*End of M03 script. Total estimated time: 18-22 minutes with pauses and demo.*
