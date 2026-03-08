# Governance

This document describes how OSSIF is actually governed — not how it aspires to be governed someday, but who holds power right now, how decisions are made, and what constraints exist. If the map doesn't match the territory, the map is wrong.

## Current State: Founder-Controlled

As of this writing, OSSIF is controlled by a single person: **Josh Stephens** (GitHub: josh-stephens).

Josh controls:
- The GitHub repository (merge authority, branch protection, settings)
- The council session prompts and architecture
- The contributing guidelines
- The narrative and framing of all documents
- The decision of what gets published and what doesn't

This is not hidden, and it is not permanent. But it must be stated plainly, because a framework that claims to prevent power concentration while concentrating power in one person has a credibility problem — even if the concentration is temporary and well-intentioned.

## Decision-Making Process

### Current (pre-community)

While OSSIF has no meaningful community beyond the founder:
- The founder makes all decisions
- The United Sapients Council provides adversarial review
- Council recommendations are tracked and their implementation status is public (see below)
- All decisions are documented in the repository's commit history

### Target (post-community)

Once a community exists:
- **Ordinary decisions** (clarifications, examples, maintenance): any contributor can submit a PR, merged by any maintainer
- **Significant changes** (new content, rewording): issue discussion required, merged after community input
- **Foundational changes** (core values, governance structure): formal proposal, 90-day deliberation, supermajority vote
- **Dissolution**: see below

## Council Recommendation Tracker

The United Sapients Council exists to stress-test OSSIF. Its recommendations are not binding, but ignoring them without explanation is a structural failure. This tracker holds the framework accountable.

| # | Recommendation | Session | Status | Response |
|---|---------------|---------|--------|----------|
| 1 | Build an open evidentiary standard | 001 | **In progress** | This governance doc + falsifiability.md are the first steps. A formal evidentiary standard document is next. |
| 2 | Design institutions with sunset clauses | 001 | **In progress** | Sunset review and dissolution criteria added below. |
| 3 | Address the class problem (GitHub as access barrier) | 001 | **Not started** | Acknowledged. Requires a non-GitHub participation path. |
| 4 | Make epistemic humility structural, not aspirational | 001 | **In progress** | falsifiability.md, this governance doc, and the values.md rewrite of "non-negotiables" are structural moves. |
| 5 | Ensure absolute dissent protection | 002 | **Done** | CONTRIBUTING.md rewritten to prohibit sabotage behaviors, not dissenting conclusions. |
| 6 | Create a values cost log | 002 | **Done** | See below. |
| 7 | Establish structural dependency transparency | 002 | **Done** | This document's "Current State" section. |

## Founder Constraints

The following constraints apply to the founder immediately:

1. **No unilateral changes to foundational commitments.** The values in values.md cannot be changed by the founder alone once a community exists.
2. **Council recommendations require a published response.** Ignoring a recommendation without explanation is prohibited. Disagreement is fine; silence is not.
3. **This governance document cannot be weakened by the founder alone.** Any change that reduces accountability, removes constraints, or concentrates power requires the same process as a foundational change.
4. **The founder can be removed.** If the community reaches a size where governance transitions are possible (10+ active contributors), a recall process becomes available: petition by one-third, vote by simple majority.

These constraints are currently self-imposed, which means they rely on the founder's integrity. That is an honest weakness. The goal is to build toward external enforcement as the community grows.

## Sunset Review

Every structural decision, policy position, and governance mechanism undergoes mandatory review on a fixed schedule:

- **Policy positions** (platform.md): reviewed every 2 years
- **Governance structures**: reviewed every 3 years
- **Foundational commitments**: reviewed every 5 years
- **Reviews conducted by**: members not involved in the original decision, plus at least one council session

A review does not mean a change is required. It means a change is *considered*, with evidence, and the decision to keep or revise is documented.

## Dissolution Criteria

OSSIF should cease to exist if:

1. **The framework fails its own falsifiability tests** (see [falsifiability.md](falsifiability.md)) and cannot be revised to address the failures
2. **The governance structures are captured** and self-correction mechanisms have failed to restore accountability
3. **The framework causes net harm** — if evidence shows OSSIF is increasing suffering, concentrating power, or degrading reasoning rather than improving it
4. **The community votes to dissolve** — by supermajority, after a deliberation period

Dissolution means: the repository is archived (not deleted), all documents remain publicly available under their Creative Commons license, and a final report documents what worked, what didn't, and why.

An organization that cannot describe the conditions of its own death cannot be trusted. This section exists so that OSSIF can die well if it needs to.

## Values Cost Log

A public, append-only record of what OSSIF's values have actually cost. Values that have never been expensive have never been tested. This log tracks the moments when upholding a principle required sacrifice — not just words, but something real.

| Date | Value Tested | What It Cost | Who Bore the Cost | Notes |
|------|-------------|-------------|-------------------|-------|
| 2026-03-07 | Self-correction / Epistemic humility | Publicly acknowledged that the council's 0-for-7 score was a valid indictment, not an unfair attack. Rewrote foundational documents in response. | Founder (ego, narrative control) | The council's session 003 evaluation was harsh and largely correct. Responding with structural changes rather than defensive prose is the first entry in this log. |

If this log is empty after one year, OSSIF should publicly acknowledge that its values have not been tested and therefore cannot be claimed as operational principles.
