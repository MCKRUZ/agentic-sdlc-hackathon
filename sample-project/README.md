# DevBoard

A minimal task-board API built with .NET 9 Minimal APIs and EF Core (in-memory). Used as an instructor demo for agentic development workshops.

## Prerequisites

- .NET 9 SDK — https://dot.net/download

No database setup required. The in-memory database is seeded automatically on startup.

## Run the API

```bash
dotnet run --project src/DevBoard.Api
```

The API starts on `http://localhost:5000` by default. Open that URL in a browser to see the board UI.

The OpenAPI spec is available at `http://localhost:5000/openapi/v1.json` in Development mode.

## Run the Tests

```bash
dotnet test
```

## API Reference

### Work Items

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/workitems` | List all work items. Query params: `assignee`, `sort` (`oldest`, `title`) |
| GET | `/api/workitems/{id}` | Get a single work item with its comments |
| POST | `/api/workitems` | Create a work item |
| PUT | `/api/workitems/{id}` | Update a work item (enforces status transition rules) |
| DELETE | `/api/workitems/{id}` | Delete a work item |
| GET | `/api/workitems/status/{status}` | Filter by status (`todo`, `in-progress`, `done`) |

### Comments

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/workitems/{id}/comments` | List comments on a work item |
| POST | `/api/workitems/{id}/comments` | Add a comment |
| DELETE | `/api/workitems/{id}/comments/{commentId}` | Delete a comment |

### Status Transition Rules

Valid transitions:
- `todo` → `in-progress`
- `in-progress` → `todo` or `done`
- `done` → `in-progress`

Attempting an invalid transition returns `400 Bad Request`.

## Project Structure

```
sample-project/
├── DevBoard.sln
├── DEMO-NOTES.md          # Instructor guide — teaching moments and demo prompts
├── src/
│   └── DevBoard.Api/
│       ├── Program.cs
│       ├── Models/        # WorkItem, Comment
│       ├── Data/          # DevBoardContext (EF Core)
│       ├── Endpoints/     # WorkItemEndpoints, CommentEndpoints
│       └── wwwroot/       # Static frontend (index.html)
└── tests/
    └── DevBoard.Api.Tests/
        └── WorkItemEndpointTests.cs
```

## Notes for Instructors

This project is intentionally imperfect — it contains four teaching moments that an AI agent can identify and fix during a live demo. See **DEMO-NOTES.md** for the full list with copy-paste prompts.
