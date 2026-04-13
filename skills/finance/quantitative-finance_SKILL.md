---
name: quantitative-finance-writing-style
description: >
  Journal-specific writing conventions for Quantitative Finance
  (ABS 3, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Quantitative Finance",
  "submit to Quantitative Finance", "match Quantitative Finance style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Quantitative Finance

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** FINANCE
- **Publisher:** Taylor & Francis (Routledge)
- **Scope:** Mathematical and computational finance; covers derivatives pricing, stochastic models, risk management, optimal execution, portfolio optimization, and machine-learning applications in finance. Publishes formal theoretical, computational, and empirical-quantitative work; does not primarily publish reduced-form behavioural or corporate finance studies.
- **Guidelines URL:** https://www.tandfonline.com/journals/rquf20/author-instructions (inaccessible during research; 403 across all T&F URL patterns)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 3
  - Chatziandreou & Karbach (2026), "Optimal execution in intraday energy markets under Hawkes processes with transient impact," v26i2, DOI 10.1080/14697688.2025.2597415 (arXiv:2504.10282)
  - Platen (2025), "Benchmark-neutral pricing," v25i12, DOI 10.1080/14697688.2024.2321234 (arXiv:2407.01542)
  - Morel, Mallat & Bouchaud (2024), "Path shadowing Monte-Carlo," v24i9 (arXiv:2308.01486)

---

## Hard Constraints (Author Guidelines)

> Official guidelines were inaccessible (HTTP 403 on all Taylor & Francis URL patterns). The entries below are inferred from consistent across-article observation and labelled accordingly. No ENFORCED classifications can be assigned without guideline confirmation.

### Structure
Cannot confirm required sections from guidelines. Observed practice: Introduction, content sections, optional Conclusion, References, Appendices. See Structural Deviations below.

### Length
Not determinable from available sources. Observed articles range from approximately 24 to 45 pages including appendices; no word-limit signal found.

### Abstract
Plain single-paragraph abstract in all three articles. Keywords appear as a distinct field immediately after the abstract (labelled "Keywords" or "Index Terms" depending on the paper's formatting origin). No structured-abstract fields (Background/Methods/Results/Conclusions) observed. Abstract length in spot-checked papers is shorter than the 150–250 word range stated in FIELD_SKILL — observed abstracts run approximately 90–150 words. Classification: PRACTICE ONLY (guideline word limit unknown).

### Citations
**Numbered bracket citations observed in all three articles** — e.g., [2], [17], [28] — not the author-year parenthetical format that FIELD_SKILL treats as universal in finance. Reference lists use numbered entries ordered by appearance or alphabetically, with author and year visible within each entry (e.g., "Platen, E. (2006)…"). Classification: PRACTICE ONLY (guideline text not confirmed, but pattern is consistent across all examined articles and reflects the journal's mathematical-finance positioning).

### Headings
Two of three articles use Arabic numerals (1, 1.1, 1.2…). One article (Morel et al., originally formatted for a physics/IEEE venue) uses Roman numerals with IEEE-style lettered subsections (II-A, II-B). Arabic numerals appear to be the norm; Roman-numeral occurrences likely reflect the author's formatting origin rather than a journal requirement. Follows FIELD_SKILL norm for Arabic numerals.

### Tables and Figures
Follows FIELD_SKILL norm. Results reported via tables (with mean ± std notation in quantitative papers) and figures with captions. No journal-specific table footnote format was determinable.

### Explicit Prohibitions
None determinable from available sources.

---

## Observed Deltas from FIELD_SKILL

### Citation Style
**FIELD_SKILL norm:** Author-year parenthetical format throughout — "(Fama and French, 1993)" — is treated as universal in finance.
**This journal:** Numbered bracket citations [N] observed consistently in all three spot-checked articles, across mathematical-finance, computational, and stochastic-control papers. Reference lists carry full author-year information within numbered entries, but in-text references are numeric.
**Classification:** PRACTICE ONLY (guidelines inaccessible; pattern consistent across all examined articles).
**Note:** This is the single most important stylistic departure from FIELD_SKILL. Authors submitting from a finance-economics background who default to author-year must convert to numbered references.

### Classification Codes
**FIELD_SKILL norm:** JEL codes appear as separate fields on the published page.
**This journal:** Mathematical papers additionally carry Mathematics Subject Classification (MSC) codes (e.g., 62P05, 60G35, 62P20) alongside JEL codes. Pure theory papers in particular include both. Empirical or computational papers may omit MSC codes entirely.
**Classification:** PRACTICE ONLY.

### Structural Deviations
**FIELD_SKILL norm:** A dedicated Conclusion section is present in "virtually all articles."
**This journal:** Conclusion section is absent in at least one published article (Chatziandreou & Karbach), which ends with the empirical analysis section followed directly by appendices. Two of three articles do include a Conclusion. The norm is relaxed relative to ABS 4*/4 journals, but a Conclusion is still the majority practice.
**Classification:** RELAXATION (ABS 3 context; absence of a Conclusion is tolerated in papers that close with a complete empirical or theoretical demonstration).

### Theoretical Content and Methods Register
**FIELD_SKILL norm:** Methods sections describe identification strategies, data sources, and regression specifications. Robustness via alternative samples and specifications.
**This journal:** The dominant methods register is formal mathematical: theorems, lemmas, stochastic differential equations, optimization problems, and proofs (often in appendices). Robustness is presented as "complementary results" or numerical sensitivity checks, not alternative regression specifications. Papers that do include empirical content report results as mean ± std across products/periods, not as regression coefficient tables with significance stars. This is a scope characteristic that reshapes every section of the paper.
**Classification:** PRACTICE ONLY (journal scope-driven, not a relaxation of style norms).

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person "we" for multi-authored papers; single-author papers use impersonal "The paper…", consistent with FIELD_SKILL's note that impersonal constructions appear occasionally)
- Abstract format (paragraph structure): FIELD DEFAULT
- Roadmap sentence in Introduction: FIELD DEFAULT (present in all checked papers, sometimes as a dedicated subsection "Structure of the Paper" rather than a closing paragraph)
- Appendices for proofs and supplementary results: FIELD DEFAULT
- Equation numbering and integration in prose: FIELD DEFAULT

---

## Common Pitfalls
1. **Using author-year citations.** The instinct from economics and finance training is to write "(Fama and French, 1993)." All examined QF articles use [N] numbered brackets. Submitting with author-year risks desk rejection or mandatory revision.
2. **Writing for a regression-table audience.** Reviewers at QF expect formal model setup and mathematical rigour. A paper that jumps directly to empirical results without a formal model or analytical characterisation will read as underspecified for this journal's scope.
3. **Omitting MSC codes on mathematical papers.** Theoretical papers in mathematical finance should include Mathematics Subject Classification codes in addition to JEL codes; omitting them signals unfamiliarity with the journal's norms.
4. **Over-length abstracts.** FIELD_SKILL targets 150–250 words, but observed QF abstracts are closer to 90–150 words. Longer abstracts are not necessarily wrong, but the journal's practice leans shorter.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://www.tandfonline.com/journals/rquf20 (and all T&F sub-URLs) | Guidelines | Inaccessible (HTTP 403) |
| https://nhh.idm.oclc.org/login?url=https://www.tandfonline.com/… | Guidelines via EZProxy | Inaccessible (authentication wall only) |
| arXiv:2504.10282 / DOI 10.1080/14697688.2025.2597415 | Full-text (ar5iv HTML) | Open access preprint |
| arXiv:2407.01542 / DOI 10.1080/14697688.2024.2321234 | Full-text (ar5iv HTML) | Open access preprint |
| arXiv:2308.01486 / QF v24i9 | Full-text (ar5iv HTML) | Open access preprint |
| https://ideas.repec.org/s/taf/quantf.html | Article index | Direct fetch |