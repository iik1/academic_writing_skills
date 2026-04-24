---
name: mathematics-operations-research-writing-style
description: >
  Journal-specific writing conventions for Mathematics of Operations Research
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Mathematics of Operations Research",
  "submit to Mathematics of Operations Research", "match Mathematics of Operations Research style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Mathematics of Operations Research

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** INFORMS
- **Scope:** Mathematical foundations of operations research — theory of optimization, mathematical programming, stochastic processes, game theory, and algorithmic analysis. Exclusively theoretical in character; applied, empirical, or computational-only papers without theoretical contribution are out of scope.
- **Guidelines URL:** https://pubsonline.informs.org/journal/moor/author-guidelines (inaccessible at time of writing — 403 on all pubsonline.informs.org paths)
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 5 (arXiv:2502.17770, 2602.05417, 2411.12385, 2302.14151, 2206.00973, 2212.06000, 2407.00307)

---

## Hard Constraints (Author Guidelines)

> Guidelines page was inaccessible. Constraints below are inferred from consistent patterns across spot-checked published articles. All are classified PRACTICE ONLY pending guideline confirmation.

### Structure
Follows FIELD_SKILL norm on general logic. No mandatory section sequence observed beyond standard mathematical paper conventions. No evidence of prescribed section names.

### Length
Not determinable from article spot-checks. No page or word cap observed in articles reviewed.

### Abstract
Unstructured prose paragraph. No structured fields (Background/Methods/Results labels). Consistent across all spot-checked articles. [PRACTICE ONLY]

### Metadata block after abstract
All spot-checked articles that include a metadata block carry two fields immediately after the abstract:
1. **Keywords** — a short comma-separated list of terms.
2. **Mathematics Subject Classification** — AMS/MSC numeric codes (e.g., "47H05, 65K15, 90C25"). These are AMS classification codes, not the INFORMS OR/MS subject taxonomy used by Operations Research.

Neither field is labeled with a word-count constraint in any article. [PRACTICE ONLY — confirmed in multiple articles; guidelines inaccessible]

### Citations
Predominantly numbered bracket references [1], [2], etc., both in-text and in the reference list. Confirmed in four of five spot-checked articles. One arXiv preprint (arXiv:2411.12385, game theory paper) used author-year format — possibly reflecting author convention in the preprint rather than the published version. INFORMS journals sometimes standardise citation format at copyediting; confirm in a published PDF before submission. [PRACTICE ONLY — strong but not fully settled]

### Headings
Decimal numbered sections (1, 2, 1.1, 2.3). Appendix or terminal proof sections may retain sequential numbering (e.g., Section 5, Section 6) rather than a formal "Appendix" label. [PRACTICE ONLY]

### Tables and Figures
Follows FIELD_SKILL norm. Tables rare; papers are predominantly theorem–proof in structure.

### Explicit Prohibitions
Not determinable (guidelines inaccessible).

---

## Observed Deltas from FIELD_SKILL

### Scope: exclusively mathematical theory (TIGHTENING)
**Field norm:** FIELD_SKILL spans a spectrum from purely theoretical to empirically grounded applied work, and explicitly notes that conventions differ modestly across this spectrum.

**This journal:** Only one end of that spectrum is published here — pure mathematical theory. Computational experiments appear occasionally as validation (e.g., small numerical illustrations confirming a theoretical bound), but papers without a formal theoretical contribution (theorems, proofs, complexity results) are out of scope. There are no empirical, applied case, or data-driven papers.

**Implication:** All FIELD_SKILL conventions that reference empirical subgenres (statistical reporting norms, empirical robustness checks, data availability conventions) do not apply here.

**Label:** TIGHTENING (scope restriction relative to field baseline)

### MSC Classification codes (PRACTICE ONLY)
**Field norm:** FIELD_SKILL does not specify a classification system after the abstract.

**This journal:** AMS Mathematics Subject Classification codes are included after the abstract in all spot-checked articles with a metadata block. This differs from other INFORMS journals (Operations Research uses the INFORMS OR/MS subject taxonomy; Management Science uses keyword lists). Authors coming from OR or MS should switch from the INFORMS taxonomy to AMS MSC codes for MOOR.

**Label:** PRACTICE ONLY

