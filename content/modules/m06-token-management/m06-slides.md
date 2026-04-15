# M06: Token Management & Context — Slide Outline

---

## Slide 1: Tokens Are Not Just a Billing Unit

A token is roughly 3/4 of a word.

- "Hello world" = ~3 tokens
- A typical function = a few hundred tokens
- A large file = several thousand tokens

**The real issue:** the model has a fixed working memory measured in tokens. Everything must fit in the context window at once. What doesn't fit gets dropped.

Tokens = the unit of attention, not just cost.

Speaker note: Lead with the "unit of attention" framing, not cost. The room already knows tokens cost money. What they probably don't know is that tokens shape what the model can reason about.

---

## Slide 2: What's Actually In the Context Window

During a typical coding session, the window holds:

- System prompt + configured skills/rules
- Full conversation history from the start of the session
- Every file the agent has read
- Every tool call output (including terminal output)
- Your current message

After an hour of active use: 50,000 to 80,000 tokens is common.

**What happens near the limit:**
- Older content gets dropped
- Performance degrades as the model attends to a very large context
- The agent starts "forgetting" earlier instructions

Speaker note: This explains something developers experience but often can't diagnose: why does the agent drift in long sessions? This slide is the answer.

---

## Slide 3: Four Strategies That Actually Help

1. **Start fresh sessions for new tasks** — don't carry 60k tokens of auth context into reporting work
2. **Use /compact** — compresses history to a summary, keeps key decisions, drops the noise
3. **Load selectively** — "look at the ValidateOrder method" not "read the whole file"
4. **Front-load constraints** — important instructions belong at the start, not the end

Mental model: treat context like RAM, not disk. Fast and powerful, but limited and volatile.

Speaker note: Don't rush this slide. These four points are the practical takeaways for the whole module. Give each one a sentence of commentary.

---

## Slide 4: Cost — Rough Numbers

| Usage Pattern | Approximate Cost |
|---|---|
| Typical coding conversation | Cents |
| Full day of active individual use | Under $5 |
| Large-file heavy sessions | Adds up faster |
| Multi-step autonomous tasks | Varies — can be significant |
| Batch API calls at scale | Requires planning |

- Don't let cost anxiety slow down normal development
- Build fresh-session and /compact habits — they improve performance AND control cost
- Prompt caching: available for repeated content (system prompts), handled automatically in most tools

Speaker note: Be honest that costs are generally low for individual use but can scale. The habits that keep performance good also keep costs predictable — emphasize that alignment.

---

## Slide 5: The Summary

| Problem | Solution |
|---|---|
| Session drifts after many messages | Start fresh, use /compact |
| Agent ignores constraints from earlier | Front-load important instructions |
| Cost growing unexpectedly | Load selectively, fresh sessions |
| Agent "forgot" something it read | It was likely dropped from context |

Tokens are working memory. Manage them the same way you manage memory in code.

Speaker note: Close here. The table recaps everything. Let them read it, don't re-read it to them. Ask if there are questions before moving on.

---

*5 slides total. Estimated deck time: 13 minutes, 2 minutes buffer.*
