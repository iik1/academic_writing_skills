---
name: mathematical-finance-writing-style
description: >
  Journal-specific writing conventions for Mathematical Finance
  (ABS 3, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Mathematical Finance",
  "submit to Mathematical Finance", "match Mathematical Finance style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Mathematical Finance

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** FINANCE
- **Publisher:** Wiley
- **Scope:** Rigorous mathematical treatment of financial problems. Primarily publishes theoretical papers using stochastic calculus, control theory, and mathematical analysis applied to pricing, portfolio optimization, risk, and market microstructure. Applied papers must have substantial mathematical content.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/14679965/homepage/forauthors.html (returned 403; could not be accessed)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 2
  - Tang & Yao, "Trading under the Proof-of-Stake Protocol" (arXiv:2207.12581; published Math. Finance 33(4), 979–1004, 2023; DOI 10.1111/mafi.12403)
  - Gao, Li & Zhou, "Reinforcement Learning for Jump-Diffusions, with Financial Applications" (arXiv:2405.16449; published Math. Finance, DOI 10.1111/mafi.70027)

---

## Hard Constraints (Author Guidelines)

> Wiley's author guidelines for this journal returned HTTP 403 on all access attempts. No hard constraints could be verified from the guidelines document. All entries below are PRACTICE ONLY unless otherwise noted.

### Structure
No verified hard constraints. See Structural Deviations below for observed practice.

### Length
Not verified from guidelines.

### Abstract
Observed practice: unstructured single paragraph; separate "Key words" field below abstract. No structured fields (Background / Methods / Results / Conclusions) observed. Word limit not verified. [PRACTICE ONLY]

### Citations
**Numbered brackets in text and reference list** — both articles use [1], [2], [3], etc. in running text and a numbered reference list at the end. This replaces the author-year parenthetical format that is standard across FIELD_SKILL. [PRACTICE ONLY — not confirmed from guidelines]

### Headings
Arabic numerals observed (1, 2, 3, 2.1, 2.2, etc.). Section titles use small-caps or bold in the journal PDF (e.g., "1. Introduction", "3.1. Stake-hoarding."). Subsection headings can be bold and inline with the first sentence of text. Consistent with FIELD_SKILL on numbering convention; formatting differs from empirical finance journals. [PRACTICE ONLY]

### Tables and Figures
Theory papers use figures to illustrate optimal strategy regions, not regression output tables. Results figures use colour-coded strategy zones. No standard regression table format observed. [PRACTICE ONLY]

### Explicit Prohibitions
None verified (guidelines inaccessible).

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Citation Style — MAJOR DELTA

**Field norm:** Author-year parenthetical throughout; numbered citation systems never used.

**This journal:** Both articles use numbered bracket citations in text — e.g., [1], [18], [22] — with a sequentially numbered reference list. Author names may appear in prose ("Markowitz [16] pioneered…") but the in-text marker is always a numbered bracket, not a year. [PRACTICE ONLY]

### Article Structure — MAJOR DELTA

**Field norm:** Canonical empirical structure: Abstract, Introduction, Data, Empirical Analysis, Conclusion.

**This journal (RELAXATION):** Papers are organised around mathematical derivations. Typical sections observed:
1. Abstract + Key words
2. Introduction
3. Model Formulation (notation, dynamics, constraints, objective)
4. Main analysis sections (one or more, labelled by mathematical problem type, e.g., "The Consumption-Investment Problem", "q-Learning Theory")
5. Application or extension sections (may include simulation and empirical study subsections)
6. Conclusion
7. References
8. Appendix (proofs, convergence results)

No Data section, no robustness section, no mechanism section in theory papers. Applied papers (Article 2) include simulation and empirical subsections within application sections, not as standalone top-level sections.

### Formal Mathematical Apparatus — MAJOR DELTA

**Field norm:** FIELD_SKILL does not describe formal theorem-proof structure; the empirical finance norm has no equivalent.

**This journal:** Results are presented as numbered formal structures: **Assumptions**, **Definitions**, **Lemmas**, **Propositions**, **Theorems**, **Corollaries**, and **Remarks**. Proofs follow immediately after, or are deferred to an appendix with the note "Proof relegated to the appendix." This apparatus replaces the regression-table-and-prose result reporting of empirical finance entirely. [PRACTICE ONLY]

### Introduction Structure — PARTIAL RELAXATION

**Field norm:** Numbered contribution list, specific quantitative magnitudes in the introduction, explicit literature review subsection.

**This journal (RELAXATION):** Article 1 (pure theory) uses a narrative "overview of main results" paragraph that names propositions/theorems by number without enumerating them in a formal "First, … Second, … Third, …" list. Quantitative magnitudes are absent because results are closed-form expressions, not estimated coefficients. Article 2 (applied theory) is closer to the FIELD_SKILL template, explicitly enumerating two major contributions and providing a roadmap. The roadmap sentence ("The rest of the paper is organized as follows…") is present in both. The literature review is brief and embedded in the introduction, not a labeled subsection. [PRACTICE ONLY]

### Results and Reporting Norms — MAJOR DELTA

**Field norm:** Regression tables with adjacent specifications, t-statistics, significance stars; prose narrates the most important coefficients with economic magnitude interpretation.

**This journal (RELAXATION):** Main results are proved, not estimated. The canonical result unit is a labelled proposition or theorem stating optimal strategy conditions (e.g., "the bang-bang strategy is optimal"), followed by a formal proof. Interpretation prose follows the proposition, explaining the economic intuition. No significance stars, no standard errors, no clustering choices. For applied papers with numerical/empirical components, simulation results appear as figures and tables, but these are secondary to the theoretical propositions. [PRACTICE ONLY]

### Robustness Treatment — RELAXATION

**Field norm:** Systematic robustness treatment with alternative samples, alternative definitions, placebo tests.

**This journal (RELAXATION):** Not applicable for pure theory papers. Applied papers may include sensitivity analyses and simulation experiments, but these serve a different function (illustrating model behaviour) rather than establishing causal identification. [PRACTICE ONLY]

### Statistical Reporting — RELAXATION

**Field norm:** Exact coefficients, standard errors, p-values or significance levels stated explicitly.

**This journal (RELAXATION):** For theoretical results, statistical reporting is replaced by mathematical proof. For papers with empirical components, reporting norms are not well-established from just one example, but appear consistent with applied mathematics rather than econometrics conventions. [PRACTICE ONLY]

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout both articles)
- Conclusion length: FIELD DEFAULT (short, 1–2 paragraphs; restates main findings and suggests future directions)
- Roadmap sentence: FIELD DEFAULT (present in both articles at the end of the introduction)
- Section numbering convention: FIELD DEFAULT (Arabic numerals)
- Confidence calibration: FIELD DEFAULT (declarative claims for proved results; hedged language for conjectures and extensions)

