# Roadmap

This document describes the concrete build path from "a set of documents on GitHub" to a functioning civic ecosystem. Each phase produces something usable. No phase requires completing all previous phases, but they build on each other naturally.

## Phase 1: The Primer (In Progress)

**What:** An adaptive conversational interface grounded in the OSSIF corpus. The front door to everything else.

**How it works:**
- A clean web chat interface — show up, no account required
- Powered by a large language model with the OSSIF documents as grounding
- The system discovers where someone is — epistemically, emotionally, culturally — through conversation, not intake forms
- Adapts its language, framing, examples, and pacing without compromising the principles
- Conversations converge on OSSIF's core ideas regardless of entry point

**Audience adaptation (not separate products — the same system, tuning itself):**
- A teenager gets different language than a retiree
- A person leaving a high-control religion gets gentler framing than a policy wonk
- Someone overwhelmed by emotions gets grounding exercises before logical frameworks
- A partisan gets their own values reflected back with better reasoning, not a lecture
- A child gets stories; a scientist gets thought experiments; an engineer gets systems diagrams
- Accessibility adaptations: screen-reader optimized, plain language, Braille-ready output (via BrailleBlaster/DAISY format), audio narration

**The invitation:** Every Primer conversation can lead to an invitation to join the OSSIF community. Not a sales pitch — a natural conclusion: "These ideas seem to resonate with you. There's a community of people reasoning together about this. Want to see it?"

**Technical stack:**
- Python or Node backend with streaming LLM responses
- Simple HTML/CSS/JS frontend — fast, accessible, works on any device
- Deployed to a public URL (primer.ossif.org or primer.eusd.org)
- Open source — the system prompt, the adaptation logic, all of it

