# Lab 01: Your First Agent Interaction

**Duration:** 30 minutes
**Track:** All tools

## Objectives

- Launch an AI agent against a real codebase and observe how it navigates files
- See how an agent reasons about code quality and risk
- Watch an agent make and revert a real code change
- Complete a multi-step task (comment + test) in a single conversation

## What You'll Do

- Point your agent at a project and ask it to explain the codebase
- Request a risk assessment and a targeted code edit
- Generate a test for the edited function, then undo all changes

## Prerequisites

- Your agent tool is installed and authenticated (see your track file if not)
- You have a project to work with: use your own, or clone the sample DevBoard project
  ```
  git clone https://github.com/MCKRUZ/devboard-sample
  ```
- Git is initialized in the project directory (`git init` if needed, then make an initial commit)

---

## Background

AI coding agents don't just complete individual prompts. They explore your codebase the same way a new teammate would: reading files, following imports, and building a mental model before acting. This lab is about observing that process, not just getting output. Pay attention to which files the agent opens, what it says before it acts, and where it hedges.

Most agents support multi-turn conversation within a session. The context from step 2 carries into step 3 and beyond. By the end of this lab you'll have run a complete mini-workflow: understand, assess, edit, test, revert. That sequence is the foundation of everything else in this hackathon.

---

## Steps

### 1. Launch your agent and point it at a project

Open your agent tool and start a new session in your project directory. The exact command depends on your tool -- see your track file.

**Expected output:** The agent acknowledges the working directory or lists files. Some tools show a file tree; others just show a prompt. Either is fine.

> If your tool asks you to select files or a folder, pick the project root.

---

### 2. Ask the agent to explain the codebase

Type this prompt exactly:

```
What does this codebase do? Give me a plain-English summary in 3-5 sentences.
```

Watch what happens before the answer arrives. Most agents will:
- Open and read several files (README, entry points, config files)
- Follow imports or dependency declarations
- Synthesize a summary from what they found

**Expected output:** A 3-5 sentence summary of the project's purpose. It should mention specific file or module names, not generic filler.

> If the summary is vague ("this is a web application"), prompt: "Be more specific. What problem does it solve and who uses it?"

---

### 3. Ask for a risk assessment

In the same session (do not start a new conversation), type:

```
What are the 3 biggest risks or code quality issues in this codebase? Be specific about file names and line numbers where possible.
```

**Expected output:** Three distinct concerns, each anchored to a real location in the code. Common findings include missing input validation, hardcoded configuration, large functions with no tests, or inconsistent error handling.

Note: the agent is working from the context it built in step 2 plus any additional reading it does now. You should see it open more files.

> If it gives generic advice ("you should add more tests"), push back: "Which specific function most needs a test, and why?"

---

### 4. Ask the agent to add a TODO comment

```
Find the most complex function in this codebase and add a TODO comment above it explaining what makes it complex and what a future developer should refactor first.
```

**Expected output:** The agent identifies a specific function, explains its reasoning for choosing it, and writes a TODO comment into the file. Most tools will show you a diff or highlight the change.

Confirm the file was actually modified:
- Check your editor, or
- Run `git diff` in your terminal

> If the agent asks for confirmation before writing, approve it. That's expected behavior.

---

### 5. Ask the agent to write a test

```
Write a unit test for the function you just commented. Use the testing framework this project already uses. If there are no existing tests, create a new test file following the conventions you see in the project.
```

**Expected output:** A new or modified test file with at least one test case for the target function. The agent should follow existing patterns (file naming, import style, assertion library) rather than inventing new ones.

Check that the test file exists and the test at minimum runs (even if it fails due to missing setup):
```
# Run whatever test command your project uses, e.g.:
npm test
pytest
dotnet test
```

---

### 6. Revert all changes

You've explored the agent's capabilities. Now undo everything so your project is clean.

**Option A -- use your agent:**
```
Revert all the changes you made in this session. The codebase should be exactly as it was when we started.
```

**Option B -- use git directly:**
```bash
git checkout .
git clean -fd
```

**Expected output:** `git status` shows a clean working tree with no modified or untracked files (other than files that existed before you started).

---

## Done?

- [ ] The agent produced a specific, accurate summary of the project (not generic filler)
- [ ] The risk assessment cited at least 2 real file names or line numbers
- [ ] A TODO comment was written into a real file and you confirmed the change with `git diff`
- [ ] A test file was created or modified with a test for the identified function
- [ ] All changes were reverted and `git status` shows a clean tree
- [ ] You observed the agent reading files before acting (not just jumping to output)

---

## Troubleshooting

**The agent says it can't access files or the directory.**
Your tool needs to be launched from inside the project directory, or you need to explicitly point it at the folder. Check your track file for the correct launch command. Some tools require you to open the folder through a UI rather than a terminal flag.

**The summary is completely wrong or nonsensical.**
The agent may have read the wrong directory. Confirm which folder it's working in by asking: "What is your current working directory and which files have you read so far?" Then relaunch from the correct location.

**The agent wrote a test using a framework the project doesn't use.**
This happens when there are no existing test files to imitate. Re-prompt: "The project uses [framework]. Rewrite the test using that framework only. Do not import anything that isn't already in package.json / requirements.txt / the .csproj file."

**Git revert didn't work cleanly.**
If `git checkout .` leaves untracked files behind, the agent created new files that aren't tracked by git. Run `git clean -fd` to remove them. If you're unsure what's new, run `git status` first to review before deleting.

---

## Stretch Goals

1. **Push the risk assessment further.** Pick one of the three risks the agent identified and ask it to fix the issue -- not just comment on it. Review the diff carefully: does the fix make sense, or did it break something?

2. **Test the test.** Intentionally break the function the agent tested (change a return value or condition), then run the test suite. Did the test catch the breakage? If not, ask the agent to strengthen it.

3. **Ask about architecture.** Prompt: "If you were onboarding a new engineer to this project, what would you tell them about the overall architecture? What would you warn them about?" Compare this answer to the risk assessment from step 3 -- do they agree?
