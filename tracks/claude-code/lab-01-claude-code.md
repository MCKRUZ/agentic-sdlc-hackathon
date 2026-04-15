# Lab 01 — Claude Code: Your First Agent Interaction

This is the Claude Code variant of Lab 01. Follow these instructions instead of the generic "launch your agent" steps in the main lab guide.

---

## Start Claude Code

Open your terminal, navigate to the lab project directory, and run:

```bash
cd /path/to/lab-project
claude
```

Claude Code prints a welcome message and shows the current directory. You are now in the interactive REPL. Every prompt you type goes directly to Claude.

---

## Give It Starting Context

Your first message should orient Claude Code to the project. Type this at the prompt and press Enter:

```
This is a Node.js Express API project. Read the package.json and src/ directory so you understand the structure before I give you tasks.
```

Claude Code will ask permission to read files. Type `y` to approve, or `a` (always) to approve all Read operations for the session without being asked again.

Wait for Claude Code to finish exploring before moving on.

---

## How to Approve or Deny Tool Use

Every time Claude Code wants to run a tool (read a file, execute a command, write code), it pauses and shows you what it plans to do.

Your options:

| What you type | What happens |
|---|---|
| `y` | Approve this one action |
| `n` | Deny this action, Claude Code will try another approach |
| `a` or `always` | Approve this tool type for the rest of the session |
| `d` or `details` | Show more detail about what it plans to do |

For this lab, use `y` for each request so you see what Claude Code is doing. Once you are comfortable, use `always` for Read and Grep operations to speed up the workflow.

---

## Task 1: Explore the Codebase

Type this prompt:

```
List all the API endpoints defined in this project and tell me what each one does.
```

Watch Claude Code read files and reason about the structure. It will use Read and Grep tools. Approve each one with `y`.

**What to notice**: Claude Code shows you the tool it wants to use and the exact arguments before it runs. You are in control of every action.

---

## Task 2: Find a Bug or Code Smell

Type this prompt:

```
Look at the route handlers in this project. Are there any missing error handling, unvalidated inputs, or obvious bugs? Show me the exact lines.
```

Claude Code will read specific files and give you an assessment with file paths and line numbers.

---

## Task 3: Write a Test

Type this prompt:

```
Write a unit test for the GET /users endpoint. Use whatever test framework is already in this project. Put the test in the correct test directory.
```

Claude Code will ask to write a file. Review what it plans to write, then approve with `y`.

---

## Task 4: Refactor One Function

Type this prompt:

```
Find the longest function in the src/ directory and refactor it to be more readable. Keep the behavior identical.
```

Claude Code will identify the function, explain the refactor plan, and ask to write the file. Read its explanation before approving.

---

## Task 5: Generate a Summary

Type this prompt:

```
Write a one-paragraph summary of what this project does, suitable for a README introduction.
```

This task requires no file writes, so no approvals are needed. Claude Code will just respond with text.

---

## Revert a Change You Do Not Like

If Claude Code made a change you want to undo:

**Option 1: Use `/undo`**

Type `/undo` at the prompt. This reverts the last file write Claude Code performed. You can run it multiple times to step back through recent changes.

**Option 2: Use git**

If your project is a git repo:

```bash
git checkout -- src/some-file.js
```

Or to revert everything since the last commit:

```bash
git checkout -- .
```

`/undo` only knows about changes made in the current Claude Code session. For anything older, use git.

---

## Reset the Conversation

If Claude Code seems confused, is carrying irrelevant context from earlier in the session, or you want to start fresh without exiting:

```
/clear
```

This wipes the conversation history. Claude Code stays running, but it no longer remembers earlier prompts. It still has access to your CLAUDE.md instructions and the current directory.

Use `/clear` between labs or when switching to a completely different task.

---

## End the Session

When you are done:

```
/exit
```

Or press Ctrl+D. Your files are saved. Nothing is lost.
