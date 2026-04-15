# M05: MCP Servers
## Presenter Script — 30 minutes including demo

---

### Section 1: The Limitation of Base Tools (5 min)

[SLIDE 1]

By now you've seen what the agent can do out of the box. It can read your files, write code, run terminal commands, search your codebase. That's already useful.

But here's what it can't do, by default.

It can't query your database to understand the actual shape of your data. It can't check Slack to see what a teammate said about that API endpoint. It can't look up the current documentation for the library you're using — it only knows what was in its training data, which has a cutoff date and doesn't include your internal packages at all.

[PAUSE — 2 seconds]

This matters more than it sounds. Half the time when an agent produces a wrong answer about a library, it's not because the model is bad — it's because the model is working from stale or incomplete information. It's doing its best with what it has. The question is: can we give it better information?

The answer is yes. That's what MCP servers do.

---

### Section 2: What MCP Is (8 min)

[SLIDE 2]

MCP stands for Model Context Protocol. It's an open standard created by Anthropic and now maintained with broad industry support. The core idea is simple: give agents a standardized way to connect to external tools and data sources.

Before MCP, every agent tool had its own proprietary plugin system. Cursor plugins, ChatGPT plugins, Copilot extensions — all different formats, all requiring separate integrations. MCP is an attempt to fix that with a single open protocol.

[PAUSE — 2 seconds]

Think of it like this: USB is a standard so you don't need a different cable for every device. MCP is trying to be that for agent integrations.

[SLIDE 3]

The protocol has three concepts worth knowing.

**Tools** are functions the agent can call. "Query this database." "Search Slack for messages containing this string." "Look up the docs for this library." Tools are the most common thing you'll encounter.

**Resources** are data the agent can read. Files, database records, API responses. Think of these as read-only context the agent can pull in on demand.

**Prompts** are reusable prompt templates exposed by the server. Less common but useful for standardizing how you ask about certain things.

[SLIDE 4]

The architecture is client/server. Your agent is the client. An MCP server is a process running locally or remotely that exposes tools and resources through the protocol. The agent discovers what a server can do by asking it, then calls those capabilities as needed during a conversation.

You configure which servers your agent connects to. The agent handles the rest — it knows to use the database tool when you ask a question that requires database data, the docs tool when you ask about a library, and so on.

---

### Section 3: The MCP Ecosystem (7 min)

[SLIDE 5]

There are already hundreds of MCP servers available. Let me walk through the ones you're most likely to use.

**context7** — This one is worth calling out first because it solves the stale docs problem directly. context7 indexes current library documentation. When you ask the agent "how do I configure retry policies in Polly?" it fetches the actual current docs, not a hallucinated answer from training data. For any team working with rapidly evolving libraries, this is immediately useful.

**filesystem** — Gives the agent access to files outside your current project directory. If you want it to read a config file in a different repo, or access shared team documentation stored somewhere else on your machine, the filesystem server handles that.

**database connectors** — There are MCP servers for PostgreSQL, SQLite, MySQL, and others. With one of these configured, you can ask the agent "what columns does the users table have?" and it will query your actual database to find out. This makes generated code dramatically more accurate because the agent is working from your real schema.

**Slack** — The agent can search your message history, read channel conversations, and look up what was discussed about a specific topic. Useful for catching up on context before making a change.

**GitHub** — Beyond what the agent can do with git locally, the GitHub MCP server gives it access to issues, pull requests, and comments. "What open issues are related to the authentication module?" becomes a real question you can ask.

**browser/Playwright** — Lets the agent control a browser. Useful for testing, scraping public data, or automating web tasks.

[PAUSE — 2 seconds]

The ecosystem is growing fast. If you need to connect the agent to something specific — your internal wiki, your issue tracker, your observability platform — there's a good chance someone has already built an MCP server for it. If not, the protocol is documented well enough that building a simple one is a few hours of work.

---

### Section 4: Installing and Configuring (5 min)

[SLIDE 6]

Adding an MCP server to your agent is a config change. Here's what it looks like for Claude Code.

Your Claude config lives at `~/.claude.json` or in a project-level `claude.json`. The MCP servers section looks like this:

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

That's it. When Claude Code starts, it launches the context7 server as a child process. The agent discovers its capabilities automatically and knows to use them when relevant.

[PAUSE — 2 seconds]

For servers that need credentials — a database connection string, a Slack token — you pass those as environment variables in the config:

```json
{
  "mcpServers": {
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

The credentials stay in your local config. They don't go into the project repo. They don't get sent to the model. The MCP server uses them to make local connections on your behalf.

One practical note: restart your agent after changing the MCP config. The server list is read on startup.

---

### Section 5: Demo Transition (5 min)

[SLIDE 7]

[DEMO CUE — switch to terminal with Claude Code running]

Let me show you this live. I have context7 configured in my Claude setup. I'm going to ask it a question that the base model would struggle with or get wrong.

[DEMO CUE — type the following prompt]

"How do I use FluentValidation in .NET 9 to validate a command object and return all errors at once? Show me a complete example with a validator class."

[PAUSE — let it run, watch the tool calls in the output]

Notice what happens here. The agent doesn't just answer from memory. You can see it calling the context7 tool — it's resolving the library ID, then querying the docs. It's pulling in current, accurate documentation before it writes the example.

[PAUSE — 2 seconds after output appears]

Compare that to asking the same question without MCP. The base model knows FluentValidation, but it might give you syntax from an older version, or miss a .NET 9 specific behavior. With context7, you're getting an answer grounded in the actual current docs.

[DEMO CUE — show the tool call output if visible, point out the source]

This is the pattern. You don't have to tell the agent when to use MCP tools. You just configure the servers, ask your question, and the agent figures out which tools to call. That's the protocol doing its job.

[SLIDE 8]

Before we move on, a quick note on trust. MCP servers run as processes on your machine. They can access whatever you give them access to. Apply the same judgment you would to any tool: don't install MCP servers from unknown sources, review what permissions each server needs, and use environment variables for credentials rather than hardcoding them.

The official Anthropic MCP server list and well-known community servers like context7 are safe. For anything else, read the source before running it.

---

*End of M05 script. Total estimated time: 30 minutes.*
