# Lab Instructions Template

<!--
  HOW TO USE THIS TEMPLATE
  ========================
  1. Copy this file to content/labs/LL-lab-name/instructions.md
  2. Replace every {{ PLACEHOLDER }} with real content
  3. Keep steps atomic — one action per step, one expected result per step
  4. The "Done Checklist" should mirror the learning objectives from the parent module
  5. Delete this comment block when done
-->

---

# Lab {{ LAB_ID }}: {{ LAB_TITLE }}

**Module:** {{ PARENT_MODULE_ID }} — {{ PARENT_MODULE_TITLE }}
**Duration:** {{ DURATION }} minutes
**Difficulty:** {{ Beginner | Intermediate | Advanced }}
**Track:** {{ ALL_TRACKS | CLAUDE_CODE | CURSOR | COPILOT }}

---

## What You Will Do

<!-- One paragraph, plain language. No jargon. Tells participants what they will build or prove. -->

In this lab you will {{ BRIEF_DESCRIPTION_OF_OUTCOME }}. By the end you will have {{ CONCRETE_ARTIFACT_OR_RESULT }}.

---

## Prerequisites

<!-- List everything that must be true before step 1. Link setup guides where possible. -->

- [ ] {{ PREREQUISITE_1 }} — see `{{ SETUP_DOC_PATH }}` if not done
- [ ] {{ PREREQUISITE_2 }}
- [ ] {{ PREREQUISITE_3 }}
- [ ] Repository cloned and dependencies installed (`{{ INSTALL_COMMAND }}`)

---

## Background

<!-- 2–4 short paragraphs or bullets. Explain the concept being practiced.
     Do not repeat module slides verbatim — add context or a worked example. -->

{{ BACKGROUND_PARAGRAPH_1 }}

{{ BACKGROUND_PARAGRAPH_2 }}

**Key terms:**

| Term | Definition |
|------|------------|
| {{ TERM_1 }} | {{ DEFINITION_1 }} |
| {{ TERM_2 }} | {{ DEFINITION_2 }} |

---

## Steps

<!-- Each step: action verb + object. One action per step.
     "Expected result" tells participants what they should see if the step worked.
     Never skip expected results — they're the fastest way to self-diagnose. -->

### Part 1: {{ PART_1_TITLE }}

**Step 1 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_1_INSTRUCTION }}

```{{ LANGUAGE }}
{{ STEP_1_CODE_OR_COMMAND }}
```

Expected result: {{ STEP_1_EXPECTED_RESULT }}

---

**Step 2 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_2_INSTRUCTION }}

Expected result: {{ STEP_2_EXPECTED_RESULT }}

---

**Step 3 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_3_INSTRUCTION }}

```{{ LANGUAGE }}
{{ STEP_3_CODE_OR_COMMAND }}
```

Expected result: {{ STEP_3_EXPECTED_RESULT }}

---

### Part 2: {{ PART_2_TITLE }}

**Step 4 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_4_INSTRUCTION }}

Expected result: {{ STEP_4_EXPECTED_RESULT }}

---

**Step 5 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_5_INSTRUCTION }}

Expected result: {{ STEP_5_EXPECTED_RESULT }}

---

**Step 6 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_6_INSTRUCTION }}

Expected result: {{ STEP_6_EXPECTED_RESULT }}

---

### Part 3: {{ PART_3_TITLE }}

**Step 7 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_7_INSTRUCTION }}

Expected result: {{ STEP_7_EXPECTED_RESULT }}

---

**Step 8 — {{ ACTION_VERB }} {{ OBJECT }}**

{{ STEP_8_INSTRUCTION }}

Expected result: {{ STEP_8_EXPECTED_RESULT }}

---

## Done Checklist

<!-- Participants tick these off before calling the lab complete.
     Each item should be directly observable — not "I understand X" but "X is working / file exists / test passes". -->

- [ ] {{ DONE_CRITERION_1 }}
- [ ] {{ DONE_CRITERION_2 }}
- [ ] {{ DONE_CRITERION_3 }}
- [ ] {{ DONE_CRITERION_4 }}

---

## Troubleshooting

<!-- List the 3–5 most common failure modes. Keep solutions concrete. -->

### {{ COMMON_ERROR_1 }}

**Symptom:** {{ ERROR_1_SYMPTOM }}

**Cause:** {{ ERROR_1_CAUSE }}

**Fix:** {{ ERROR_1_FIX }}

---

### {{ COMMON_ERROR_2 }}

**Symptom:** {{ ERROR_2_SYMPTOM }}

**Cause:** {{ ERROR_2_CAUSE }}

**Fix:** {{ ERROR_2_FIX }}

---

### {{ COMMON_ERROR_3 }}

**Symptom:** {{ ERROR_3_SYMPTOM }}

**Cause:** {{ ERROR_3_CAUSE }}

**Fix:** {{ ERROR_3_FIX }}

---

### Still stuck?

Ask a facilitator, or post in `#hackathon-help` with:
1. The step number where you got stuck
2. The exact error message or unexpected output
3. What you already tried

---

## Stretch Goals

<!-- Optional. For participants who finish early. Each goal should be independent —
     completing one should not be required to attempt another. -->

### Stretch 1 — {{ STRETCH_1_TITLE }}

{{ STRETCH_1_DESCRIPTION }}

Hint: {{ STRETCH_1_HINT }}

---

### Stretch 2 — {{ STRETCH_2_TITLE }}

{{ STRETCH_2_DESCRIPTION }}

Hint: {{ STRETCH_2_HINT }}

---

### Stretch 3 — {{ STRETCH_3_TITLE }}

{{ STRETCH_3_DESCRIPTION }}

Hint: {{ STRETCH_3_HINT }}

---

## Notes

<!-- Space for participants to jot things down during the lab. -->

&nbsp;

&nbsp;

&nbsp;
