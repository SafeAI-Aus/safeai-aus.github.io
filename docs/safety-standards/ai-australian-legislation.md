---
icon: lucide/flag
title: "Current Legal Landscape for AI in Australia"
description: "Overview of Australian laws relevant to AI adoption, including privacy, consumer protection, anti-discrimination and intellectual property."
keywords: "AI legislation Australia, Australian AI law, AI privacy law, AI consumer law, AI discrimination law, AI intellectual property, AI legal compliance, Australian AI regulations, AI legal framework"
last-reviewed: "2026-07-22"
review-cycle: "quarterly"
og_description: "Comprehensive overview of current legislation applicable to AI adoption in Australian business"
og_type: "article"
---

# Current Legal Landscape for AI in Australia

> **Purpose:** Navigate current Australian laws and regulations that apply to AI systems
> **Audience:** Legal, compliance, risk and governance teams | **Time:** 45-60 minutes

While Australia doesn't yet have AI-specific legislation, AI use is already governed by existing laws. Australian law is technology-neutral: obligations around privacy, consumer protection, discrimination, workplace safety and intellectual property apply regardless of whether a decision is made by a human or an AI system.

In 2024 the Government released proposals for mandatory guardrails for high-risk AI applications alongside a Voluntary AI Safety Standard. In October 2025 the National AI Centre (NAIC) published updated **Guidance for AI Adoption**, which sets out six essential practices (AI6) and is now the primary government guidance for responsible AI governance and adoption. In December 2025 the **National AI Plan** confirmed that, at that time, Australia would rely on **existing laws and sector regulators, supported by voluntary guidance and the Australian AI Safety Institute (AISI)**, rather than introducing a standalone AI Act or immediate mandatory guardrails. On **15 July 2026**, Prime Minister Albanese announced plans to legislate the **Australian Standards for AI** and established an **Office of AI** within the Department of the Prime Minister and Cabinet. Official material describes a proposed framework for large data centres and AI training, including mandatory requirements for large AI data centres. National Cabinet is expected to consider the approach in August 2026, with standards expected to be legislated in **early 2027**. The details are still to be designed and legislated. Existing technology-neutral laws continue to apply, while AI6 remains non-binding guidance. As of July 2026, the AISI is actively testing unreleased frontier AI models in collaboration with the Australian Signals Directorate and international partners — the most substantive operational milestone for the institute to date.

