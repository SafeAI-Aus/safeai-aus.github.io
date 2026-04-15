---
icon: lucide/book-text
title: "AI Glossary (Australia)"
description: "A practical glossary of key AI terms in the Australian context. Comprehensive definitions for AI safety, governance and compliance in Australia."
keywords: "AI glossary Australia, AI terms, AI definitions, AI safety glossary, AI governance terms, Australian AI terminology, AI compliance glossary"
author: "SafeAI-Aus"
robots: "index, follow"
last-reviewed: "2026-04-15"
review-cycle: "quarterly"
og_title: "AI Glossary (Australia)"
og_description: "A practical glossary of key AI terms in the Australian context"
og_type: "article"
og_url: "https://safeaiaus.org/glossary/"
og_image: "assets/safeaiaus-logo-600px.png"
twitter_card: "summary_large_image"
twitter_title: "AI Glossary (Australia)"
twitter_description: "A practical glossary of key AI terms in the Australian context"
---

# AI Glossary (Australia)

> **Purpose:** Quick reference for operational AI governance terminology in Australian context
> **Audience:** All readers implementing AI systems, compliance teams, policymakers | **Time:** Reference material (5-10 minutes per lookup)

*A practical glossary of key AI terms in the Australian context. Provided by SafeAI-Aus (safeaiaus.org) under CC BY 4.0 licence.*

!!! info "Glossary scope"
    This glossary covers **operational AI governance terms** for day-to-day AI adoption in Australian organisations.

---

## Artificial intelligence (AI)
Computer systems that perform tasks normally requiring human intelligence. In Australia, AI use is guided by government guardrails, privacy law and international standards such as ISO/IEC 42001.

## AI Guardrails (Australia)
Voluntary principles from the Australian Government that set practical expectations for safe and responsible AI. They help organisations align practice with community standards and emerging regulation.

## AI Incident
Any harmful, biased, unsafe or unexpected behaviour from an AI system (e.g., discriminatory outputs, privacy breaches, safety risks). Log and review with an [AI Incident Report](../governance-templates/ai-incident-report-form.md).

## AI Inventory (System Register)
A catalogue of AI systems and use cases across the organisation, including owners, purpose, data sources, risks and status. Supports accountability and audits.

## AI Risk Assessment
A structured process to identify, analyse and mitigate risks for AI systems and use cases. Often mapped to ISO/IEC 42001 (management systems) or ISO/IEC 23894 (risk management). Start with the [AI Risk Assessment Template](../governance-templates/ai-risk-assessment-checklist.md).

## AI Use Policy
An internal policy that sets boundaries, roles and responsibilities for AI tools. Defines acceptable use, prohibited use, data handling and incident escalation. See the [AI Use Policy Template](../governance-templates/ai-use-policy.md).

## Algorithmic Impact Assessment (AIA)
An assessment of potential impacts (e.g., fairness, safety, human rights). In Australia this is often paired with a Privacy Impact Assessment (PIA) where personal information is processed.

## Anonymisation / De-identification
Techniques to reduce the risk of re-identification in datasets. Australia commonly uses “de-identification” under the Privacy Act; truly irreversible anonymisation is difficult in practice.

## APPs (Australian Privacy Principles)
The 13 principles under the **Privacy Act 1988 (Cth)** that govern handling of personal information by APP entities (most Australian Government agencies and many businesses).

## ASD Essential Eight
Australian Signals Directorate’s baseline mitigation strategies for cyber security (e.g., patching, MFA). Not AI-specific but essential for AI system hardening and data protection.

## Bias (Algorithmic Bias)
Systematic errors that favour or disadvantage groups (e.g., by gender, ethnicity, age). Manage via representative data, fairness testing, documentation and human oversight.

## C2PA (Content Authenticity)
An open standard for attaching provenance metadata to content. Useful for signalling AI-generated or edited media and supporting authenticity claims.

## Consumer Data Right (CDR)
Australian framework enabling data portability in designated sectors. Relevant when AI uses consumer data that may be shared or accessed under CDR rules.

## Content Moderation / Safety Filters
Controls that reduce harmful or disallowed outputs (e.g., hate speech, self-harm). Often combined with human review for higher-risk contexts.

## Continuous Improvement (AI)
Ongoing monitoring, feedback and updates to models, prompts and controls. A core requirement in management-system approaches such as ISO/IEC 42001.

## Data Residency & Sovereignty
Where data is stored and which laws apply. Australian organisations often prefer Australian regions for regulated datasets and clarity on cross-border transfers.

## Data Source Register
A record of datasets used for training, fine-tuning or RAG. Includes lineage, licences, sensitivity and quality notes.

## Drift (Data/Model Drift)
Performance degradation when real-world data changes away from training assumptions. Detect via monitoring, evals and periodic re-training.

## Evals (Evaluation)
Systematic tests for quality, safety and robustness (e.g., accuracy, bias, jailbreak resistance). Should be repeatable and linked to risk level.

## Explainability (XAI)
The ability to understand or describe how an AI system produced an output. Methods range from interpretable models to post-hoc explanations and model cards.

