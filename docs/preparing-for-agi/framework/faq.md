---
icon: lucide/help-circle
title: "C·A·G·R Framework FAQ"
description: "Frequently asked questions about the C·A·G·R Framework, SafeAI-Aus approach to AI safety and how our methodology differs from mainstream AI safety research."
keywords: "CAGR FAQ, AI safety FAQ, SafeAI-Aus approach, AI safety framework questions, containment alignment governance resilience"
last-reviewed: "2026-07-18"
review-cycle: "quarterly"
og_description: "Frequently asked questions about the C·A·G·R Framework and SafeAI-Aus approach to AI safety"
og_type: "article"
twitter_description: "Frequently asked questions about the C·A·G·R Framework and SafeAI-Aus approach to AI safety."
tags:
  - Framework
  - Resources
---

# C·A·G·R Framework FAQ

> **Purpose:** Answer common questions about the C·A·G·R Framework and SafeAI-Aus approach
> **Audience:** Anyone seeking to understand our methodology and how it relates to broader AI safety work | **Time:** 15-20 minutes

This page addresses frequently asked questions about the **Containment · Alignment · Governance · Resilience (C·A·G·R)** framework and how SafeAI-Aus approaches AI safety.

---

## About the Framework

### What is the C·A·G·R Framework?

C·A·G·R is a practical framework for managing advanced AI and AGI risks using familiar risk management principles. It stands for:

- **[Containment](containment.md)** — Preventing and restricting dangerous AI capabilities
- **[Alignment](alignment.md)** — Making AI systems safe by design
- **[Governance](governance.md)** — Laws, institutions and coordination mechanisms
- **[Resilience](resilience.md)** — Maintaining essential functions when things go wrong

The framework helps Australian organisations translate technical AI safety concepts into actionable strategies.

### Why four pillars instead of three?

We separate **containment** from **governance** because they answer different questions. Containment covers preventive and technical controls; governance establishes who sets, enforces and reviews the rules. The distinction also clarifies Australia's leverage: we have more control over domestic deployment and governance than frontier development overseas.

### Who is the framework for?

C·A·G·R is designed for:

- **Government** — Policy makers, regulators, national security planners
- **Business** — Executives, risk managers, boards considering AI strategy
- **Communities** — Local governments, community organisations, households
- **Researchers** — Those wanting to understand how technical AI safety applies in Australian context

---

## Framework Scope and Limitations

### What are the current limitations of AGI safety?

The C·A·G·R framework reflects current best practice, not complete solutions. Key limitations:

