# Skill: /workshop-module

## Trigger

`/workshop-module`

## Description

Generates a new workshop module by creating both the presenter script and the slide outline from the project templates. Prompts for the required inputs, then writes both files.

## Instructions

When this skill is triggered, do the following:

### Step 1 — Gather Inputs

Ask the user for the following. Collect all of them in a single prompt response before proceeding:

1. **Module ID** — zero-padded two-digit number and short slug, e.g. `03-context-files`
2. **Module Title** — human-readable title, e.g. "Writing Effective Context Files"
3. **Duration** — total module time in minutes, e.g. `45`
4. **Key Concepts** — a comma-separated list of 3–5 core ideas this module teaches, e.g. "CLAUDE.md structure, autonomy tiers, naming conventions"
5. **Lab ID** (optional) — if this module has a corresponding lab, provide its ID, e.g. `lab-03`; otherwise leave blank

If any of these are missing from the trigger command, ask for them before writing any files.

### Step 2 — Derive Values

From the inputs, derive:

- `MODULE_DIR` = `content/modules/{{ MODULE_ID }}/`
- `SCRIPT_PATH` = `content/modules/{{ MODULE_ID }}/script.md`
- `SLIDES_PATH` = `content/modules/{{ MODULE_ID }}/slides.md`
- `SECTION_TITLES` — split the key concepts list into logical section titles (one concept per section where possible)

### Step 3 — Read Templates

Read both template files before generating output:

- `templates/module-script.md`
- `templates/module-slides.md`

### Step 4 — Generate Script File

Write `content/modules/{{ MODULE_ID }}/script.md` using the script template as the base structure. Fill in all `{{ PLACEHOLDER }}` values using the inputs gathered in Step 1. Apply these rules:

- Replace `{{ MODULE_ID }}`, `{{ MODULE_TITLE }}`, `{{ DURATION }}` with exact values provided
- Distribute the key concepts across Section 1, Section 2, Section 3 in the script body
- Set section durations so that Opening + Sections + Lab Handoff + Debrief = total DURATION
- Use `{{ LAB_ID }}` if provided; otherwise remove lab-related placeholders and note "No lab for this module"
- Leave `{{ DEMO_ID }}` placeholders intact — do not invent demo IDs
- Leave `{{ AUTHOR_NAME }}` and `{{ YYYY-MM-DD }}` as placeholders for the author to fill in
- Do not delete the marker convention comment block — it's reference material for the author

### Step 5 — Generate Slides File

Write `content/modules/{{ MODULE_ID }}/slides.md` using the slides template as the base structure. Fill in all `{{ PLACEHOLDER }}` values using the inputs gathered in Step 1. Apply these rules:

- Each key concept gets at least one slide
- Demo slides reference `[DEMO CUE: {{ DEMO_ID }}]` — leave the ID as a placeholder
- Code example slides use a fenced code block with `{{ LANGUAGE }}` as a placeholder
- Image slides reference `../../assets/images/{{ IMAGE_FILENAME }}` as a placeholder
- Maintain the `Speaker note:` convention on every slide

### Step 6 — Confirm Output

After writing both files, output:

```
Module {{ MODULE_ID }} created:
  Script : content/modules/{{ MODULE_ID }}/script.md
  Slides : content/modules/{{ MODULE_ID }}/slides.md

Remaining placeholders to fill in manually:
  - {{ AUTHOR_NAME }} and {{ YYYY-MM-DD }} in script metadata
  - [DEMO CUE: {{ DEMO_ID }}] — add real demo IDs once demos are written
  - {{ IMAGE_FILENAME }} — add asset paths once visuals are created
  - {{ LANGUAGE }} and code snippets in fenced blocks
```

List any additional placeholders that were not filled automatically.

## Notes

- Do not modify `templates/module-script.md` or `templates/module-slides.md` — they are read-only source templates.
- Do not create the module directory if it already exists without confirming with the user first.
- If `workshop.yaml` exists at the project root, prompt the user to add the new module entry manually — do not modify `workshop.yaml` automatically.