**Status:** Live at [primer.711bf.org](https://primer.711bf.org). FastAPI backend with Gemini Flash 3 streaming, full OSSIF corpus as system prompt context. Iterating on conversation quality and adaptation logic.

## Phase 1.5: Web Contributions (Committed — 1 week)

**What:** A browser-based contribution mechanism so people can participate in OSSIF without knowing git.

**The problem:** The council identified this as "the class problem" — requiring GitHub literacy to contribute creates a barrier that filters for a narrow demographic. A framework about inclusive reasoning that can only be improved by people who know `git rebase` has a credibility gap.

**How it works:**
- The documentation site at [ossif.711bf.org](https://ossif.711bf.org) gets an "Edit this page" button on every document
- Clicking it opens a simple web editor — no GitHub account required
- Submissions go through a moderation queue (initially founder-reviewed, transitioning to community-reviewed)
- Accepted changes become PRs on the repository automatically
- Contributors are credited by name or pseudonym in the commit history

**Why this matters:** Every unaddressed access barrier is a filter on who gets to shape the framework. Git is a tool for developers, not a prerequisite for civic participation.

**Timeline:** Operational within one week of this commit. This is a commitment, not an aspiration.

## Phase 2: The Platform

**What:** A member communication and governance space — the place OSSIF members find common ground, deliberate, and organize.

**How it works:**
- Self-hosted, independently operated — not Discord, not Slack, not beholden to anyone's moderation policy or business model
- Structured channels for deliberation, not just chat
- Proposal/voting infrastructure built on the governance procedures in [governance.md](governance.md)
- Trust Token integration for identity and participation without surveillance
- Exportable — anything you write, you can take with you

**Why not use existing platforms:**
- Existing platforms optimize for engagement, not reasoning
- Their moderation policies change without notice or consent
- Their business models create conflicts of interest with OSSIF's mission
- Self-hosting means the community owns its infrastructure

**Technical direction:**
- Matrix protocol (federated, open source, encrypted) as the likely foundation
- Custom frontend that enforces OSSIF's deliberation norms (evidence requirements, steelman prompts, structured receipts)
- Or a custom build if Matrix doesn't fit — the interaction patterns matter more than the protocol

## Phase 3: The Lens

**What:** A candidate and policy transparency tool. Shows voters what their representatives actually do, through the lens of OSSIF principles.

**How it works:**
- Aggregates independently sourced data: voting records, donor lists, public statements, lobbying relationships
- Maps each candidate's actual positions against their public platform — surfaces contradictions
- Generates personalized research packets: "Here are the candidates on your ballot, here's what OSSIF's analysis shows, here's what you should ask about"
- Not partisan — applies the same evidence standards to every candidate regardless of party
- The SIFT Check and Baloney Detection Kit applied to political claims in real time

**Data sources:**
- Congressional voting records (public APIs)
- FEC donor data (public)
- Lobbying disclosures (public)
- Public statements and social media (archived, timestamped)
- News coverage cross-referenced against primary sources

**The goal:** Make it trivially easy for any voter to see when they're being lied to. Not by telling them what to think — by showing them the receipts and teaching them to read them.

## Phase 4: Safe Harbor

**What:** An open-source video platform with AI-powered content moderation, designed for organizations that need to curate safe viewing environments — schools, churches, families, community centers.

**How it works:**
- Any organization can deploy their own instance — no central authority decides what's appropriate
- Videos are submitted, not scraped — curators choose what enters the library
- Every submitted video is analyzed frame-by-frame by Gemini models before publication:
  - Content classification (violence, language, themes, age-appropriateness)
  - Deceptive content detection (videos that start innocuous and shift — the Peppa Pig problem)
  - Compliance check against the organization's stated standards
  - Full analysis report attached to each video, publicly viewable
- No ads. No algorithmic recommendations optimized for watch time. No autoplay rabbit holes.
- Clean grid interface that organizations can customize

**Builds on:** The [youtube-collection](https://github.com/josh-stephens/youtube-collection) project — 57K video library with Gemini analysis pipeline already operational.

**Technical direction:**
- Self-hostable (Docker container or simple deployment)
- Video storage: organization's choice (local, S3, existing YouTube embeds with controls)
- Gemini multimodal analysis pipeline (already proven in youtube-collection)
- Organization admin panel for setting content standards and reviewing flagged videos

## Phase 5: The Interface

**What:** An adaptive, WebSocket-driven universal interface that can become whatever the user needs — media browser, device controller, home dashboard, accessibility tool.

**The insight:** A sufficiently capable streaming interface doesn't need to be one thing. The same full-screen canvas that shows curated videos can also show security camera feeds, device controls, sensor data, communication tools — anything that can be rendered as HTML and driven by a WebSocket.

**What this enables:**
- **Home automation:** Voice-controlled or gesture-controlled device management — garage doors, cameras, lights, climate — through a single adaptive interface
- **Accessibility:** The interface reshapes itself for the user's needs — large controls, voice-only, screen-reader optimized, simplified layouts
- **Ambient awareness:** Camera feeds with recognition (your kids arriving home), sensor dashboards, notification streams
- **Personality:** AI-driven responses to events — greeting family members through speakers, contextual announcements, humor as a feature
- **User customization:** Every element of the screen is rearrangeable, resizable, and replaceable by the user

**Technical direction:**
- Full-screen web app, WebSocket backbone for real-time state
- Home Assistant integration for device control and sensor data
- TTS models (Kokoro, etc.) for voice output
- Camera integration (Reolink, etc.) with recognition capabilities
- The same principles as OSSIF's technology doc: simple HTML, works on any device, open source, privacy by default

**This is the long game.** Phases 1–4 serve the civic mission directly. Phase 5 is the ambient infrastructure that makes interacting with all of it feel natural rather than effortful.

## Cross-Cutting Concerns

These apply to every phase:

**Accessibility is not an afterthought.** Every interface ships with screen-reader support, plain language options, high contrast modes, keyboard navigation, and exportable text. Braille and audio adaptations are first-class output formats.

**Open source everything.** Code, content, algorithms, data models, system prompts, moderation criteria. If it runs OSSIF infrastructure, it's public.

**Privacy by default.** Data minimization. Consent-based sharing. Local-first storage. No surveillance as a feature.

**Self-hostable.** Every component should be deployable by anyone. OSSIF's infrastructure is a reference implementation, not a monopoly.

**Internationalization.** All user-facing content translated into 10+ languages via the automated Gemini pipeline (already operational for the document corpus).

## Current State

| Phase | Status | Next Step |
|-------|--------|-----------|
| Documents | Live at [ossif.711bf.org](https://ossif.711bf.org) — 14 docs, translated to French, 9 more languages in pipeline | Full 10-language translation run |
| The Primer | Live at [primer.711bf.org](https://primer.711bf.org) — streaming chat with full corpus | Conversation quality iteration, user testing |
| Web Contributions | **Committed — 1 week** | Build edit UI on docs site, submission queue, auto-PR |
| The Platform | Conceptual ([technology.md](technology.md) governance layer) | Evaluate Matrix vs custom build |
| The Lens | Conceptual | Research data source APIs, prototype scorecard |
| Safe Harbor | Foundation exists ([youtube-collection](https://github.com/josh-stephens/youtube-collection)) | Adapt analysis pipeline for moderation use case |
| The Interface | Conceptual + existing home automation infrastructure | Prototype WebSocket canvas with HA integration |

## Timeline Philosophy

This is a multigenerational project. The founder will not see it completed. That's fine.

What matters is that each phase produces something useful *now* — not a promise for later. The Primer helps someone think more clearly today. The Lens helps someone vote more wisely this cycle. Safe Harbor helps a parent protect their kid this week.

Build what's useful. Ship it. Iterate. Let the community decide what comes next.
