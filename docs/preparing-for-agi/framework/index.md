---
icon: lucide/shield-alert
title: "C·A·G·R Framework - AGI Safety & Governance Framework"
description: "The Containment, Alignment, Governance, Resilience (C·A·G·R) framework helps Australian organisations manage advanced AI and AGI risks using defence-in-depth principles."
keywords: "CAGR framework, AGI safety framework, AI governance framework Australia, defence in depth AI, AI containment, AI alignment, AI resilience, advanced AI risk management, AI safety Australia"
last-reviewed: "2026-07-18"
review-cycle: "quarterly"
og_title: "C·A·G·R Framework - AGI Safety & Governance"
og_description: "Defence-in-depth framework for managing advanced AI and AGI risks in Australia."
og_type: "article"
twitter_title: "C·A·G·R Framework - AGI Safety"
twitter_description: "Defence-in-depth framework for managing AGI risks in Australia."
faq:
  - question: "What is the C·A·G·R framework?"
    answer: "C·A·G·R stands for Containment, Alignment, Governance, Resilience - four interconnected pillars for managing advanced AI risks using defence-in-depth principles."
  - question: "Why does Australia need an AGI safety framework?"
    answer: "Australia imports frontier AI from the US and China but bears full impact when deployed in critical infrastructure. We need frameworks to evaluate and govern systems we didn't build."
  - question: "What is defence-in-depth in AI safety?"
    answer: "Defence-in-depth uses multiple independent layers of protection, assuming any single measure may fail. It's adapted from nuclear safety and cybersecurity for AI risk management."
tags:
  - Framework
  - Containment
  - Alignment
  - Governance
  - Resilience
---

# Containment · Alignment · Governance · Resilience Framework

> **Purpose:** Practical framework for managing advanced AI risks using familiar risk management principles
> **Audience:** Government, business and community organisations | **Time:** 30-45 minutes

## What this page is for

The **C·A·G·R framework** (Containment · Alignment · Governance · Resilience) is a SafeAI-Aus planning framework for Australian organisations. It applies **defence-in-depth** principles from nuclear safety and cybersecurity to advanced AI safety, governance and resilience.

C·A·G·R translates technical concepts into familiar risk-management language. It covers both catastrophic safety failures and governance challenges that persist even when systems behave as intended.

After reading this page, you'll understand:

- how C·A·G·R maps AI risks onto standard risk management
- what each of the four pillars (Containment, Alignment, Governance, Resilience) means in practice
- how the three layers of defence-in-depth work
- where to find detailed guidance and assurance evidence

---

## The C·A·G·R Framework: Defence-in-Depth as Strategy

