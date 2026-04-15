# M06: Token Management & Context
## Presenter Script — 15 minutes, no demo

---

### Section 1: What Tokens Are (3 min)

[SLIDE 1]

Tokens come up in two contexts and people often conflate them: cost and capability. They're related but distinct, and the capability angle matters more for how you work day to day.

A token is roughly three-quarters of a word. "Hello world" is about three tokens. A typical function is a few hundred tokens. A large file might be several thousand.

The reason this matters is that the model has a fixed working memory — the context window — measured in tokens. Everything the model knows about your current conversation, your code, your files, your instructions, has to fit inside that window at once. When something doesn't fit, it gets dropped.

[PAUSE — 2 seconds]

So tokens aren't just a billing unit. They're the unit of attention. The model can only reason about what's currently in the window. This shapes every decision about how you structure long conversations.

---

### Section 2: The Context Window (4 min)

[SLIDE 2]

Current models have large context windows — in the range of 100,000 to 200,000 tokens for frontier models. That sounds like a lot, and for most tasks it is. But long agentic sessions consume tokens faster than you'd expect.

Here's what's in the window during a typical coding session:

Your system prompt and any skills or rules you've configured. The full conversation history going back to the start of the session. Every file the agent has read. Every tool call output — including all those lines from terminal commands. Your latest message.

After an hour of active use, a session can easily hit 50,000 or 80,000 tokens. Once you approach the limit, two things happen. The model starts dropping older content from the window — usually the oldest parts of the conversation. And performance degrades even before the hard limit, because the model has to attend to a very large context to find the relevant parts.

[PAUSE — 2 seconds]

This is why long sessions drift. It's not that the model got worse. It's that the context it's working from got noisier as older, potentially contradictory information accumulated.

The practical symptoms: the agent forgets what you told it earlier, contradicts a decision it made twenty messages ago, or produces output that ignores constraints you specified at the start of the session.

---

### Section 3: Practical Strategies (5 min)

[SLIDE 3]

There are four strategies that actually help.

**Start fresh sessions for new tasks.** This is the most effective one. When you finish a feature and start a new one, open a new conversation. Don't carry forward a 60,000-token session about the authentication module into your work on the reporting module. The old context is noise, not signal.

**Use /compact or summarization.** Most agent tools have a command or feature that compresses the conversation history into a summary. Claude Code has `/compact`. This keeps the key decisions and context while discarding the verbose back-and-forth that accumulated getting there. Use it when you feel a session getting long — don't wait until you hit the limit.

**Be selective about what you load.** When you ask the agent to read a file, it reads the whole file. If you only need one function, tell it which function to look at. "Look at the `ValidateOrder` method in OrderService.cs" is more efficient than "read OrderService.cs" when that file is 800 lines long.

**Front-load your constraints.** Instructions at the start of a conversation are in the most stable part of the context. If you put your constraints at the end — "by the way, all output should use kebab-case filenames" — that instruction might drift out of focus in a long session. Put the important stuff first.

[PAUSE — 2 seconds]

The underlying mental model: treat the context window like RAM, not disk. Fast, powerful, but limited and volatile. Design your sessions around that constraint.

---

### Section 4: Cost Awareness (3 min)

[SLIDE 4]

On the cost side: for most development tasks during a hackathon or normal workday, costs are low. A typical coding conversation costs cents. A full day of active use with a frontier model like Claude Sonnet is likely under five dollars for an individual developer.

Where costs climb:

Long sessions with large files. If every message causes the agent to re-process a 10,000-line file, that adds up fast.

Autonomous multi-step tasks. When you kick off an agent task that runs 20 tool calls, each step consumes tokens. Complex agentic workflows can cost significantly more than conversational use.

Batch operations at scale. If you're running a script that calls the API hundreds of times, cost planning matters.

[PAUSE — 2 seconds]

The practical guidance: don't let cost anxiety slow you down during normal development. The productivity gains are worth it. But do build the habit of starting fresh sessions and using compaction, because those habits keep costs predictable and keep the agent performing well — those two goals align.

Prompt caching is worth knowing about: some providers offer discounted token rates for repeated content in the same session, like a system prompt you send on every call. If you're building a system that calls the API programmatically, look into caching. For interactive use today, it's handled automatically.

---

*End of M06 script. Total estimated time: 15 minutes.*