**Alignment verification:** We cannot yet reliably verify that advanced AI systems are truly aligned with stated goals. Systems may appear safe during evaluation but pursue different objectives in deployment ([deceptive alignment](../concepts.md#what-is-ai-alignment)). Current evaluation methods don't scale to superhuman capabilities—the [UK AI Security Institute](https://www.aisi.gov.uk/) and [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) acknowledge these gaps.

**Capability thresholds:** The framework becomes critical when AI systems can autonomously pursue goals, adapt strategies or operate across domains. Consider:

- **Low-risk (standard IT risk management):** Image classifiers, spell checkers, basic chatbots without internet access
- **Medium-risk (enhanced oversight needed):** AI agents with tool use, systems making consequential decisions, multi-step autonomous workflows
- **High-risk (C·A·G·R applies):** Systems that can develop novel strategies, autonomous cyber/bio capabilities, persuasive models deployed at scale, critical infrastructure automation

We cannot specify exact thresholds—capabilities emerge unpredictably. Evaluate based on autonomy, scope of action and consequences of failure.

**Coordination challenges:** Many protections require international cooperation we don't yet have. Containment measures work best with global [compute governance](../concepts.md#what-is-compute-governance) and [model weight](../concepts.md#what-are-model-weights) security—currently fragmented across jurisdictions.

### Where does C·A·G·R apply?

**For advanced AI (high confidence):** C·A·G·R works well when AI systems are powerful but not superintelligent, technical containment is feasible, governance can meaningfully constrain deployment and resilience provides meaningful protection. This covers most plausible near-to-medium term scenarios.

**For extreme AGI scenarios (lower confidence):** If dangerous superintelligent systems are created, containment likely fails—prevention becomes paramount. Alignment becomes load-bearing. Resilience has limits against global loss of control. Governance remains important but may be insufficient.

Australia's strategy should address both: building capability across all pillars while recognising that for worst-case scenarios, prevention (Containment Layer 1) and alignment are most critical.

### How does C·A·G·R manage time as a strategic resource?

Each pillar addresses time differently: **Containment** can delay dangerous deployment, **Governance** shapes its pace, **Resilience** creates recovery time and **Alignment** reduces the gap between capability and safety.

**Strategic principle:** Any policy that doesn't address timing—buying time, using time effectively or shaping deployment pace—is likely insufficient for managing advanced AI risks.

**Coordination constraint:** These strategies work best with international coordination. Australia acting alone can buy some time but cannot slow global capability development.

---

## Containment Questions

### Isn't containment the same as governance?

No. Governance creates authority, rules and accountability. [Containment](containment.md) covers preventive and technical controls used to restrict dangerous capabilities within those rules.

### Won't compute governance and export controls just drive AI development underground or offshore?

Some activity may move, but frontier training still depends on concentrated compute, energy and chip supply chains that are difficult to hide completely. Coordinated controls can preserve visibility and leverage, provided they are targeted and allow legitimate research. See [Containment](containment.md#1-compute-governance) for limitations and trade-offs.

### Can AI control methods really contain a sufficiently advanced AI?

Not necessarily, especially for superintelligent systems. AI control may provide meaningful protection for advanced systems, but C·A·G·R does not assume it will contain every capability indefinitely. This is why [Containment](containment.md) includes prevention and why Alignment and Resilience remain necessary.

### Won't licensing slow down innovation?

Risk-based licensing shouldn't burden low-risk systems. The goal is proportionate oversight: stringent for dangerous capabilities and critical deployments, light-touch elsewhere. Innovation in low-risk domains continues; high-risk domains get appropriate scrutiny.

---

## Governance Questions

### Won't regulation stifle innovation?

Proportionate regulation should minimise burdens for low-risk uses while applying greater scrutiny to consequential systems. Clear rules can reduce uncertainty and support responsible innovation; poor regulation can impose unnecessary costs, while under-regulation can cause harm and undermine trust. See [Governance](governance.md#1-regulatory-frameworks-and-standards).

### Can Australia really influence global AI development?

Not through unilateral regulation of frontier training (which mostly happens overseas). But:

- Our laws govern deployment here
- Procurement standards influence global providers
- Strategic partnerships amplify our voice
- Technical contributions (evaluation, research) matter regardless of size

### Why not just let industry self-regulate?

Self-regulation has a role — but the problem isn't bad faith. It's that there is significant variation in what "self-regulation" means across frontier labs. Disclosure practices, risk thresholds, evaluation methods and commitments to halt development differ substantially. This variance is itself the governance problem. METR's [analysis of frontier lab safety policies](https://metr.org/common-elements) (2025) found nine common elements across most policies — suggesting convergence is possible — but adoption remains voluntary and no formal enforcement mechanism yet exists.

A proportionate approach: self-regulation for low-risk systems, mandatory standards (drawing on emerging convergence like METR's common elements) for high-risk and frontier systems, with independent verification rather than self-assessment alone.

### Isn't international coordination unrealistic given geopolitical tensions?

Difficult, not impossible. Nuclear arms control, pandemic preparedness and international aviation show that competitors can coordinate around shared risks. AI coordination will be partial and imperfect, but common evaluation methods, incident sharing and standards can still reduce risk. See [Governance](governance.md#4-international-coordination).

---

## Applying the Framework

### How do I use C·A·G·R in practice? (Worked example)

**Consider an AI system used in public hospital triage:**

**Containment:** Was this system properly evaluated before deployment? Are there licensing requirements for high-risk medical AI? Can it be monitored in real-time for dangerous behaviours? Are there technical controls preventing unsupervised critical decisions?

**Alignment:** Is the system optimising for patient outcomes or bed occupancy rates? Does it treat different patient groups fairly? Has it been tested under realistic conditions including edge cases? Can clinicians understand why it makes particular recommendations?

**Governance:** What regulatory requirements exist? Who approved it? Who can audit decisions? What happens when it makes errors—is there clear liability? Are there mandatory incident reports? Can patients appeal AI-influenced decisions?

**Resilience:** If the system fails or is compromised, can hospitals revert to manual triage immediately? Are staff trained and practiced? Are contingencies tested regularly? Do emergency plans account for AI failures during pandemics or mass casualty events?

The same questions apply across domains—from critical infrastructure to financial services to public administration.

---

## How SafeAI-Aus differs from mainstream AI safety

Our framework differs in emphasis from much technical AI safety work:

### 1. More emphasis on resilience

We give **resilience** greater prominence because Australia cannot control all overseas development or assume every safeguard will work. Maintaining essential functions and recovery capability is practical even under deep uncertainty.

### 2. Four pillars instead of three

As noted above, we split containment from governance because the distinction matters for understanding Australia's leverage and the different types of measures involved.

### 3. More policy-oriented

We translate technical concepts for government, business and community audiences, with more emphasis on institutional design, practical implementation and Australian context than on detailed laboratory research.

### 4. Explicit scope limitations

C·A·G·R is most actionable for **advanced AI where human oversight remains meaningful**. For superintelligence scenarios, containment and resilience may have severe limits, making prevention and alignment more important.

### 5. Focus on what Australia can control

Unlike frameworks designed for frontier labs or major powers, C·A·G·R focuses on Australia's practical levers: deployment standards, procurement, domestic institutions, regional partnerships and national resilience.

---

## General Questions

### Is SafeAI-Aus affiliated with the government?

No. SafeAI-Aus is an independent, community-driven initiative. We reference government standards and collaborate with public institutions, but we're not a government project.

### Why focus on Australia specifically?

Australia is a sophisticated deployer and regulator of frontier systems developed mostly overseas. We need approaches suited to that position: limited control over upstream development, but meaningful influence through procurement, deployment rules, evaluation, partnerships and resilience.

### How does this relate to the Guidance for AI Adoption (AI6)?

The Australian Government's [Guidance for AI Adoption (AI6)](../../safety-standards/guidance-for-ai-adoption-ai6.md), published in October 2025, is now the primary guidance for responsible AI adoption. Its six essential practices update and simplify the earlier [Voluntary AI Safety Standard](../../safety-standards/voluntary-ai-safety-standard-10-guardrails.md), whose practices are incorporated into the detailed implementation guidance.

C·A·G·R complements AI6 by addressing **advanced AI and AGI preparedness** across uncertain timelines:

- AI6: "How do we adopt and govern AI responsibly today?"
- C·A·G·R: "How do we prepare for transformative AI risks?"

### Where can I learn more about the concepts used?

- **[AGI Concepts](../concepts.md)** — Detailed definitions of AGI, alignment, containment and related terms
- **[AI Glossary (Australia)](../../resources/glossary.md)** — Operational AI governance vocabulary
- **[Framework Overview](index.md)** — How C·A·G·R fits together

---

## Where to Next

!!! tip "Explore the Framework"

    **Framework pillars:**

    - [Containment](containment.md) — Preventing and restricting dangerous capabilities
    - [Alignment](alignment.md) — Making systems safe by design
    - [Governance](governance.md) — Laws and institutions
    - [Resilience](resilience.md) — Maintaining function when things go wrong

    **See the framework in action:**

    - [AGI Scenarios](../scenarios/index.md) — How risks could unfold
    - [AGI Timelines](../timelines.md) — When advanced AI might arrive

    **Practical implementation:**

    - [Preparing for AGI](../index.md) — Overview of AGI preparedness
    - [Governance Templates](../../governance-templates/policy-template-library.md) — Tools for current AI governance

---

??? note "Disclaimer & Licence"
    **Disclaimer:** This content provides general guidance on AI safety concepts. SafeAI-Aus has exercised care in preparation but does not guarantee accuracy. Organisations should adapt guidance to their specific context.

    **Licence:** Licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to copy, adapt and redistribute with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*
