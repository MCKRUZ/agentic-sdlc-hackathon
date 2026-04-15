# Lab 03: Build a Skill

**Duration:** 35 minutes
**Track:** All tools

## Objectives

- Identify a workflow in your development process that you repeat often enough to automate
- Write a reusable custom skill (slash command or prompt template) that encodes that workflow
- Test, refine, and share the skill with other hackathon participants

## What You'll Do

- Choose a workflow from the suggested list or bring your own
- Write a complete skill file using the provided anatomy
- Run the skill against real code, refine it, and share it

## Prerequisites

- Lab 01 complete (you can run a basic agent session)
- Lab 02 recommended (a context file makes skill output more accurate)
- Your agent tool supports custom skills or slash commands (see your track file -- most do)

---

## Background

A skill is a saved, reusable prompt with structure. Instead of typing a long prompt from memory every time you want a PR description written, you type `/pr-description` and the skill fires. The difference between a skill and a plain saved prompt is that a skill is explicit about its inputs, its expected output format, and its constraints. That structure is what makes the output consistent across different invocations.

Skills are also where you capture institutional knowledge. A "code review" skill for your team can encode your specific checklist -- security concerns, performance patterns, style rules -- rather than relying on the agent's generic best practices. Over time, a good set of skills is more valuable than any individual prompt, because they accumulate the judgment calls your team has already made.

---

## Steps

### 1. Choose a workflow to automate

Pick one from the list below, or bring your own if you have something more relevant.

**Suggested workflows:**

| Skill Name | What It Does |
|---|---|
| Commit message generator | Reads staged diff, writes a conventional commit message |
| PR description writer | Reads branch diff vs. main, writes title + summary + test plan |
| Code reviewer | Reviews a file or function against your project's standards |
| Test generator | Writes unit tests for a given function or class |
| Bug report formatter | Turns a freeform bug description into a structured report |
| Standup summary | Reads recent git log and open PRs, writes a standup update |
| Dependency auditor | Reviews added/changed dependencies for version and security concerns |
| Refactor planner | Identifies a complex function and proposes a refactor plan without changing code |

Pick the one that would save you the most time in a normal workweek. If none of these fit, define your own.

---

### 2. Learn the anatomy of a skill file

Every skill file has the same five parts:

```markdown
---
name: skill-name-here
description: One sentence. What does this skill do and when should you use it?
---

## Instructions

[Core prompt that runs when this skill is triggered. Written in second person ("You are...", "Your job is..."). Be specific about inputs, outputs, and constraints.]

## Input

[Describe what context the skill needs. Does it read staged files? The current file? A selected function? Be explicit.]

## Output Format

[Describe exactly what the output should look like. Include structure, length, and any required sections.]

## Constraints

[What should this skill never do? What assumptions must it not make?]

## Example

[One complete example: what the input looks like and what ideal output looks like. This is the most important part -- agents imitate examples more reliably than they follow prose instructions.]
```

The `name` and `description` fields power the slash command. The rest shapes the output.

---

### 3. Write your skill file

Create a new file with your skill's content. The location depends on your tool -- see your track file for the exact path. Common locations:

- Claude Code: `.claude/commands/skill-name.md`
- Cursor: `.cursor/rules/skill-name.mdc`
- Copilot: stored in the chat interface or `.github/`
- Continue: `.continue/prompts/skill-name.prompt`

**Work through each section of the anatomy.** Don't skip the Example section -- it is the single biggest factor in output quality.

Here is a complete example skill to use as a reference:

---

**Example: Commit Message Generator**

```markdown
---
name: commit-message
description: Generates a conventional commit message from the current staged diff.
---

## Instructions

You are a commit message writer. Your job is to read the staged git diff and produce a single, well-formed conventional commit message. You do not summarize every file changed -- you identify the intent of the change and express it concisely.

## Input

Read the output of `git diff --staged`. If there is no staged diff, say so and stop.

## Output Format

A single commit message in this format:

```
type(scope): short description under 72 characters

Optional body: explain WHY this change was made, not what files changed.
Wrap at 72 characters. Skip if the subject line is self-explanatory.