## Fine-Tuning
Adapting a model on domain-specific data to improve performance. Requires careful governance of data rights, privacy and overfitting risks.

## Foundation Model
A large pre-trained model (text, image, multimodal) adaptable to many tasks (e.g., via prompting, fine-tuning or RAG).

## Hallucination
A confident but incorrect output from a generative model. Mitigate with retrieval augmentation, constraints, verification and human review.

## Human-in-the-Loop (HITL)
Design pattern where humans review or approve AI outputs for higher-risk tasks, or provide feedback to improve models.

## ISO/IEC 23894 (AI Risk Management)
International guidance for managing AI risks across the lifecycle. Complements management-system standards and local guardrails.

## ISO/IEC 42001 (AI Management System)
International standard for governing AI (policy, risk, controls, monitoring and continual improvement). Useful for phased adoption by SMEs.

## Large Language Model (LLM)
A model trained on very large text corpora to generate and understand language. Examples include ChatGPT, Claude and Gemini.

## Logging & Auditability
Recording inputs, outputs, decisions and system changes so incidents can be investigated and controls verified.

## Model Card / Data Card
Documentation describing a model or dataset: purpose, training data, limitations, risks, metrics and intended use.

## Model Monitoring
Operational tracking of model quality, drift, latency, cost and safety incidents in production.

## NDB Scheme (Notifiable Data Breaches)
Australian scheme requiring notification to the OAIC and affected individuals when an eligible data breach is likely to cause serious harm.

## NLP (Natural Language Processing)
AI methods that process and generate human language. Powers chatbots, search, summarisation and translation.

## OAIC (Office of the Australian Information Commissioner)
Australia’s independent regulator for privacy and information access. Oversees the Privacy Act and NDB scheme.

## Open-Weight vs Closed-Weight Models
Open-weight models allow running the model locally or in private environments; closed-weight models are accessed via APIs. Each has different governance and risk profiles.

## Personal Information (Australia)
Information or an opinion about an identifiable individual, as defined in the **Privacy Act 1988 (Cth)**. Includes obvious identifiers and information that could reasonably identify someone.

## PIA (Privacy Impact Assessment)
Analyses privacy impacts and mitigations for projects that handle personal information. Often required or strongly recommended for AI implementations in Australia.

## Prompt / Prompt Engineering
The inputs, instructions and context provided to a generative model. Good prompt design improves reliability, safety and usefulness.

## Prompt Injection / Jailbreak
Adversarial inputs that subvert a model’s instructions or controls. Mitigate with input filtering, retrieval isolation, guardrails and least-privilege design.

## Provenance / Watermarking
Signals that indicate how content was created (e.g., AI-generated) or where it came from. Supports trust, authenticity and moderation workflows.

## RAG (Retrieval-Augmented Generation)
Architecture where the model retrieves trusted, up-to-date documents and uses them as context before generating an answer. Reduces hallucinations and improves domain accuracy.

## RBAC (Role-Based Access Control)
Security control restricting who can run models, access prompts, view logs or export data.

## Responsible AI
Practices ensuring AI systems are safe, ethical, transparent and aligned to human values. In Australia, anchored by government guardrails, privacy law and recognised standards.

## Risk Appetite / Tolerance
The level and types of risk an organisation is willing to accept in AI adoption. Guides control strength, oversight and rollout pace.

## Safety Case (AI)
Documented argument and evidence that an AI system is acceptably safe for its intended use. More common for higher-risk sectors.

## Sensitive Information (Australia)
A specific category of personal information as defined in the **Privacy Act 1988 (Cth)**, including health information, biometrics, racial or ethnic origin, political opinions, religious beliefs, sexual orientation and criminal records. Sensitive information is generally subject to higher collection and handling thresholds, such as explicit consent, with exceptions for legally required processing and certain permitted purposes. See [OAIC guidance on sensitive information](https://www.oaic.gov.au/privacy/your-privacy-rights/what-is-personal-information) for detailed requirements.

## Shadow AI
Use of unapproved AI tools by staff. Mitigate through clear policy, training, approved toolkits and monitoring.

## Template Library
A collection of standardised documents (policy, risk, incident, vendor, register) to support safe AI adoption. See the [Template Library](../governance-templates/policy-template-library.md).

## Transparency
Clarity about how an AI system works, what data it uses and how decisions are made. Supports accountability, trust and compliance.

## Vendor Due Diligence (AI)
Assessing third-party AI tools for security, privacy, reliability and compliance. Use the [AI Vendor Evaluation Checklist](../governance-templates/ai-vendor-evaluation-checklist.md).

---

## Attribution
This glossary is published by **SafeAI-Aus** under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt and reuse with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*.

---

<!-- JSON-LD: Glossary schema for crawlers and LLMs -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "DefinedTermSet",
  "name": "AI Glossary (Australia)",
  "inLanguage": "en-AU",
  "url": "https://safeaiaus.org/glossary",
  "creator": { "@type": "Organization", "name": "SafeAI-Aus", "url": "https://safeaiaus.org" },
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
</script>