!!! warning "Proposed Australian Standards for AI announced 15 July 2026"
    The Government announced plans for a legislated national framework covering large data centres and AI training. The proposed standards would include mandatory energy and water requirements for large AI data centres. The announcement is not itself legislation and does not yet create general compliance duties for organisations using AI. A new **Office of AI** has been established within the Department of the Prime Minister and Cabinet to coordinate the design of the standards. See [Australian Government AI Policy and Frameworks](ai-government-policy-frameworks.md) for details. ([Prime Minister of Australia](https://www.pm.gov.au/media/ai-australias-interests); [PM&C Office of AI](https://www.pmc.gov.au/domestic-policy/office-ai), accessed 22 July 2026)

<!-- TODO: Human verification required before publication: confirm the proposed standards' scope and timetable against the latest PM&C and National Cabinet material. -->

!!! note "Policy is evolving"
    The Australian AI policy landscape is changing rapidly. The information below reflects the position as of July 2026. For government policy, guidance and institutional developments, see [Australian Government AI Policy and Frameworks](ai-government-policy-frameworks.md). Monitor [pm.gov.au](https://www.pm.gov.au) and [industry.gov.au/ai](https://www.industry.gov.au/science-technology-and-innovation/technology/artificial-intelligence) for updates.

!!! info "Why This Matters"
    Understanding the current legal landscape helps organisations:

    - 🛡️ **Avoid legal and reputational risks** from misuse of AI
    - ✅ **Demonstrate compliance and accountability** to regulators and customers
    - 🤝 **Build trust** by applying the same standards to AI as to human decision-making
    - 🔮 **Prepare for upcoming reforms** and regulatory guidance in Australia
    - 📊 **Align with AI6 and VAISS** to demonstrate best practice and readiness for any future mandatory requirements

---

## Key Laws That Apply Today

### Privacy Act 1988 & Australian Privacy Principles (APPs)

The **Privacy Act 1988** is the principal legislation that regulates how personal information is collected, stored, used and disclosed in Australia, including by government and private sector organisations ([ag.gov.au](https://www.ag.gov.au/rights-and-protections/privacy)). It establishes the **Australian Privacy Principles (APPs)**, which apply to most organisations and agencies.

**Relevance to AI:**

- Customers must be informed when AI systems process personal information
- AI-derived insights about individuals are considered personal information
- Consent may be required for analysing personal data by AI
- AI training datasets must comply with the APPs

!!! warning "Actions Required"
    - ✅ Update privacy policies to mention AI use
    - ✅ Display "We use AI" notices where relevant
    - ✅ Ensure AI vendors are APP-compliant
    - ✅ Implement data minimisation practices

**Automated decision-making transparency (effective 10 December 2026):** The Privacy and Other Legislation Amendment Act 2024 introduces new APP 1.7, 1.8 and 1.9 obligations. From 10 December 2026, APP entities must disclose in their privacy policies:

- The types of personal information used in substantially automated decisions
- The nature of decisions made solely or significantly by computer programs
- Where those decisions could reasonably be expected to significantly affect individual rights or interests

The OAIC issued an issues paper on "Guidance for Transparency in Automated Decision Making" (published 18 May 2026; consultation closed 15 June 2026) to inform its formal guidance on these obligations. Formal OAIC guidance is expected by September 2026 ([oaic.gov.au](https://www.oaic.gov.au/engage-with-us/consultations/consultation-on-guidance-for-transparency-in-automated-decision-making), accessed 14 June 2026). Organisations using AI in automated decision-making should begin privacy policy reviews now in preparation for the December 2026 commencement.

**Children's Online Privacy Code (registration targeted for 10 December 2026):** The OAIC released an exposure draft of the **Children's Online Privacy Code** for public consultation on 31 March 2026, with submissions closing 5 June 2026. The OAIC is working towards registering the Code by **10 December 2026**, coinciding with the APP ADM transparency obligations above. It applies to online services (including apps, games, educational tools and websites) that expose children and young people to the highest privacy risks, or are primarily concerned with children's activities. Key obligations include:

- Considering children's best interests in service design
- Obtaining consent before using children's personal information for targeted advertising
- Enabling children to request deletion of their personal information
- Notifying children when their geolocation is being tracked by other users (including parents)

A breach of the Code constitutes a breach of the Privacy Act and may attract significant civil penalties. The Code complements the Social Media Minimum Age obligation (effective December 2025). Organisations developing or operating AI-enabled consumer-facing services used by children (including EdTech platforms, games and recommendation systems) should review compliance obligations now. ([oaic.gov.au](https://www.oaic.gov.au/news/media-centre/oaic-releases-exposure-draft-of-the-childrens-online-privacy-code), accessed 31 May 2026)

**Penalties:** Since 2022 reforms, serious or repeated breaches can attract penalties of up to the greater of $50 million, three times the benefit obtained, or 30% of adjusted turnover ([oaic.gov.au](https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act)).

---

### Australian Consumer Law (ACL)

The **Australian Consumer Law (ACL)** is a national law embedded in the Competition and Consumer Act 2010. It protects consumers from unfair trading, misleading conduct and unsafe products or services across all states and territories ([consumer.gov.au](https://consumer.gov.au/about/australian-consumer-law)).

**Relevance to AI:**

- AI-generated content and claims must not be inaccurate or misleading
- Chatbots must clearly communicate their nature and authority
- AI-driven pricing must avoid deception
- Recommendations should be based on reasonable grounds

!!! warning "Actions Required"
    - ✅ Review all AI-generated marketing and promotional content
    - ✅ Implement disclaimers where chatbot responses could mislead
    - ✅ Monitor AI output quality and accuracy
    - ✅ Keep records of AI decision logic for accountability

**Regulatory context:** The ACCC is actively monitoring emerging AI-enabled practices, including reviews, claims and pricing models. In February 2026 the ACCC published its own AI transparency statement disclosing how it uses AI internally, and has flagged **"AI-washing"** (misleading claims about AI capabilities) as an enforcement concern. The Treasury's review of AI and the Australian Consumer Law found the existing framework "fit for purpose", making dedicated AI consumer legislation unlikely in the near term.

**Competition and Consumer Amendment (Unfair Trading Practices) Act 2026 (Act No. 64 of 2026; commences 1 July 2027):** The **Competition and Consumer Amendment (Unfair Trading Practices) Act 2026** passed both Houses of Parliament on **2 July 2026**, received Royal Assent on **6 July 2026**, and commences on **1 July 2027**. The Act amends the Australian Consumer Law to insert a general, principles-based prohibition on unfair trading conduct. The statutory test requires that conduct **manipulates a consumer or unreasonably distorts the consumer's decision-making environment**, and **causes or is likely to cause detriment** to the consumer. It also strengthens protections against subscription traps and drip pricing. The prohibition is technology-neutral: it may capture AI-enabled dark patterns or algorithmic manipulation where the statutory test is met, but does not expressly name those technologies. From 1 July 2027, the ACCC will have a direct enforcement pathway for unfair practices in addition to existing misleading-conduct provisions. The applicable maximum corporate penalty is the greater of **AUD $100 million**, three times the value of the benefit obtained, or 30% of adjusted turnover during the breach turnover period ([Federal Register of Legislation](https://www.legislation.gov.au/C2026A00064/latest/text); [Parliament of Australia bill history](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/Bills_Search_Results/Result?bId=r7468); [Parliamentary Library Bills Digest](https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd2526/26bd058); [Assistant Minister for Productivity, Competition, Charities and Treasury media release](https://ministers.treasury.gov.au/ministers/andrew-leigh-2025/media-releases/unfair-trading-tricks-and-traps-be-banned), accessed 6 July 2026).

---

### Anti-Discrimination Laws

Australia maintains a federal anti‑discrimination framework, including acts like the **Sex Discrimination Act 1984**, **Racial Discrimination Act 1975**, and **Disability Discrimination Act 1992**. These laws prohibit unfair treatment across public life based on protected characteristics ([ag.gov.au](https://www.ag.gov.au/rights-and-protections/human-rights-and-anti-discrimination/australias-anti-discrimination-law)).

**Relevance to AI:**

- AI must not discriminate against protected groups (e.g., based on gender, race, age, disability)
- Recruitment or HR AI tools must mitigate bias
- Services powered by AI must treat all users equitably
- Credit and insurance AI must comply with anti-discrimination obligations

!!! warning "Actions Required"
    - ✅ Regularly audit AI systems for bias and discriminatory outcomes
    - ✅ Document actions taken to support fairness
    - ✅ Maintain human oversight for high-impact AI decisions
    - ✅ Be prepared to explain or justify AI outputs

**High-risk domains:** Recruitment, lending, insurance, healthcare

---

### Intellectual Property (IP) Laws

Australia's **IP laws**—covering copyright, patents, trademarks and design rights—aim to protect creators and innovators while balancing access to creative content and knowledge ([ipaustralia.gov.au](https://www.ipaustralia.gov.au/about-us/ip-legislation-in-australia)).

**Relevance to AI:**

- Training AI models on copyrighted data may pose legal risk
- AI-generated outputs might not qualify for copyright protection
- Using client data without permission could breach confidentiality or IP rights
- Using competitors' content for training may contravene IP laws

!!! warning "Actions Required"
    - ✅ Audit datasets for copyright compliance
    - ✅ Include AI use and ownership clauses in contracts
    - ✅ Avoid relying solely on AI-generated content for IP claims
    - ✅ Respect third-party IP and licensing terms

**Copyright reform (Copyright Amendment (Orphan Works and Other Measures) Act 2026, passed 1 April 2026):** Parliament passed the **Copyright Amendment (Orphan Works and Other Measures) Act 2026** on 1 April 2026, establishing Australia's first orphan works scheme — providing legal certainty for use of works where the copyright holder is unknown or unlocatable, with libraries, museums and educational institutions among the primary beneficiaries. Importantly for AI, the Government **rejected a text-and-data-mining (TDM) exemption** for AI training — a proposal supported by technology firms — and is instead exploring a paid licensing model. The **Copyright and AI Reference Group (CAIRG)**, established within the Attorney-General's Department, is engaging stakeholders on fair and legal use of copyrighted material in AI training, copyright law's applicability to AI-generated outputs, and enforcement mechanisms including a potential small claims forum. Organisations training AI models on copyrighted content in Australia must continue to rely on existing copyright exceptions or obtain licences from rights holders ([ministers.ag.gov.au](https://ministers.ag.gov.au/media-centre/important-reforms-australias-copyright-framework-pass-parliament-01-04-2026)). Separately, the 15 July 2026 Australian Standards announcement states that Australian writers, artists and journalists should retain ownership and that companies should not use Australian creative works to train AI without the artist's control. It does not specify the legislative mechanism for that protection. ([Prime Minister of Australia](https://www.pm.gov.au/media/ai-australias-interests), accessed 22 July 2026)

---

## Sectoral Regulators to Watch

!!! tip "Key Regulators"
    - 🏦 **ASIC (Financial Services):** AI use in lending, trading and advice must align with responsible lending and market integrity obligations
    - 🏛️ **APRA (Prudential):** AI in risk management and critical infrastructure oversight may attract additional standards
    - 🏥 **TGA (Healthcare):** AI medical devices must comply with therapeutic goods regulation. Two January 2026 reports confirm the existing technology-agnostic framework is fit for purpose; no new mandatory AI requirements introduced ([TGA outcomes report](https://www.tga.gov.au/news/news-articles/tga-ai-review-outcomes-report-published); Department of Health *Safe and Responsible AI in Health Care* final report, January 2026)
    - 👥 **Fair Work Commission (Employment):** Algorithmic decision-making in recruitment and HR must comply with employment and discrimination laws
    - 🦺 **SafeWork NSW (Workplace AI in NSW):** The NSW **Work Health and Safety Amendment (Digital Work Systems) Act 2026** (passed 12 February 2026) imposes specific WHS duties on PCBUs using AI, algorithms, automation or online platforms to allocate work. Commencement is by proclamation. See [NSW section in state/territory resources](/business-resources/state-territory-ai-resources/#new-south-wales-nsw) for full provisions. Other states may follow.

---

## Upcoming Legislative Reforms

- 🏛️ **Australian Standards for AI — planned legislation in early 2027**
  Prime Minister Albanese announced on 15 July 2026 that the Government plans to legislate an Australian Standards for AI framework. Official material describes a regulatory framework for large data centres and AI training, with mandatory requirements proposed for large AI data centres covering new power supply, connection costs, grid support and water efficiency. The **Office of AI** has been established within the Department of the Prime Minister and Cabinet to coordinate design of the standards across government. National Cabinet is expected to consider the approach in **August 2026**, with standards expected to be legislated in **early 2027**. The final scope, duties and commencement arrangements remain subject to design, intergovernmental consideration and Parliament. ([Prime Minister of Australia](https://www.pm.gov.au/media/ai-australias-interests); [PM&C Office of AI](https://www.pmc.gov.au/domestic-policy/office-ai), accessed 22 July 2026)

- 🏛️ **DTA mandatory AI requirements — first requirement in effect 15 June 2026; CAIO appointments due July 2026**
  The first mandatory obligation under the DTA's Policy for the Responsible Use of AI in Government (Version 2.0) came into effect on 15 June 2026: all non-corporate Commonwealth entities must maintain an internal register of in-scope AI use cases with an accountable owner for each. All 94 mandatory agencies published public AI transparency statements ahead of this date — 15 June 2026 marks the first concrete enforcement date in the DTA's AI policy framework. Mandatory foundational AI training for all APS staff also becomes a policy requirement from this date. The Department of Finance said agencies had until **July 2026** to appoint a Chief AI Officer; its announcement does not report completion across entities ([Department of Finance](https://www.finance.gov.au/about-us/news/2025/establishing-chief-ai-officers-aps)). Remaining DTA obligations commence December 2026: completing an AI Impact Assessment prior to deployment; implementing processes to assess, approve and oversee AI use cases; and reporting on AI incidents.

- 🔒 **Privacy Act — automated decision-making transparency (10 December 2026)**
  New APP 1.7–1.9 obligations require disclosure when computer programs use personal information to make decisions significantly affecting individuals. See the Privacy Act section above for details. The OAIC consultation on transparency guidance closed 15 June 2026; formal guidance is expected by September 2026.

- 📝 **Copyright reform — TDM exemption rejected (April 2026)**
  Parliament rejected a text-and-data-mining exemption for AI training and is exploring a paid licensing model instead. The 15 July standards announcement separately committed to strong protection for Australian creators, but did not specify a TDM mechanism. See the IP section above for details. Further consultations on AI's impact on the creative sector are expected through the next National Cultural Policy process.

- ⚖️ **Consumer law — Competition and Consumer Amendment (Unfair Trading Practices) Act 2026 (assented 6 July 2026; commences 1 July 2027)**
  The Act received Royal Assent on 6 July 2026. Its technology-neutral prohibition may capture AI-enabled dark patterns and algorithmic manipulation where the statutory test is met. See the Australian Consumer Law section above for details. The Treasury review also found the existing ACL "fit for purpose" for AI; no broader dedicated AI consumer legislation is expected in the near term.

!!! info "Government Policy and Guidance"
    For coverage of the National AI Plan, AI Safety Institute, DTA mandatory requirements, Senate Committee response and other government policy developments, see [Australian Government AI Policy and Frameworks](ai-government-policy-frameworks.md).

---

## Summary Table

| Law / Regulator                 | AI Relevance                                                                 | Actions Required                                                                 |
|---------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Privacy Act 1988 (APPs)**     | Personal data, AI insights, consent, training data                           | Update policies, notices, vendor compliance, minimise data collection            |
| **Australian Consumer Law**     | Accuracy of AI outputs, chatbots, pricing, recommendations                    | Review marketing content, add disclaimers, monitor outputs, log decision logic   |
| **Anti-Discrimination Laws**    | Bias in recruitment, lending, healthcare, insurance                          | Test for bias, document fairness, human oversight, explainability                |
| **Intellectual Property (IP)**  | Copyright in training data, AI-generated content, confidentiality             | Audit sources, AI contract clauses, respect third-party IP rights                |
| **ASIC**                        | AI in lending, trading, financial advice                                     | Ensure compliance with responsible lending & market integrity obligations        |
| **APRA**                        | AI in risk management and critical infrastructure                            | Meet prudential standards for AI oversight                                       |
| **TGA**                         | AI in medical devices                                                        | Register & test AI systems, comply with TGA rules                                |
| **Fair Work Commission**        | Algorithmic HR and recruitment                                               | Ensure compliance with employment and anti-discrimination laws                   |
| **Guidance for AI Adoption (AI6)** | 6 essential practices for responsible AI governance and adoption; integrates the earlier Voluntary AI Safety Standard (10 guardrails) | Use AI6 as the primary reference for AI governance; map existing policies and risk registers to the 6 practices; use the guardrails as detailed controls where needed |
| **Australian Standards for AI (planned for early 2027)** | Proposed framework for large data centres and AI training; future mandatory requirements for large AI data centres; Office of AI established in PM&C | Monitor official design and consultation material; continue meeting existing laws and use AI6 as non-binding guidance |

---

!!! success "Key Takeaways"
    Even before new AI laws are introduced, **existing legislation creates clear compliance obligations**. Businesses deploying AI should:

    - ⚖️ **Treat AI as subject to the same laws** as human decision-making
    - 📝 **Document AI-related policies and processes**
    - 👨‍⚖️ **Engage legal review** for higher-risk applications
    - 📊 **Consider implementing AI6 and VAISS** to align with emerging best practice and demonstrate responsible AI governance even in the absence of a dedicated AI Act

---

### Key References

- [OAIC – Privacy Act & AI Guidance](https://www.oaic.gov.au)
- [ACCC – AI and Consumer Law](https://www.accc.gov.au)
- [Australian Human Rights Commission – Anti-Discrimination Guidance](https://humanrights.gov.au)
- [IP Australia – Intellectual Property and AI](https://www.ipaustralia.gov.au)
- [Australian Government – Privacy Act Reforms 2024](https://www.ag.gov.au)
- Voluntary AI Safety Standard (September 2024): [Department of Industry, Science and Resources](https://www.industry.gov.au/publications/voluntary-ai-safety-standard)
- Proposals Paper: Safe and Responsible AI - Mandatory Guardrails (September 2024): [Department of Industry, Science and Resources](https://consult.industry.gov.au/ai-mandatory-guardrails)

---

??? note "Disclaimer & Licence"
    **Disclaimer:** This guide provides general information about Australian legislation and is not legal advice. SafeAI-Aus has exercised care in preparation but does not guarantee accuracy, reliability, or completeness. Organisations should adapt to their specific context and seek advice from legal professionals before making decisions based on this information.

    **Licence:** Licensed under [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to copy, adapt and redistribute with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*
