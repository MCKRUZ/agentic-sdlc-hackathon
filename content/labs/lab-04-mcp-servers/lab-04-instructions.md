# Lab 04: Add an MCP Server

**Duration:** 25 minutes
**Track:** All tools

## Objectives

- Understand what MCP servers are and why they extend agent capabilities beyond built-in tools
- Install and configure at least one MCP server for your agent
- Run prompts that exercise the MCP server and compare output quality to the baseline

## What You'll Do

- Choose an MCP server from the recommended list
- Install it and wire it into your agent's configuration
- Run 3 prompts that specifically use the server, then compare against the same prompts without it

## Prerequisites

- Lab 01 complete (working agent session)
- Node.js 18+ installed (`node --version` to check)
- Your agent tool supports MCP (see your track file -- Claude Code, Cursor, and Continue do; Copilot does not yet)

---

## Background

MCP (Model Context Protocol) is an open standard that lets AI agents call external tools during a conversation. Without MCP, your agent is limited to what it can do natively: read files, run shell commands, and call its built-in tools. With MCP, you can give the agent access to live documentation, database clients, browser automation, calendar data, vector search, and anything else that exposes an MCP-compatible server.

The key difference from a plugin or extension is that MCP servers are composable and tool-agnostic. You configure them once and they work across any MCP-compatible agent. You can run multiple servers simultaneously, and the agent decides which one to call based on the task. For this lab, you'll install one server to see the pattern -- the same steps apply to any server on the registry.

---

## Steps

### 1. Choose an MCP server

Pick one from the recommended list below based on what would be most useful to you. If you're unsure, start with **context7** -- it has the broadest everyday utility.

| Server | What It Does | Best For |
|---|---|---|
| **context7** | Fetches up-to-date library documentation on demand | Anyone using a framework or library (React, FastAPI, EF Core, etc.) |
| **sequential-thinking** | Gives the agent an explicit reasoning scratchpad for complex problems | Debugging, architecture decisions, multi-step planning |
| **filesystem** (extended) | Extends file system access with search, move, and metadata operations | Projects with complex file structures |
| **github** | Reads issues, PRs, and repo metadata from GitHub | Anyone with a GitHub-hosted project |

---

### 2. Install the MCP server

Most MCP servers are distributed as npm packages and run via `npx` -- no global install needed.

For **context7:**
```bash
npx -y @upstash/context7-mcp@latest --help
```
This verifies the package is reachable. If it prints usage info, it works.

For **sequential-thinking:**
```bash
npx -y @modelcontextprotocol/server-sequential-thinking --help
```

For **filesystem:**
```bash
npx -y @modelcontextprotocol/server-filesystem --help
```

For **github:**
```bash
npx -y @modelcontextprotocol/server-github --help
```

If `npx` is not available, install Node.js from nodejs.org and restart your terminal.

---

### 3. Configure your agent to use the server

You need to add the server to your agent's MCP configuration file. The file location depends on your tool -- see your track file for the exact path. Common locations:

- Claude Code: `~/.claude/claude_config.json` or `.claude/settings.json` in your project
- Cursor: `.cursor/mcp.json` in your project
- Continue: `~/.continue/config.json`

The configuration format is the same regardless of tool. Here is the generic structure and a complete example for context7:

**Generic MCP config structure:**
```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "package-name@version"],
      "env": {
        "OPTIONAL_ENV_VAR": "value"
      }
    }
  }
}
```

**Complete example -- context7:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

**Complete example -- sequential-thinking:**
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**Running two servers at once:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

If an existing `mcpServers` block is already in your config file, add your new server entry inside it -- do not create a second `mcpServers` key.

---

### 4. Restart your agent and verify the server loaded

Close and reopen your agent session. Most tools show a list of active MCP servers at startup or in a status panel. Look for:
- A log line like `MCP server "context7" started`
- The server name appearing in a tools list or sidebar
- A confirmation message when you ask: "What MCP tools do you have available?"

**Expected output:** The agent lists at least one MCP tool from the server you installed. For context7, you should see tools named something like `resolve-library-id` and `get-library-docs`.

> If the server doesn't appear, do not skip ahead. Diagnose it now using the troubleshooting section.

---

### 5. Run 3 prompts that use the MCP server

The prompts below are written for context7. Adapt them if you chose a different server.

