---
name: journal-urban-economics-writing-style
description: >
  Journal-specific writing conventions for Journal of Urban Economics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Urban Economics",
  "submit to Journal of Urban Economics", "match Journal of Urban Economics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Urban Economics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Elsevier (ScienceDirect)
- **Scope:** Publishes empirical and theoretical research in urban economics, covering housing markets, land use, labor markets in cities, urban schooling, transportation, and spatial economics.
- **Guidelines URL:** https://www.sciencedirect.com/journal/journal-of-urban-economics/publish/guide-for-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 1 (Hanushek et al. 2026, JUE 153, DOI 10.1016/j.jue.2026.103857)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm for overall section architecture. No required section order is mandated by the guidelines. However, Elsevier requires: (1) a **CRediT authorship contribution statement** at the end of the manuscript before the appendix, (2) a **data availability statement**, and (3) a **declaration of generative AI and AI-assisted technology use** as a new section placed before the references list. These three elements are ENFORCED and have no parallel in FIELD_SKILL.

### Length
No word or page limit stated in the guidelines. Articles can be as compact as ~14 pages including appendix (observed). FIELD DEFAULT for length expectations.

### Abstract
Unstructured prose — no labeled fields (Purpose, Methods, Findings, etc.). No stated word limit; observed abstracts are short (~120 words). Label: PRACTICE ONLY (confirmed in article; guidelines do not specify format or word limit).

### Citations
Elsevier Harvard author-year style. Deviates from the field norm on two points:

1. **In-text format**: Year is placed in a separate set of parentheses immediately after the author name — "(Author (Year))" — even inside a parenthetical citation, producing nested parentheses: "(e.g. Lavy (2020); Pham, Nguyen, and Springer (2021))". The comma-separated "(Author, Year)" format common in AER-family journals is not used here. Label: ENFORCED (publisher convention).

2. **Reference list format**: Full first names are spelled out for all authors (not initials). Year follows the last author name separated by a comma, before the title. Journal names are abbreviated. Example format: `Author Last, Author First, Co-Author Last, Co-Author First, Year. Title in sentence case. J. Abbrev. Name Volume (Issue), pages.` Label: ENFORCED (publisher convention).

### Keywords
Keywords are required. Label: ENFORCED.

### JEL Codes
Not required and not present in published articles. The ARTICLE INFO box lists only "Keywords" — no JEL Classification field appears. This is a departure from many ABS 4*/4 economics journals that mandate JEL codes. Label: PRACTICE ONLY.

### Headings
Arabic numerals for main sections (1, 2, 3…). Subsections within sections may use lowercase letter labels (a., b., c.) rather than decimal numbering (3.1, 3.2…). Label: PRACTICE ONLY (observed; not specified in guidelines).

### Tables and Figures
Follows FIELD_SKILL norm. Tables and figures are embedded in or near the relevant text, not collected at the end.

### Explicit Prohibitions
- AI tools cannot be listed as authors or co-authors. ENFORCED.
- Multiple, redundant, or concurrent publication is prohibited. ENFORCED.
- Authorship changes after acceptance are prohibited. ENFORCED.
- Inclusive language is required: avoid descriptors implying superiority based on age, gender, race, ethnicity, culture, sexual orientation, or disability unless directly relevant to the research. ENFORCED.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Structural Deviations

**Standalone Related Literature section in empirical papers.** FIELD_SKILL states that a standalone Related Literature section is "more common in theory papers" and "often omitted in shorter empirical papers where literature is surveyed within the Introduction." The observed empirical article (Hanushek et al.) includes a full standalone literature section (Section 2, "Literature on performance pay") positioned between the Introduction and the Institutional Background section. This pattern — Introduction / Literature / Institutional Background / Data / Methods / Results / Mechanisms / Conclusion — appears to be acceptable and may be common at this ABS 3 venue. Label: PRACTICE ONLY, RELAXATION (ABS 3 may accommodate standalone lit review in empirical papers more readily than ABS 4*/4 norm).

### Citation Format

As detailed under Hard Constraints: the Elsevier "(Author (Year))" nested parentheses in-text format and full-first-name reference list diverge from the AER-style comma-separated "(Author, Year)" pattern taken as the field baseline. Label: ENFORCED.

### Other Journal-Specific Patterns

**No JEL codes.** JUE does not display or require JEL classification codes. Submitting without JEL codes is correct. Including them would be out of place. Label: PRACTICE ONLY.

**CRediT authorship contribution statement.** Each author's specific contribution (Writing, Methodology, Data curation, etc.) must be itemised using the CRediT taxonomy at the end of the article. This is an Elsevier-wide requirement not present in the FIELD_SKILL baseline. Label: ENFORCED.

**Data availability statement.** A formal statement about data availability or access procedures is required. Label: ENFORCED.

**AI use declaration.** A statement disclosing any use of generative AI must appear in a dedicated section before the reference list. If no AI was used, the statement should say so. Label: ENFORCED.

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Active voice: FIELD DEFAULT
- Abstract type (unstructured prose): FIELD DEFAULT
- Introduction structure (hook → question → approach → results → contributions → roadmap): FIELD DEFAULT
- Hedging intensity (low, claim-forward): FIELD DEFAULT
- Statistical reporting precision (quantitative magnitudes with significance): FIELD DEFAULT
- Robustness checks as standard component: FIELD DEFAULT
- Footnotes for qualifications, not primary citations: FIELD DEFAULT
- Appendix for supplementary tables and technical detail: FIELD DEFAULT
- Citation density by section (high introduction, low conclusion): FIELD DEFAULT
- Paraphrase over direct quotation: FIELD DEFAULT

---

## Common Pitfalls

1. **Including JEL codes when they are not required or expected.** JUE does not use JEL classifications. Omit them from submissions; do not import them from working paper versions.

2. **Using comma-separated "(Author, Year)" citation format.** JUE follows Elsevier Harvard style: "(Author (Year))" with nested parentheses. Check this carefully when converting a paper formatted for AER or a similar journal.

3. **Omitting the CRediT statement, data availability statement, or AI use declaration.** All three are Elsevier hard requirements. Manuscripts missing these elements will be returned before review.

4. **Over-length reference list entries using initials only.** Elsevier Harvard style requires full first names for all authors in the reference list, not initials. Entries formatted with initials (e.g., "Abadie, A., Diamond, A., Hainmueller, J.") should be expanded to full first names.

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
| https://www.sciencedirect.com/journal/journal-of-urban-economics/publish/guide-for-authors | Guidelines | Direct fetch (partial; truncated) |
| Hanushek et al. (2026), "The effects of comprehensive pay reform on achievement in urban schools," JUE 153, 103857 | Full-text | Open access PDF via author page (hanushek.stanford.edu) |