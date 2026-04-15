# Agentic SDLC Hackathon

A full-day, instructor-led workshop teaching developers the fundamentals of agentic software development. Tool-agnostic core curriculum with tool-specific lab tracks (starting with Claude Code).

**Duration:** 7 hours (9:00 AM - 4:00 PM)
**Audience:** Developers - any stack, beginner to AI agentic tools
**Max Participants:** 100 (individual work)
**Format:** Alternating presentation + hands-on labs

---

## Learning Objectives

By the end of this workshop, participants will be able to:

1. Explain what agentic development is and how it differs from copilot/autocomplete tools
2. Use an AI coding agent out-of-the-box to explore, explain, and modify a real codebase
3. Create a project context file (e.g., CLAUDE.md) that meaningfully improves agent output
4. Build a reusable custom skill or slash command that automates a common workflow
5. Configure and use at least one MCP server to extend agent capabilities
6. Describe token management strategies and apply them to avoid context window issues
7. Map the agentic SDLC to their own development workflow

---

## Schedule

| Time  | Duration | Topic                          |
|-------|----------|--------------------------------|
| 09:00 | 15 min   | Welcome & Logistics            |
| 09:15 | 30 min   | M01: The Agentic Mental Shift  |
| 09:45 | 30 min   | M02: OOB Tool Usage + Demo     |
| 10:15 | 30 min   | LAB 01: First Agent Interaction|
| 10:45 | 15 min   | Break                          |
| 11:00 | 20 min   | M03: Project Context Files     |
| 11:20 | 40 min   | LAB 02: Write Your Context File|
| 12:00 | 60 min   | Lunch                          |
| 13:00 | 40 min   | M04: Skills & Custom Commands  |
| 13:40 | 35 min   | LAB 03: Build a Skill          |
| 14:15 | 15 min   | Break                          |
| 14:30 | 30 min   | M05: MCP Servers               |
| 15:00 | 30 min   | LAB 04: Add an MCP Server      |
| 15:30 | 15 min   | M06: Token Management & Context|
| 15:45 | 15 min   | M07: Agentic SDLC & Wrap-up    |

---

## Repository Structure

```
agentic-sdlc-hackathon/
├── workshop.yaml               # Master config - modules, labs, timing
├── content/
│   ├── modules/                # Presenter scripts + slide content (m01-m07)
│   ├── labs/                   # Lab instructions (lab-01-lab-04)
│   ├── facilitator/            # Facilitator guide, timing, troubleshooting
│   └── demos/                  # Demo scripts and assets
├── participant/
│   ├── workbook/               # Participant workbook (printed + digital)
│   └── reference-cards/        # Quick-reference cheat sheets
├── sample-project/             # Instructor demo app (DevBoard)
├── tracks/
│   ├── claude-code/            # Claude Code lab variants + setup
│   ├── cursor/                 # Cursor-specific (planned)
│   └── factory-ai/             # Factory.ai-specific (planned)
├── templates/                  # Content templates per type
├── references/                 # Source materials, guidelines
└── tools/                      # Build automation scripts
```

---

## Quick Start

```bash
# View workshop structure
cat workshop.yaml

# Build participant workbook (PDF)
python tools/build_workbook.py

# Build facilitator guide
python tools/build_facilitator_guide.py
```

---

## Tool Tracks

| Track       | Tool        | Status   |
|-------------|-------------|----------|
| claude-code | Claude Code | Complete |
| cursor      | Cursor      | Planned  |
| factory-ai  | Factory.ai  | Planned  |

Each track lives under `tracks/{tool}/` and contains tool-specific setup instructions and lab variants.

---

## Sample Project

**DevBoard** - a minimal task-tracking REST API + static frontend used for instructor live demos.

- Stack: .NET 9 Minimal API + EF Core (in-memory) + vanilla HTML/JS
- Location: `sample-project/`
- Participants use their own projects for labs - DevBoard is demo-only

---

## Content Pipeline

```
outline -> script -> slides -> demo -> facilitator-guide -> participant-workbook -> validate
```

Use `/workshop-module` to draft a new module, `/workshop-lab` to draft a new lab.