Australia faces [three interconnected strategic challenges](../index.md#what-strategic-challenges-does-australia-face): we can't verify what we import, international coordination is hard and time is a constraint.

C·A·G·R organises a defence-in-depth response across four interconnected pillars.

**The gap we're filling:** Technical AI safety research uses specialised terminology that doesn't map to operational risk management. International frameworks assume direct oversight of frontier AI labs. Australian guidance focuses on current AI risks rather than advanced AI preparedness.

**Design choices:**

- **Familiar foundations:** Maps directly onto prevention, safety by design, compliance and resilience—risk management you already do
- **Honest about Australia's position:** We don't control frontier AI development overseas, so we focus on what we can control: deployment standards, procurement, governance and national resilience
- **Defence-in-depth:** Assumes any single measure can fail and uses multiple overlapping protections
- **Action-oriented:** Each pillar connects to concrete guidance for government, business and communities

**Why now:** AI capability and deployment can change faster than legislation, institutional capability and international coordination. [METR's measurements](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) track rapid growth in the length of software tasks frontier models can complete autonomously; this is one capability indicator, not a direct measure of AGI. A [Good Ancestors survey](https://www.goodancestors.org.au/our-work/ai-safety/aisi-expert-survey) (December 2025, n=139) found 88.8% of its selected AI safety respondents wanted Australia's AI Safety Institute to prioritise catastrophic risks or take a balanced approach. These signals support anticipatory planning, but do not validate C·A·G·R itself.

**How it was developed:** C·A·G·R is a SafeAI-Aus synthesis. Its influences include international AI safety research from [Anthropic](https://www.anthropic.com/research), [Google DeepMind](https://www.deepmind.com/safety-and-ethics), [OpenAI](https://openai.com/safety) and the [UK AI Security Institute](https://www.aisi.gov.uk/); [ISO 31000](https://www.iso.org/iso-31000-risk-management.html); defence-in-depth in [nuclear safety](https://www.nrc.gov/reading-rm/basic-ref/glossary/defense-in-depth) and [cybersecurity](https://csrc.nist.gov/glossary/term/defense_in_depth); [BlueDot Impact's defence-in-depth model](https://blog.bluedot.org/p/course-portfolio-vision); biosecurity practice; and consultation with researchers and practitioners.

---

!!! warning "Current limitations"

    C·A·G·R is a planning aid, not a complete or validated safety solution. Key gaps include unreliable alignment verification, unclear capability thresholds and limited international coordination. See [Framework Scope and Limitations](faq.md#framework-scope-and-limitations).

---

## How C·A·G·R relates to risk management you already know

Australia already uses prevention, safety by design, compliance and resilience to manage risk. C·A·G·R maps those functions to advanced AI:

| **Risk function** | **C·A·G·R pillar** | **Core question** |
|-------------------|--------------------|-------------------|
| Prevention | **Containment** | Can we stop dangerous systems from being built, accessed or deployed? |
| Safety by design | **Alignment** | Do systems behave as intended across relevant conditions? |
| Rules and accountability | **Governance** | Do authority, oversight and redress work in practice? |
| Continuity and recovery | **Resilience** | Can essential functions withstand failures and recover? |

**What makes AI different:**

C·A·G·R isn't just standard risk management with new labels. AI systems have some properties that stretch traditional approaches:

- **Opacity:** Even experts often can't fully explain why systems make particular decisions
- **Emergent behaviour:** Capabilities and failures can appear that weren't present during testing
- **Speed and scale:** AI-enabled actions can outpace human oversight and decision-making
- **Compounding effects:** AI systems interact with each other in ways that are hard to predict
- **Power concentration:** A small number of global actors control key capabilities
- **Dual-use:** The same capabilities that enable beneficial uses also enable harmful ones

These properties make reliance on any single safeguard especially fragile.

---

## What are the four pillars of C·A·G·R?

### Containment: How Do We Prevent Dangerous AI Systems?

Containment is about stopping dangerous AI systems before they cause harm. This includes preventing dangerous training runs, restricting deployment of high-risk systems and maintaining technical controls over powerful AI.

Containment includes:

- Compute governance: oversight of chips, data centres and large training runs
- Export controls and supply chain security for advanced hardware
- AI control methods: monitoring, restrictions and containment protocols
- Licensing and safety evaluations before deployment

**For Australia:** We have limited leverage over frontier AI training (mostly happening overseas), but significant influence through compute governance, deployment licensing and procurement requirements.

[Read more: Containment in depth](containment.md)

### Alignment: How Do We Make AI Systems Reliably Safe?

Alignment is about the behaviour and objectives of AI systems. We care that systems:

- Behave predictably and safely across a wide range of conditions
- Don't pursue goals that diverge from human intent, law or public interest
- Resist being repurposed or "jailbroken" for harm
- Remain safe and controllable as capabilities scale

**For Australia:** We mostly import advanced models, so alignment means being able to evaluate and constrain their behaviour in our context, not just trusting provider claims.

[Read more: Alignment in depth](alignment.md)

### Governance: What Laws and Institutions Do We Need?

Governance is about laws, institutions and coordination that shape how AI is developed and deployed. Even well-aligned systems can cause harm if used at inappropriate scale or in contexts where errors are unacceptable.

Governance includes:

- Regulatory frameworks and standards appropriate to risk levels
- Clear responsibilities across regulators and public bodies
- International coordination to avoid dangerous capability races
- Transparency, reporting and accountability mechanisms

**For Australia:** Governance is where we have real sovereignty — our laws apply to systems deployed here, even if trained overseas. We can also influence international coordination through strategic partnerships.

[Read more: Governance in depth](governance.md)

### Resilience: How Do We Cope When Things Go Wrong?

Resilience is the capability to detect, respond to and recover from AI-related harms while maintaining essential functions and social cohesion.

Even with good containment, alignment and governance, systems can fail in unexpected ways, malicious actors can exploit capabilities and compounding events can overwhelm normal safeguards.

Resilience spans:

- National and institutional continuity planning
- Biosecurity and cybersecurity hardening
- Detection, response and recovery capabilities
- Community and household resilience
- Social cohesion and trusted communication

**For Australia:** Resilience is the capability we can build regardless of what happens overseas or in systems we do not control.

[Read more: Resilience in depth](resilience.md)

---

## Why do all four pillars matter?

Each pillar covers a failure the others cannot fully address:

- **Alignment without containment or governance** can still permit dangerous access and deployment.
- **Governance without containment** may act only after dangerous capabilities already exist.
- **Containment and governance without resilience** leave essential functions brittle when prevention fails.
- **Resilience without prevention, alignment or governance** treats recurring harm instead of reducing its causes.

Effective strategy considers all four pillars, then gives each weight according to the organisation's responsibilities, exposure and practical influence.

---

## When should you escalate AGI preparedness?

As the AI systems you deploy become more capable, your preparedness measures should scale accordingly. Drawing on [Responsible Capability Scaling](https://deepmindsafetyresearch.medium.com/agi-safety-and-alignment-at-google-deepmind-a-summary-of-recent-work-8e600aca582a) approaches from frontier labs, you should define capability thresholds that trigger escalation.

**Escalation principle:** Higher capability systems require stronger safeguards across all four pillars:

- **Current advanced AI** (tool use, extended reasoning) → Documented risk assessment, evaluation, red-teaming and tested fallbacks proportionate to the use case
- **High-autonomy systems** (multi-step planning, environment interaction) → Runtime monitoring, approval gates and incident exercises
- **Critical integration** (essential infrastructure, cross-system dependencies) → Isolation boundaries, rollback capability, continuity planning and engagement with the applicable regulator
- **Systems capable of autonomous AI R&D** → **Pause deployment** pending safety validation, governance review and appropriate international coordination

These are illustrative escalation points—you should adapt thresholds to your organisation's risk tolerance and deployment context. For implementation details, see the individual [Containment](containment.md), [Alignment](alignment.md), [Governance](governance.md) and [Resilience](resilience.md) pages.

---

## What are the three layers of defence-in-depth?

C·A·G·R applies **[defence-in-depth](https://www.nrc.gov/reading-rm/basic-ref/glossary/defense-in-depth)** from nuclear safety and cybersecurity through three layers. Each layer assumes earlier protections may fail, and all four pillars can contribute across the layers.

### Layer 1: Prevent dangerous AI training
*Stopping dangerous systems from being created in the first place*

This is primarily the domain of **Containment**, but involves all pillars:

- Compute governance: oversight of chips, data centres and training runs
- Export controls and supply chain security
- International cooperation on frontier model safety standards
- Research capacity for evaluating training risks

**Australia's role:** Limited direct leverage over overseas AI labs, but significant influence through compute supply chains, international partnerships and setting expectations for systems deployed here.

### Layer 2: Constrain dangerous capabilities and deployments
*If systems are trained, require evidence of safety and effective controls*

This layer integrates **Containment**, **Alignment** and **Governance**:

- Safety evaluations and licensing before deployment
- AI control methods: monitoring, restrictions, containment protocols
- Regulatory requirements appropriate to risk levels
- Access controls and use policies
- Ongoing monitoring and incident reporting

**Australia's role:** Strong sovereignty here. Our laws govern deployment, procurement sets standards and we can require evidence of safety properties.

### Layer 3: Withstand dangerous AI actions and failures
*If dangerous systems exist and escape control, maintain essential functions*

This is the domain of **Resilience**, supported by **Governance**:

- National and sectoral continuity plans for AI-related threats
- Manual fallbacks and "safe modes" for critical services
- Biosecurity and cybersecurity hardening
- Community preparedness, trusted local communication and support networks
- Capability to function during disruptions to AI-mediated services

**Australia's role:** This is a core sovereign capability that Australia should build regardless of what happens overseas.

**Note on ordering:** We present these layers top-down (1→2→3) to reflect the logic of defence-in-depth: prevent first, constrain if prevention fails, withstand if containment fails. For practical planning, start from the bottom: establish Layer 3 continuity capability, build Layer 2 controls where you have authority, then contribute to Layer 1 measures where you have influence.

---

## How should you use the C·A·G·R framework?

**For risk assessment:** Consider your current AI dependencies across all four pillars and three layers. Are you neglecting a relevant protection or over-relying on one?

**For strategy:** Give greatest weight to the pillars where you have responsibility and practical leverage, while checking that important dependencies on the other pillars are visible. Prioritise bottom-up: Layer 3 first (what you must be able to do), Layer 2 (where you have control), then Layer 1 (where you have influence).

**For exercises:** Combine with [AGI scenarios](../scenarios/index.md). For each scenario, ask what containment, alignment, governance and resilience would look like in your context. Test whether your current capabilities work under stress.

**For policy:** Use C·A·G·R to structure proposals—which pillar(s) and layer(s) does this address? Where are the gaps?

---

## Next steps

**Explore each pillar:**

- [Containment](containment.md) — preventing dangerous AI systems from being built or deployed
- [Alignment](alignment.md) — making AI systems reliably safe and aligned with human values
- [Governance](governance.md) — laws, institutions and international coordination
- [Resilience](resilience.md) — withstanding and recovering from AI-related disruptions

**Apply to scenarios:**

- [AGI Scenarios for Australia](../scenarios/index.md) — work through concrete scenarios using C·A·G·R

**Apply to your responsibilities:**

- [Sector Guidance](../../sector-guidance/index.md) — translate C·A·G·R into decisions for government, business, communities and national security

**Demonstrate preparedness:**

- [AGI Assurance](assurance.md) — evidence and testing for advanced AI preparedness

**For researchers:**

- [Framework FAQ](faq.md#how-safeai-aus-differs-from-mainstream-ai-safety) — how SafeAI-Aus differs from mainstream AI safety
- [AGI Concepts](../concepts.md) — technical AI safety terminology

---

??? note "Disclaimer & Licence"
    **Disclaimer:** This content provides strategic guidance on AGI preparedness frameworks. SafeAI-Aus has exercised care in preparation but does not guarantee accuracy or completeness. Organisations should adapt guidance to their specific context and may wish to seek professional advice.

    **Licence:** Licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to copy, adapt and redistribute with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*
