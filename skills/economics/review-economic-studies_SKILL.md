---
name: review-economic-studies-writing-style
description: >
  Journal-specific writing conventions for Review of Economic Studies
  (ABS 4*, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Review of Economic Studies",
  "submit to Review of Economic Studies", "match Review of Economic Studies style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Review of Economic Studies

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** ECON
- **Publisher:** Oxford University Press (on behalf of Review of Economic Studies Ltd.)
- **Scope:** General economics; theory, applied, and structural work across all fields.
- **Guidelines URL:** https://restud.com/submissions/
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 1 (Aguiar, Bils & Boar, "Who Are the Hand-to-Mouth?", NBER WP 26643 rev. May 2023, published RES Vol. 92, 2025)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm, with the following mandated order: title page → abstract with keywords → main text → acknowledgements → funding section (separate) → conflict of interest declaration (separate) → references → appendices.

**Acknowledgements must appear at the end of the main text, before references, and must NOT be placed in footnotes.** This overrides the widespread practice of putting acknowledgements in a footnote on the title page or cover page. [ENFORCED]

### Length
Main manuscript (title, all tables, figures, references, appendices combined): **under 45 pages**. Exceptions require prior editor approval. Online appendix: **not exceeding 30 pages**, reserved for additional results and robustness not central to the paper. [ENFORCED]

### Abstract
Unstructured prose. **Maximum 150 words.** Keywords required alongside abstract. No structured fields (no Background, Findings, etc.). JEL codes appear on the abstract page but are not part of the abstract word count. [ENFORCED]

### Citations
Follows FIELD_SKILL norm (author-year, parenthetical or in-text). No specific style guide named in the guidelines.

### Headings
Follows FIELD_SKILL norm. Observed practice: Arabic numerals with decimal subsections (1, 2, 3.1, 4.2…); appendix sections lettered (A1, A2, A1.1…). **Non-standard abbreviations are explicitly prohibited in headings.** [ENFORCED]

### Tables and Figures
Tables must have a title and footnotes where necessary; numbered consecutively with Arabic numerals. **Explicitly prohibited: vertical lines, colored text, and shading.** Units in parentheses at column tops. [ENFORCED]

### Explicit Prohibitions
- Simultaneous submission to other journals. [ENFORCED]
- Resubmission of a previously rejected manuscript without explicit editor invitation. [ENFORCED]
- Non-standard abbreviations in section headings. [ENFORCED]

### Data Availability
Authors must make data, programs, and computational details available for replication. The journal endorses DCAS (Data and Code Availability Standard v1.0). Exemption requests must be stated in the cover letter at initial submission. [ENFORCED]

### Submission
Single PDF containing the complete manuscript. Submitted via Editorial Express (editorialexpress.com/restud). Submission fee: USD 200 (reduced to USD 120 for students, early-career researchers, and researchers from low/middle-income countries).

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Structural Deviations

**Related Literature sub-heading within Introduction.** FIELD_SKILL notes that a standalone Related Literature section is often omitted in shorter empirical papers, with the literature surveyed within the Introduction. In the spot-checked RES article, related work is positioned inside the Introduction under a bold inline label "**Related Work.**" (functioning as a named paragraph, not a numbered section). This makes the positioning explicit without consuming a top-level section number. [PRACTICE ONLY]

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural throughout, including sole-author convention)
- Register and formality: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction structure and roadmap: FIELD DEFAULT
- Citation style (author-year): FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Statistical reporting (coefficients with SE in parentheses, quantitative specificity in prose): FIELD DEFAULT
- Hedging intensity: FIELD DEFAULT
- Conclusion length and function: FIELD DEFAULT
- Null results handling: FIELD DEFAULT

---

## Common Pitfalls

1. **Acknowledgements in a title-page footnote.** RES explicitly forbids acknowledgements in footnotes; they must appear as a prose section at the end of the main text before references. This conflicts with how most NBER and IZA working papers are formatted.
2. **Breaching the 45-page limit.** The limit is all-inclusive (title, body, tables, figures, references, appendices). Authors routinely underestimate length when tables are embedded in-text.
3. **Vertical lines in tables.** Common in some disciplines and word-processor defaults; explicitly prohibited.
4. **Resubmitting a rejected manuscript.** RES bars resubmission of rejected papers without an explicit invitation from the editor. Doing so will result in desk rejection.

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
| https://restud.com/submissions/ | Guidelines | Direct fetch |
| Aguiar, Bils & Boar, NBER WP 26643 (rev. May 2023) — published RES Vol. 92 (2025) | Full-text working paper | NBER direct (PDF) |