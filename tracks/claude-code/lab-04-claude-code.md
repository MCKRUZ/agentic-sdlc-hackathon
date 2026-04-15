# Lab 04 — Claude Code: Add an MCP Server

This is the Claude Code variant of Lab 04. MCP (Model Context Protocol) servers give Claude Code new tools beyond its built-in capabilities. This lab adds two servers: context7 for live library documentation, and sequential-thinking for structured reasoning.

---

## MCP Config Location

All MCP servers are configured in the Claude Code settings file:

- **Windows**: `C:\Users\<you>\.claude\settings.json`
- **macOS/Linux**: `~/.claude/settings.json`

If this file does not exist yet, create it. Open it in any text editor.

---

## Add context7

context7 gives Claude Code access to up-to-date documentation for thousands of libraries and frameworks. Instead of guessing at API signatures, Claude Code looks them up in real time.

Add this to your `settings.json`:

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

---

## Add sequential-thinking

sequential-thinking gives Claude Code a structured reasoning tool. It is useful for multi-step planning, debugging non-obvious issues, and architectural decisions.

Add it alongside context7:

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

This is the complete `settings.json` content with both servers. If you already have other settings in the file (like `"theme"`), add the `"mcpServers"` block at the top level alongside them:

```json
{
  "theme": "dark",
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

---

## Restart Claude Code

MCP servers are launched at startup. After editing `settings.json`, you must exit and reopen Claude Code:

1. Type `/exit` at the Claude Code prompt (or press Ctrl+D)
2. Run `claude` again in your project directory

Claude Code will start the MCP servers in the background during launch. If a server fails to start, you will see an error message.

---

## Verify MCP Servers Loaded

After restarting, run this command at the Claude Code prompt:

```
/mcp
```

You should see output listing both `context7` and `sequential-thinking` as connected servers with their available tools.

Alternatively, ask:

```
What MCP servers do you have access to, and what tools do they provide?
```

Claude Code will list the loaded servers and describe what each one can do.

---

## Using context7: 3 Example Prompts

context7 is triggered when you include the phrase **"use context7"** in your prompt. This tells Claude Code to look up live documentation rather than relying on training data.

**Example 1: Look up a specific API**

```
How do I configure middleware in Express 5? Use context7 to get the current docs.
```

**Example 2: Debug a library-specific issue**

```
I'm getting a "Cannot set headers after they are sent" error in Express. Use context7 to find the correct way to handle this.
```

**Example 3: Scaffold code using the latest API**

```
Write a FastAPI route that uses dependency injection for database sessions. Use context7 to make sure you're using the current FastAPI patterns, not outdated ones.
```

Without "use context7," Claude Code may rely on its training data, which can be outdated for fast-moving libraries. Include the phrase whenever you need accurate, current documentation.

---

## Troubleshooting

**MCP server not found / command not found**

Claude Code runs `npx` to download and start MCP servers. If `npx` is not available or fails, the server will not start.

Check:
```bash
npx --version
```

If this fails, your Node.js install is incomplete or not on your PATH. Reinstall Node.js from https://nodejs.org.

**Permission errors on Windows**

If you see `EACCES` or access denied errors when MCP servers start:

1. Run your terminal as Administrator (right-click, "Run as administrator") and try again
2. If that works, the issue is npm's global cache permissions. Fix them permanently:
   ```bash
   npm config set cache "C:\Users\<you>\AppData\Local\npm-cache" --global
   ```

**Execution policy errors on Windows**

If PowerShell blocks `npx` with a policy error:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**MCP server shows as connected but tools do not work**

Run `/mcp` and check that the tool names are listed under the server. If the server shows as connected but lists zero tools, the server package may have failed to download. Try running the npx command manually to see the error:

```bash
npx -y @upstash/context7-mcp@latest
```

**Network / proxy issues**

If your machine is behind a corporate proxy, `npx` may fail to download MCP packages. Set the proxy for npm:

```bash
npm config set proxy http://your-proxy:port
npm config set https-proxy http://your-proxy:port
```

Then restart Claude Code.

**context7 returns no results**

Some library names need to be specific. If context7 cannot find documentation for a library name, try using the npm package name directly:

```
Use context7 to look up docs for @tanstack/react-query
```

instead of:

```
Use context7 to look up docs for React Query
```
