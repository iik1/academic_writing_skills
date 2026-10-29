---
name: journal-of-applied-probability-writing-style
description: >
  Journal-specific writing conventions for Journal of Applied Probability
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Applied Probability",
  "submit to Journal of Applied Probability", "match Journal of Applied Probability style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Applied Probability

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON (Applied Probability / Stochastic Processes)
- **Publisher:** Cambridge University Press / Applied Probability Trust
- **Scope:** Research papers and short communications in applied probability theory, including Markov chains, random walks, stochastic processes, queuing theory, and applications to epidemiology, finance, and network science.
- **Guidelines URL:** https://www.cambridge.org/core/journals/journal-of-applied-probability/information/author-instructions
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 13 articles sampled from Volume 63 (June 2026) and recent preprints (2024–2026)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure and Type
- **JAP (Journal of Applied Probability):** Research papers maximum 25 printed pages; short communications of few pages (notes, work-in-progress, letters to editor).
- **Paper Assignment:** Submissions are routed to either JAP or AAP (Advances in Applied Probability) by the Executive Editor based on length and scope.
- **Section Ordering:** Standard (Introduction, Methods/Theory, Results, Conclusion), but not mandated. Mathematical papers may use Theorem/Proof environments interspersed with prose.

### Length
- **Research papers:** Maximum 25 printed pages.
- **Short communications:** Few pages (no specific limit stated; guidance says "few").

### Abstract
- **Format:** Non-mathematical description of subject matter and results.
- **Length:** 4–10 lines.
- **Keywords:** Required; must detail manuscript contents.
- **MSC Classification:** Mandatory; use 2020 Mathematics Subject Classification scheme.
- **Exemption:** Letters to the Editor are exempt from abstract and keywords requirements.

### Submission Format
- **File type:** Single PDF file (not LaTeX source initially).
- **Submission system:** ScholarOne platform (distinct account required; Cambridge Core login does not transfer).
- **Upon acceptance:** LaTeX source files and all associated materials must be provided.

### Citation Style
- Not explicitly stated in author guidelines extracted. Standard mathematical convention is author-year parenthetical or superscript numbers; guidelines do not specify. Observe published articles for consistency (see Sources).

### Headings
- Not explicitly mandated. Section headings may use Roman or Arabic numerals (see FIELD_SKILL baseline).

### Figures and Tables
- **Citation:** Must be referenced in text.
- **Numbering:** Consecutive Arabic numerals with captions.
- **Accessibility:** All figures require alt-text descriptions; tables require descriptions; attention to color contrast and text clarity per WCAG 2.1 Level AA standards.

### Supplementary Material
- Submit simultaneously with main article.
- Undergoes peer review alongside manuscript.
- Published online only on Cambridge Core (not in print).
- Not copyedited; published as approved by Editor in Chief.

### Explicit Prohibitions and Requirements
- **Plagiarism:** Manuscripts screened via iThenticate. Suspected plagiarism handled per COPE guidelines.
- **AI Disclosure:** Authors must declare use of AI tools (text/image generation, translation, data analysis). Include tool name, version, dates used, and detailed usage description.
- **ORCID:** Corresponding authors must identify using ORCID.
- **Copyright:** Authors/employers retain copyright; Cambridge University Press is granted a licence to publish.

### Optional Formatting Tools
- **Recommended:** Use of Applied Probability LaTeX class file (aptpub.cls) and template (template.tex) "will considerably increase the speed at which papers are processed."
- Includes: apt.bst bibliography style and guide.pdf documentation.
- Use is optional but strongly encouraged for faster processing.

---

## Observed Deltas from FIELD_SKILL

### Voice and Person
**DELTA OBSERVED - RELAXATION of field norm.**

FIELD_SKILL states: "first-person plural is the near-universal default" and "we" is used as subject of most analytical and descriptive sentences, even in sole-authored papers.

JAP articles show **lower incidence of first-person plural.** Sample articles include:
- Passive constructions: "properties of negative regression dependence (NRD)... were established" (Su et al., 2025) rather than "we established."
- Mixed voice: Authors alternate between "we study" (active, plural) and passive formulation ("it is shown that...") within the same paper.
- Abstract patterns: Several abstracts avoid "we" entirely, using impersonal structures ("the paper addresses," "this work frames").

**Classification:** PRACTICE ONLY / Relaxation. Field baseline expects near-universal first-person; JAP permits and frequently uses passive voice. For authors from ECON field, this represents a slight relaxation of register expectations.

**Recommendation:** Use "we" when asserting novel contributions, but passive voice is accepted and common for describing prior work or methods. Match the voice of your subdiscipline within probability theory (stochastic processes, financial mathematics, etc. have slightly different conventions).

### Technical Density and Acronym Conventions
**DELTA OBSERVED - Higher than field baseline.**

FIELD_SKILL notes: "Technical vocabulary density is high throughout... Acronyms for well-known estimators, datasets, and concepts are used freely once introduced."

JAP exhibits **even higher technical density.** Sample observation:
- Acronyms introduced without full explanation in abstract, assuming reader familiarity (e.g., NRD, NLTD, NRTD, NA without initial expansion in some contexts).
- Mathematical notation integrated directly into prose prose without simplified translation.
- Reader assumed to hold specialist knowledge of stochastic processes, not general probability literacy.

