---
icon: lucide/shield-check
title: "AGI Assurance - Evidence for Advanced AI Preparedness"
description: "How Australian organisations can seek evidence, testing and accountability for advanced-AI preparedness using the C·A·G·R framework."
keywords: "AGI assurance, AI safety evidence, advanced AI testing, AI preparedness verification, C·A·G·R assurance, AI safety auditing"
author: "SafeAI-Aus"
robots: "index, follow"
last-reviewed: "2026-07-18"
review-cycle: "quarterly"
og_title: "AGI Assurance - Evidence for Advanced AI Preparedness"
og_description: "Demonstrate AGI preparedness through evidence, testing and accountability."
og_type: "article"
og_url: "https://safeaiaus.org/preparing-for-agi/framework/assurance/"
og_image: "https://safeaiaus.org/assets/safeaiaus-logo-600px.png"
twitter_card: "summary_large_image"
twitter_title: "AGI Assurance"
twitter_description: "Evidence and testing for advanced AI preparedness."
tags:
  - Framework
  - Governance
  - Assurance
---

# AGI Assurance: Evidence for Advanced AI Preparedness

> **Purpose:** Demonstrate AGI preparedness through evidence, testing and accountability
> **Audience:** Risk leaders, boards, regulators and organisations deploying advanced AI | **Time:** 10-15 minutes

## Beyond compliance to capability

Standard AI assurance asks: *Are we following the rules?*

AGI assurance asks harder questions about your organisation:

- Can you actually shut down your most capable AI systems if they behave unexpectedly?
- Would you detect if an AI system was pursuing goals you didn't intend?
- Could your organisation function if AI-mediated services failed for a week?
- Who is accountable when AI systems make consequential decisions?

Advanced AI failures may not resemble traditional IT failures: systems can behave unexpectedly, optimise for unintended goals or reveal hidden dependencies during crises.

**This page extends [operational AI assurance](../../governance-templates/ai-assurance-transparency-auditing-reporting.md)** (system registers, safety notes, vendor transparency) to cover the additional evidence needed for advanced AI and AGI preparedness.

---

## The evaluation gap

Assurance depends on evaluation, but current methods have structural limits.

### Benchmarks are saturating

Frontier models are outpacing established evaluation suites. Near-perfect scores reduce a benchmark's usefulness and can create false confidence: high scores may mean the benchmark has been outgrown, not that a system is safe.

