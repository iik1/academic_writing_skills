---
name: insurance-mathematics-economics-writing-style
description: >
  Journal-specific writing conventions for Insurance: Mathematics and Economics
  (ABS 3, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Insurance: Mathematics
  and Economics", "submit to Insurance: Mathematics and Economics",
  "match Insurance: Mathematics and Economics style", or when reviewing a draft
  against this journal's requirements.
---

# Journal Writing Skill: Insurance: Mathematics and Economics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** FINANCE
- **Publisher:** Elsevier
- **Scope:** International journal covering actuarial science, including life and non-life insurance, reinsurance, ruin theory, mortality modeling, risk measures, and quantitative insurance economics. Spans probability, statistics, and mathematical finance — more mathematical than most ABS 3 FINANCE outlets.
- **Guidelines URL:** https://www.sciencedirect.com/journal/insurance-mathematics-and-economics/publish/guide-for-authors
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 2 (arXiv:2211.06568 = IME Vol. 118, pp. 25–43; arXiv:2110.08630 = IME Vol. 117, pp. 170–181)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No mandatory section list is prescribed. Structure is determined by paper type (see Structural Deviations below). [GUIDELINE ONLY — guidelines name no required sections beyond abstract and references]

### Length
No word or page limits specified in the guidelines.

### Abstract
Unstructured single paragraph; no word limit stated in guidelines. In practice: 150–200 words. No required labeled fields. [GUIDELINE ONLY for word limit; PRACTICE ONLY for length estimate]

### Highlights
**3–5 bullet points required**, each ≤85 characters (including spaces). Submitted as a separate file or field. Summarize the core findings for display on ScienceDirect. [ENFORCED]

### Citations
Author-year format in text: "(Author, Year)" or "Author (Year)". Consistent with FIELD_SKILL. Reference list follows Elsevier author-year style: "Author, I., Year. Title. Journal Volume, Pages." — year is not parenthesized in the reference list. [ENFORCED — Elsevier house style]

### Headings
Follows FIELD_SKILL norm (Arabic numerals, hierarchical).

### Tables and Figures
Follows FIELD_SKILL norm for format. Tables are uncommon in purely theoretical papers; results are delivered via theorem statements.

### Explicit Prohibitions
- AI tools may not be listed as authors or co-authors.
- Authorship changes are rejected post-acceptance.
- Inclusive language is required: gender-neutral constructions, no assumptions about readers' beliefs. [GUIDELINE ONLY — inclusive language]

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations

**Field norm:** Canonical empirical finance structure (Introduction → Data → Empirical Analysis → Robustness → Conclusion).

**This journal:** A large share of IME papers are purely or primarily mathematical. The dominant section structure for theory papers is:

1. Introduction
2. Background / Preliminaries / Setup (notation, definitions, assumptions)
3. Main Theory (theorems, propositions)
4. Applications / Examples (illustrating the theory with specific risk measures, insurance models, etc.)
5. Conclusion
6. References
7. Appendix (proofs, extensions)

A dedicated **Data** section and **Robustness** section are absent from theory papers and are present only in empirical or simulation-heavy papers. Even hybrid papers (theory + numerical illustration) may compress the data treatment into a brief subsection of the application section.

**Classification:** PRACTICE ONLY

### Mathematical Proof Structure

**Field norm:** FIELD_SKILL does not describe theorem-proof architecture; it describes empirical results reported in regression tables.

**This journal:** Formal mathematical structures are the primary vehicle for results in most IME papers:

- **Definition**, **Assumption**, **Theorem**, **Proposition**, **Lemma**, **Corollary**, **Remark**, **Example** are numbered sequentially within their type (e.g., Theorem 3.3, Proposition 2, Lemma 1).
- **Proof** blocks follow immediately after each theorem/proposition/corollary, typically ending with a tombstone (□ or QED).
- Results sections are organized around these labeled structures, not around regression specifications or hypothesis tests.

This structure coexists with first-person prose connecting the formal results. Authors narrate the intuition before and after each theorem, but the theorem statement itself is set apart typographically.

**Classification:** PRACTICE ONLY

### Statistical Reporting

**Field norm:** Results in regression tables; economic significance stated in basis points or percentage of sample mean; t-statistics or standard errors reported.

**This journal:** For purely theoretical papers, none of these norms apply. Results are formal mathematical statements verified by proof; there are no coefficients, significance stars, or economic magnitudes to report. For empirical and simulation papers, numerical results appear in tables but the emphasis is on model fit, distributional accuracy, or algorithmic performance rather than identification of causal effects or economic magnitudes.

The FIELD_SKILL requirement to state economic magnitude is a **RELAXATION** at this journal: it applies only to the empirical minority of submissions.

**Classification:** RELAXATION (for the economic significance norm)

### JEL Codes

**Field norm:** FIELD_SKILL notes JEL codes appear as separate fields on the published page.

**This journal:** JEL codes are not used. Authors provide subject-area keywords (e.g., "Credibility, Surrogate modeling, Ratemaking, Bayesian Regression, Experience Rating"). No JEL classification fields appear in published articles.

**Classification:** PRACTICE ONLY

### Voice and Register

**Field norm:** First-person plural ("we") as primary voice.

**This journal:** "We" remains primary ("We propose," "We characterize," "We show"). However, impersonal constructions — "this paper proposes," "this paper introduces" — appear more frequently than in ABS 4*/4 finance journals, including in abstracts. Both patterns are accepted; no single voice is enforced.

**Classification:** RELAXATION (minor; "this paper" is more common than FIELD_SKILL baseline suggests)

---

## Dimensions With No Delta
- Voice and person (primary): FIELD DEFAULT — "we" is dominant
- Citation density by section: FIELD DEFAULT
- Introduction structure: FIELD DEFAULT — gap identification, research question, method preview, contribution list, roadmap all present
- Paragraph density and sentence length: FIELD DEFAULT
- Conclusion length and moves: FIELD DEFAULT
- Hedging conventions: FIELD DEFAULT
- Peer review type: single anonymized (not a writing norm, but noted)

---

## Common Pitfalls

1. **Omitting Highlights.** The 3–5 bullet requirement (≤85 characters each) is enforced by the submission system. Finance authors unfamiliar with Elsevier's ScienceDirect workflow may miss this field entirely.

2. **Structuring as a pure empirical finance paper.** Submissions without a formal model or mathematical theoretical contribution are likely desk-rejected. The journal expects actuarial or mathematical content even in empirical papers; a regression study without theoretical framing is out of scope.

3. **Reporting results without formal theorem structure.** Authors from mainstream empirical finance may present main results only as regression output. IME readers expect core results to be stated as formal propositions or theorems when the paper has theoretical content, even if it is a hybrid paper.

4. **Including JEL codes.** The journal does not use JEL classification. Submitting with JEL codes copied from a finance journal template is harmless but marks the author as unfamiliar with the journal's format.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://www.sciencedirect.com/journal/insurance-mathematics-and-economics/publish/guide-for-authors | Guidelines | Direct fetch (partial — content truncated by ScienceDirect) |
| arXiv:2211.06568 (IME Vol. 118, pp. 25–43, 2024) | Full-text PDF | arXiv open access |
| arXiv:2110.08630 (IME Vol. 117, pp. 170–181, 2024) | Full-text PDF | arXiv open access |