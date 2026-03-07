# Technology

OSSIF's technology serves its mission — it is not the mission itself. If a simpler tool works, use the simpler tool. The designs below represent the eventual architecture; implementation should be incremental and pragmatic.

## The Avatar Conversation Portal

The "front door" of OSSIF. A place where anyone can engage in structured dialogue about current events, policy, and civic engagement.

### What it does:

The Avatar is not an authority. It is a **moderator, coach, and explainer**. It does four things well:

1. **Clarify claims** — "What are we asserting? Let's separate the factual claims from the opinions."
2. **Request evidence** — "What would change your mind about this?"
3. **Surface tradeoffs** — "Who benefits? Who pays? What are the risks?"
4. **Keep it humane** — "No scapegoats, no cruelty-as-policy, no dehumanization."

### How it works:

- Users log in to talk to the OSSIF Avatar, which follows OSSIF principles in all interactions
- Conversations produce a **structured receipt**: claims made, evidence provided, uncertainties identified, proposed actions (vote registration, contact your representative, community meeting dates)
- Sometimes the founder (or other OSSIF volunteers) will be live instead of the AI — streamed conversations about current events with people doing their daily check-in
- The Avatar adapts its communication style to the user while maintaining consistent principles

### Design principles:

- The Avatar never claims authority — it asks questions and provides frameworks
- All conversations are optionally recordable and exportable
- The system should feel like talking to a thoughtful friend, not an interrogation

## Trust Tokens

A non-monetary digital token that represents commitment to OSSIF principles. Not a cryptocurrency in the financial sense — a **reputation signal**.

### Core concept:

- Each sapient entity can earn **one** Trust Token by demonstrating understanding of and commitment to OSSIF principles
- The token has no monetary value — its worth comes entirely from the social capital it represents
- Possessing the token means you've been evaluated as "cognizant" — you understand the framework and have agreed to its principles
- The token can be revoked by committee for public, documented violations of core principles
- Revocation includes clear explanation and a path to restoration

### Design decisions:

- **One token, one entity, one vote** — no accumulation, no wealth advantage
- **Placeholder tokens** for public entities (governments, corporations, public figures) with default status based on public actions
- **1 token = 1 vote** for steering OSSIF priorities (advocacy, outreach, resource allocation)
- **Public API** for anyone to check OSSIF status of any entity
- **Permissioned blockchain** for the ledger — publicly verifiable, committee-managed for revocation

### What the token is NOT:

- Not a currency — it cannot be bought, sold, or traded
- Not a social credit score — it's binary (you have it or you don't, based on transparent criteria)
- Not a gate to basic services — OSSIF participation doesn't require a token

### Considerations:

- The evaluation process must be objective and testable, not subjective or political
- Privacy must be protected — the system verifies commitment, not surveils behavior
- The blockchain component should be used only if it genuinely adds value over simpler alternatives
- The system must scale to potentially billions of entities (including sapient AI)

## Community and Governance Layer

The democratic infrastructure of OSSIF.

### Components:

**Public Principles Charter**
- Short, concrete, amendable
- The document people actually read and sign
- Version-controlled with clear change logs

**Deliberation Process**
- Structured discussion with evidence requirements
- Proposal template: goal, evidence, harms/risks, mitigation, cost, what would falsify it
- Community deliberation followed by voting
- Published results with minority reports allowed

**Conflict and Moderation System**
- Clear appeals process
- Logged decisions
- Guardrails against abuse of moderation power

### Preventing "founder capture":

The governance structure is explicitly designed so that:
- The founder has no permanent special authority
- Principles can be amended by community vote
- Leadership rotates and is elected
- All governance decisions are public and auditable

## The Mutual Aid Fund (Basic Dignity Income)

A pilot program for material support that demonstrates OSSIF values in practice.

### Design:

- **Opt-in contributions** with suggested tiers (not "half your income" as a rule)
- **Equal distribution** across all participant accounts, capped at a reasonable ceiling
- **Clear eligibility, caps, and auditable rules**
- **No political agreement required to receive help** — decoupled from belief
- **Transparent reporting**: how much collected, how many helped, what outcomes

### Naming alternatives (better than "UBI"):

- Basic Dignity Income
- Civic Stability Dividend
- Participation Dividend
- Human Floor Guarantee

### Key principle:

Separate "participation incentives" from "aid" — it must never become pay-for-belief.

## The Living Record Library

An open-access archive of all OSSIF interactions, decisions, and discussions.

### Purpose:

- **Collective learning** — everyone learns from each other's questions and reasoning
- **Transparency** — shows how decisions were reached, how principles were applied
- **Continuous improvement** — analysis of common questions and misunderstandings feeds back into the Primer
- **Accountability** — public record of governance actions

### Implementation:

- Searchable by topic, date, and type
- Open license (Creative Commons) for all content
- Accessible via simple web interface
- Exportable for offline use, research, or remixing

## OSSIF Account and Identity

### Requirements:

- **Sapient ID** — a unique, privacy-preserving identifier
- **SSO-based** with ability to transfer to other identity systems
- **Location setting** down to city level for local organizing
- **No profanity filter** on display names — freedom of expression in identity
- **Transparent and safe** — blockchain-based if that adds genuine value, simpler if it doesn't

## Technical Principles

Across all systems:

- **Simple HTML interfaces** — fast, accessible, works on any device
- **No external dependencies** where possible — works offline, works on old hardware
- **Open source everything** — code, content, algorithms, data models
- **Privacy by default** — data minimization, consent-based sharing, local-first storage
- **Exportable** — anything a user creates or interacts with can be downloaded as plain text
- **Accessible** — screen-reader friendly, high-contrast modes, text-to-speech, ARIA roles

## Implementation Priority

1. **This repository** — the documents you're reading right now
2. **A simple website** — renders these documents with clean navigation
3. **The Avatar Portal** — even a basic chatbot that follows OSSIF conversation principles
4. **The Primer prototype** — an adaptive version of the critical thinking toolkit
5. **Governance tools** — proposal/voting infrastructure
6. **Trust Token pilot** — small-scale proof of concept
7. **Mutual Aid pilot** — tiny fund with strict caps and full transparency

Each phase should be usable and valuable on its own. No phase depends on completing all previous phases. Start small, ship something, iterate.
