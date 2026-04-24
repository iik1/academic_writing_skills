---
name: informs-journal-computing-writing-style
description: >
  Journal-specific writing conventions for INFORMS Journal on Computing
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for INFORMS Journal on Computing",
  "submit to INFORMS Journal on Computing", "match INFORMS Journal on Computing style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: INFORMS Journal on Computing

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** INFORMS (PubsOnLine)
- **Scope:** Computational methods and software in operations research and management science; covers algorithm design, implementation, and computational experimentation. Papers must have a substantive computing contribution — purely theoretical work without computational treatment is out of scope.
- **Guidelines URL:** https://pubsonline.informs.org/page/ijoc/submission-guidelines (access restricted; not retrievable during skill generation)
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 3 (10.1287/ijoc.2024.0938; 10.1287/ijoc.2024.0927; 10.1287/ijoc.2023.0055)

---

## Hard Constraints (Author Guidelines)

> Guidelines page was inaccessible during skill generation. Constraints below are inferred from consistent practice across all spot-checked articles and from the INFORMSJoC GitHub organization structure.

### Structure
No fixed required section sequence stated. Observed structures vary by paper type (algorithm papers, software papers, computational study papers) and do not follow a single template. Follows FIELD_SKILL norm for theoretical/methodological papers; software-focused papers reorganise sections around package architecture and experiments rather than model/analysis/results.

### Length
Not confirmed from guidelines.

### Abstract
Unstructured. Follows FIELD_SKILL norm.

### Citations
Author-year format in parentheses: "Author et al. (year)". Consistent with standard INFORMS style. Follows FIELD_SKILL norm on citation density and engagement.

### Headings
Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm.

### Code and Data Repository — ENFORCED
Every accepted paper must have a companion repository archived in the INFORMSJoC GitHub organization (https://github.com/INFORMSJoC). The repository receives a distinct DOI with a `.cd` suffix (e.g., `10.1287/ijoc.2023.0055.cd`). Authors must cite both the paper DOI and the code/data DOI; the README template for the repository is standardised across all published papers.

### Explicit Prohibitions
Not confirmed from guidelines.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Structural Deviations

**FIELD_SKILL norm:** canonical section sequence (Introduction → Model → Analysis → Results → Conclusion) with appendices for proofs.

**IJOC practice:** Section structure varies substantially by contribution type. Software papers replace Model/Analysis with sections describing package architecture, API design, and usage examples. All papers — regardless of type — include a dedicated computational experiments section. Papers consistently reference an "Online Appendix" for proofs, extended tables, and pseudocode. [PRACTICE ONLY — section naming is not prescribed, but computational experiments are present in all observed papers.]

### Other Journal-Specific Patterns

**Reproducibility requirement:** Every paper's companion repository is archived under the INFORMSJoC GitHub organisation with its own `.cd` DOI. The repository README follows a standard template with sections for citation (dual-DOI), description, installation, replication instructions, and results. Reproducibility statements appear within the relevant paper sections (e.g., within the Experiments section) rather than in a standalone "Data Availability" section. [ENFORCED — consistent across all three spot-checked papers and reflected in the INFORMSJoC GitHub organisation's uniform structure.]

**Computational scope constraint:** Because IJOC is explicitly a computing journal, the expected contribution profile shifts relative to FIELD_SKILL's full spectrum. Papers must foreground algorithmic or software contributions; theoretical findings are presented in support of computational claims rather than as ends in themselves. Authors from the more mathematical end of OR&MANSCI should frame contributions around what the algorithm achieves computationally, not what the theorem establishes analytically. [RELAXATION relative to FIELD_SKILL's ABS 4*/4 baseline — formal proof apparatus is present but secondary to computational demonstration.]

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Argumentation structure (CARS model, gap/contribution/roadmap): FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Abstract format (unstructured, problem/method/result): FIELD DEFAULT
- Use of "we": FIELD DEFAULT
- Online appendix for proofs and robustness checks: FIELD DEFAULT
- Explicit enumerated contribution statements: FIELD DEFAULT

---

## Common Pitfalls

1. **Missing companion repository.** Submitting without a code/data archive in the INFORMSJoC GitHub organisation, or without citing the `.cd` DOI alongside the paper DOI, is a structural non-compliance specific to IJOC.
2. **Insufficient computational validation.** Framing a paper primarily around theoretical results with only cursory experiments underserves IJOC's scope; reviewers expect substantive benchmarking, comparison with state-of-the-art solvers, and ablation studies.
3. **Over-claiming novelty without reproducible evidence.** IJOC's reproducibility infrastructure means results claims are verifiable; performance claims unsupported by archived, runnable code are likely to receive sceptical reviews.
4. **Using theoretical OR/MS paper structure for a software paper.** Software contributions should be structured around package design, implementation details, and empirical validation — not around the model/theorem/proof arc that dominates ABS 4*/4 theory papers in this field.

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://pubsonline.informs.org/page/ijoc/submission-guidelines | Guidelines | Inaccessible (403) |
| 10.1287/ijoc.2024.0938 (Sudoso & Aloise, column generation/MSSC) | Full-text preprint | arXiv:2410.06187 HTML |
| 10.1287/ijoc.2024.0927 (Archetti et al., colorful components) | Full-text preprint | arXiv:2408.16508 HTML |
| 10.1287/ijoc.2023.0055 (Wouda et al., PyVRP) | Full-text preprint | arXiv:2403.13795 HTML |
| https://github.com/INFORMSJoC | Repository organisation | Direct fetch |