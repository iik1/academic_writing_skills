---
name: ieee-transactions-engineering-management-writing-style
description: >
  Journal-specific writing conventions for IEEE Transactions on Engineering Management
  (ABS 3, OPS&TECH). Use alongside opsandtech-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for IEEE Transactions on Engineering Management",
  "submit to IEEE Transactions on Engineering Management", "match IEEE TEM style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: IEEE Transactions on Engineering Management

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OPS&TECH
- **Publisher:** IEEE
- **Scope:** Technology and engineering management, innovation management, R&D management, digital platforms, project management in engineering contexts, and the intersection of operations management with information systems and technology.
- **Guidelines URL:** https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/
- **Field baseline:** opsandtech-field-writing-style
- **Articles spot-checked:** 1 (DOI: 10.1109/TEM.2024.3384960 — "Review Helpfulness Scores vs. Review Unhelpfulness Scores," Yu, Gutt & Khern-am-nuai, 2024)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No mandatory section sequence prescribed beyond Introduction and References. Observed practice follows the FIELD_SKILL quantitative empirical template, but with numbered sections throughout (see Headings below). Discussion and Conclusion are typically merged into a single section.

### Length
No journal-specific word or page limit identified from guidelines pages. IEEE-wide limits apply via the submission portal; authors should verify at submission.

### Abstract
**ENFORCED.** Single unstructured paragraph, maximum 250 words. No labeled fields (Purpose/Methods/Results/Conclusions). No mathematical symbols, abbreviations, footnotes, references, or equations permitted within the abstract. Followed by 3–5 Index Terms drawn from the IEEE Thesaurus (labeled "Index Terms:" in the published typeset version; authors may submit as "Keywords:" in the manuscript). This deviates from any field norm specifying structured abstracts.

### Citations
**ENFORCED — overrides FIELD_SKILL.** IEEE uses a **numbered citation system**, not author-date. In-text citations appear as bracketed integers: [1], [2], [4, 5], [10–12]. The FIELD_SKILL baseline specifying author-date (APA-adjacent) format does not apply here. Reference lists use IEEE format: numbered entries, authors cited as initials + surname (e.g., "S. M. Mudambi and D. Schuff"), title in quotation marks, journal name in italics, volume, number, page range, and year.

### Headings
**PRACTICE ONLY.** IEEE convention uses Arabic-numeral section numbering throughout: primary sections as 1., 2., 3.; subsections as 2.1, 2.2, 3.1, etc. Headings are bold. FIELD_SKILL does not specify numbering conventions; this is a journal-specific structural norm.

### Tables and Figures
Follows IEEE accessibility standards: use both color and shape/pattern to encode information (for color-vision-deficiency readers); connect data labels directly to elements where possible. Table titles appear above tables in bold; figure captions appear below figures. Standard errors in regression tables appear in parentheses beneath coefficients; significance levels indicated by asterisks.

### Explicit Prohibitions
- No mathematical symbols in the article title or abstract (IEEE-wide rule; may cause display errors).
- Funding disclosure must appear in the first footnote of the paper, not in an Acknowledgments section.
- Do not repeat prior conference presentation content without disclosing the prior DOI in the first footnote.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Citation Format
**Delta — ENFORCED (overrides FIELD_SKILL).**
FIELD_SKILL specifies author-date (APA-adjacent) in-text citations as the field norm. IEEE TEM uses numbered brackets throughout: [1], [4, 5], [10–12]. The reference list is formatted in IEEE style (numbered, initials-first author format), not APA. This is the most consequential delta for authors switching from management journals.

### Citation Density
**Delta — PRACTICE ONLY.**
In the article examined, citation clusters appear in brackets containing multiple numbers simultaneously (e.g., [10, 11], [6-9]), which compresses citation density visually compared to author-date strings. High citation density in Introduction and Literature Review is still present, but the numbered format makes it less visually prominent than in APA-format journals.

### Structural Deviations
**Delta — PRACTICE ONLY.**
Managerial implications are not presented in a dedicated subsection. In the observed article, managerial implications appear as prose paragraphs within the merged Discussion and Conclusion section, interleaved with theoretical contributions and limitations. FIELD_SKILL states "a dedicated subsection is expected in most outlets"; at this ABS 3 journal, this is RELAXATION — the norm is integration rather than a separate subsection.

Limitations similarly appear as prose paragraphs within Discussion and Conclusion rather than in a dedicated section.

### Other Journal-Specific Patterns
**Index Terms — ENFORCED.**
Published articles require IEEE Index Terms (3–5 terms from the IEEE Thesaurus), placed immediately after the abstract. This is not a feature of management journals in the OPS&TECH field baseline. In preprint/manuscript form, authors may use a "Keywords:" label; the IEEE typesetter converts this to "Index Terms:" in the published version.

**First footnote — ENFORCED.**
Author affiliations, submission/acceptance dates, corresponding author contact, and full funding disclosure all appear in a formatted first footnote (not in the body or Acknowledgments). This is an IEEE house style requirement with no equivalent in the FIELD_SKILL baseline.

**Section numbering — PRACTICE ONLY.**
All sections and subsections carry Arabic numeral prefixes (e.g., "4.1 Research Context", "5.2 The Generation of Unhelpfulness Scores"). This is standard IEEE convention not mentioned in FIELD_SKILL.

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT — first-person plural ("we") used throughout.
- Hedging intensity: FIELD DEFAULT — moderate hedging in interpretation, direct contribution claims.
- Statistical significance thresholds: FIELD DEFAULT — asterisks *** p<0.01, ** p<0.05, * p<0.1; robust standard errors in parentheses.
- Paragraph and sentence style: FIELD DEFAULT — medium-to-long sentences in theory sections; tighter in results.
- Introduction rhetorical structure (CARS): FIELD DEFAULT — gap, research questions, contribution preview, findings preview all present.
- Robustness tests: FIELD DEFAULT — robustness analyses reported in appendix tables.
- Endogeneity treatment: FIELD DEFAULT — addressed explicitly (propensity score matching, panel fixed effects).
- Appendix use: FIELD DEFAULT — supplementary tables in appendix.

---

## Common Pitfalls

1. **Using author-date citations.** The single most common error for authors trained in management journals. Every in-text citation must be a numbered bracket [N]. Switching citation managers to IEEE style before drafting saves extensive revision.

2. **Placing funding information in Acknowledgments.** IEEE requires all funding and support information in the first footnote, not in a separate Acknowledgments section. Acknowledgments, if present, are for non-financial thanks only.

3. **Including math symbols in the abstract.** IEEE processing systems may fail to render Greek letters, operators, or subscripts in abstracts. Write out variable names in words if needed.

4. **Expecting a structured abstract.** Authors familiar with journals that require Purpose/Design/Findings/Originality fields should note that IEEE TEM uses a plain prose paragraph. No field labels are used.

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
| https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/ | Guidelines (IEEE-wide) | Direct fetch |
| https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/structure-your-article/ | Guidelines (IEEE-wide) | Direct fetch |
| 10.1109/TEM.2024.3384960 (Yu, Gutt & Khern-am-nuai 2024) | Full-text (preprint) | arxiv.org/abs/2407.05207 |