**For context7 -- run all three:**

Prompt 1 (documentation lookup):
```
Using context7, how do I paginate results in [the ORM or framework your project uses]?
Show me the current API, not a generic example.
```
Replace `[the ORM or framework]` with something real from your project: Entity Framework, Prisma, SQLAlchemy, ActiveRecord, etc.

Prompt 2 (version-specific behavior):
```
Using context7, what changed in [your framework] between version [X] and [Y] that affects how middleware is configured?
```

Prompt 3 (debugging with docs):
```
I'm getting this error: [paste a real error from your project or use a recent one from memory].
Use context7 to look up the relevant documentation and suggest a fix based on the current API.
```

**For sequential-thinking -- run all three:**

Prompt 1:
```
Use sequential thinking to plan how I would add rate limiting to this API.
Think through the constraints before proposing a solution.
```

Prompt 2:
```
Use sequential thinking to identify the most likely root cause of this bug: [describe a real or hypothetical bug].
```

Prompt 3:
```
Use sequential thinking to decide whether this codebase should use a monorepo or separate repositories as it grows.
Consider the current team size, deployment model, and dependency patterns you can see in the code.
```

**Observe:** Watch whether the agent explicitly calls the MCP tool (most tools show this as a tool invocation log). The answer quality should reflect real, current documentation rather than the model's training data.

---

### 6. Compare: same question without the MCP server

Pick one of the prompts from step 5. Start a fresh session, disable the MCP server (or simply ask the question without the "use context7" instruction), and run the same prompt.

Compare the two answers:
- Is the without-MCP answer based on potentially outdated training data?
- Does it cite specific version numbers or API signatures?
- Does it hedge more ("I believe the API is...") vs. the MCP-backed answer?

Note what you observe. You'll discuss this during the debrief.

---

## Done?

- [ ] MCP server package was verified reachable via `npx`
- [ ] MCP config file was edited with a valid JSON entry for your chosen server
- [ ] Agent restarted and confirmed the server is loaded (via log, status panel, or direct question)
- [ ] All 3 prompts from step 5 were run and produced output that visibly used the MCP server
- [ ] Step 6 comparison was completed and you noted at least one concrete difference
- [ ] The MCP config file is committed to your project (if project-scoped) or noted for your own records

---

## Troubleshooting

**The MCP server doesn't appear after restart.**
First, validate your JSON. MCP config files fail silently on syntax errors. Paste your config into a JSON validator (jsonlint.com or `node -e "JSON.parse(require('fs').readFileSync('config.json','utf8'))"`) and fix any issues. Then confirm the file is in the location your tool expects -- check your track file.

**`npx` command fails with a network or registry error.**
You may be behind a corporate proxy or firewall. Try `npm install -g @upstash/context7-mcp` to install globally instead, then change the `command` in your config from `"npx"` to `"context7-mcp"` and remove the `"-y"` arg. If npm itself is blocked, talk to a facilitator -- there may be a local mirror available.

**The agent says it has no MCP tools available.**
Not all versions of all agent tools support MCP. Check your track file for the minimum required version. If your tool version is too old, update it first. If your tool doesn't support MCP at all (some Copilot configurations), you'll need to skip to the stretch goals or use a different tool for this lab.

**The agent calls the MCP server but returns an error from it.**
The server itself may have a startup error. Run the `npx` command manually in your terminal and look at the output -- it will usually print a clear error (missing env variable, unsupported Node version, etc.). Fix the underlying issue, then restart the agent.

---

## Stretch Goals

1. **Install a second MCP server** and use both in the same session. Ask a question that benefits from both: for example, use context7 to look up the correct API, then use sequential-thinking to plan a refactor that incorporates it. Observe whether the agent coordinates between the two tools without you explicitly directing it.

2. **Find a domain-specific MCP server** from the official registry (github.com/modelcontextprotocol/servers or mcp.so). Find one that's directly relevant to your project's stack and get it running. Useful options include database clients (Postgres, SQLite), cloud provider CLIs (AWS, Azure), or monitoring tools (Datadog, Sentry).

3. **Measure the documentation freshness gap.** Pick a library that released a major version in the past 12 months. Ask the agent (without MCP) what the current API looks like. Then ask again with context7. How far off was the training-data answer? Document the specific API differences. This is the most concrete way to show a teammate why MCP servers matter.
