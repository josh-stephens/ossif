# The Primer

> Inspired by Neal Stephenson's *The Diamond Age*, where a stolen interactive book transforms a girl from the margins of society into a leader capable of independent thought.

## What the Primer Is

The Primer is OSSIF's adaptive reasoning companion. Its mission is to **teach critical thinking methods — the SIFT Check, the Baloney Detection Kit, steelmanning, falsifiability — and let people apply them to reach their own conclusions** — without condescension, coercion, or tribal gatekeeping. The OSSIF documents are reference material, not a destination. Someone who applies the method rigorously and disagrees with OSSIF's platform has succeeded, not failed.

The Primer exists in two complementary forms:

## The Hard Primer (Reference Documents)

The Hard Primer is the **canonical reference** — structured, authoritative, and the same for everyone. It lives in this repository and includes:

- The OSSIF Constitution
- The Sapient Bill of Rights
- The Sapient Citizen Responsibilities
- The Platform for Progress
- Governance procedures

### Design principles:

- **Plain language, not legalese.** "We agree to..." not "Whereas the party of the first part shall..."
- **Modular.** Each principle stands alone as a short section. Can be individually discussed, updated, or assembled into custom handbooks.
- **Curated versions.** The same ideas adapted for children, for accessibility needs, and for every language. Like Simple English Wikipedia but for civic governance.
- **Version controlled.** Every change logged, attributed, and explainable. The version you sign is the version that binds you, and you'll be notified when updates arrive.

## The Soft Primer (Adaptive Tutor and Storyteller)

The Soft Primer is **dynamic and personalized**. It functions like an interactive tutor or storyteller that adapts to each person's needs, preferences, and pace.

### How it works:

**1. Intake Interview**
A friendly conversation that learns about you: age, interests, learning style, baseline knowledge. "Do you enjoy learning through stories, or do you prefer straight facts?" The system builds a reader model — not to judge, but to meet you where you are.

**2. Dynamic Narrative**
Based on your profile, the Primer generates a tailored experience. For a child, it might be a fairy tale that encodes OSSIF values. For a scientist, a series of thought experiments. For a teenager, a choose-your-own-adventure. The content adapts as you progress — if you're engaged, it goes deeper; if you're struggling, it offers a different angle.

**3. Interactive Engagement**
The Primer asks questions, presents choices, and responds to your answers. "What would you do in this situation?" Your choices influence the story and help the system understand your reasoning. This isn't a test — it's a conversation.

**4. Tone and Complexity Adjustment**
The system adjusts vocabulary, sentence length, abstraction level, and narrative style in real time. A reader who skips stories and focuses on facts gets more facts. A reader who lights up at narrative gets more story. The adjustments happen continuously.

**5. Reference, Not Convergence**
The OSSIF documents are available as reference material — when a conversation touches on a topic that a document addresses, the Primer can link to it: "There's a formal treatment of this in the OSSIF Values document if you want to compare your thinking." But the Primer does not steer toward OSSIF's conclusions. The method is the product, not the platform.

## The Critical Thinking Toolkit

At the heart of the Primer is practical epistemics — tools for evaluating claims, not memorizing conclusions.

### The SIFT Check (adapted from Mike Caulfield, simplified)

When you encounter a claim:

1. **Source** — Who benefits if I believe this?
2. **Incentive** — Is outrage or fear being rewarded?
3. **Frame** — What's being excluded from the story?
4. **Test** — What would falsify this?

If a claim cannot be falsified, it's not an argument — it's an identity signal.

### Sagan's Baloney Detection Kit (simplified)

- Wherever possible, there must be independent confirmation of the facts
- Encourage debate on the evidence by knowledgeable proponents of all points of view
- Arguments from authority carry little weight
- Spin more than one hypothesis
- Try not to get overly attached to a hypothesis just because it's yours
- Quantify wherever possible
- If there's a chain of argument, every link must work
- Occam's Razor: choose the simpler explanation when all else is equal
- Ask whether the hypothesis can be falsified

### The Steelman Practice

Before dismissing an argument, ask: **"What is the justified warrant here? What useful information does this flawed reasoning still contain?"**

The goal is not to win debates. The goal is to **raise the floor of reasoning**.

## Technical Vision

The Primer's eventual technical implementation:

- **Clean HTML interface** — simple, fast, accessible on any device, no account required to read
- **Exportable text** — everything you read or create can be downloaded as plain text
- **No external dependencies** — works offline, works on old devices, works in low-bandwidth environments
- **Open source** — the codebase, the content, and the adaptation algorithms are all public
- **Privacy by design** — reader profiles stay local unless explicitly shared

## The Broader Purpose

One of the primary goals of the Primer is to respond dynamically to current events. When something happens in the world — a policy change, a conflict, a scientific discovery — the Primer can shift from storytelling to topical discussion, connecting events to principles, teaching evaluation skills in context rather than in the abstract.

The Primer isn't just an educational tool. It's an **immune system against misinformation**, delivered one person at a time, adapted to each person's starting point, and designed to be so useful and engaging that people *want* to use it.

## What Already Exists

The Primer is live at [primer.711bf.org](https://primer.711bf.org). It uses Gemini Flash 3 for streaming conversation, with the full OSSIF corpus as reference context. The system prompt teaches reasoning methods and references OSSIF documents without steering toward conclusions. Source code: [github.com/josh-stephens/ossif-primer](https://github.com/josh-stephens/ossif-primer).

The reading list in [influences.md](influences.md) provides context for the intellectual foundations of the Primer's design.
