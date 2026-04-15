# M05: MCP Servers — Slide Outline

---

## Slide 1: What the Agent Can't Do (Yet)

Out of the box, the agent can:
- Read and write files in your project
- Run terminal commands
- Search your codebase

But it can't:
- Query your actual database
- Check your Slack or internal wiki
- Access current library docs (training data has a cutoff)

Speaker note: This is the setup slide. Don't rush past the "can't" list — those limitations are exactly why people should care about MCP. Let the frustration land before offering the solution.

---

## Slide 2: What MCP Is

**Model Context Protocol** — an open standard for connecting agents to external tools and data.

- Created by Anthropic, now broadly supported
- Replaces dozens of proprietary plugin systems with one protocol
- Analogy: USB standardized device connections. MCP standardizes agent integrations.

Speaker note: The USB analogy works well for this audience. Use it and move on — don't over-explain the protocol history.

---

## Slide 3: Three Things MCP Exposes

| Concept | What It Is | Example |
|---|---|---|
| Tools | Functions the agent can call | "Query this database" |
| Resources | Data the agent can read | A file, a DB record |
| Prompts | Reusable prompt templates | Standardized queries |

- Tools are the most common — you'll interact with these most
- The agent discovers capabilities automatically when a server is connected

Speaker note: This slide can move fast. Most of the room only needs to know "tools" for today. Resources and prompts are context.

---

## Slide 4: Client / Server Architecture

```
Your Agent (client)
     |
     | MCP Protocol
     |
MCP Server (local process or remote)
     |
External System (DB, Slack, GitHub, docs...)
```

- You configure which servers the agent connects to
- The agent decides which tools to call based on your question
- You don't have to tell it when to use MCP — it figures that out

Speaker note: Draw this on screen if you have a whiteboard handy. The key point is that the agent is autonomous about tool selection — you don't have to manage it manually.

---

## Slide 5: Key MCP Servers Worth Knowing

| Server | What It Does |
|---|---|
| context7 | Current library docs, resolved at query time |
| filesystem | Access files outside current project |
| postgres / sqlite | Query your actual database schema and data |
| Slack | Search message history by topic or channel |
| GitHub | Issues, PRs, comments — via API |
| Playwright/browser | Automated browser control |

- Hundreds of servers available and growing
- Internal/custom servers can be built in a few hours

Speaker note: Ask the room: "Which of these would you use today?" Good engagement moment. Database connectors and context7 usually get the most hands.

---

## Slide 6: Configuring an MCP Server

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

- Config lives in `~/.claude.json` or project-level config
- Credentials go in `env` — never in the repo
- Restart the agent after changes

Speaker note: This is the hands-on config slide. People will take a photo of this. Make sure it's visible and readable.

---

## Slide 7: Demo — context7 + FluentValidation in .NET 9

[Live demo]

Prompt: "How do I use FluentValidation in .NET 9 to validate a command and return all errors at once? Show a complete example."

Watch the agent:
1. Recognize it needs current docs
2. Call the context7 tool automatically
3. Return an answer grounded in actual, current documentation

Speaker note: This is the demo slide — you're not reading it, you're doing the demo. Flip back if you lose your place. Point out the tool call in the output explicitly; some people won't notice it otherwise.

---

## Slide 8: A Note on Trust

MCP servers run as processes on your machine.

- Only install servers from sources you trust
- Review what permissions each server requests
- Use environment variables for credentials — never hardcode
- Official Anthropic servers and major community servers (context7) are safe
- For anything else: read the source before running

Speaker note: Don't dwell here, but don't skip it. Security-conscious developers will appreciate that you addressed it. One minute max.

---

## Slide 9: The Takeaway

Before MCP: the agent works from training data alone.

After MCP: the agent works from training data plus your live systems.

- More accurate code because it knows your real schema
- More accurate library usage because it reads current docs
- Reachable context: Slack history, GitHub issues, internal wikis

One config change. Significant capability upgrade.

Speaker note: Close on this. The point is that MCP is a multiplier on everything the agent already does. It's not a separate feature — it makes every other feature more accurate.

---

*9 slides total. Estimated deck time: 25 minutes with demo, 5 minutes buffer.*
