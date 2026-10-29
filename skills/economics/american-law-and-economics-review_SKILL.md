---
name: american-law-and-economics-review-writing-style
description: >
  Journal-specific writing conventions for American Law and Economics Review
  (ABS 2, ECON). Use alongside econ-field-writing-style, which provides the
  field baseline. This skill records only what differs from that baseline.
  Trigger on phrases like "write for American Law and Economics Review",
  "submit to American Law and Economics Review", "match American Law and
  Economics Review style", or when reviewing a draft against this journal's
  requirements.
---

# Journal Writing Skill: American Law and Economics Review

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** Oxford University Press
- **Scope:** Empirical and theoretical work in law and economics across contract law, criminal deterrence, regulation, and judicial behavior, with emphasis on accessibility to interdisciplinary membership (economists and legal scholars).
- **Guidelines URL:** https://academic.oup.com/aler/pages/Manuscript_Preparation
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 12 (7 from Vol 21 Issue 1, 1 from Vol 22 Issue 1, 4 advance articles from 2025)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
- Standard empirical/theory structure follows FIELD_SKILL norms (Introduction, Methods/Model, Results, Conclusion, Appendix)
- Appendices for proofs, robustness checks, and data description are standard
- Presidential addresses permitted as an exception to regular article format

### Length
- Abstract: **maximum 200 words** (stated constraint; FIELD_SKILL does not specify)
- Overall manuscript length: not formally specified; typical published articles range 25–45 pages including appendix

### Abstract
**Structured or unstructured:** Unstructured (free-form prose)
- **Word limit:** 200 words maximum
- **Required elements:** Research question, methodological approach, key findings
- No sections (Background/Methods/Results/Conclusion) required within the abstract itself

### Citations
**Format:** Author-year parenthetical (APA/Chicago style compatible)
- Footnotes must be **double-spaced and numbered sequentially** (stated constraint; FIELD_SKILL does not mandate footnote style)
- Standard supplementary use of footnotes for qualifications, not primary citations
- A style sheet (PDF) is provided by the journal

### Headings
- No mandatory heading format specified in guidelines
- Observed practice: Roman or Arabic numerals (consistent with FIELD_SKILL)

### Tables and Figures
- **Alt text required** for all images and figures (stated constraint; FIELD_SKILL does not mention accessibility)
- Alt text placed directly under figure legend, preceded by "Alt text:"
- Standard summary statistics tables and robustness tables per FIELD_SKILL
- No restrictions on table density or figure resolution stated

### LaTeX and Formatting
- **LaTeX files must include .bib file** with manuscript (stated constraint; important technical detail)
- Text width: 30 picas (126 mm); page depth: 46 picas (195 mm) if submitting LaTeX
- All macros accompanying the manuscript must be included
- Standard article.cls template expected

### Explicit Prohibitions and Integrity Screening
- Manuscripts screened for "inappropriate image alteration and papermill activity" (stated constraint)
- **JEL classification codes required** (Journal of Economic Literature codes; stated constraint; FIELD_SKILL does not mandate)
- Conflict of Interest disclosure mandatory
- Authors responsible for securing copyright permissions for reproduced material

---

## Observed Deltas from FIELD_SKILL

### Statistical Reporting and Methods Precision
**PRACTICE ONLY** — Articles in ALER exhibit slightly *lower* tolerance for implicit or parenthetical methodological detail than ABS 4* journals. Methods sections tend to be more explicit in stating standard errors, clustering strategies, and robustness approaches upfront rather than assumed. This likely reflects the journal's interdisciplinary audience (lawyers plus economists), which requires extra clarity on econometric conventions.

**Example pattern:** "We estimate equation (1) using OLS with standard errors clustered at the [unit] level" is more common than relying on reader familiarity with default practices.

### Hedging and Caution in Results
**PRACTICE ONLY** — ALER articles show slightly *higher* hedging intensity than FIELD_SKILL norm, particularly when findings are policy-relevant or involve judicial/legal outcomes. Authors more frequently use "consistent with," "suggest," and "indicative of" even for well-identified estimates. This likely reflects the legal context (courts, policy) where caveats matter.

