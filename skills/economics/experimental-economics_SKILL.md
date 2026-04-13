---
name: experimental-economics-writing-style
description: >
  Journal-specific writing conventions for Experimental Economics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Experimental Economics",
  "submit to Experimental Economics", "match Experimental Economics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Experimental Economics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Cambridge University Press (from Vol. 28, 2025; previously Springer)
- **Scope:** Publishes laboratory and field experimental research in economics; the flagship journal of the Economic Science Association. Fully open access from 2025.
- **Guidelines URL:** https://www.cambridge.org/core/journals/experimental-economics/information/author-instructions/preparing-your-materials
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 1 (Charness, Samek & van de Ven, 2022, DOI 10.1007/s10683-021-09726-7)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No mandatory section order stated in guidelines. In practice, experimental papers replace the standard FIELD_SKILL empirical structure (Data → Empirical Strategy → Results) with a design-oriented structure: Introduction → (Literature Review) → Experimental Design/Setup → Procedures → Hypotheses → Results → Discussion/Conclusion. No fixed naming required. See Structural Deviations below.

### Length
No word or page limit stated in guidelines.

### Abstract
Unstructured. 150–250 words. No undefined abbreviations permitted. **ENFORCED** (observed: ~200 words, unstructured, in spot-checked article).

4–6 keywords required. **ENFORCED.**

### Citations
Author-year parenthetical. Consistent with FIELD_SKILL. Footnotes carry supplementary qualifications, not primary citations. Follows FIELD_SKILL norm.

### Headings
Arabic-numbered sections and subsections. Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm. Table notes explain variable definitions and statistical details.

### Explicit Prohibitions
1. **No deception**: The journal does not consider studies employing deception of participants. Any procedure that might be considered deception must be explicitly disclosed. **ENFORCED.**
2. **No simultaneous submission** to other journals.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Statistical Reporting

**Field norm:** Regression-based inference (OLS, IV, probit) with coefficient tables; standard error treatment stated precisely.

**This journal:** Nonparametric tests dominate for within-experiment comparisons: Wilcoxon-Mann-Whitney, Wilcoxon signed rank test, and Spearman rank correlations are primary inferential tools. Results reported as mean differences with associated p-values rather than coefficient tables. Regression appears as a secondary tool. **PRACTICE ONLY** (observed consistently in spot-checked article).

In addition, key empirical findings are presented as numbered, bold-labeled statements ("**Result 1** …", "**Result 2** …") embedded in the Results section. These serve as explicit signposts summarizing each finding. This convention does not appear in FIELD_SKILL. **PRACTICE ONLY.**

### Structural Deviations

**Field norm:** Empirical papers follow Introduction → Data → Empirical Strategy → Results → Robustness → Conclusion.

**This journal:** The empirical structure is replaced by an experiment-specific architecture. Typical sections include: Experimental Design (or Setup), Experimental Procedures, Hypotheses (or Predictions), Results, and Discussion. Standalone Literature Review sections appear more commonly than in standard ABS 4*/4 empirical papers—observed in the spot-checked article. The final substantive section is often titled "Discussion" rather than "Conclusion." **PRACTICE ONLY** (one article; treat as directional).

### Other Journal-Specific Patterns

**Mandatory replication and ethics package:** These requirements exceed FIELD_SKILL data description norms. All are **ENFORCED** by guidelines:

1. **Experimental instructions**: Original participant instructions must be submitted in full as an appendix. English translation required if the experiment was not conducted in English.
2. **IRB approval**: All human-subjects research must include the IRB project number in the text or a footnote. If IRB approval was not required, a statement to that effect is mandatory.
3. **Data and code**: Prior to publication, authors must provide: (a) all raw data as an ASCII/text file, and (b) all computer programs, configuration files, or scripts used to run the experiment and analyze data.
4. **Preregistration**: Authors are strongly encouraged to preregister studies and include a link in the manuscript. **GUIDELINE ONLY** (not mandatory).
5. **Participant recruitment**: Authors must describe the recruitment method, any exclusion criteria (e.g., prior participation), and how choices were incentivized. **ENFORCED.**

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural throughout)
- Active voice preference: FIELD DEFAULT
- Citation format: FIELD DEFAULT (author-year parenthetical)
- Introduction structure: FIELD DEFAULT (hook → question → approach → results → contributions → roadmap)
- Hedging intensity: FIELD DEFAULT (low; external validity hedging standard)
- JEL classification: Required (FIELD DEFAULT for economics journals)
- Roadmap paragraph: FIELD DEFAULT (present in spot-checked article)

---

## Common Pitfalls

1. **Submitting a paper with any form of participant deception.** The journal's prohibition is absolute and applies to gray-area deception (e.g., confederates, misleading instructions). Papers will not be considered.
2. **Omitting experimental instructions from the appendix.** This is a submission requirement, not a post-acceptance task. Missing instructions at submission creates desk-reject risk.
3. **Reporting only regression-based inference for within-experiment comparisons.** Reviewers in this field expect nonparametric tests (Wilcoxon, Mann-Whitney) as the primary evidence for treatment effects; relying solely on regressions without nonparametric corroboration reads as incomplete.
4. **Forgetting the replication package.** Raw data and analysis code are required before publication. Plan data infrastructure before submission, not after acceptance.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://www.cambridge.org/core/journals/experimental-economics/information/author-instructions/preparing-your-materials | Guidelines (Cambridge, current) | Web search extraction |
| https://link.springer.com/journal/10683/submission-guidelines | Guidelines (Springer, archived) | Web search extraction |
| Charness, Samek & van de Ven (2022), "What is considered deception in experimental economics?", *Experimental Economics* 25:385–412, DOI 10.1007/s10683-021-09726-7 | Full-text article | Cambridge Core OA PDF |