# Skill: /workshop-validate

## Trigger

`/workshop-validate`

## Description

Validates the completeness and consistency of all workshop content. Checks that every entry in `workshop.yaml` has the required files, that no TODO markers remain in scripts, and that every `[DEMO CUE]` marker has a corresponding entry in the facilitator guide.

## Instructions

When this skill is triggered, run all checks below in sequence. Collect all findings before reporting — do not stop at the first failure. Output a summary table at the end showing pass/fail per check.

---

### Check 1 — Module Files Exist

**Source of truth:** `workshop.yaml`

For every module listed under the `modules:` key in `workshop.yaml`:

1. Resolve the expected script path: `content/modules/{{ module.id }}/script.md`
2. Resolve the expected slides path: `content/modules/{{ module.id }}/slides.md`
3. Verify both files exist on disk

**Failure format:**
```
[FAIL] Module {{ module.id }}: missing {{ script.md | slides.md | both }}
```

**Pass format:**
```
[PASS] Module {{ module.id }}: script.md + slides.md present
```

---

### Check 2 — Lab Files Exist

**Source of truth:** `workshop.yaml`

For every lab listed under the `labs:` key in `workshop.yaml`:

1. Resolve the expected instructions path: `content/labs/{{ lab.id }}/instructions.md`
2. Verify at least one track file exists in the same directory:
   - `claude-code-track.md`
   - `cursor-track.md`
   - `copilot-track.md`
3. Both conditions must be true for a pass

**Failure format:**
```
[FAIL] Lab {{ lab.id }}: missing {{ instructions.md | all track files | both }}
```

**Pass format:**
```
[PASS] Lab {{ lab.id }}: instructions.md + at least one track file present
```

---

### Check 3 — No TODO Markers in Scripts

For every `script.md` file found under `content/modules/`:

1. Search for any of these patterns (case-insensitive):
   - `TODO`
   - `FIXME`
   - `{{ ` (unfilled placeholder — double curly brace with a space inside)
   - `[TODO`
2. Report each occurrence with file path and line number

**Failure format:**
```
[FAIL] {{ file_path }}:{{ line_number }} — TODO/unfilled placeholder: "{{ matched_text }}"
```

**Pass format:**
```
[PASS] No TODO markers or unfilled placeholders found in scripts
```

---

### Check 4 — DEMO CUE Markers Have Corresponding Facilitator Guide Entries

**Facilitator guide path:** `content/facilitator/facilitator-guide.md`

1. Scan every `script.md` file under `content/modules/` for all `[DEMO CUE: *]` markers
2. Extract the demo ID from each marker (the part after `[DEMO CUE: ` and before `]`)
3. For each extracted demo ID, verify that `content/facilitator/facilitator-guide.md` contains a section header or anchor referencing that ID
   - Match strategy: look for `## {{ DEMO_ID }}` or `### {{ DEMO_ID }}` or `<!-- demo: {{ DEMO_ID }} -->` in the guide
4. Report any demo IDs found in scripts that have no corresponding entry in the guide

**Failure format:**
```
[FAIL] Demo ID "{{ demo_id }}" referenced in {{ script_path }}:{{ line_number }} has no entry in facilitator-guide.md
```

**Pass format:**
```
[PASS] All DEMO CUE markers have corresponding facilitator guide entries
```

---

### Check 5 — Module IDs in workshop.yaml Match Directory Names

For every module in `workshop.yaml`:

1. Confirm that `content/modules/{{ module.id }}/` directory exists
2. Confirm the module ID in `workshop.yaml` exactly matches the directory name (no case drift, no typos)

**Failure format:**
```
[FAIL] Module "{{ module.id }}" in workshop.yaml has no matching directory content/modules/{{ module.id }}/
```

---

### Check 6 — Lab IDs in workshop.yaml Match Directory Names

Same as Check 5 but for labs under `content/labs/`.

---

### Output Format

After running all checks, print:

```
Workshop Validation Report
==========================
Generated: {{ current date and time }}

RESULTS
-------
Check 1 — Module files         : {{ PASS | FAIL (N issues) }}
Check 2 — Lab files            : {{ PASS | FAIL (N issues) }}
Check 3 — TODO markers         : {{ PASS | FAIL (N issues) }}
Check 4 — DEMO CUE coverage    : {{ PASS | FAIL (N issues) }}
Check 5 — Module ID alignment  : {{ PASS | FAIL (N issues) }}
Check 6 — Lab ID alignment     : {{ PASS | FAIL (N issues) }}

ISSUES
------
{{ List every [FAIL] line from all checks, grouped by check number.
   If no failures, print "None — all checks passed." }}

SUMMARY
-------
{{ N }} checks passed. {{ N }} checks failed. {{ Total issues }} issues found.
{{ "Workshop is ready for delivery." if all pass, else "Fix the issues above before running the workshop." }}
```

---

## Error Handling

- If `workshop.yaml` does not exist: output `[ERROR] workshop.yaml not found at project root. Cannot run checks 1, 2, 5, or 6.` and run checks 3 and 4 against all files found on disk.
- If `content/facilitator/facilitator-guide.md` does not exist: output `[ERROR] facilitator-guide.md not found. Cannot run Check 4.` and skip Check 4.
- If `content/modules/` directory does not exist: output `[ERROR] content/modules/ directory not found. Cannot run checks 3 or 4.`
- Do not throw on missing files — report them as failures and continue.

## Notes

- This skill is read-only. It does not create, modify, or delete any files.
- Run this skill before every workshop delivery and after every content PR merge.
- For CI integration, this skill's logic can be ported to a shell script at `scripts/validate-workshop.sh`.
