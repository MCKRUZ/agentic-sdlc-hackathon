# Claude Code Setup Guide

## System Requirements

- **OS**: Windows 10/11, macOS 12+, or Linux (Ubuntu 20.04+)
- **Node.js**: 20 or higher (`node --version` to check)
- **npm**: Comes with Node.js, version 10+ preferred
- **Git**: Required for most workflows (`git --version` to check)
- **Terminal**: Windows Terminal, PowerShell 7+, or any bash-compatible shell

If you need Node.js: https://nodejs.org — download the LTS version.

---

## Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

Verify the install:

```bash
claude --version
```

---

## Authenticate

Run this command in any directory:

```bash
claude
```

On first launch, Claude Code opens a browser tab and asks you to sign in to claude.ai. Complete the sign-in, return to the terminal, and you are authenticated. Your credentials are stored locally and persist across sessions.

If the browser does not open automatically, Claude Code prints a URL. Copy and paste it into your browser manually.

---

## First Launch

Navigate to your project directory before starting Claude Code:

```bash
cd /path/to/your/project
claude
```

Claude Code reads the directory context on startup. Always launch from inside the project you are working on, not from your home directory.

---

## Key Keyboard Shortcuts and UI Overview

Once the REPL is open:

| Action | Shortcut |
|---|---|
| Submit prompt | Enter |
| Newline in prompt | Shift+Enter |
| Interrupt running task | Ctrl+C |
| Exit Claude Code | /exit or Ctrl+D |
| Scroll output | Mouse wheel or arrow keys |

**Slash commands** (type these at the prompt):

| Command | What it does |
|---|---|
| `/help` | Show all available commands |
| `/clear` | Clear conversation history and reset context |
| `/undo` | Revert the last file change Claude Code made |
| `/status` | Show current context, working directory, and active CLAUDE.md files |
| `/mcp` | List loaded MCP servers and their tools |
| `/exit` | Quit Claude Code |

When Claude Code wants to run a tool (read a file, run a command, write code), it pauses and asks for permission. You respond with:

- `y` — approve this one time
- `n` — deny
- `a` or `always` — approve this tool for the rest of the session without asking again

---

## Settings File

Location:

- **Windows**: `%USERPROFILE%\.claude\settings.json` (i.e., `C:\Users\<you>\.claude\settings.json`)
- **macOS/Linux**: `~/.claude/settings.json`

This file controls global behavior. A minimal starting config:

```json
{
  "theme": "dark",
  "autoApprove": false,
  "mcpServers": {}
}
```

**Key fields to configure:**

- `"theme"` — `"dark"` or `"light"`
- `"autoApprove"` — set `true` only if you trust Claude Code to run tools without prompting (not recommended for beginners)
- `"mcpServers"` — where you add MCP server integrations (covered in Lab 04)
- `"allowedTools"` — array of tool names Claude Code can use without asking, e.g., `["Read", "Glob", "Grep"]`

---

## How CLAUDE.md Works in Claude Code

CLAUDE.md files are plain markdown files that give Claude Code persistent instructions. Claude Code loads them automatically at startup and applies them to every prompt in the session.

**Priority order (highest to lowest):**

1. **Global**: `~/.claude/CLAUDE.md` (applies to all projects on your machine)
2. **Project root**: `<project>/.claude/CLAUDE.md` or `<project>/CLAUDE.md` (applies to the whole project)
3. **Subdirectory**: `<project>/src/CLAUDE.md` (applies only when working in that directory)

When multiple files exist, Claude Code merges them. More specific files take precedence over broader ones. If a project CLAUDE.md says "use tabs" and your global CLAUDE.md says "use spaces," the project file wins for that project.

**What to put in CLAUDE.md:**

- Coding conventions (language, formatting, patterns)
- Project structure and architecture notes
- Commands to run tests, builds, or linting
- What tools or frameworks the project uses
- Anything you would tell a new developer on day one

---

## How to Install MCP Servers in Claude Code

MCP (Model Context Protocol) servers extend Claude Code with new tools. You configure them in `~/.claude/settings.json` under the `mcpServers` key.

Each entry specifies how to start the server. Claude Code launches it automatically on startup.

Example config with two servers:

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

After editing `settings.json`, exit Claude Code and reopen it. Run `/mcp` to confirm the servers loaded.

See Lab 04 for a full walkthrough.

---

## Permission Modes

Claude Code asks before using tools. You can control this behavior:

**Session-level approval**: When prompted, type `always` to approve a tool for the whole session.

**Config-level allowlist** (settings.json):

```json
{
  "allowedTools": ["Read", "Glob", "Grep", "Bash"]
}
```

Tools in this list run without prompting. Tools not in the list still ask.

**`autoApprove: true`** approves everything silently. Use this only in throwaway sandbox environments, not on a real project.

---

## Common Gotchas on Windows

**Path separators**: Claude Code accepts both `\` and `/` in paths, but if you write paths in CLAUDE.md or prompts, prefer forward slashes to avoid escaping issues.

**Execution policy errors**: If `npx` or `npm` fails with a policy error in PowerShell, run:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**`claude` not found after install**: Close and reopen your terminal after `npm install -g`. The PATH update requires a new shell session.

**Long paths**: Windows has a 260-character path limit by default. If you hit errors in deeply nested projects, enable long paths:
```
Settings > System > For developers > Enable Win32 long paths
```

**Antivirus interference**: Some antivirus tools block `npx` from downloading MCP servers. If MCP servers fail to start, add your Node.js install directory to the antivirus exclusion list.

**Line endings**: If Claude Code generates files with `\r\n` endings that break scripts, add this to your project `.gitattributes`:
```
* text=auto
*.sh text eol=lf
```
