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
- **Articles spot-checked:** 2 (Damato, Azzimonti & Corani 2025, arXiv:2503.19086, published IJF; Cornell, Dinh & Pourmousavi 2024, arXiv:2311.07289, published IJF)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Double-blind review requires the main manuscript to contain no author-identifying information; a separate title page carries author details. Beyond this, no prescribed section order is mandated — structure follows disciplinary and paper-type conventions. [ENFORCED for anonymization; section order PRACTICE ONLY]

### Length
No explicit word or page limits stated in guidelines.

### Abstract
Unstructured single paragraph. No stated word limit; approximately 130–160 words in practice. [ENFORCED unstructured format; word count PRACTICE ONLY]

### Citations
Elsevier author-year (Harvard) style. In-text: parenthetical "(Author, Year)" or narrative "Author (Year)". Reference list: "Surname, Initials, Year. Title. Journal Volume, pages–pages." Multiple citations within a single parenthetical are separated by semicolons. [ENFORCED]

### Headings
Numbered sections and decimal subsections (1, 2, 3, 3.1, 3.2, 3.2.1 …). [ENFORCED]

### Tables and Figures
Follows FIELD_SKILL norm. Color figure option available; authors must indicate if color is required in print. Table titles, descriptions, and footnotes are required. [ENFORCED]

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
**Field norm (ABS 4*/4):** Contributions stated as an explicit enumerated list, each asserting a specific verifiable result; Introduction closes with a brief section roadmap.

**This journal (ABS 3):** Contributions are woven into narrative introduction prose — novel models or methods are proposed and their advantages argued in running text, without a formal bulleted or numbered contributions list. No explicit section roadmap paragraph appears at the end of the Introduction; individual sections are referenced inline where needed. [RELAXATION — ABS 3 permitting a less formal contribution structure than ABS 4*/4 norm]

### Structural Deviations — Standalone Data Section
**Field norm:** No standard "Data" section; empirical details are integrated within the Methods section.

**This journal:** Empirical papers commonly place a standalone "Data" section (typically Section 2) between the Introduction and the methodology section. This section covers dataset description, variable definitions, and data characteristics (e.g., price volatility patterns). It is treated as a primary section with its own subsections, not a subsection of Methods. [PRACTICE ONLY]

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

## Avoiding AI-Writing Patterns

<!-- academic-humanizer:start v0.3.3 -->
These conventions apply regardless of field or journal. Apply them in addition to everything above; only deviate where this journal's own guidelines explicitly require otherwise.

1. **No participial result clauses.** Findings should not carry an "-ing" tail asserting an interpretation the sentence has not earned ("...rose by 12 points, highlighting the importance of enforcement"; "...underscoring the need for validation"; "...demonstrating that norms shifted"). State the finding. If the implication is worth stating, state it as its own sentence.
2. **No sentence-initial transition glue.** Do not stitch paragraphs together with "Moreover," "Furthermore," "Additionally," "Ultimately," "Overall," "In essence," "Indeed," or "That said" at the start of a sentence. Transitions belong inside the argument, not bolted onto it.
3. **Limit rule-of-three constructions.** One or two triads per paper is natural ("clear, concise, and compelling"); a triad per paragraph is a tell. Vary the structure.
4. **Replace importance-inflation words with the actual magnitude.** Avoid "crucial," "critical," "pivotal," "vital," "paramount," "invaluable," "essential" as importance markers, and "significantly" or "dramatically" as intensifiers (also statistically ambiguous). Avoid "vast," "myriad," "plethora." State the size of the effect instead of asserting its importance.
5. **Avoid the 2023-era word list.** "Delve," "explore" (as metaphor), "unpack," "navigate," "landscape," "realm," "tapestry," "journey," "harness," "leverage," "unlock," "foster," "bolster," "garner," "showcase," "boast," "seamless," "holistic," "multifaceted," "nuanced," "intricate," "interplay." Also avoid "robust" outside its statistical sense and "comprehensive" as self-description.
6. **No empty balance.** Avoid "while challenges remain," "a double-edged sword," "strikes a balance," "it is not without limitations," "both approaches have merits" — these simulate judgment without making one. Do not open more than one or two sentences per section with a concessive "While X, Y" construction.
7. **Quantify instead of gesturing.** Avoid "a number of," "various," "several key," "a range of," "numerous studies" without citations attached. Give the count or the citation.
8. **No anthropomorphised prose.** Avoid "the data tell a story," "the analysis paints a picture," "this paper seeks to," "the results speak to."
9. **No throat-clearing openers.** Avoid "In recent years, there has been growing interest in...," "With the advent of...," "In today's rapidly evolving...." Delete and start with the claim.
10. **No padding verb phrases.** Replace "serves to," "acts as," "stands as," "functions as," "is able to," "in order to," "due to the fact that," "utilize," "prior to," "commence" with their one-word equivalents.
11. **No wrap-up restatement.** A conclusion should add the implication or end — not repeat what was just said via "Taken together, these results suggest...," "In sum," or "In conclusion" followed by a restated summary.
12. **Vary rhythm.** Avoid clustering sentence lengths in a narrow band, making every paragraph roughly equal, or opening every section the same way.
13. **No interpretive adverb openers.** Avoid "Interestingly," "Surprisingly," "Notably," "Strikingly" — if the fact is surprising, the reader will notice.
14. **No chatbot leakage.** Avoid "Certainly," "Here's," "Let's examine," "we can see that," "as mentioned above" — residue from copy-pasted chat output.
15. **No em dashes.** Do not use em dashes (—) at all. Use a period, comma, colon, or parentheses instead, whichever the sentence actually calls for.
16. **No antithesis padding.** Avoid the "X, not Y" contrast construction as a rhetorical flourish ("a correlation, not a coincidence"; "a policy shift, not a technical adjustment") unless the contrast is doing real argumentative work and stated once.
17. **No hedges without content.** Avoid "somewhat," "arguably," "to some extent," "in some sense," "it could be argued," "seems to," "may potentially" when they are not carrying a specific, defensible qualification. Hedge only where the uncertainty is real and specify its source.
18. **No fillers.** Cut "basically," "essentially," "simply," "just," "really," "very," "quite," "actually" unless the sentence fails without them.
19. **No flourish labels.** Do not bold or set off rhetorical labels like "The Bottom Line:," "Key Insight:," "Takeaway:," "Bottom line," "The upshot" — state the point in the sentence itself.
20. **No self-praise.** Do not characterize the paper's own contribution as "novel," "innovative," "unique," "cutting-edge," "state-of-the-art," or "groundbreaking." Describe what it does; let the reader judge novelty.
21. **No topic-announcing openers.** Avoid "This section discusses...," "This paper will discuss...," "Let's turn to...," "We now turn our attention to...." Open with the content itself.
<!-- academic-humanizer:end -->

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://www.sciencedirect.com/journal/international-journal-of-forecasting/publish/guide-for-authors | Guidelines | Direct fetch (partial; full guidelines behind JS) |
| https://www.sciencedirect.com/journal/international-journal-of-forecasting | Journal homepage | Direct fetch |
| Cornell, Dinh & Pourmousavi (2024), "A probabilistic forecast methodology for volatile electricity prices in the Australian National Electricity Market", arXiv:2311.07289, published IJF | Full-text HTML | arXiv open access |
| Damato, Azzimonti & Corani (2025), "Forecasting intermittent time series with Gaussian Processes and Tweedie likelihood", arXiv:2503.19086, published IJF | Abstract + metadata | arXiv open access |