Optional footer: breaking changes, issue references (Closes #123).
```

Valid types: feat, fix, refactor, docs, test, chore, perf, ci, style

Rules:
- Lowercase subject line, no period at the end
- Imperative mood ("add feature" not "added feature" or "adds feature")
- Scope is optional but useful (e.g., "feat(auth): ...")
- Do not mention file names in the subject line
- Do not use the word "refactor" for bug fixes or new features

## Constraints

- Never invent functionality that isn't in the diff
- Never write a message longer than what the diff justifies
- If the diff is too large or unfocused to summarize in one message, say so and suggest splitting it

## Example

**Input diff (excerpt):**
```diff
+ export function validateEmail(email: string): boolean {
+   return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
+ }
```

**Output:**
```
feat(validation): add email format validator

Needed for user registration form. Using a regex that covers the common
case without the edge-case complexity of RFC 5321 full compliance.
```
```

---

### 4. Test the skill on real code

Trigger the skill in your agent. The exact invocation depends on your tool (see your track file):
- Claude Code: type `/commit-message` in the chat
- Cursor: type `/commit-message` in the composer
- Others: see track file

Run it against a real piece of your project. Stage a few files first if your skill needs a diff:
```bash
git add src/some-file.ts
```

Then trigger the skill and observe the output.

**Expected output:** Output that matches the format you defined in your skill file. It should feel noticeably more structured and consistent than a freeform prompt would produce.

---

### 5. Refine based on what it missed

Read the output critically. For each thing that's wrong or missing, add a constraint or example to your skill file. Common issues:

- Output is too long: add "Keep the output under X lines" to the Output Format section
- Wrong tone or vocabulary: add an example that shows the style you want
- Missing a required section: add it to the Output Format section explicitly
- Includes things you don't want: add them to Constraints

Make at least one refinement and re-run the skill. Compare the two outputs.

---

### 6. Share your skill

Paste the following into the shared document (link in Slack or posted by the facilitator):

- Skill name (the trigger word)
- One-sentence description of what it does
- One example of output it produced (just 3-5 lines is fine)

You'll be able to browse what other participants built during the debrief.

---

## Done?

- [ ] You chose a workflow from the list or defined your own
- [ ] The skill file has all five sections filled in (name, description, instructions, output format, constraints, example)
- [ ] The skill file is in the correct location for your tool
- [ ] You ran the skill on real code and got structured output
- [ ] You made at least one refinement and re-ran to confirm the improvement
- [ ] Your skill name and description are in the shared document

---

## Troubleshooting

**The slash command doesn't appear or doesn't trigger.**
The file is probably in the wrong location or has a syntax error in the front matter. Check that the `---` delimiters are present and that there are no extra spaces in the `name:` field. Restart your agent after creating the file -- most tools don't hot-reload skill files.

**The output ignores the format I specified.**
Your Output Format section is too abstract. Replace prose descriptions with a literal template. If you want a three-section output, show all three sections as headers with placeholder text. Agents reproduce structure they can see much more reliably than structure they have to infer from a description.

**The skill produces different output every time.**
Some variance is normal. If the output is radically different across runs, your instructions are ambiguous. The most common cause is a vague Instructions section. Rewrite it to remove any sentence that could be interpreted two different ways. The Example section is the strongest stabilizer -- make it more detailed.

**My tool doesn't support skill files.**
A few tools require skills to be configured through a UI rather than a file. Check your track file. If your tool has no skill support at all, save your skill as a plain text file and paste it as a system prompt at the start of each session -- it still gives you the consistency benefit.

---

## Stretch Goals

1. **Chain two skills.** Write a second skill that takes the output of the first as input. For example: a "PR description writer" that takes a commit message (from your commit-message skill) and expands it into a full PR body. Trigger them in sequence in one session.

2. **Add conditional logic.** Extend your skill to handle two different cases. For example, a code reviewer that behaves differently for test files vs. production code. Use explicit branching in your Instructions section: "If the file path contains `/test`, then... Otherwise..."

3. **Convert a team process into a skill.** Pick a process from your team's wiki or runbook -- a deployment checklist, an incident postmortem template, a sprint planning format. Convert it into a skill that generates a filled-in version of that document from project context. Run it and evaluate whether it would actually save time in practice.
