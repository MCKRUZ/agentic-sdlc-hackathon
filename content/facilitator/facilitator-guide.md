# Facilitator Guide: Agentic SDLC Hackathon

**Audience:** Developers, all stacks, beginner to agentic AI tools
**Format:** Full-day workshop (~100 participants)
**Tone:** Direct and practical. No hype.

---

## Before the Day

### Room Setup Checklist

- [ ] Projector or large display visible from all seats (minimum 100" equivalent at 100 people)
- [ ] Presenter screen or second monitor so you can see notes while projecting
- [ ] HDMI/USB-C adapters on hand (at least 3 spares)
- [ ] WiFi network name and password printed and posted at every table -- test throughput with 20+ concurrent connections the day before
- [ ] Dedicated facilitator machine connected to ethernet, not WiFi
- [ ] Power strips at every table: minimum 2 outlets per seat
- [ ] Extension cords (6+ spares at the front)
- [ ] Whiteboard or flip chart with markers for parking lot questions
- [ ] Printed participant workbooks stacked by table, or QR code posted to digital version
- [ ] Water and snacks confirmed for morning break and lunch
- [ ] Clock visible from presenter position or timer on second screen
- [ ] Backup machine with demo project and slides already loaded

### Participant Setup Checklist (Must Be Done Before Arrival)

Distribute this list at least 3 days before the event via email.

**Required installs:**
- [ ] An agentic coding assistant installed and authenticated
  - Claude Code (recommended): `npm install -g @anthropic-ai/claude-code` -- requires Anthropic API key
  - Cursor (alternative): download from cursor.com, sign in
  - GitHub Copilot Workspace (alternative): requires GitHub subscription
- [ ] Node.js 20 or later: verify with `node --version`
- [ ] Git: verify with `git --version`
- [ ] A code editor (VS Code strongly recommended for consistency)
- [ ] A terminal they are comfortable with (bash, zsh, or PowerShell)

**Required before arriving:**
- [ ] Cloned the DevBoard sample project: `git clone https://github.com/[your-org]/devboard-sample`
  - OR brought their own project they want to work on (must be a real codebase, not a blank repo)
- [ ] Confirmed the tool opens and responds to a test prompt ("Hello, what files are in this directory?")
- [ ] API key or subscription active (costs are real -- warn them ahead of time)

**Recommended:**
- [ ] Read the tool's "getting started" page (15 minutes)
- [ ] Reviewed the participant workbook intro section

### Facilitator Prep Checklist

- [ ] Slides loaded and advanced through once end-to-end
- [ ] DevBoard sample project cloned fresh on the demo machine (`git clone`, not a copy)
- [ ] Demo project has no existing CLAUDE.md or .cursor/rules file -- you'll create it live
- [ ] All 4 demo scripts reviewed out loud at least once
- [ ] MCP server (context7) installed and tested on demo machine: `claude mcp add context7 -- npx -y @upstash/context7-mcp@latest`
- [ ] Confirmed MCP server responds to a test query before the day
- [ ] Sample skill files on USB drive AND a shared Google Drive / network folder (have both)
- [ ] Shortened lab versions prepared for the troubleshooting section (see Troubleshooting below)
- [ ] Parking lot whiteboard section labeled and ready
- [ ] Co-facilitator or TA briefed on lab flow and common errors if available
- [ ] Timer app or browser tab ready for lab countdowns
- [ ] Feedback form link ready to share at wrap-up

### Recommended Room Configuration for 100 People

Use round or rectangular tables of 6-8 people each, not theater seating. Participants need to work on laptops and talk to each other during labs.

- 13-17 tables, 6-8 seats each
- Aisles wide enough for you to walk to any table in under 30 seconds
- Screen visible from all seats -- if the room is wide, use two side-by-side displays
- Facilitator position: front-center, not behind a podium
- Power runs down the center of each table or up through the floor -- not daisy-chained across walkways
- Consider assigning a "table lead" at each table who has already used an agentic tool before

---

## Day-of Schedule

| Time | Block | Duration | Facilitator Action | Participant Action | Notes |
|------|-------|----------|-------------------|-------------------|-------|
| 09:00 | Welcome | 15 min | Introduce yourself and co-facilitators. Explain the day's structure. State ground rules: ask questions via the parking lot board, labs are for doing not watching, mistakes are fine. Confirm WiFi is working. Do a quick show of hands: who has used an agentic tool before? | Log into their machine. Open the sample project in their editor. Pull up the participant workbook. | Take note of the hand-raise count -- it tells you how much you need to slow down in M01. |
| 09:15 | M01: Agentic Mental Shift | 30 min | Walk through the mental model slide deck. Core message: this tool is not autocomplete -- it reads context, plans steps, and executes across files. Cover: what the agent loop is, what "context window" means in plain terms, how the tool decides what to do. No live coding yet. | Listen and take notes. Answer the polling questions if you use an audience tool. | Go slow here. The biggest failure mode in the rest of the day is participants treating the tool like a search box. Get the mental model right first. |
| 09:45 | M02: Out-of-the-Box Tool Usage + Demo | 30 min | Run Demo 01 (see Live Demo Scripts below). Show the tool cold -- no config, no special setup. Walk through a real question, a file-reading request, and a small code change. Narrate what the tool is doing and why. | Watch the demo. Follow along in their own project if they want, but not required yet. | Keep the demo project simple. The goal is to show the tool works, not to impress with complexity. |
| 10:15 | LAB 01: First Interaction | 30 min | Post the lab instructions on screen. Walk the room. Answer questions at tables. Call out time at 15 minutes remaining and 5 minutes remaining. | Open their project. Follow the LAB 01 worksheet. Ask the agent a navigation question, a code explanation question, and one small change. | The most common issue: people ask vague questions and get vague answers. Redirect them to be specific. |
| 10:45 | Break | 15 min | Step away from the mic. Be available for 1:1 questions. Reset demo machine to clean state for Demo 02. | Coffee, stretch, compare notes with tablemates. | Hard stop at 11:00. |
| 11:00 | M03: Context Files + Demo | 20 min | Explain what a context file is (CLAUDE.md, .cursor/rules, etc.) and why it exists. Cover: how the tool reads it on every request, what belongs in it, what doesn't. Run Demo 02 (see Live Demo Scripts below): show a before/after prompt with and without a context file. | Watch the demo. Start thinking about what they'd put in their own context file. | Keep the before/after tight. The difference should be obvious within 2 prompts. |
| 11:20 | LAB 02: Writing Your Context File | 40 min | Post lab instructions. Walk the room and read over shoulders. The goal is for every participant to have a real, working context file committed to their project by end of lab. | Create a CLAUDE.md (or equivalent) for their project. Run 3 prompts against it. Iterate. Commit it. | The most common mistake: writing a wall of generic instructions. Push them toward specific, factual statements about their actual project. |
| 12:00 | Lunch | 60 min | Eat. Do not demo anything. Be available for questions but encourage people to step away from their laptops. | Eat. Step away. | Hard start at 13:00. |
| 13:00 | M04: Skills (Custom Commands) + Demo | 40 min | Explain what skills/slash commands/custom commands are depending on the tool. Core concept: a skill is a reusable, parameterized prompt stored as a file in the project. Run Demo 03 (see Live Demo Scripts below): build a /commit-message skill live. Show it working. | Watch the demo. | Building the skill live is more credible than showing a pre-built one. Go slow through each step. |
| 13:40 | LAB 03: Building a Skill | 35 min | Post lab instructions. Walk the room. Participants who finish early: challenge them to make the skill handle edge cases or build a second skill. | Build at least one skill for their project. Test it. | Common issue: skills that are too generic. Help them pick something concrete from their actual workflow. |
| 14:15 | Break | 15 min | Reset demo machine for Demo 04. Check in with any participants who are struggling. | Break. | Hard stop at 14:30. |
| 14:30 | M05: MCP Servers + Demo | 30 min | Explain the Model Context Protocol in plain terms: it is a way to give the agent access to external data sources and tools beyond what's in the repository. Cover: what servers exist, how they're registered, what they cost (usually nothing extra -- compute cost is on your API usage). Run Demo 04 (see Live Demo Scripts below). | Watch the demo. Note the MCP server quick reference in the workbook. | Do not go deep on building MCP servers. That is advanced. Today's goal is using existing ones. |
| 15:00 | LAB 04: Adding an MCP Server | 30 min | Post lab instructions. Walk the room. The most common issue is install errors -- have the troubleshooting steps ready. | Install and test at least one MCP server. | context7 is the recommended default because it's well-tested and broadly useful. |
| 15:30 | M06: Token Management | 15 min | Cover: what a context window is, why it fills up, how to keep it healthy. Practical rules: use /compact or /clear when the conversation gets long, put permanent context in files not chat history, scope your requests. No demo. | Listen and take notes. | This is short but important. Token burn is the most common complaint from new users after the first week. |
| 15:45 | M07: Agentic SDLC + Wrap-up | 15 min | Show where each tool used today fits in the full development lifecycle: planning, coding, reviewing, testing, deploying. Cover the 6-week sprint integration model briefly. Hand out or share the feedback form link. Thank everyone. | Fill out feedback form. Ask final questions. Exchange contact info with tablemates. | End on time. People have trains to catch. |

---

## Live Demo Scripts

### Demo 01: First Interaction (DevBoard Sample Project)

**Setup:** DevBoard project is cloned. No CLAUDE.md. No previous conversation history. Terminal is open in the project root.

**Goal:** Show the tool working cold, reading real files, and making a real change.

**Steps:**

1. Open your terminal in the DevBoard root directory.

2. Start the agent tool:
   ```
   claude
   ```
   (or open Cursor in the project folder)

3. Type exactly:
   ```
   What is this project? Give me a one-paragraph summary based on the files you see.
   ```
   Wait for the response. Point out that the tool is reading actual files, not making something up.

4. Type:
   ```
   What are the main entry points for this application? List the files and explain what each one does.
   ```
   Walk participants through the response. Point out how it cites specific files.

5. Type:
   ```
   The README says to run `npm start` but there is no start script in package.json. Add one that runs `node src/index.js`.
   ```
   Show the diff before accepting. Accept it. Run `npm start` to prove it works.

6. Say: "That is the whole demo. No configuration. No special setup. It read the project, understood the structure, and made a targeted change. That is what out-of-the-box looks like."

**What can go wrong:**
- Tool fails to start: check API key with `echo $ANTHROPIC_API_KEY`
- Response is vague: your project might need a more specific prompt -- show them how to add more detail
- npm start fails: the DevBoard project might be missing a dependency -- run `npm install` first

---

### Demo 02: Before/After Context File

**Setup:** DevBoard project is open. No CLAUDE.md exists yet.

**Goal:** Show a concrete, observable difference in agent behavior with and without a context file.

**Steps:**

1. Type this prompt WITHOUT a context file:
   ```
   Add input validation to the user registration form. Make sure it follows our conventions.
   ```
   Show the response. It will be generic -- probably just HTML5 required attributes or basic JS validation. Point this out.

2. Create a new file at the project root called `CLAUDE.md`. Type this into it:
   ```markdown
   # DevBoard Project Context

   ## Stack
   - Backend: Node.js + Express
   - Frontend: Vanilla JS, no framework
   - Database: SQLite via better-sqlite3
   - Tests: Jest

   ## Conventions
   - All validation happens server-side in the route handlers, not client-side
   - Error messages are returned as JSON: { error: "message" }
   - Never use inline styles -- use the existing CSS classes in styles.css
   - Form inputs must have corresponding labels with matching `for` and `id` attributes

   ## What Not to Do
   - Do not add new npm dependencies without asking
   - Do not modify the database schema without asking
   ```

3. Save the file. Now type the SAME prompt again:
   ```
   Add input validation to the user registration form. Make sure it follows our conventions.
   ```
   Show the response. It should now reference server-side validation, JSON error responses, and follow the label/input convention.

4. Say: "Same prompt. Different answer. The context file is how you make the tool useful for your specific project instead of generic for any project."

**What can go wrong:**
- The before response happens to be good: add something more obscure to your context file, like a specific error format, so the difference is clear
- The after response ignores the context file: check that CLAUDE.md is in the project root, not a subdirectory

---

### Demo 03: Building a /commit-message Skill Live

**Setup:** DevBoard project with CLAUDE.md from Demo 02. There are uncommitted changes in the working tree (make a small change to a JS file before the demo).

**Goal:** Build a functional skill from scratch, live, and use it immediately.

**Steps:**

1. Explain the concept first: "A skill is a markdown file that lives in a specific directory. When you invoke it, the tool reads that file and executes the instructions. It can accept parameters."

2. Create the directory:
   ```bash
   mkdir -p .claude/commands
   ```
   (or `.cursor/commands` for Cursor)

3. Create a new file at `.claude/commands/commit-message.md`. Type this content:
   ```markdown
   # commit-message

   Generate a conventional commit message for the current staged changes.

   ## Instructions
   1. Run `git diff --staged` to see what is staged.
   2. If nothing is staged, run `git diff HEAD` instead and note that changes are unstaged.
   3. Write a commit message following the Conventional Commits format:
      - Type: feat, fix, refactor, docs, test, chore, perf, ci
      - Format: `type(scope): description` -- scope is optional
      - Description: imperative mood, lowercase, no period, under 72 characters
      - If changes are complex, add a blank line followed by a body paragraph
   4. Print the commit message only. Do not run git commit.
   ```

4. Save the file. Now invoke it:
   ```
   /commit-message
   ```
   (In Claude Code this is a slash command. In Cursor, use the `@` reference to the file.)

5. Show the output. It should be a clean, properly formatted commit message based on the actual staged diff.

6. Say: "You just built a skill. It took 90 seconds. It will work on every project where you install this file, and you can share it with your team by committing it to the repo."

**What can go wrong:**
- Nothing is staged: run `git add .` before the demo
- The skill file is not found: confirm the directory path matches the tool's convention (`.claude/commands` for Claude Code, check tool docs for others)
- The output format is wrong: edit the instructions in the skill file and re-run -- show this as a feature, not a bug

---

### Demo 04: Adding context7 MCP Server Live

**Setup:** DevBoard project open. Agent tool running.

**Goal:** Install an MCP server, confirm it's loaded, and use it to answer a real question.

**Steps:**

1. Explain: "MCP stands for Model Context Protocol. An MCP server is a process that the agent can query during a conversation. It adds capabilities the agent doesn't have by default -- like looking up live documentation."

2. Run the install command:
   ```bash
   claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
   ```
   (For other tools, show the equivalent config entry in `.cursor/mcp.json` or equivalent.)

3. Restart the agent:
   ```
   /exit
   claude
   ```

4. Verify the server is loaded:
   ```
   /mcp
   ```
   context7 should appear in the list with a green connected status.

5. Now ask a question that benefits from live docs:
   ```
   Using the context7 docs, show me how to set up a connection pool with better-sqlite3. Show the exact API calls.
   ```
   Point out that the tool is calling the context7 server to retrieve current documentation, not relying on its training data.

6. Compare by asking the same question without the `context7 docs` hint to show the difference.

7. Say: "You now have live documentation access built into your agent. It costs nothing extra beyond your normal API usage."

**What can go wrong:**
- npx fails: check Node.js version (`node --version` should be 20+)
- Server shows as disconnected: run `claude mcp list` to check registration, then `/mcp` again after a moment
- context7 returns nothing useful: try a more popular library like Express or Jest -- coverage varies

---

## Handling Common Questions

**"Is this just ChatGPT in my editor?"**
No. A chat interface sends your message and waits for a response. An agentic coding tool reads your files, runs commands, edits code, and takes sequences of actions. It has access to your actual project state. That said, the underlying model is often similar -- the difference is in what the tool does with the conversation.

**"Can it break my code?"**
Yes, it can introduce bugs just like a human developer can. You should review every change before accepting it. Most tools show you a diff before writing anything. Use version control. Run your tests after any agent-driven change.

**"How much does this cost?"**
It depends on the tool and your usage. Claude Code with the Anthropic API: roughly $5-$50/month for typical developer usage, billed per token. Cursor: $20/month flat for the Pro plan with included usage. GitHub Copilot: $10-$19/month. Heavy usage or large codebases cost more. Check the pricing page for your chosen tool.

**"What if I don't want it reading my whole codebase?"**
Most tools read files on demand, not all at once. You can use a `.claudeignore` or `.gitignore`-style file to exclude directories. For sensitive data: never put secrets in source files regardless of whether you use an agent tool.

**"Can it commit and push without me knowing?"**
Only if you explicitly ask it to. By default, tools show you proposed changes and wait for approval. If you tell the tool "commit and push this," it will try to do that. Build a habit of reviewing the action list before confirming anything that modifies git history.

**"Which tool should I use?"**
It depends on your workflow. Claude Code is best for terminal-first developers who want maximum control. Cursor is best for developers who want an IDE-integrated experience. GitHub Copilot is best if you are already in the GitHub ecosystem. Start with one and learn it well before switching.

**"How is this different from GitHub Copilot?"**
Copilot's core feature is inline autocomplete -- it predicts the next line as you type. Agentic tools take multi-step actions: they read multiple files, plan a sequence of changes, execute them, and respond to your feedback. Copilot is a faster typist. An agentic tool is a collaborator.

**"What happens if it makes a mistake?"**
You catch it in review, revert the change with git, and try again with a clearer prompt. This is why you always work in a clean git state before running the agent. The tool making a mistake is not a disaster if your version control hygiene is solid.

**"Can it work on legacy code?"**
Yes, often better than expected. Legacy code is just code -- the tool can read it. The challenge is that undocumented systems are harder to give context about. A good context file describing the legacy system's quirks goes a long way.

**"Is my code being sent to the cloud?"**
Yes. Your code is sent to the model provider's API with each request. Review your tool's privacy policy and data processing agreement. Most enterprise plans offer data residency and no-training-data guarantees. Do not send code that contains secrets, PII, or data covered by an NDA without verifying your data handling terms.

---

## Troubleshooting

### Tool Won't Install

**Claude Code:**
- Requires Node.js 20+. Check with `node --version`. Install from nodejs.org if needed.
- Requires a valid `ANTHROPIC_API_KEY` environment variable. Check with `echo $ANTHROPIC_API_KEY`.
- On Windows, run the terminal as a standard user, not Administrator.
- Common error: `EACCES permission denied` on install. Fix with `npm install -g --prefix ~/.npm-global @anthropic-ai/claude-code` and add `~/.npm-global/bin` to PATH.

**Cursor:**
- Download the `.dmg` (Mac) or `.exe` (Windows) directly from cursor.com -- do not use a third-party download.
- If the app does not open on Mac, go to System Preferences > Security and allow it.

### Agent Not Finding Files

- Confirm the terminal is open in the project root, not a parent directory. Run `pwd` to check.
- On Windows, path separators can cause issues. Use forward slashes in prompts.
- If the tool is ignoring a specific file, check whether it is listed in `.gitignore` -- many tools respect it.
- For large projects, the tool may not read every file. Ask it explicitly: "Read the file at src/auth/login.ts and tell me what it does."

### MCP Server Not Loading

1. Run `claude mcp list` to see registered servers.
2. Run `/mcp` inside the agent to see connection status.
3. If the server shows as disconnected: kill the agent, wait 5 seconds, restart. MCP servers start as child processes and occasionally need a restart.
4. If context7 says "could not connect": check that npx can reach the internet. On corporate networks, a proxy may block it. Test with `npx -y cowsay hello`.
5. If the error is `command not found: npx`: Node.js is not in PATH. Fix the Node.js install first.

### Lab Running Over Time (Abbreviated Versions)

Use these if you need to cut a lab short to stay on schedule.

**LAB 01 (abbreviated, 10 minutes):**
Ask the agent one question only: "Explain the main purpose of this project in 3 bullet points." Accept or reject the answer. That's it.

**LAB 02 (abbreviated, 15 minutes):**
Give participants the pre-written context file template from the workbook. Have them fill in the stack and conventions sections only. Skip the "What Not to Do" section. Commit it.

**LAB 03 (abbreviated, 10 minutes):**
Give participants the pre-built `/commit-message` skill file from the USB drive. Drop it into their project and invoke it. Skip building it from scratch.

**LAB 04 (abbreviated, 10 minutes):**
Run the context7 install command as a group, instructor-led. Verify it shows as connected. Ask one question together. Skip individual iteration.

### Participant on Windows vs. Mac Differences

| Situation | Windows | Mac/Linux |
|-----------|---------|-----------|
| Open terminal in project | Right-click folder > "Open in Terminal" or `cd` to path in PowerShell | `cd` in Terminal, or right-click in Finder |
| Check Node version | `node --version` in PowerShell | Same in Terminal |
| Set environment variable | `$env:ANTHROPIC_API_KEY="..."` in PowerShell | `export ANTHROPIC_API_KEY="..."` in bash/zsh |
| Create directory | `mkdir .claude\commands` or `mkdir -p .claude/commands` | `mkdir -p .claude/commands` |
| Path separators in prompts | Use forward slashes anyway -- the agent handles it | Forward slashes |
| Line endings | If git shows everything as changed after agent edits, run `git config core.autocrlf true` | Not an issue |
| claude command not found | Restart PowerShell after npm install. Check PATH. | Run `source ~/.zshrc` or restart Terminal |
