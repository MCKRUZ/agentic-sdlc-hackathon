# MCP Server Quick Reference

> Model Context Protocol (MCP) servers extend your AI agent with real tools.
> Install once per machine. Configure in your agent's MCP settings file.

---

## Server Directory

| Server Name | Purpose | Install Command | When to Use |
|---|---|---|---|
| **context7** | Live library documentation — resolves current API signatures, config options, and version-specific behavior for any open-source package | `npx -y @upstash/context7-mcp` | Writing or debugging code that uses a third-party library; you're unsure about an API; anything where stale training data might give wrong answers |
| **sequential-thinking** | Structured step-by-step reasoning — forces the model to think through problems before answering | `npx -y @modelcontextprotocol/server-sequential-thinking` | Planning multi-file features; debugging non-obvious issues; weighing architectural trade-offs |
| **filesystem** | Read and write local files with explicit path permissions | `npx -y @modelcontextprotocol/server-filesystem /path/to/allow` | Giving the agent access to a specific project directory without full shell access; auditing files without running code |
| **GitHub MCP** | Full GitHub API — issues, PRs, branches, file contents, search | `npx -y @modelcontextprotocol/server-github` | Creating/reviewing PRs from the agent, searching issues, reading files in remote repos, automating release notes |
| **Postgres MCP** | Query a live Postgres database with read-only safety | `npx -y @modelcontextprotocol/server-postgres postgresql://user:pass@host/db` | Exploring schema, writing and validating SQL, debugging data issues without leaving the chat |
| **SQLite MCP** | Query a local SQLite database file | `npx -y @modelcontextprotocol/server-sqlite /path/to/db.sqlite` | Local dev databases, embedded app storage, prototyping queries before promoting to Postgres |
| **Slack MCP** | Send messages, read channels, search history | `npx -y @modelcontextprotocol/server-slack` | Posting automated updates, searching past decisions in Slack, generating standup summaries from channel history |
| **Puppeteer / Browser** | Headless browser — navigate pages, click, fill forms, screenshot | `npx -y @modelcontextprotocol/server-puppeteer` | E2E testing flows, scraping pages the agent needs to read, automating web-based workflows that have no API |

---

## MCP Config File Locations

| Tool | Config File |
|------|-------------|
| Claude Code | `~/.claude/claude_desktop_config.json` (desktop) or `claude mcp add` CLI |
| Cursor | `.cursor/mcp.json` in project root or global `~/.cursor/mcp.json` |
| VS Code Copilot | `.vscode/mcp.json` in project root |

---

## Minimal Config Example (Claude Desktop)

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..." }
    }
  }
}
```

---

## Tips

- Start with **context7 + sequential-thinking** — highest signal-to-noise ratio for SDLC work.
- **filesystem** is safer than full shell access for demos and shared machines.
- Servers run as local processes — no data leaves your machine except to the model API.
- Run `npx -y <package> --help` to see server-specific flags before adding to config.
