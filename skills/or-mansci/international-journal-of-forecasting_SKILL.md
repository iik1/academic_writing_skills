---
name: international-journal-forecasting-writing-style
description: >
  Journal-specific writing conventions for International Journal of Forecasting
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for International Journal of Forecasting",
  "submit to International Journal of Forecasting", "match International Journal of Forecasting style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: International Journal of Forecasting

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Elsevier (official publication of the International Institute of Forecasters)
- **Scope:** Empirical, applied, and methodological forecasting research spanning economic, financial, energy, supply-chain, and demographic forecasting; machine learning and statistical approaches to prediction; decision-making under forecast uncertainty. The journal bridges theory and real-world forecasting practice.
- **Guidelines URL:** https://www.sciencedirect.com/journal/international-journal-of-forecasting/publish/guide-for-authors
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 1 full-text (Damato, Azzimonti & Corani 2025, arXiv:2502.19086, published in IJF special issue "ML/AI-Driven Forecasting in the Supply Chain")

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Double-blind review requires the main manuscript to contain no author-identifying information; a separate title page carries author details. Beyond this, no prescribed section order is mandated — structure follows disciplinary and paper-type conventions. In practice (Article 1): Introduction → standalone Literature Review → Model/Methods → Experiments (with Discussion as a subsection) → Conclusions → CRediT statement → Competing Interest declaration → Acknowledgments → References → Appendices. [ENFORCED for anonymization; otherwise PRACTICE ONLY for section order]

### Length
No explicit word or page limits stated in guidelines.

### Abstract
Unstructured single paragraph. No stated word limit; approximately 130–160 words in practice. [ENFORCED unstructured format; word count PRACTICE ONLY]

### Citations
Elsevier author-year (Harvard) style. In-text: parenthetical "(Author, Year)" or narrative "Author (Year)". Reference list: "Surname, Initials, Year. Title. Journal Volume, pages–pages." Multiple citations within a single parenthetical are separated by semicolons. [ENFORCED]

### Headings
Numbered sections and decimal subsections (1, 2, 3, 3.1, 3.2, 3.2.1 …). [ENFORCED]

### Tables and Figures
Follows FIELD_SKILL norm. Color figure option available; authors must indicate if color is required in print.

### Explicit Prohibitions
- Manuscripts previously published or simultaneously under review elsewhere are prohibited.
- Author-identifying information must be absent from the main manuscript file.
- Generative AI tools may not be listed as authors; any use must be disclosed in a dedicated declaration placed before the References section.
- Language must be American or British English — not a mixture of the two.
- Inclusive language is required: avoid bias, stereotypes, or exclusionary framing.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the OR&MANSCI field baseline.

### Introduction Structure — Contributions and Roadmap
**Field norm (ABS 4*/4):** Contributions stated as an explicit enumerated list (bullet points or numbered claims), each asserting a specific, verifiable result; Introduction closes with a brief section roadmap.

**This journal (ABS 3):** In the article observed, contributions are woven into narrative introduction prose — the novel models are proposed and their advantages argued in running text, without a formal bulleted or numbered contributions list. No explicit section roadmap paragraph appears at the end of the Introduction; instead, individual sections are referenced inline (e.g., "as described in Sec. 3.2"). [RELAXATION — ABS 3 permitting a less formal contribution structure than ABS 4*/4 norm]

### Reproducibility and Code Availability
**Field norm:** Robustness evidence is expected; no specific code-sharing norm at field level.

**This journal:** IJF operates a named reproducibility program (CASCaD) that independently verifies the numerical results of accepted papers. Published articles carry a footnote confirming CASCaD verification and date. Authors are expected to make code and data publicly available (e.g., via GitHub); this is documented in a dedicated appendix or data availability statement. [PRACTICE ONLY for CASCaD footnote; GUIDELINE ONLY for data/code availability expectation]

### Replication Studies
**Field norm:** Not addressed at field level.

**This journal:** Explicitly encourages submission of replication studies of highly-cited work. Confirmations of prior results require minimal documentation (~1 page); non-replications require detailed explanation of divergent results. [GUIDELINE ONLY]

### Publisher-Mandated Structural Additions
The following sections are required by Elsevier and do not appear in FIELD_SKILL:
- **CRediT authorship contribution statement**: Each author's specific contributions listed by CRediT taxonomy role (e.g., Conceptualization, Methodology, Writing – original draft). Placed after the Conclusions. [ENFORCED]
- **Declaration of competing interest**: Mandatory declaration of financial or personal relationships that could have influenced the work. [ENFORCED]
- **Declaration of generative AI and AI-assisted technologies in the writing process**: Required when any AI tool was used; placed before References. [ENFORCED]

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Active voice: FIELD DEFAULT
- Register and formality: FIELD DEFAULT
- Abstract content: FIELD DEFAULT (problem, approach, main finding)
- Literature review placement: FIELD DEFAULT (standalone section immediately after Introduction is common)
- Discussion placement: FIELD DEFAULT (integrated as subsection within Results/Experiments, not standalone)
- Citation density by section: FIELD DEFAULT
- Statistical reporting: FIELD DEFAULT (tables as primary vehicle for quantitative comparisons; prose interprets key contrasts)
- Hedging patterns: FIELD DEFAULT
- Conclusion structure: FIELD DEFAULT (synthesises contributions, reconnects to gap, states limitations, identifies future directions)
- Appendix use: FIELD DEFAULT (technical derivations, robustness tables, code details moved to appendices)

---

## Common Pitfalls

1. **Forgetting the anonymization requirement.** IJF uses double-blind review. Any author name, institution, acknowledgment, or self-citation pattern left in the main manuscript file is a submission error. Remove all identifying information before uploading the main file.

2. **Omitting the CRediT statement.** Many OR&MANSCI authors are unfamiliar with the CRediT taxonomy. It is mandatory at Elsevier journals; omitting it typically triggers a revision request at the technical check stage.

3. **Omitting the GenAI declaration.** Even partial use of AI writing tools (e.g., grammar checking with an LLM) must be declared. Silence on this point when AI was used is a policy violation.

4. **Submitting without code or data.** The journal's CASCaD reproducibility program means numerical results will be independently verified. Papers without accessible code or data are at a disadvantage at both review and post-acceptance stages. Plan for public code/data release from the outset.

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://www.sciencedirect.com/journal/international-journal-of-forecasting/publish/guide-for-authors | Guidelines | Direct fetch (partial; full guidelines behind JS) |
| https://www.sciencedirect.com/journal/international-journal-of-forecasting | Journal homepage | Direct fetch |
| Damato, Azzimonti & Corani (2025), "Forecasting intermittent time series with Gaussian Processes and Tweedie likelihood", arXiv:2502.19086v5, published IJF | Full-text PDF | arXiv open access |
