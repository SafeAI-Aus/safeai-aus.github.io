---
icon: lucide/folder-kanban
title: "AI Project Register Template"
description: "AI project register template for Australian businesses to track initiatives, governance responsibilities, risks and review status."
keywords: "AI project register template, AI project tracking, AI governance tracking, AI compliance register, AI project management, Australian AI safety, AI project oversight"
last-reviewed: "2026-04-15"
review-status: "pending"
review-cycle: "quarterly"
og_description: "Comprehensive AI project register template for Australian businesses"
og_type: "article"
howto:
  name: "How to Set Up and Maintain an AI Project Register"
  description: "Step-by-step guide to creating a central record of all AI initiatives for governance oversight"
  totalTime: "PT30M"
  steps:
    - name: "Assign register ownership"
      text: "Designate the PMO, ICT or risk/governance function as the owner responsible for maintaining the register."
    - name: "Create entries for each AI initiative"
      text: "At project initiation, record project information, ownership, governance details and technical specifications using the template fields."
    - name: "Complete risk and compliance assessment"
      text: "Record the guardrail assessment status, supporting evidence, assessor, assessment date, risk level and mitigation controls for each initiative."
    - name: "Track financial and lifecycle details"
      text: "Record budget, actual spend, ROI targets and key dates including pilot, production, review and sunset milestones."
    - name: "Review and update regularly"
      text: "Update the register at least quarterly, or more frequently for high-risk projects. Use it at go/no-go review points to assess compliance."
faq:
  - question: "How often should the AI project register be updated?"
    answer: "At minimum quarterly, or more frequently for high-risk or high-impact projects. Update entries whenever significant changes occur such as new risks, model version changes or governance decisions."
  - question: "Who should own the AI project register?"
    answer: "The register should be owned by the PMO, ICT or risk/governance function. It serves as a central source of truth for governance, risk and compliance monitoring across all AI initiatives."
  - question: "What is the minimum information needed for each entry?"
    answer: "At minimum, record the project name, description, project owner, risk level, guardrail assessment status, assessment record and key dates. The assessment record identifies the assessor, assessment date, framework version, scope and supporting evidence. Expand with financial, technical and ethics details as the project matures."
---

# AI Project Register

> **Purpose:** Central record of all AI initiatives within your organisation for governance oversight
> **Audience:** PMO, ICT, risk and governance teams | **Time:** 30 minutes setup, ongoing updates

This register helps you maintain a central record of all AI initiatives. It:

- Ensure visibility across all AI-related projects
- Provide a single source of truth for governance, risk and compliance monitoring
- Support decision-making through consistent project documentation and guardrail alignment

!!! info "When to Use"
    - 🎯 **At project initiation:** Create a new entry for each AI initiative
    - 🔄 **During project lifecycle:** Update details as the project evolves (e.g., risks, model versions)
    - ✅ **At review points:** Use the register to review go/no-go criteria, supporting assessments and unresolved guardrail gaps

    **Relevant Guardrails:** 1, 2, 9, 10 (from the Australian Voluntary AI Safety Standard)  

---

## AI Project Register Template (Template)

### Project Register Fields

| Section | Field | Description | Example Entry |
|---------|-------|-------------|---------------|
| **Project Information** | Project Name | Title of the AI initiative | Customer Insights Chatbot |
|  | Description | Short summary of the project’s purpose | Automating first-line customer queries using an LLM |
|  | Objectives | Key business goals or outcomes expected | Reduce response time by 40% |
|  | Timeline | Planned start/end dates, key milestones | Start: Aug 2025, Pilot: Nov 2025 |
| **Ownership & Governance** | Project Owner | Person accountable for delivery | Jane Smith, Head of CX |
|  | Stakeholders | Business units and key contacts | IT, Risk, Legal, Operations |
|  | Approval Status | Formal governance decision | Approved by ICT Steering Committee |
| **Risk Assessment** | Guardrail Compliance | Recorded assessment against identified VAISS (2024) controls: Yes/Partial/No/Not assessed; link the assessment record | Guardrails 1, 2, 9: Yes; 10: Not assessed (illustrative) |
|  | Assessment Record | Assessor, assessment date, framework version, assessed scope, evidence links and unresolved gaps | Assessment record [Document ID/Link], VAISS 2024, scope: chatbot pilot; stakeholder engagement pending |
|  | Risk Level | Overall risk rating (Low/Med/High) | Medium |
|  | Mitigations | Key risk controls applied | Human-in-the-loop escalation for safety checks |
| **Technical Details** | Data Sources | Internal/external data powering the model | CRM data, anonymised chat logs |
|  | Model Information | Model type, vendor, or custom build details | GPT-4o, fine-tuned |
|  | Infrastructure | Hosting, deployment environment | Azure Cloud, containerised |
| **Financial** | Budget Allocated | Total approved budget | $250,000 |
|  | Actual Spend | Current expenditure | $125,000 |
|  | ROI Target | Expected return | 40% efficiency gain |
| **Dependencies** | Related Projects | Other initiatives this depends on | Data Lake Project |
|  | System Integrations | Systems this connects with | CRM, ERP, Analytics |
| **Lifecycle** | Pilot Date | When pilot begins | 1 Nov 2025 |
|  | Production Date | Go-live target | 1 Feb 2026 |
|  | Review Date | Next formal review | 1 May 2026 |
|  | Sunset Date | Planned decommission | 1 Feb 2028 |
| **Ethics** | Ethics Review | Status of ethical assessment | Completed - Low Risk |
|  | Bias Testing | Results of bias evaluation | Passed all criteria |
| **Benefits** | Benefits Realised | Actual vs planned benefits | 35% efficiency (target 40%) |
| **Monitoring & Updates** | Version History | Track model releases or changes | v1.0 (Aug 2025), v1.1 (Oct 2025) |
|  | Performance Metrics | Agreed KPIs or benchmarks | Accuracy >85%, CSAT >90% |
|  | Change Log | Notes of updates, retraining, risks | Retrained with new dataset Sep 2025 |
| **Decision Framework** | Go/No-Go Criteria | Conditions for continuation | Meets KPIs, passes compliance review |
|  | Escalation Path | Who is notified if risks emerge | Escalate to CIO and AI Risk Committee |