**Classification:** FIELD DEFAULT, but skewed higher. This is not a journal-specific deviation but an emphasis within the probability/stochastic processes subfield. ECON baselines (derived from econometrics journals) permit less assumption of specialist notation.

### Hedging Language
**DELTA OBSERVED - Lower than FIELD_SKILL.**

FIELD_SKILL allows cautious hedging for external validity, causal interpretation, and data limitations. JAP articles show **even more definitive claims without qualification:**

- "We prove that S is NA and NRTD" (Su et al.) without softening like "our analysis suggests."
- Results presented as mathematically established facts rather than empirical findings subject to measurement error.

**Classification:** FIELD DEFAULT / Relaxation. Probability theory allows certainty in mathematical proofs that econometric estimation does not. No additional hedging is required beyond FIELD_SKILL norms.

### Citation Density and Positioning
Follows FIELD_SKILL norm. High in Introduction, medium in Methods, low in Results/Conclusion.

### Sentence and Paragraph Style
Follows FIELD_SKILL norm. Long, complex sentences justified by logical precision; paragraphs dense and substantive.

---

## Dimensions With No Delta

- **Abstract and Introduction strategy:** FIELD DEFAULT (results previewed, literature positioned, contributions stated explicitly)
- **Rhetorical moves:** FIELD DEFAULT (motivating hook, research question, methodology, main results announced)
- **Results reporting:** FIELD DEFAULT (quantitative specificity, economic/practical significance noted alongside statistical significance)
- **Argumentation structure:** FIELD DEFAULT (gap framing, positioning relative to prior work)
- **Conclusion form:** FIELD DEFAULT (synthesis of findings, limitations acknowledged, future directions suggested)
- **Tense usage:** FIELD DEFAULT (mixed: data/methods in past tense; theoretical results/model properties in present tense)

---

## Common Pitfalls

1. **Over-explaining mathematical preliminaries in prose:** JAP assumes readers know stochastic process theory. Do not define "Markov chain" or "stopping time" in detail unless novel usage is central. State required definitions concisely and move to application.

2. **Insufficient rigor in proof statements:** Because hedging is low, claims must be airtight. Asymptotic results ("as n → ∞") must be stated with full precision. Avoid "approximately" or "roughly" where "with high probability" or "in probability" are technically required.

3. **Inadequate disclosure of AI tool usage:** Failure to declare AI assistance (ChatGPT, mathematical SymPy, data analysis tools) will trigger plagiarism flag via iThenticate. Declare even minor uses explicitly with tool name, version, and dates.

4. **Neglecting accessibility standards:** All figures must have alt-text; tables must have textual descriptions. Failure to meet WCAG 2.1 Level AA standards can delay publication. Test color contrast ratios in figures.

---

## Avoiding AI-Writing Patterns

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

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://www.cambridge.org/core/journals/journal-of-applied-probability/information/author-instructions | Author Guidelines (Official) | Fetched direct |
| https://www.cambridge.org/core/journals/journal-of-applied-probability/information/author-instructions/preparing-your-materials | Manuscript Preparation (Official) | Fetched direct |
| https://arxiv.org/abs/2403.13868 | Article Sample: "Analysing heavy-tail properties of Stochastic Gradient Descent..." (Damek & Mentemeier, 2024) | Abstract + Metadata |
| https://arxiv.org/abs/2303.02965 | Article Sample: "Localized geometry detection in scale-free random graphs" (Bet, Michielan & Stegehuis, 2023) | Abstract + Metadata |
| https://arxiv.org/abs/2505.01971 | Article Sample: "Negative dependence in knockout tournaments" (Su, Zou & Hu, 2025) | Abstract + Metadata |
| https://arxiv.org/abs/2312.10883 | Article Sample: "Backward stochastic difference equations on lattices..." (Fukasawa, Sato & Sekine, 2023) | Abstract + Metadata |
| https://www.cambridge.org/core/journals/journal-of-applied-probability/latest-issue | Latest Issue Table of Contents (Volume 63, Issue 2, June 2026) | Fetched direct |
| https://research.com/journal/journal-of-applied-probability | Journal Impact & Scope (2025) | Reference |
| https://www.appliedprobability.org/publications/journal-of-applied-probability | Applied Probability Trust (Publisher Info) | Reference |

---

## Notes

**Access Limitations:** Most JAP articles are paywalled behind Cambridge Core. Analysis relied on abstracts, metadata, and arXiv preprints of papers later published in JAP (which authors typically post before or simultaneous with submission). Voice and structural patterns were inferred from abstracts and available front matter rather than full-text analysis. A sample of 13 articles across 2024–2026 was reviewed for consistency checks. For style replication at the highest fidelity, consult 2–3 recent full-text articles in your specific subfield (e.g., queuing theory, financial stochastic processes) within JAP.

**Author Guidelines Completeness:** Official guidelines available from Cambridge do not specify citation format (author-year vs. numbered) or explicit section heading conventions. These are inferred from published articles and standard mathematical convention. Authors should verify against a recent article in their specific research area before final submission.