[METR's task-completion time-horizon research](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) found that the length of tasks frontier agents could complete with 50% reliability doubled roughly every seven months over the six years studied. This finding is specific to the tasks and evaluation method studied, but it shows why evaluation methods need regular review.

### System cards: useful but limited

Frontier labs publish system cards documenting capabilities, limitations and safety testing. These improve transparency but have assurance limitations:

1. **Self-assessment.** The lab that built the model also evaluates and documents it. Independent verification is not yet standard practice.
2. **Volume and accessibility.** Extensive documentation can make scrutiny difficult for resource-constrained regulators and deployers.
3. **Agentic capability gaps.** Current system cards rarely describe agentic capabilities — the ability to chain autonomous actions across systems — in enough detail for deployers to assess operational risk.

### The auditing ecosystem gap

The independent frontier-AI auditing ecosystem is still emerging. Australia's domestic capacity remains limited, so it can draw on international institutes, standards bodies and research organisations—including the UK AI Security Institute, NIST, Epoch and METR—while building local capability.

**What this means for assurance:** Do not treat results from labs, benchmarks or auditors as definitive evidence of safety. Triangulate independent evidence under realistic conditions and state what evaluations cannot establish.

---

## Assurance questions for each C·A·G·R pillar

For each pillar, we identify the core assurance question, what evidence demonstrates capability, how to test it, who owns it and review frequency.

### Containment: Can you control high-capability systems?

**Core question:** Can you demonstrate deployment controls for high-capability systems?

| Aspect | Details |
|--------|---------|
| **Evidence** | Licensing approvals, access logs, shutdown test records, capability evaluation reports |
| **Testing** | Red-team penetration tests, quarterly shutdown drills, access control audits |
| **Owner** | CISO |
| **Review** | Quarterly to board |

**Key test:** Can you shut down your most autonomous AI system within 4 hours? Have you tested this under realistic conditions (not just tabletop)?

### Alignment: Do systems behave as intended?

**Core question:** Can you show systems behave as intended under adversarial conditions?

| Aspect | Details |
|--------|---------|
| **Evidence** | Evaluation reports, adversarial test results, misalignment incident logs, behavioural monitoring dashboards |
| **Testing** | Pre-deployment safety testing, ongoing behavioural monitoring, red-teaming |
| **Owner** | CTO/AI Lead |
| **Review** | Pre-deployment + continuous |

**Key test:** Has the system been tested against realistic adversarial inputs? Do you have monitoring that would detect goal drift or unexpected optimisation?

### Governance: Does oversight actually function?

**Core question:** Can you show that oversight mechanisms work in practice, not just on paper?

| Aspect | Details |
|--------|---------|
| **Evidence** | Risk assessments, policy compliance audits, stakeholder consultation records, escalation logs |
| **Testing** | Third-party audits, regulatory reviews, escalation pathway tests |
| **Owner** | Chief Risk Officer |
| **Review** | Annual + major changes |

**Key test:** When was the last time someone escalated an AI concern? What happened? If the answer is "never," your oversight may exist on paper only.

### Resilience: Can you function without AI?

**Core question:** Can you maintain essential functions if AI systems fail?

| Aspect | Details |
|--------|---------|
| **Evidence** | Continuity plans, tested manual procedures, drill after-action reports, staff training records |
| **Testing** | Incident response exercises, service continuity tests under realistic conditions |
| **Owner** | COO/Emergency Management |
| **Review** | Bi-annual drills |

**Key test:** If your primary AI systems were unavailable for 72 hours, how long would it take to restore essential services using manual processes? Have you tested this?

---

## Dangerous capability evaluation

For systems at the frontier of capability, standard assurance is insufficient. Systems should be independently tested for:

- **Biological capabilities:** Can the system assist with pathogen design or synthesis?
- **Cyber capabilities:** Can it discover vulnerabilities or write exploit code?
- **Deception capabilities:** Can it manipulate users or conceal its reasoning?
- **Autonomous capabilities:** Can it pursue goals across extended time horizons?

**Who should evaluate:** Appropriately qualified external evaluators, working with the relevant regulator and drawing on Australia's [AI Safety Institute](https://www.industry.gov.au/science-technology-and-innovation/technology/artificial-intelligence/ai-safety-institute) where relevant. The institute provides technical analysis and regulator support; it is not the enforcement body for every sector.

<!-- TODO(human verification): Reconfirm the AI Safety Institute's technical-analysis and regulator-support functions against the linked Department of Industry, Science and Resources page before publication. Source checked 18 July 2026. -->

**When to re-evaluate:** At deployment, after significant capability upgrades and periodically as capabilities scale.

---

## Toward assurance standards: METR common elements

Frontier AI assurance remains immature, but common practices are emerging. [METR's analysis of frontier AI safety policies](https://metr.org/common-elements) (2025) identifies nine elements across most major lab commitments:

| Element | Assurance implication |
|---------|----------------------|
| **Capability thresholds** | Define what risk levels trigger enhanced oversight |
| **Model weight security** | Protect against unauthorised access or release |
| **Deployment mitigations** | Controls in place before and during deployment |
| **Halting conditions (deployment)** | Criteria for pulling deployed systems |
| **Halting conditions (development)** | Criteria for pausing training |
| **Full capability elicitation** | Testing designed to surface maximum capabilities, not just typical use |
| **Timing and frequency** | Regular evaluation cadence, not just pre-deployment |
| **Accountability** | Internal and external accountability mechanisms |
| **Policy updating** | Commitment to revise policies as evidence accumulates |

**For Australian organisations:** These nine elements provide a practical checklist for assurance conversations with AI vendors. Ask providers: which of these elements does your safety policy cover? Where is the evidence? Who verified it independently?

Over time, these common elements could inform mandatory assurance requirements. Any enforceable requirements would need to come through legislation, regulation or an authorised sectoral body; Australia's AI Safety Institute can contribute technical evidence and methods.

---

## Implementation pathway

**Start with operational assurance:** If you don't have a [system register, safety notes and vendor transparency](../../governance-templates/ai-assurance-transparency-auditing-reporting.md), start there. AGI assurance builds on these foundations.

**Layer on AGI-specific evidence:** As you deploy more capable systems, add:

1. Shutdown and access control testing (Containment)
2. Behavioural monitoring and adversarial testing (Alignment)
3. Escalation pathway verification (Governance)
4. Manual fallback drills under realistic conditions (Resilience)

**Scale with capability:** Low-autonomy systems need basic assurance. High-autonomy systems in critical contexts need all four pillars tested regularly.

---

## Where to next

- [C·A·G·R Framework Overview](index.md) — how the four pillars fit together
- [Operational AI Assurance](../../governance-templates/ai-assurance-transparency-auditing-reporting.md) — foundational assurance practices
- [Framework FAQ](faq.md) — common questions about applying C·A·G·R
- [AGI Scenarios](../scenarios/index.md) — test your assurance against concrete scenarios

---

??? note "Disclaimer & Licence"
    **Disclaimer:** This content provides guidance on AGI assurance practices. SafeAI-Aus has exercised care in preparation but does not guarantee accuracy. Organisations should adapt guidance to their specific context and risk profile.

    **Licence:** Licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to copy, adapt and redistribute with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*