Treat a status as the recorded outcome of an assessment, not independent proof of compliance. Do not mark a control “Yes” without evidence for its assessed scope. Record who reviewed it, when, and what remains unresolved. Example entries are illustrative and are not verified approvals.

---

## How to Maintain the Register  

- **Ownership:** The AI Project Register should be owned by the PMO, ICT, or Risk/Governance function.  
- **Frequency of Updates:** At minimum, quarterly updates, or more frequently for high-risk/high-impact projects.  
- **Integration:** Link the register with project governance forums, risk registers and compliance reporting.  
- **Audit & Oversight:** Use the register to locate current assessments and evidence for governance or compliance reviews. Reassess entries after material changes; the register alone does not establish compliance.  

---

## Status Tracking

**Overall Status:** [ ] On Track  [ ] At Risk  [ ] Delayed  [ ] On Hold  [ ] Cancelled

**Health Indicators:**

- Schedule: 🟢 Green / 🟡 Amber / 🔴 Red
- Budget: 🟢 Green / 🟡 Amber / 🔴 Red
- Risk: 🟢 Green / 🟡 Amber / 🔴 Red
- Compliance: 🟢 Green / 🟡 Amber / 🔴 Red  

---

## Document Links
- Risk Assessment: [Document ID/Link]  
- Vendor Evaluation: [Document ID/Link]  
- Incident Reports: [Document ID/Link]  
- Ethics Review: [Document ID/Link]  
- Business Case: [Document ID/Link]  
- Guardrail Assessment Record: [Document ID/Link]  
- Stakeholder Engagement and Actions: [Document ID/Link]  
- Testing, Limitations and Disclosure Records: [Document ID/Link]  

---

## Alignment with Australian Standards

<!-- TODO: Human-verify The proposed AI6/VAISS (2024) support mappings and the evidence recorded for each assessed control. -->

The register can organise evidence for selected practices in [AI6](https://www.ai.gov.au/staying-safe-and-responsible/essential-ai-practices/guidance-ai-adoption-implementation-guidance) and [VAISS (2024)](https://www.industry.gov.au/publications/voluntary-ai-safety-standard/10-guardrails). Keeping an entry does not demonstrate that a practice has been implemented.

!!! success "Framework Support"
    === "AI6 Essential Practices"
        ✓ **Decide who is accountable** — Ownership fields record responsibility; confirm the person has the authority and resources to act

        ✓ **Understand impacts and plan accordingly** — Risk fields point to assessments and mitigation decisions

        ✓ **Share essential information** — The register supports internal information sharing; link the records of any required supplier, user or stakeholder disclosures separately

    === "Voluntary AI Safety Standard (10 Guardrails)"
        ✓ **Guardrail 1 – Accountability and governance** — Ownership and approval fields record assigned responsibilities and decisions

        ✓ **Guardrail 10 – Stakeholder engagement and fairness** — Link evidence of engagement and resulting actions; ethics-review and bias-test statuses alone do not demonstrate engagement

        ✓ **Guardrail 9 – Records** — Entries and linked records document projects, assessments, changes and decisions

        ✓ **Guardrail 2 – Risk management** — Risk and mitigation fields link each initiative to its risk-management process

Guardrail labels above are shortened summaries, not a complete statement of the controls.

---

## Next Steps

**Where to go from here:**

- 📊 **Need a central log of project-specific risks?** → [AI Risk Register](ai-risk-register.md)
- 📋 **Need to establish AI governance policies?** → [AI Use Policy](ai-use-policy.md)

---

??? note "Disclaimer & Licence"
    **Disclaimer:** This template provides best practice guidance for Australian organisations. SafeAI-Aus has exercised care in preparation but does not guarantee accuracy, reliability, or completeness. Organisations should adapt to their specific context and may wish to seek advice from legal, governance, or compliance professionals before formal adoption.

    **Licence:** Licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to copy, adapt and redistribute with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*
