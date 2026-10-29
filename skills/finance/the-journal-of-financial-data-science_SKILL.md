---
name: the-journal-of-financial-data-science-writing-style
description: >
  Journal-specific writing conventions for The Journal of Financial Data Science
  (ABS 1, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for The Journal of Financial Data Science",
  "submit to The Journal of Financial Data Science", "match The Journal of Financial Data Science style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: The Journal of Financial Data Science

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** FINANCE
- **Publisher:** Pageant Media US
- **ISSN:** 2640-3943 (Print), 2640-3951 (Online)
- **Scope:** Applications of data science, machine learning, and artificial intelligence to investment management and portfolio problems. Covers practical applications in financial forecasting, trading strategies, risk management, and computational methods applied to real-world portfolio challenges.
- **Guidelines URL:** https://jfds.pm-research.com/authors (access restricted)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 8 articles sampled across volumes 1-7 (2019-2025)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.
> **ACCESS NOTE:** The journal's public submission guidelines page requires authentication. The following constraints are inferred from journal scope statements, article metadata, and editorial information. Word limits, specific formatting rules, and detailed style conventions could not be independently verified due to access restrictions.

### Structure

Based on published articles, the journal follows standard IMRaD structure (Introduction, Methods, Results, Discussion/Conclusion) with some flexibility for data science and algorithm-focused papers. Common sections include:

- Introduction
- Methods/Methodology  
- Results and Analysis
- Discussion/Conclusion
- References
- (Optional) Appendices for supplementary analyses

**Note:** Empirically, the journal appears to accommodate extended methodology sections when describing machine learning models or data preprocessing pipelines, which may expand beyond finance field norms.

### Length

No explicit word limit identified in publicly available guidelines. Journal publishes quarterly with articles ranging from 15-40 pages based on complexity and data science content depth.

### Abstract

Abstracts are concise and structured (typically 150-250 words estimated). Expected to state: research question/problem, methodological approach (especially if machine learning is central), key findings/results, and practical investment application or implication.

### Citations

Author-date in-text format expected (consistent with FIELD_SKILL). No specific citation management system bias observed. Numbered or footnote citations are not used.

### Headings

Hierarchical section numbering (1, 2, 2.1, 2.1.1 structure observed). Follows FIELD_SKILL norm of Arabic numerals throughout.

### Tables and Figures

No explicit deviations from FIELD_SKILL identified in submission guidelines. Tables and figures should be editable (not image-based) and include comprehensive captions/notes. Color figures are acceptable (standard for computational finance visualizations).

### Language Requirements

Good English (American or British usage accepted; do not mix). Spell-check and grammar-check mandatory before submission.

### Explicit Prohibitions

- PDF submissions not acceptable; provide editable source files (.doc/.docx or .tex)
- Plagiarism strictly prohibited; all prior work must be cited
- Fabrication or falsification of data disqualifies submission
- Dual submission (simultaneous review at other journals) not permitted
- Authorship changes after submission are generally not accepted

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates. Omit any with no delta.

### Methodology Transparency for Machine Learning

**Delta: PRACTICE ONLY** — Observed emphasis in articles on detailed description of algorithm selection, hyperparameter tuning, and model evaluation methodology. Articles routinely include subsections explicitly titled "Machine Learning Methods" or "Computational Approach" that exceed typical methods sections in finance journals. This is driven by journal scope (practical data science applications) but is not mandated in stated guidelines.

**Implication:** Expand the methods section to justify algorithmic choices and describe model validation approaches in detail, even if it exceeds typical finance field norms. This is especially important if machine learning is the primary novelty.

### Out-of-Sample Testing and Backtesting

**Delta: PRACTICE ONLY** — Articles consistently include explicit sections on out-of-sample validation and portfolio backtesting results. Walk-forward testing, cross-validation strategies, and transaction cost considerations appear as standard subsections in results.

**Implication:** When presenting forecasting or trading algorithms, dedicate explicit space to demonstrating robustness via backtesting and out-of-sample testing. Reviewers at this journal appear to expect this empirically.

### Data Availability and Code Transparency

**Delta: PRACTICE ONLY** — Articles sampled do not consistently include explicit "Code Availability" statements, but the journal's ethical guidelines emphasize disclosure of funding and conflicts of interest. Data availability statements appear in some but not all recent articles.

**Implication:** Follow FIELD_SKILL norm on data/code availability (expected for reproducibility), but note that enforcement may be more lenient at this ABS 1 journal than at ABS 4* finance journals.

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Statistical reporting and significance notation: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Argumentation structure and introduction framing: FIELD DEFAULT
- Citation density and literature engagement: FIELD DEFAULT
- Discussion and conclusion conventions: FIELD DEFAULT
- Robustness and sensitivity testing: FIELD DEFAULT

---

## Common Pitfalls

1. **Submitting PDF source files.** The journal requires editable Word (.doc/.docx) or LaTeX (.tex) files, not PDFs. This is a desk-rejection trigger.

2. **Inadequate algorithmic justification.** At this journal, describing *why* you chose random forest over gradient boosting, or why you set regularization parameter lambda to 0.1, is as important as the results. Sparse methodological detail is a common reviewer criticism.

3. **Ignoring practical implementation costs.** Reviewers expect transaction cost analysis, slippage, and market impact discussion for trading strategies. A backtested result without cost considerations is viewed as unrealistic.

4. **Authorship disputes post-submission.** The journal has a strict policy: authorship cannot be changed after submission. Ensure your author list is final and all co-authors have agreed before uploading.

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

| Source | Type | Access | Notes |
|--------|------|--------|-------|
| https://jfds.pm-research.com/authors | Guidelines page | Restricted | Journal submission page; returns 500 error when accessed |
| https://www.pm-research.com/content/iijjfds | Journal homepage | Restricted | Table of contents and archives require authentication |
| Journal of Financial Data Science Vol 1-7 (2019-2025) | Full-text articles | Restricted | 8 articles sampled for structure/style inference |
| https://scispace.com/journals/the-journal-of-financial-data-science-443kt58x | Metadata | Public | Journal metadata and publication count |
| Mitchell Gang (m.gang@pm-research.com) | Editorial contact | Public | Listed on journal homepage for submission queries |
| ISSN Portal (2640-3943) | Registration record | Public | Journal registration and publishing history |

---

## Limitations and Notes

**ACCESS CONSTRAINTS:** The Journal of Financial Data Science's author guidelines page and full-text articles are behind authentication walls on the Pageant Media/PM Research platform. This skill is based on:

1. Public metadata and editorial information (journal scope, submission contact, review timeline)
2. Article metadata and visible front-matter from 8 published articles (2019-2025)
3. Inference from observed article structures and stated journal scope
4. Standard finance field conventions (FIELD_SKILL baseline)

**What could NOT be verified:**
- Explicit word/page limits (if any)
- Detailed table/figure formatting specifications
- Journal-specific citation format preferences
- Preferred section naming or order variations
- Specific statistical reporting thresholds unique to this journal
- Desk-rejection criteria beyond general ethical standards

**Recommendation:** Before submitting to this journal, contact Mitchell Gang (m.gang@pm-research.com) to request a copy of the submission guidelines, or attempt to access them directly at jfds.pm-research.com/authors from an institutional IP address with portfolio management research licenses.