---

## Common Pitfalls

1. **Using author-year citations.** Mathematical Finance uses numbered brackets [1], [2], etc. Submitting with author-year format (e.g., "Merton (1973)") is a formatting mismatch. Converting to numbered citations before submission is necessary.

2. **Structuring the paper as an empirical finance paper.** A standalone Data section, robustness section with alternative clustering, or economic magnitude paragraph will read as out of place. Structure results as propositions and theorems, not tables.

3. **Omitting formal mathematical apparatus.** Results stated in prose without theorems, lemmas, and proofs will not match the journal's conventions. All non-trivial claims should be supported by a labelled formal statement.

4. **Over-enumerating contributions in the introduction.** Pure theory papers at this journal use a results-overview narrative rather than a "First … Second … Third …" contribution list. The latter is acceptable (Article 2 uses it) but is not required and may read as over-formatted for shorter theoretical papers.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://onlinelibrary.wiley.com/page/journal/14679965/homepage/forauthors.html | Guidelines | 403 — inaccessible |
| Tang & Yao (arXiv:2207.12581; DOI 10.1111/mafi.12403) | Full-text article | PDF via arxiv.org |
| Gao, Li & Zhou (arXiv:2405.16449; DOI 10.1111/mafi.70027) | Full-text article | HTML + PDF via arxiv.org |