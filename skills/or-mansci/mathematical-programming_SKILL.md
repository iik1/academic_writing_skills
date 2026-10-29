---
name: mathematical-programming-writing-style
description: >
  Journal-specific writing conventions for Mathematical Programming
  (ABS 4, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Mathematical Programming",
  "submit to Mathematical Programming", "match Mathematical Programming style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Mathematical Programming

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** OR&MANSCI
- **Publisher:** Springer (official journal of the Mathematical Optimization Society)
- **Scope:** Publishes original research, expositions, surveys, and short communications spanning all aspects of mathematical optimization — theory, computation, and applications. Series A is the general research outlet; Series B focuses on single topics per issue, sometimes tied to conferences or symposia.
- **Guidelines URL:** https://link.springer.com/journal/10107/submission-guidelines
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 2 (Goujaud, Taylor & Dieuleveut 2025, DOI 10.1007/s10107-025-02269-2, arXiv:2307.11291; Bennouna & Van Parys 2025, DOI 10.1007/s10107-025-02259-4, arXiv:2109.06911)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No mandated section sequence beyond standard mathematical paper conventions. Series A accepts four distinct article types: original research articles, expositions, surveys, and short communications. Series B is editorially commissioned around a focused topic; check with editors before submitting there. [ENFORCED]

### Length
No explicit page limit for regular research articles. Editorial board "strongly encourages concise manuscripts; the length of a manuscript should reflect its contribution." [GUIDELINE ONLY — advisory, not a hard cap]

Short Communications: maximum 12 pages. [ENFORCED]

### Abstract
Unstructured prose, 150–250 words. Consistent with FIELD_SKILL norm on prose format; the word-count range is journal-specified. [ENFORCED]

### Keywords
Authors must provide 4–6 keywords for indexing purposes, placed after the abstract. [ENFORCED]

### Mathematics Subject Classification
Authors must supply Mathematics Subject Classification (MSC 2020) codes. An "appropriate number" of codes is required; no fixed count is specified. This field appears between the keywords and the first section. [ENFORCED]

### Citations
Author-year format throughout: citations appear as "Author [Year]" (e.g., "Polyak [1964]") inline in text and in the reference list. Numbered bracket citations (e.g., [1], [2]) are not used. This is a confirmed departure from journals in the same field that use numbered references. [ENFORCED — confirmed in articles]

### Headings
Decimal numbering (1, 1.1, 1.1.1). Appendices use lettered labels (A, B, C, …) with decimal sub-headings (A.1, A.2). Follows FIELD_SKILL norm on numbered headings.

### Tables and Figures
Follows FIELD_SKILL norm. All figures and graphical material must be embedded in the single PDF submitted during peer review.

### Explicit Prohibitions
- Do not include the LaTeX `geometry` package; it overrides journal page margins.
- Do not alter page size or margins from the svjour3 template defaults.

### LaTeX Requirement
Manuscripts must be prepared in LaTeX using Springer's `svjour3` macro package with the `smallextended` formatting option. This is not optional; a Word alternative is available only for Mathematical Programming Computation (a companion journal), not for Mathematical Programming itself. [ENFORCED]

---

## Observed Deltas from FIELD_SKILL

### Citation Style
**Field norm (FIELD_SKILL):** FIELD_SKILL establishes that direct quotation is absent and citations position prior work, but does not specify numbered vs. author-year format.

**This journal:** Author-year format only. References appear as "Author [Year]" (square-bracket year) in running text and in the reference list. Numbered citation brackets ([1], [2]) — common in some OR/management science journals — are not used. Writers accustomed to INFORMS-style numbered references (Operations Research, Management Science) must switch formats. [ENFORCED — guideline + confirmed in two articles]

### Structural Additions (MSC Codes and Keywords)
**Field norm (FIELD_SKILL):** No mention of Mathematics Subject Classification or required keyword blocks.

**This journal:** Two mandatory metadata elements appear between the abstract and the first section:
1. Keywords (4–6 terms)
2. MSC 2020 classification codes (appropriate number, no fixed count)

These are required for indexing and are distinct from any keywords embedded in the abstract. [ENFORCED]

### Article Types Beyond Standard Research
**Field norm (FIELD_SKILL):** Implicitly assumes original empirical or theoretical research articles.

**This journal:** Expositions and surveys are explicitly welcomed alongside original research and short communications. Authors writing a survey or exposition should signal this clearly in the cover letter; different review criteria apply. [ENFORCED — stated in journal scope]

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Register and formality: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction CARS structure: FIELD DEFAULT
- Related work placement (subsection within Introduction): FIELD DEFAULT
- Theorem/proposition formatting with inline proof sketches and appendix-deferred full proofs: FIELD DEFAULT
- Hedging patterns: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Null/mixed results handling: FIELD DEFAULT
- Conclusion structure: FIELD DEFAULT

---

## Common Pitfalls

1. **Wrong citation format.** Using numbered references ([1], [2]) instead of author-year ("Author [Year]") is the single most visible formatting error. The journal's LaTeX template enforces this automatically; do not override the bibliography style.

2. **Missing MSC codes or keywords.** Omitting the Mathematics Subject Classification block or the 4–6 keyword line will trigger desk rejection or a formatting round-trip. Both fields must appear between the abstract and the first section heading.

3. **Submitting a Short Communication over 12 pages.** The 12-page cap for Short Communications is hard. If the manuscript grows during revision, reclassify it or trim before resubmitting.

4. **Including the LaTeX `geometry` package.** The guidelines explicitly prohibit it because it overrides journal margins. Remove it from the preamble before submission even if it was used during drafting.

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
| https://link.springer.com/journal/10107/submission-guidelines | Guidelines | Web search extraction (direct fetch blocked by 303 redirect) |
| Goujaud, Taylor & Dieuleveut (2025), DOI 10.1007/s10107-025-02269-2 | Full-text article | arXiv preprint html (arXiv:2307.11291v2) |
| Bennouna & Van Parys (2025), DOI 10.1007/s10107-025-02259-4 | Abstract + metadata | arXiv abstract page (arXiv:2109.06911) |