### Citation style: numbered references (PRACTICE ONLY)
**Field norm:** FIELD_SKILL does not specify numbered vs. author-year but the baseline was derived from journals (Management Science, Operations Research) that use INFORMS author-year style.

**This journal:** Numbered bracket citations [1], [2] dominate across spot-checked articles, consistent with mathematics journal conventions rather than INFORMS management science conventions. Authors switching from Management Science or Operations Research should reformat references accordingly.

**Label:** PRACTICE ONLY — consistent across most articles but not confirmed in guidelines; verify against a published PDF before final submission.

### Proof section labeling (PRACTICE ONLY)
**Field norm:** FIELD_SKILL treats appendices as a near-universal device for full proofs, clearly labelled as "Appendix."

**This journal:** Terminal proof sections sometimes carry sequential numeric labels (e.g., "Section 5: Proofs of Some Lemmas") rather than a formal "Appendix" or "A" heading. In other papers, the standard appendix label is used. Both conventions appear. Authors should follow whichever convention fits their proof structure; no single format is enforced.

**Label:** PRACTICE ONLY

### Related Work placement (PRACTICE ONLY)
**Field norm:** FIELD_SKILL notes placement varies between a subsection of the Introduction and a standalone post-Introduction section.

**This journal:** The full range appears: a standalone "Literature and Perspective" section at position 2 (arXiv:2407.00307); a subsection labeled "Related work and comparison" within the Introduction (arXiv:2301.03113); and integration without a dedicated heading (arXiv:2602.05417, 2212.06000). All three are observed. No single placement is dominant.

**Label:** PRACTICE ONLY — wider variance than FIELD_SKILL implies

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Register and formality: FIELD DEFAULT (highly formal, technically dense)
- Sentence and paragraph style: FIELD DEFAULT (mathematical notation integrated into running prose)
- Introduction structure (CARS model): FIELD DEFAULT
- Contribution enumeration: FIELD DEFAULT (explicit enumerated claims)
- Theorem/proposition formatting with inline remarks: FIELD DEFAULT
- Hedging patterns (mathematical scoping of claims): FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Conclusion structure: FIELD DEFAULT (reconnects to gap, explicit future directions)

---

## Common Pitfalls

1. **Wrong classification codes.** Authors from management science or OR backgrounds may default to the INFORMS OR/MS subject taxonomy (used in Operations Research) or omit classifications entirely. MOOR articles consistently use AMS Mathematics Subject Classification codes — use MSC 2020 numeric codes, not the INFORMS taxonomy.

2. **Citation format mismatch.** Authors accustomed to INFORMS author-year style (Management Science, Operations Research) will need to switch to numbered references for MOOR. Verify against a recently published MOOR article before final submission.

3. **Submitting applied or empirical work.** The journal's scope is the mathematics of operations research. A paper that applies known methods to data, or reports a computational case study without a formal theoretical contribution, is likely to be desk-rejected on scope grounds.

4. **Framing proofs as a separate online supplement.** Unlike INFORMS management science journals that have a well-developed e-companion convention, MOOR papers tend to include proof sections directly in the document (as terminal numbered sections or a conventional appendix). Do not assume the e-companion infrastructure applies here.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://pubsonline.informs.org/journal/moor/author-guidelines | Guidelines | Inaccessible (403 on all pubsonline.informs.org paths) |
| arXiv:2502.17770 (Liu, Lin, Xu — Lower Complexity Bounds) | Full-text | arXiv HTML |
| arXiv:2602.05417 (Solla, Royset — Optimistic Bilevel Optimization) | Abstract + metadata | arXiv abstract page |
| arXiv:2411.12385 (Ickstadt, Theobald, von Stengel — Stable-Set Bound) | Full-text | arXiv HTML |
| arXiv:2302.14151 (Khademnia, Davarnia — Convexification of bilinear terms) | Full-text | arXiv HTML |
| arXiv:2206.00973 (Lu, Mei — Primal-dual extrapolation) | Full-text | arXiv HTML |
| arXiv:2212.06000 (Ghosal, Nutz — Convergence Rate of Sinkhorn) | Full-text | arXiv HTML |
| arXiv:2407.00307 (Yu, Henderson, Pasupathy — Frank-Wolfe Recursion) | Full-text | arXiv HTML |