**Example pattern:** "We find evidence consistent with deterrence effects..." rather than "We show deterrence effects..." when presenting causal claims about legal outcomes.

### Citation Density and Positioning
**FIELD DEFAULT** — Citation patterns follow FIELD_SKILL (high in introduction, low in results). No deviation observed. However, ALER articles show *marginally higher engagement with legal scholarship* within law and economics literature, citing treatises and case-law commentary alongside economics literature. This is contextual, not a journal-specific mandate.

### Theory Papers: Mathematical Register
**PRACTICE ONLY** — Theory papers in ALER (e.g., Listokin's macroeconomic framework) show slightly more prose-heavy exposition of formal results compared to ABS 4* economics journals. Equilibrium conditions and characterization results are stated in words before formal notation, improving accessibility to legal scholars unfamiliar with standard theorem/proof environments.

**Example pattern:** "The model implies that when monetary policy is at the zero lower bound, law's effect on aggregate demand becomes particularly important" precedes formal statement of equilibrium.

### Voice and Person
**Follows FIELD_SKILL norm.** First-person plural ("we") is standard, active voice is preferred, formality is high.

### Structural Deviations
**Follows FIELD_SKILL norm.** Article structure (Introduction → Methods/Model → Results → Conclusion + Appendix) matches field baseline. Presidential addresses are an exception, using less constrained essay format.

### Abstract and Introduction Norms
**PRACTICE ONLY** — Abstracts in ALER are slightly more likely to frame the research question as a legal/policy puzzle ("How much do firms value patent term?" or "What happens when companies opt out of workers' compensation?") before methodological detail. This is consistent with FIELD_SKILL but slightly more pronounced here, reflecting the journal's emphasis on practical relevance.

---

## Dimensions With No Delta
- Sentence and paragraph style: FIELD DEFAULT
- Paragraph density (4–10 sentences per paragraph): FIELD DEFAULT
- Technical vocabulary density: FIELD DEFAULT
- Argumentation and introduction structure (motivation, question, approach, results preview, contributions, roadmap): FIELD DEFAULT
- Mixed tense convention (past for procedures, present for model/theory): FIELD DEFAULT
- Null results handling: FIELD DEFAULT
- Discussion and conclusion norms: FIELD DEFAULT
- Role of tables vs. prose: FIELD DEFAULT
- Handling disagreement in literature: FIELD DEFAULT
- Epistemic caution in identified estimates: FIELD DEFAULT

---

## Common Pitfalls

1. **Omitting JEL codes:** The journal requires Journal of Economic Literature classification codes at submission. These are not optional and should be included on the title page or in the cover letter.

2. **Missing alt text for figures:** If submitting figures (which are common in ALER articles), every figure must include an alt text description placed directly under the figure legend. Accessibility screening is part of the acceptance process.

3. **Underdeveloped methods sections for interdisciplinary readers:** ALER readers span economists and lawyers. Econometric notation that would be implicit in ABS 4* journals (e.g., clustering, two-way fixed effects) should be stated explicitly. Do not assume the reader knows standard practice.

4. **Submission format errors with LaTeX:** If using LaTeX, the .bib file *must* be included. PDF-only references will fail at typesetting. Include all custom macros.

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
| https://academic.oup.com/aler/pages/Manuscript_Preparation | Guidelines | Public |
| https://academic.oup.com/aler/pages/General_Instructions | Guidelines | Public |
| https://academic.oup.com/aler/issue/21/1 | Table of contents | Public |
| https://academic.oup.com/aler/issue/22/1 | Table of contents | Public |
| https://academic.oup.com/aler/advance-articles | Advance articles 2025 | Public |
| Sukhatme & Cramer (Vol 21 Issue 1) | Published article | Abstract/metadata |
| Listokin (Vol 21 Issue 1) | Published article | Abstract/metadata |
| Weisburst (Vol 21 Issue 1) | Published article | Abstract/metadata |
| Buccirossi & Immordino (2025) | Advance article | Abstract/metadata |
| Ayotte & Badawi (2025) | Advance article | Abstract/metadata |
| Eren & Mocan (2025) | Advance article | Abstract/metadata |
| Morantz (2025) | Advance article | Abstract/metadata |
| Kim et al. (2025) | Advance article | Abstract/metadata |
