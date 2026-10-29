---
name: journal-of-multivariate-analysis-writing-style
description: >
  Journal-specific writing conventions for Journal of Multivariate Analysis
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Multivariate Analysis",
  "submit to Journal of Multivariate Analysis", "match Journal of Multivariate Analysis style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Multivariate Analysis

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Elsevier
- **Scope:** Publishes new methodology and theoretical developments in multivariate statistics (cluster/discriminant/factor analysis, copulas, functional data, high-dimensional inference, graphical models, extreme-value theory) together with applications to multidimensional data. Explicitly excludes univariate models, including single-response regression and univariate time series.
- **Guidelines URL:** https://www.sciencedirect.com/journal/journal-of-multivariate-analysis/publish/guide-for-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 6 (Abramovich & Pensky, "Feature selection and classification of high-dimensional normal vectors" [UCF-hosted proof]; NSF PAR-hosted JMVA article, vol. 193 (2023) 105114, on robust inference for change points in high dimensions; arXiv 2411.18334, "Large multi-response linear regression estimation based on low-rank pre-smoothing" [JMVA-targeted preprint]; plus titles/abstracts for "AUK-based test for mutual independence," "Robust factor analysis with exponential squared loss," "Nonlinear functional principal component analysis using neural networks," and "High-dimensional factor copula models with estimation of latent variables")

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No mandated section list; structure is left to authors but is expected to include proofs of all propositions, theorems, and lemmas in the main text or an appendix — never in a separate online-only supplement. Single-anonymized peer review (author identities visible to reviewers).

### Length
Papers should not exceed 25 pages (guide states an expected range of 15-25 pages).

### Abstract
Unstructured, maximum 250 words. Must stand alone (often displayed separately from the article): avoid citations unless essential, and avoid non-standard abbreviations. 1-7 keywords required.

### Citations
No mandated reference format at submission — any style is acceptable provided it is applied consistently and includes author names, title, year, volume, and pagination/article number where applicable.

### Headings
Not specified beyond standard numbered sections; no field-specific override observed.

### Tables and Figures
Not specified beyond standard Elsevier norms; no field-specific override observed.

### Explicit Prohibitions
Univariate-model papers (single-response regression, univariate time series) are out of scope and will be rejected as unsuitable regardless of quality. Proofs may not be relegated to a standalone online supplement — they must appear in the paper or its appendix.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
FIELD_SKILL's empirical (Introduction / Data / Empirical Strategy / Results / Robustness / Conclusion) and theory (Introduction / Literature / Model / Analysis / Results / Conclusion) templates do not describe this journal's typical structure. JMVA articles instead follow a mathematical-statistics template: Introduction; Model/Method setup with formal notation; Theoretical Analysis (asymptotic properties, presented as numbered Theorems/Propositions/Lemmas with Proofs, often deferred to an appendix but still within the paper); a combined "Examples" or "Numerical Results" section containing both a simulation study and a real-data application; Concluding Remarks. There is no separate "Identification Strategy," "Institutional Setting," or policy-motivated Introduction hook — the motivating case is typically a methodological gap (an estimator's inefficiency, a test's low power in high dimensions) rather than a real-world policy question. ENFORCED by convention, not stated in guidelines.

### Statistical Reporting
Results are reported primarily as formal mathematical statements (convergence rates, consistency, asymptotic distributions) rather than as point estimates with economic-magnitude interpretation. Simulation sections report performance metrics (e.g., misclassification error, MSE, power/size of tests) numerically and via tables/figures comparing the proposed method against competitors, but there is no expectation of "economic significance" narration as in FIELD_SKILL — the relevant significance is statistical/computational (rate of convergence, finite-sample performance). PRACTICE ONLY, consistent across all sampled articles.

### Citation Density
Citation density is lower and more front-loaded than FIELD_SKILL describes for empirical/theory econ papers. Related work is cited densely in the Introduction to place the method in the statistics literature, but Theory/Analysis and Examples sections cite only for borrowed lemmas, competing estimators being benchmarked, or prior asymptotic results being extended — there is no "positioning relative to prior work" narrative comparable to econ's gap-framing rhetoric. RELAXATION relative to FIELD_SKILL (ABS 3 may relax, not redefine).

### Other Journal-Specific Patterns
Proofs are formal, numbered (Theorem/Proposition/Lemma/Remark), and may be placed in an appendix, but per the guidelines may never be moved to an external supplement — this is a hard, enforced constraint distinct from FIELD_SKILL's silence on proof placement. ENFORCED.

---

## Dimensions With No Delta
- Voice and person (first-person plural, active voice): FIELD DEFAULT
- Hedging and epistemic caution outside formal results: FIELD DEFAULT
- Paraphrase vs. direct quotation: FIELD DEFAULT
- Roadmap paragraph convention: FIELD DEFAULT (present in sampled introductions)

---

## Common Pitfalls
- Submitting a paper centered on a univariate model (single-response regression or univariate time series) — explicitly out of scope regardless of methodological quality.
- Framing the Introduction around a policy question or empirical puzzle in the style of an applied econ paper rather than a methodological gap in multivariate statistics.
- Moving proofs to an online-only supplement instead of the main text or appendix.
- Writing an abstract that relies on citations or undefined abbreviations to stand alone, violating the guide's explicit abstract requirement.

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
| https://www.sciencedirect.com/journal/journal-of-multivariate-analysis/publish/guide-for-authors | Guidelines | WebSearch snippet extraction (direct fetch returned 403) |
| Abramovich & Pensky, JMVA (UCF-hosted proof PDF) | Full-text | WebFetch of publicly hosted author copy |
| JMVA 193 (2023) 105114, robust inference for change points | Full-text (partial/encoded) | WebFetch via NSF PAR repository |
| arXiv:2411.18334 (JMVA-targeted preprint) | Full-text | WebFetch via arXiv |
| "AUK-based test for mutual independence" (vol. 214, 2026) | Title/abstract | WebFetch of publisher recent-articles listing |
| "Robust factor analysis with exponential squared loss" (vol. 213, 2026) | Title/abstract | WebFetch of publisher recent-articles listing |
| "Nonlinear functional principal component analysis using neural networks" (vol. 212, 2026) | Title/abstract | WebFetch of publisher recent-articles listing |
| "High-dimensional factor copula models with estimation of latent variables" | Abstract | WebSearch snippet |
