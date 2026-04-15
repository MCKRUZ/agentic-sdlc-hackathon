# Skill: /workshop-lab

## Trigger

`/workshop-lab`

## Description

Generates a new lab by creating the base instructions file and a Claude Code track variant from the project lab template. Prompts for the required inputs, then writes both files.

## Instructions

When this skill is triggered, do the following:

### Step 1 — Gather Inputs

Ask the user for the following. Collect all of them in a single prompt response before proceeding:

1. **Lab ID** — zero-padded two-digit number and short slug, e.g. `lab-03-context-files`
2. **Lab Title** — human-readable title, e.g. "Writing Your First CLAUDE.md"
3. **Duration** — estimated completion time in minutes, e.g. `30`
4. **Parent Module ID** — the module this lab belongs to, e.g. `03-context-files`
5. **Objectives** — a comma-separated list of 2–4 measurable outcomes, e.g. "create a CLAUDE.md, define autonomy tiers, verify the agent respects them"
6. **Tracks** — which tool tracks this lab supports (choose one or more: `all`, `claude-code`, `cursor`, `copilot`)

If any of these are missing from the trigger command, ask for them before writing any files.

### Step 2 — Derive Values

From the inputs, derive:

- `LAB_DIR` = `content/labs/{{ LAB_ID }}/`
- `INSTRUCTIONS_PATH` = `content/labs/{{ LAB_ID }}/instructions.md`
- `CLAUDE_TRACK_PATH` = `content/labs/{{ LAB_ID }}/claude-code-track.md`
- `DONE_CRITERIA` — one done criterion per objective, phrased as an observable outcome (not "I understand X" but "X file exists / test passes / command succeeds")

### Step 3 — Read Template

Read the template file before generating output:

- `templates/lab-instructions.md`

### Step 4 — Generate Base Instructions File

Write `content/labs/{{ LAB_ID }}/instructions.md` using the lab template as the base structure. Fill in all `{{ PLACEHOLDER }}` values using the inputs gathered in Step 1. Apply these rules:

- Set `LAB_ID`, `LAB_TITLE`, `DURATION`, `PARENT_MODULE_ID`, `PARENT_MODULE_TITLE` from inputs
- Set `TRACK` to the tracks provided (if `all`, write "All Tracks")
- Convert each objective into a numbered Step group — create one Part per 2–3 related objectives
- Generate Done Checklist items directly from the objectives, phrased as observable outcomes
- Pre-populate 3 Troubleshooting entries with the most common failure modes for this type of lab:
  - If the lab involves a config file: "Config file not found"
  - If the lab involves running a command: "Command not found / permission denied"
  - If the lab involves an AI tool: "Agent ignoring the context file"
  - Add a third entry relevant to the specific lab content
- Set Stretch Goals to `{{ STRETCH_GOAL_PLACEHOLDER }}` — do not invent stretch goals
- Leave all `{{ CODE_OR_COMMAND }}` placeholders intact for the author to fill in

### Step 5 — Generate Claude Code Track Variant

Write `content/labs/{{ LAB_ID }}/claude-code-track.md`. This file is a variant of the base instructions tailored specifically for Claude Code users. Structure:

```markdown
# Lab {{ LAB_ID }}: {{ LAB_TITLE }} — Claude Code Track

> This is the Claude Code variant of the lab. For the tool-agnostic version,
> see instructions.md.

## Claude Code-Specific Setup

- Ensure Claude Code is installed: `npm install -g @anthropic-ai/claude-code`
- Verify version: `claude --version`
- Working directory: the project root from the hackathon repo

## Steps

<!-- Mirror the steps from instructions.md, but replace all generic
     "open your AI tool" references with specific Claude Code commands,
     slash commands, and @ file references.

     Example substitutions:
       Generic: "Ask your agent to explain the codebase"
       Claude Code: `claude "Give me a map of this codebase..."` or use /explain

     Leave {{ STEP_CONTENT }} placeholders where the base instructions
     have not yet been filled in. -->

{{ CLAUDE_CODE_STEPS }}

## Claude Code Tips for This Lab

- Use `@filename` to give the agent direct file context without copy-paste
- Use `/clear` between exercises to reset context
- The CLAUDE.md you create in this lab will take effect immediately in the same session
```

### Step 6 — Confirm Output

After writing both files, output:

```
Lab {{ LAB_ID }} created:
  Base instructions : content/labs/{{ LAB_ID }}/instructions.md
  Claude Code track : content/labs/{{ LAB_ID }}/claude-code-track.md

Parent module      : content/modules/{{ PARENT_MODULE_ID }}/
Tracks supported   : {{ TRACKS }}

Remaining placeholders to fill in manually:
  - Step content and code/command examples in both files
  - Stretch goals
  - Any track-specific step variations (Cursor, Copilot) if applicable
```

List any additional placeholders that were not automatically filled.

## Notes

- Do not modify `templates/lab-instructions.md` — it is a read-only source template.
- Do not create the lab directory if it already exists without confirming with the user first.
- If additional tracks (Cursor, Copilot) were specified, note in the output that those variant files are not generated by this skill and must be created manually or by re-running with a track-specific skill.
- If `workshop.yaml` exists at the project root, prompt the user to add the new lab entry manually — do not modify `workshop.yaml` automatically.
