---
name: annals-statistics-writing-style
description: >
  Journal-specific writing conventions for Annals of Statistics
  (ABS 4*, SOC SCI). Use alongside soc-sci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Annals of Statistics",
  "submit to Annals of Statistics", "match Annals of Statistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Annals of Statistics

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** SOC SCI (cross-listed; journal is fundamentally a mathematical statistics outlet)
- **Publisher:** Institute of Mathematical Statistics (IMS), hosted on Project Euclid
- **Scope:** Statistical theory and methodology — formal mathematical treatment of estimation, inference, high-dimensional statistics, nonparametric methods, Bayesian theory. Does not publish applied empirical social science, qualitative research, or ethnography.
- **Guidelines URL:** https://imstat.org/journals-and-publications/annals-of-statistics/annals-of-statistics-manuscript-preparation/
- **Field baseline:** soc-sci-field-writing-style
- **Articles spot-checked:** 2 (arXiv:2504.09279 "No-Regret Generative Modeling via Parabolic Monge-Ampère PDE", accepted AOS; arXiv:2501.06652 "High-order Accurate Inference on Manifolds", to appear AOS)

---

## Preliminary Warning

The FIELD_SKILL baseline was derived from applied social science journals. The Annals of Statistics is a pure mathematical statistics journal. Nearly every structural, rhetorical, and reporting convention differs from FIELD_SKILL. Authors approaching AOS from a social science background should treat this skill as a near-complete replacement for the baseline, not a minor supplement.

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No prescribed section sequence beyond an introduction and a reference list. Papers are organised as the mathematical argument requires: typically Introduction → numbered theoretical development sections → Appendices (proofs, technical lemmas) → References. There is no required Data, Methods, Results, or Discussion section. [ENFORCED]

### Length
Main manuscript must not exceed **25 pages** using the AOS LaTeX style files. Material beyond this limit must be placed in separate Supplementary Material. [ENFORCED]

### Abstract
Plain unstructured paragraph; no structured-abstract subheadings, no keyword list required by the template. No word limit is stated in the guidelines. [GUIDELINE ONLY — no explicit enforcement mechanism]

### Citations
IMS journals offer both author-year (`imsart-nameyear.bst`) and numbered (`imsart-number.bst`) BibTeX style files. Articles spot-checked use author-year consistently: "Author (Year)" in-text and "Author, A. (Year). Title…" in the reference list. Use author-year unless editors specify otherwise. [PRACTICE ONLY — guideline does not mandate one style]

### Headings
Sections are numbered hierarchically (Section 1, Subsection 1.1, etc.). Descriptive section titles are used but the numbering scheme is mandatory under the AOS template. [ENFORCED via template]

### Tables and Figures
No specific rules stated in the publicly available guidelines beyond the template formatting constraints. Do not use packages or commands that override the template layout. [ENFORCED: "Please do not use any packages or commands that affect the layout or formatting"]

### Supplementary Material
- Supplement must be a **separate file** from the main paper. [ENFORCED]
- **No cross-references** from the main paper to specific objects (equations, figures, theorems) in the supplement using `\ref{}`; these resolve to "??". Reference supplement sections by name only: "Section 4 of the Supplementary Material (Author (Year))". [ENFORCED]
- All supplemental files are posted as-is upon publication; the journal does not typeset or edit them. [ENFORCED]

### Affiliations
List **one affiliation per author** (department and university only). Additional affiliations belong in the Acknowledgments section. [ENFORCED]

