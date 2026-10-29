---
name: international-organization-writing-style
description: >
  Journal-specific writing conventions for International Organization
  (ABS 4, SOC SCI). Use alongside soc-sci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for International Organization",
  "submit to International Organization", "match International Organization style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: International Organization

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** SOC SCI
- **Publisher:** Cambridge University Press (on behalf of The IO Foundation)
- **Scope:** Covers the full field of international affairs; articles must propose generalizable theories, improve social scientific knowledge, and/or offer new empirical insights on international relations and global politics. Studies must address an international or cross-border phenomenon as a major cause or effect; single-country work must explicitly connect to broader international dynamics.
- **Guidelines URL:** https://www.cambridge.org/core/journals/international-organization/information/author-instructions/preparing-your-materials
- **Field baseline:** soc-sci-field-writing-style
- **Articles spot-checked:** 2 (Jost et al. 2024, IO 78(1):1–37; Ecker-Ehrhardt et al. 2024, IO 78(4):731–765)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No prescribed section sequence beyond the standard IMRaD-adjacent structure. The official LaTeX template lists: title, running title, author information, abstract, body, supplementary material (optional), appendix (optional), references, author biographies, acknowledgements, keywords. Abstract and acknowledgements must be submitted separately from the manuscript file.

### Length
- **Research articles:** maximum 14,000 words. [ENFORCED]
- **Research notes:** maximum 8,000 words. [ENFORCED]
- **Supplementary material:** authors are strongly encouraged to limit supplementary material; it should rarely exceed 20 pages. [GUIDELINE ONLY]

### Abstract
Unstructured. Must be submitted separately from the manuscript. Must not contain any identifying information (blind review). Specific word limit not stated in accessible guidelines. [ENFORCED — no identifying information; GUIDELINE ONLY — word limit not confirmed]

### Citations
**This is the primary delta from FIELD_SKILL.** Upon acceptance, IO requires **short author-date footnotes** rather than parenthetical in-text references. At submission stage, any generally accepted citation standard is acceptable. The published format uses Chicago author-year style placed in footnotes (via `\footcite{}` in the LaTeX template), not as parenthetical references embedded in prose. Reference list includes only directly cited sources; newspaper/magazine articles and unpublished interviews appear in footnotes only, with no reference list entry. [ENFORCED]

### Headings
Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm. Notes below tables and figures are standard.

### Explicit Prohibitions
- Manuscripts already published elsewhere (journals or books) are not evaluated.
- Manuscripts currently under review elsewhere are not evaluated.
- A manuscript where half or more of the ideas and/or evidence have been previously published or are under review elsewhere is deemed insufficiently original.
- No identifying information in the abstract or manuscript (blind review requirement).

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where IO deviates from the field baseline.

### Citation Style
**Field norm (FIELD_SKILL):** Parenthetical in-text author-date citations are standard in quantitative political science and socio-economic analysis (e.g., Smith 2020, 45).

**IO practice:** Citations appear as author-date footnotes, not as in-text parenthetical references. The text is kept free of parenthetical citation markers; superscript numbers direct readers to footnotes where short author-date references appear (e.g., footnote: "Smith 2020, 45."). This is confirmed both in the official guidelines and in published articles. [ENFORCED]

### Structural Deviations
**Field norm:** Online appendix/supplementary material is common but has no stated page cap across the field.

**IO practice:** Supplementary material is explicitly discouraged beyond 20 pages, especially at initial submission. [GUIDELINE ONLY]

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Register: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Argumentation and rhetorical moves (CARS structure): FIELD DEFAULT
- Methods conventions (tense, detail, robustness checks): FIELD DEFAULT
- Results and statistical reporting norms: FIELD DEFAULT
- Discussion and conclusion norms: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT

---

## Common Pitfalls
1. **Using in-text parenthetical citations in the final manuscript.** IO's citation system is footnote-based author-date, not the parenthetical style used in most political science journals (APSR, AJPS, ISQ). Authors who write their draft in standard political science parenthetical style must reformat to footnotes before final submission.
2. **Submitting a manuscript with identifying information in the abstract.** The abstract is submitted as a separate file and must be fully anonymized; self-citations, institutional affiliations, and project names that identify authors must be removed.
3. **Exceeding the word limit for research articles (14,000 words) or research notes (8,000 words).** IO enforces distinct category limits; authors should clarify their submission category upfront.
4. **Submitting single-country work without explicit framing of the international dimension.** IO's scope requires the international or cross-border phenomenon to function as a major cause or effect; a purely domestic study will be desk-rejected as out of scope.

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
| https://www.cambridge.org/core/journals/international-organization/information/author-instructions/preparing-your-materials | Guidelines | Web search extraction |
| https://www.overleaf.com/latex/templates/ino-latex-template-for-submissions-to-the-international-organization-journal/wgzvjqgswybk | Official LaTeX template | Direct fetch |
| Jost et al. (2024) "Advisers and Aggregation in Foreign Policy Decision Making," IO 78(1):1–37 | Full-text article | Cambridge Core PDF |
| Ecker-Ehrhardt et al. (2024) "Ideology and Legitimacy in Global Governance," IO 78(4):731–765 | Full-text article | Cambridge Core PDF |