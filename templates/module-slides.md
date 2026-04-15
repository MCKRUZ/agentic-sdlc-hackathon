# Module Slides Template

<!--
  HOW TO USE THIS TEMPLATE
  ========================
  1. Copy this file to content/modules/MM-module-name/slides.md
  2. Replace every {{ PLACEHOLDER }} with real content
  3. Each H2 (##) heading = one slide title
  4. Bullets under the heading = slide body content
  5. "Speaker note:" lines are for the presenter only — not shown on screen
  6. Delete this comment block when done

  CONVENTIONS
  -----------
  ## Slide Title         — The slide's on-screen title (H2)
  - Bullet               — On-screen body text. Keep each bullet under 10 words.
  Speaker note: ...      — Presenter-only guidance. One or more lines. Indented with two spaces
                           if it spans multiple lines. Never shown to the audience.
  ---                    — Slide separator (horizontal rule)

  SLIDE DESIGN RULES
  ------------------
  - Max 5 bullets per slide. If you need more, split the slide.
  - One idea per slide. If the title has "and", it's probably two slides.
  - Code snippets: use fenced code blocks inside the slide. Keep them to 10 lines max.
  - Images: reference as ![alt text](../../assets/images/filename.png)
-->

---

## {{ MODULE_TITLE }}

- Module {{ MODULE_ID }}
- {{ DURATION }} minutes
- {{ TRACK_NAME }}

Speaker note: Welcome the room. State the module ID so participants can follow along in the workbook. If running behind schedule, cut Section 3 — it's the least critical.

---

## Agenda

- {{ AGENDA_ITEM_1 }}
- {{ AGENDA_ITEM_2 }}
- {{ AGENDA_ITEM_3 }}
- Lab: {{ LAB_TITLE }}

Speaker note: Read through the agenda briefly. Do not spend more than 60 seconds here.

---

## Why This Matters

- {{ PAIN_POINT_OR_MOTIVATION_1 }}
- {{ PAIN_POINT_OR_MOTIVATION_2 }}
- {{ PAIN_POINT_OR_MOTIVATION_3 }}

Speaker note: Ground the content in something the audience already experiences. Use the warm-up poll results to make this land.

---

## {{ SECTION_1_TITLE }}

- {{ KEY_POINT_A }}
- {{ KEY_POINT_B }}
- {{ KEY_POINT_C }}

Speaker note: {{ SPEAKER_CONTEXT_FOR_SECTION_1 }}

---

## {{ CONCEPT_OR_DIAGRAM_SLIDE_TITLE }}

<!-- If this slide is primarily a diagram or screenshot, note that here -->

![{{ ALT_TEXT }}](../../assets/images/{{ IMAGE_FILENAME }})

Speaker note: Walk through the diagram left-to-right. Emphasize {{ EMPHASIS_POINT }}. Common question: "{{ ANTICIPATED_QUESTION }}" — answer: "{{ ANSWER }}".

---

## Demo: {{ DEMO_TITLE }}

- Goal: {{ WHAT_WE_WILL_SHOW }}
- Repo: `{{ DEMO_REPO_PATH }}`
- Starting state: {{ STARTING_STATE }}

Speaker note: [DEMO CUE: {{ DEMO_ID }}] — switch to terminal/IDE now. If the demo breaks, skip to the next slide and use the fallback screenshot at assets/images/{{ DEMO_FALLBACK_IMAGE }}.

---

## What We Just Saw

- {{ TAKEAWAY_1 }}
- {{ TAKEAWAY_2 }}
- {{ TAKEAWAY_3 }}

Speaker note: Consolidate before moving on. Invite one question before advancing.

---

## {{ SECTION_2_TITLE }}

- {{ KEY_POINT_A }}
- {{ KEY_POINT_B }}
- {{ KEY_POINT_C }}

Speaker note: {{ SPEAKER_CONTEXT_FOR_SECTION_2 }}

---

## {{ CODE_EXAMPLE_SLIDE_TITLE }}

```{{ LANGUAGE }}
{{ CODE_SNIPPET }}
```

Speaker note: Read the key lines aloud. Do not read every line. Highlight {{ LINE_OR_BLOCK_TO_HIGHLIGHT }} — that's the part that matters.

---

## {{ SECTION_3_TITLE }}

- {{ KEY_POINT_A }}
- {{ KEY_POINT_B }}
- {{ KEY_POINT_C }}

Speaker note: {{ SPEAKER_CONTEXT_FOR_SECTION_3 }} — this section is cuttable if time is short.

---

## Lab: {{ LAB_TITLE }}

- Duration: {{ LAB_DURATION }} minutes
- File: `content/labs/{{ LAB_ID }}/instructions.md`
- Goal: {{ LAB_ONE_LINE_GOAL }}

Speaker note: Read the three bullets aloud. Confirm everyone has the instructions open before stepping away. Watch for participants stuck on {{ COMMON_BLOCKER }}.

---

## Key Takeaways

- {{ TAKEAWAY_1 }}
- {{ TAKEAWAY_2 }}
- {{ TAKEAWAY_3 }}

Speaker note: Keep this tight — 60 seconds max. These should map directly to the learning objectives on slide 1.

---

## Up Next: {{ NEXT_MODULE_TITLE }}

- {{ NEXT_MODULE_TEASER_POINT_1 }}
- {{ NEXT_MODULE_TEASER_POINT_2 }}
- Break: {{ BREAK_DURATION }} minutes

Speaker note: End on time. Do not start the teaser if you are over by more than 2 minutes — just call the break.

---

## Resources

- Slides: {{ SLIDES_URL }}
- Repo: {{ REPO_URL }}
- Docs: {{ DOCS_URL }}
- Lab: `content/labs/{{ LAB_ID }}/instructions.md`

Speaker note: These will be in the participant workbook. No need to read them aloud.