### Explicit Prohibitions
- Do not use LaTeX packages or commands that override the template's margins, font, or layout.
- Do not submit work previously published or currently under review elsewhere.
- Do not copy literature reviews or summaries of known methods from existing sources (self-transcription prohibited).
- Do not include `\ref{}` cross-references in the main paper pointing to supplement objects.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Fundamental Genre Difference
**Field norm:** FIELD_SKILL assumes empirical research (quantitative or qualitative) with a recognisable social-science structure. **This journal:** publishes formal mathematical statistics. The entire evidential apparatus — theorems, lemmas, propositions, proofs — replaces the Data/Methods/Results structure assumed by FIELD_SKILL. Authors must think in terms of mathematical argument, not empirical narrative. [PRACTICE ONLY — not stated in guidelines but constitutive of the journal's identity]

### Structure
**Field norm:** Introduction → Theory/Literature → Data and Methods → Results → Discussion/Conclusion. **This journal:** Introduction → numbered mathematical development sections (named by their content, e.g. "Main Results," "Minimax Lower Bounds," "Simulation Studies") → Appendices containing proofs → References. Proof appendices are standard and expected; social-science-style robustness-check sections do not appear. Theoretical contributions are stated as numbered theorems, propositions, corollaries, lemmas, and remarks — not as bullet-point findings or paragraph-level assertions. [PRACTICE ONLY] [DELTA: replaces FIELD_SKILL structure entirely]

### Voice and Register
**Field norm:** First-person plural "we" dominant in multi-authored quantitative work; active voice preferred in introduction and discussion. **This journal:** Mixed. "We" is used ("we establish," "we show"), but passive constructions for stating results are equally prevalent ("it can be shown," "the following is proved"). Mathematical register is universal: no qualitative, ethnographic, or policy register appears. [PRACTICE ONLY]

### Statistical and Mathematical Reporting
**Field norm:** Prose narration of effect sizes, confidence intervals, and substantive magnitudes; tables carry evidential burden; narrative robustness checks. **This journal:** Results are proved, not narrated. The evidential standard is formal proof, not statistical significance. A "result" is a theorem with stated conditions and a proof. Asymptotic rates, minimax bounds, and convergence properties replace effect sizes and p-values. Where simulation studies appear they illustrate theory, not substitute for it. Citation of numerical results in prose refers to theorem numbers ("by Theorem 2.1") not table rows. [PRACTICE ONLY] [DELTA: replaces FIELD_SKILL reporting norms entirely]

### Introduction Structure
**Field norm:** CARS model (territory → gap → contribution), often with enumerated contributions. **This journal:** CARS logic is present — papers establish the problem's importance, survey prior results, and state the paper's contribution — but the contribution is stated in mathematical terms (rates achieved, conditions relaxed, estimator constructed). Introductions frequently include a "Notation" or "Organisation" subsection at the end. Contributions are often stated as theorem previews or informal claims that are later formalised, rather than enumerated bullet-points. [PRACTICE ONLY]

### Hedging and Epistemic Register
**Field norm:** Moderate hedging calibrated to evidence strength; causal language hedged when identification is imperfect. **This journal:** Claims are either proved (stated without hedge) or conjectured (explicitly labelled as conjecture or open problem). There is no middle-ground epistemic hedging typical of observational social science ("these findings are consistent with"). If a theorem is proved under stated assumptions, it is asserted without hedge. [PRACTICE ONLY] [DELTA: tightens FIELD_SKILL hedging norm]

### Ethics, Positionality, and Pre-registration
**Field norm:** Ethics statements, data availability notes, and (in qualitative work) researcher positionality are increasingly standard. **This journal:** None of these appear in articles; guidelines do not require them. This journal publishes mathematical theory, which generates no human-subjects data. [PRACTICE ONLY — absence, not a prohibition]

---

## Dimensions With No Delta

- Citation density by section: FIELD DEFAULT (introduction and literature sections are denser; proof sections are citation-lean — structurally analogous to FIELD_SKILL norms by section type)
- Paraphrase vs. quotation: FIELD DEFAULT (paraphrase from secondary sources; primary data are mathematical objects, not interview excerpts)
- Acknowledgments format: FIELD DEFAULT (funding, individuals, institutions — matches FIELD_SKILL)

---

## Common Pitfalls

1. **Submitting an empirical paper.** AOS does not publish applied analyses of social data, policy evaluations, or qualitative studies. The journal requires original mathematical contributions to statistical theory or methodology.
2. **Exceeding 25 pages.** Additional proofs and technical material must go into a separate Supplementary Material file, not appended to the main manuscript.
3. **Cross-referencing the supplement with `\ref{}`.** These commands produce "??" in the typeset output. Reference supplementary sections by name in prose only.
4. **Using packages that override the AOS template.** The template controls all layout parameters; conflicting packages are explicitly prohibited and may require revision before processing.

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://imstat.org/journals-and-publications/annals-of-statistics/annals-of-statistics-manuscript-preparation/ | Guidelines | Direct fetch |
| https://imstat.org/journals-and-publications/annals-of-statistics/annals-of-statistics-supplement-instructions/ | Guidelines | Direct fetch |
| https://imstat.org/journals-and-publications/annals-of-statistics/annals-of-statistics-ethical-principles/ | Guidelines | Direct fetch |
| https://vtex-soft.github.io/texsupport.ims-aos/ | Template documentation | Direct fetch |
| arXiv:2504.09279 (accepted AOS) | Full-text preprint | arXiv PDF |
| arXiv:2501.06652 (to appear AOS) | Full-text preprint | arXiv PDF |