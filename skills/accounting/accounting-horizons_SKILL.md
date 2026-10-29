---
name: accounting-horizons-writing-style
description: >
  Journal-specific writing conventions for Accounting Horizons
  (ABS 3, ACCOUNT). Use alongside account-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Accounting Horizons",
  "submit to Accounting Horizons", "match Accounting Horizons style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Accounting Horizons

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ACCOUNT
- **Publisher:** American Accounting Association (AAA)
- **Scope:** Bridges academic accounting research and non-academic audiences (practitioners, regulators, students). Publishes original research and "perspectives" (commentaries, thought pieces, historical reviews, debates). Broad coverage: auditing, financial reporting, governance, taxation, ethics, information systems, sustainability.
- **Guidelines URL:** https://aaahq.org/Research/Journals/Accounting-Horizons/Editorial-Policy
- **Field baseline:** account-field-writing-style
- **Articles spot-checked:** 1 confirmed via search-result snippet showing section structure (DOI: 10.2308/HORIZONS-2024-121; confirmed section pattern "I. SYNOPSIS AND CONTRIBUTION TO PRACTICE · II. BACKGROUND AND RESEARCH QUESTIONS · III. RESEARCH METHOD · IV. RESULTS · V. DISCUSSION AND CONCLUSION"); full-text access blocked behind paywall.

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure

The first section MUST be titled **"Synopsis and Insights for Practice"** (or substitute the specific audience, e.g., "Synopsis and Insights for Regulators"). This section **replaces the traditional introduction**. It must: (a) name the non-academic audience the paper addresses, and (b) explain what insights the paper offers to that audience. The remaining section order follows standard empirical conventions (Background/Literature, Method, Results, Discussion and Conclusion). [ENFORCED]

### Length

- **Initial submission:** Maximum 25 pages text + 40 pages total (excluding title page and abstract); double-spaced, 12-point font, 1-inch margins.
- **Accepted papers:** Generally 20 pages text + 35 pages total.
- **Perspectives:** Same limits, but editors may waive them for "clear, coherent, and concise" writing.
- Shorter papers explicitly welcomed. [ENFORCED]

### Abstract

- **150-word maximum.**
- Must be **written with a practice audience in mind** — not a specialist academic abstract. Should convey topic, methods, and findings accessibly. [ENFORCED]

### Citations

AAA author-date style per *The Chicago Manual of Style* (16th ed.): no comma between author and year — "(Author Year)" not "(Author, Year)". Two authors: "(Fehr and Schmidt 2003)"; three or more: "(Scholes et al. 2008)". Spelling per *Webster's Collegiate Dictionary*. [ENFORCED]

### Headings

AAA format per manuscript preparation guide: First-level headings centered, bold, ALL CAPITALS, numbered with Roman numerals (I., II., III.). Second-level: flush left, bold, title case. Third-level: flush left, bold, italic, title case. [ENFORCED]

### Tables and Figures

Guidelines explicitly **encourage graphical/visual presentations** and call for **minimal use of tables**. Figures submitted as separate files (EPS, TIFF, PDF, JPEG, PNG); must be interpretable in grayscale. Every table/figure must be referenced in the text. [ENFORCED]

### Explicit Prohibitions

- No simultaneous submission to other journals.
- No prior publication (preprints on SSRN acceptable; publicly available conference proceedings may constitute prior publication and require editor consultation).
- No undisclosed generative AI use (disclosure statement required after abstract).
- Missing IRB approval/exemption for human-subjects research is grounds for desk rejection.
- No undisclosed conflicts of interest (mandatory COI form at submission).
- No keyboard-formatted tables; must use Word/Excel/LaTeX.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register

**RELAXATION.** FIELD_SKILL specifies a clinical, technical register with high technical density and implicit specialist audience. Accounting Horizons explicitly requires "clear, concise, and plain language that is comprehensible to a broad audience" with **"minimal use of jargon and mathematical notations."** Authors must address practitioners or regulators, not only academic peers. The register is still formal but must be accessible. Avoid dense econometric prose; prefer explanatory prose over notational formalism.

### Statistical Reporting

**RELAXATION.** FIELD_SKILL treats tables as the primary vehicle and expects high mathematical/statistical density. Accounting Horizons guidelines explicitly call for **minimal tables** and **encourage figures** instead. Mathematical equations and heavy regression notation should be reduced or moved to appendices where possible. Economic significance explanations in plain terms are more important than precise statistical notation.

### Structural Deviations

**ENFORCED.** The introduction as described in FIELD_SKILL (establishing significance, surveying the gap, previewing results, stating contributions) does not appear as a standalone "Introduction" section. That content is restructured into **"Synopsis and Insights for Practice"**, which leads with practitioner-relevant takeaways rather than gap-framing. The CARS-model introduction pattern is subordinated to a practice-impact framing. The contribution statement and results preview still appear but are filtered through "what does this mean for practitioners/regulators?"

### Other Journal-Specific Patterns

**PRACTICE ONLY.** Search-result snippets from recent articles show the first section titled as "SYNOPSIS AND CONTRIBUTION TO PRACTICE" (rather than the guideline's exact phrasing "Synopsis and Insights for Practice"), confirming that the exact label varies by paper and audience. Authors may adapt the phrasing to match the specific non-academic audience addressed.

**GUIDELINE ONLY.** The journal also publishes "perspectives" (commentaries, debates, historical reviews, editorials), which are not covered by FIELD_SKILL's research-paper conventions. These follow a more discursive structure without hypothesis development, methods, or results sections.

---

## Dimensions With No Delta

- Citation style (author-date, no comma): FIELD DEFAULT (AAA format consistent with FIELD_SKILL)
- Heading numbering (Roman numerals, ALL CAPS first-level): FIELD DEFAULT (AAA style already noted in FIELD_SKILL)
- Past tense in methods: FIELD DEFAULT
- Explicit limitations paragraph in conclusion: FIELD DEFAULT
- Parallel results structure matching hypothesis order: FIELD DEFAULT
- First-person plural ("we"): FIELD DEFAULT
- Active voice: FIELD DEFAULT

---

## Common Pitfalls

1. **Opening with a traditional introduction.** The first section must be "Synopsis and Insights for Practice," not "Introduction." Submitting a standard FIELD_SKILL introduction as the opening section will likely trigger a desk rejection or mandatory revision.
2. **Abstract written for academics.** The 150-word abstract must address practitioners, not journal reviewers. Dense technical abstracts fail this requirement.
3. **Heavy mathematical notation and regression tables.** The explicit guideline to minimize jargon and mathematical notations, and to prefer figures over tables, is frequently violated by authors trained on ABS 4*/4 expectations. Reduce equation notation; explain models in plain prose; replace tables with figures where feasible.
4. **Exceeding the page limit.** The 40-page total limit at initial submission is tighter than typical ABS 4*/4 submissions. Reviewers and editors enforce this; a 60-page archival paper formatted for TAR or JAE will require substantial compression.

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
| https://aaahq.org/Research/Journals/Accounting-Horizons/Editorial-Policy | Guidelines | Direct fetch |
| https://aaahq.org/Research/Journals/Accounting-Horizons/Guide-for-Authors | Guidelines | Direct fetch |
| https://aaahq.org/Research/Journals/Manuscript-Preparation-Guide | AAA style guide | Direct fetch |
| DOI: 10.2308/HORIZONS-2024-121 (Improving Inventory Management Quality) | Article structure | Search-result snippet (full text paywalled) |