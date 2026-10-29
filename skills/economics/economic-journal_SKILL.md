---
name: economic-journal-writing-style
description: >
  Journal-specific writing conventions for Economic Journal
  (ABS 4, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Economic Journal",
  "submit to Economic Journal", "match Economic Journal style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Economic Journal

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** ECON
- **Publisher:** Oxford University Press on behalf of the Royal Economic Society (RES)
- **Scope:** General interest economics journal publishing theoretical, applied, and policy-oriented papers in all fields. Explicitly welcomes both qualitative and quantitative methods; actively solicits well-powered null results.
- **Guidelines URL:** https://academic.oup.com/ej/pages/general_instructions
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 2 (Gagliarducci & Tabellini, "Faith and Assimilation: Italian Immigrants in the US," EJ 135(670):1814–1851, 2025 [NBER w30003]; Cassidy, "Revenue Persistence and Public Service Delivery," EJ 135(670):1749–1813 area, 2025 [MPRA 114464])

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm. No mandatory section ordering is prescribed beyond what the empirical or theory paper norms require. Historical Background / Institutional Setting sections are common and accepted. A dedicated Discussion section before the Conclusion appears in practice (Cassidy) and is not discouraged.

### Length
**Regular papers:** No explicit word limit found in accessible guidelines. In practice, published articles run 30–50 manuscript pages.

**Short papers:** Hard cap of **< 6,000 words** and **≤ 5 exhibits** (tables + figures combined), explicitly modelled on the AER:Insights format. Short paper status must be declared in the submission cover letter. Short papers are held to the same quality standard as regular papers and go through full peer review. [ENFORCED — stated in guidelines and confirmed in table-of-contents labelling in published issues]

### Abstract
Unstructured single-paragraph abstract. No explicit word limit recoverable from public-access guidelines. JEL codes required; submitted via the Editorial Express portal. [ENFORCED for JEL codes]

### Citations
Author-year parenthetical style throughout. Confirmed in both spot-checked articles: "(Becker and Woessmann, 2009)", "(Shah, 2006, p. 17)". Footnotes carry supplementary qualifications and literature pointers, not primary citations. Follows FIELD_SKILL norm.

### Headings
Numbered Arabic sections in both spot-checked articles. Sub-sections numbered (2.1, 2.2, …). Follows FIELD_SKILL norm on numbering conventions.

### Tables and Figures
For short papers, the combined exhibit count (tables + figures) is capped at 5. No explicit cap stated for regular articles. [ENFORCED for short papers]

### Explicit Prohibitions
- Manuscripts not meeting the Instructions to Authors will not be considered for publication.
- Authors facing data-access restrictions **must** request a formal data exemption **at the point of first submission**; retroactive exemption requests are not permitted. [ENFORCED]
- Acceptance is not granted until results pass a reproducibility check by the Data Editor. [ENFORCED]

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Submission Fee
EJ charges a submission fee payable at the end of the submission process. A discounted fee is available to RES members. No other ABS 4*/4 economics journal in the FIELD_SKILL baseline charges a submission fee at this stage.
**Delta classification: ENFORCED** (stated in guidelines; authors must confirm agreement to pay before submission is accepted).

### Short Paper Article Type
EJ operates a formally labelled short paper track (< 6,000 words, 5 exhibits), introduced in 2020. Papers in this category are distinguished in the table of contents and in editorial statistics. The same editorial decision process and quality threshold applies. When submitting a short, self-contained paper of this length, authors should designate it as a short paper in the cover letter; otherwise it may be evaluated against regular-paper expectations.
**Delta classification: ENFORCED**

### Replication and Reproducibility Requirements
EJ imposes a structured, editor-enforced replication policy that goes beyond the general FIELD_SKILL expectation that methods be described in sufficient detail for a trained economist to replicate in principle. Specific requirements:
- A replication package must accompany accepted papers. The package must include: a ReadMe file, data sources and any manipulation steps, code, software version, package versions, and an estimated computation time.
- Where data cannot be published (restricted data), authors must request a formal exemption at first submission and, where feasible, grant the Data Editor temporary access or provide a synthetic dataset.
- A dedicated Data Editor (separate from the managing editors) conducts pre-acceptance reproducibility checks; conditional acceptance is withheld until the check passes.

**Delta classification: ENFORCED** (stated in guidelines and confirmed via Data Editor infrastructure documented in annual reports; operationally distinct from the FIELD_SKILL baseline norm of "sufficient for replication in principle").

### Prior Rejection Letters Encouraged
EJ explicitly invites authors to include editors' decision letters and referee reports from prior journal rejections with the submission, on the stated rationale that this improves decision speed and quality. This is unusual among top economics journals and has no counterpart in FIELD_SKILL.
**Delta classification: GUIDELINE ONLY** (stated in guidelines; not verifiable from article text)

### Explicit Welcome of Null Results
The editorial board statement explicitly names "applied submissions on policy-relevant questions that make an important contribution by demonstrating precisely identified zero effects" as a category of welcome submission. FIELD_SKILL notes that null results are "publishable when the question is important and identification is strong," but does not state this affirmatively. EJ's editorial positioning treats well-powered nulls as a positive submission category rather than a permissible exception.
**Delta classification: GUIDELINE ONLY**

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction structure (hook → question → approach → results → contributions → roadmap): FIELD DEFAULT
- Roadmap paragraph: FIELD DEFAULT (confirmed in both spot-checked articles)
- Citation format (author-year parenthetical): FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Statistical reporting and economic significance norms: FIELD DEFAULT
- Hedging intensity: FIELD DEFAULT
- Conclusion norms: FIELD DEFAULT
- Handling of disagreement with prior literature: FIELD DEFAULT
- Identification strategy as required element in empirical papers: FIELD DEFAULT

---

## Common Pitfalls

1. **Missing data exemption at submission.** If you use restricted or proprietary data, the exemption must be flagged at first submission, not when revisions are requested. Failure to do so is grounds for rejection without review.

2. **Treating the short paper track as a lighter-touch option.** Short papers (< 6,000 words, 5 exhibits) go through full peer review at the same quality bar. Submitting without declaring short paper intent—or submitting a paper near the 6,000-word limit without the short paper designation—causes mis-categorisation.

3. **Inadequate replication package.** EJ's pre-acceptance reproducibility check is a binding editorial gate. A replication package that names data sources but omits data manipulation steps, software versions, or computation estimates will fail the check and delay or block acceptance.

4. **Omitting prior rejection letters when available.** While not required, the editorial board explicitly requests them to speed up decisions. Omitting them when they exist passes up a mechanism the editors have said improves decision quality.

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
| https://academic.oup.com/ej/pages/general_instructions | Guidelines | Direct fetch (partial; JS-heavy page) |
| https://res.org.uk/wp-content/uploads/2024/08/Economic-Journal-2023-Annual-Report-FINAL.pdf | Guidelines supplement / policies | Direct fetch via pdftotext |
| Gagliarducci & Tabellini, NBER w30003 (EJ 135(670):1814–1851, 2025) | Full-text (preprint) | NBER direct PDF via pdftotext |
| Cassidy, MPRA 114464 (EJ 135(670), 2025) | Full-text (preprint) | MPRA direct PDF via pdftotext |