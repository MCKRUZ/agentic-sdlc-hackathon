# Module Script Template

<!--
  HOW TO USE THIS TEMPLATE
  ========================
  1. Copy this file to content/modules/MM-module-name/script.md
  2. Replace every {{ PLACEHOLDER }} with real content
  3. Use the marker conventions below throughout the SCRIPT BODY section
  4. Delete this comment block when done

  MARKER CONVENTIONS
  ------------------
  [SLIDE N]       — Advance to slide N. Place at the top of each slide's talking points.
  [PAUSE]         — Hold for questions or let the audience absorb the previous point.
                    Optional note in parentheses: [PAUSE — wait for hands]
  [DEMO CUE: ID]  — Switch to a live demo. ID must match a demo entry in
                    content/facilitator/facilitator-guide.md (e.g., [DEMO CUE: codebase-tour]).
                    The facilitator guide describes exact steps, expected output, and recovery paths.
  [ACTIVITY]      — Audience participation moment (poll, think-pair-share, chat response).
  [TRANSITION]    — Brief bridging sentence before moving to the next section.
-->

---

## Module Metadata

| Field      | Value                        |
|------------|------------------------------|
| Module ID  | {{ MODULE_ID }}              |
| Title      | {{ MODULE_TITLE }}           |
| Duration   | {{ DURATION }} minutes       |
| Track      | {{ TRACK_NAME }}             |
| Author     | {{ AUTHOR_NAME }}            |
| Last Updated | {{ YYYY-MM-DD }}           |

---

## Learning Objectives

By the end of this module, participants will be able to:

1. {{ OBJECTIVE_1 }}
2. {{ OBJECTIVE_2 }}
3. {{ OBJECTIVE_3 }}

<!-- Add or remove objectives as needed. Aim for 3–5 measurable outcomes. -->

---

## Prerequisites

- {{ PREREQUISITE_1 }}
- {{ PREREQUISITE_2 }}

---

## Materials Needed

- Slides: `content/modules/{{ MODULE_ID }}/slides.md`
- Demo repo: {{ DEMO_REPO_URL }}
- Lab: `content/labs/{{ LAB_ID }}/instructions.md`

---

## Script Body

### Opening ({{ X }} min)

[SLIDE 1]

"Welcome to {{ MODULE_TITLE }}. In the next {{ DURATION }} minutes, we're going to cover {{ BRIEF_TOPIC_SUMMARY }}."

[PAUSE — let the room settle]

"Before we dive in — quick show of hands: {{ WARM_UP_QUESTION }}?"

[ACTIVITY — note responses on a sticky note or whiteboard]

"Great. That tells me {{ ADAPTIVE_RESPONSE }}. Let's keep that in mind as we go."

[TRANSITION]

---

### Section 1: {{ SECTION_1_TITLE }} ({{ X }} min)

[SLIDE 2]

"{{ OPENING_STATEMENT_FOR_SECTION_1 }}"

- Key point: {{ POINT_A }}
- Key point: {{ POINT_B }}

[PAUSE]

"The reason this matters is {{ WHY_IT_MATTERS }}."

[SLIDE 3]

"Let's make this concrete."

[DEMO CUE: {{ DEMO_ID_1 }}]

"What you just saw: {{ EXPLAIN_WHAT_DEMO_SHOWED }}."

[PAUSE — invite questions]

[TRANSITION]

---

### Section 2: {{ SECTION_2_TITLE }} ({{ X }} min)

[SLIDE 4]

"Now that we understand {{ SECTION_1_CONCEPT }}, let's look at {{ SECTION_2_CONCEPT }}."

{{ TALKING_POINTS_FOR_SECTION_2 }}

[SLIDE 5]

[DEMO CUE: {{ DEMO_ID_2 }}]

[PAUSE]

[TRANSITION]

---

### Section 3: {{ SECTION_3_TITLE }} ({{ X }} min)

[SLIDE 6]

{{ TALKING_POINTS_FOR_SECTION_3 }}

[PAUSE — check for understanding: "Any questions before we move to the lab?"]

---

### Lab Handoff ({{ X }} min)

[SLIDE 7]

"Here's what you're going to do in the lab:"

1. {{ LAB_STEP_SUMMARY_1 }}
2. {{ LAB_STEP_SUMMARY_2 }}
3. {{ LAB_STEP_SUMMARY_3 }}

"Open `content/labs/{{ LAB_ID }}/instructions.md`. You have {{ LAB_DURATION }} minutes. I'll be circulating — flag me if you hit a blocker."

[PAUSE — confirm everyone has the file open]

---

### Debrief & Close ({{ X }} min)

[SLIDE 8]

"Let's come back together. {{ DEBRIEF_QUESTION_TO_ROOM }}?"

[ACTIVITY — take 2–3 responses]

"To summarize what we covered:"

- {{ RECAP_POINT_1 }}
- {{ RECAP_POINT_2 }}
- {{ RECAP_POINT_3 }}

[SLIDE 9]

"In the next module, {{ NEXT_MODULE_TEASER }}. See you in {{ BREAK_DURATION }} minutes."

---

## Timing Tracker

| Section         | Target (min) | Actual (min) |
|-----------------|--------------|--------------|
| Opening         | {{ X }}      |              |
| Section 1       | {{ X }}      |              |
| Section 2       | {{ X }}      |              |
| Section 3       | {{ X }}      |              |
| Lab Handoff     | {{ X }}      |              |
| Debrief & Close | {{ X }}      |              |
| **Total**       | **{{ DURATION }}** |        |

---

## Facilitator Notes

<!-- Add anything a co-facilitator needs to know: common confusion points, slide numbers
     that need an internet connection, audience-specific variations, etc. -->

- {{ FACILITATOR_NOTE_1 }}
- {{ FACILITATOR_NOTE_2 }}
