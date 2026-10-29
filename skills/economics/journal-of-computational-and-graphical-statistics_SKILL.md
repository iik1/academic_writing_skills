---
name: journal-of-computational-and-graphical-statistics-writing-style
description: >
  Journal-specific writing conventions for Journal of Computational and Graphical Statistics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Computational and Graphical Statistics",
  "submit to Journal of Computational and Graphical Statistics", "match Journal of Computational and Graphical Statistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Computational and Graphical Statistics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON (ABS classification; substantively a statistics/computational methodology journal)
- **Publisher:** Taylor & Francis, jointly with the American Statistical Association, Institute of Mathematical Statistics, and Interface Foundation of North America
- **Scope:** Publishes methodological advances in computational and graphical methods for statistics and data analysis — numerical methods, algorithms (e.g., MCMC, optimization), graphical displays and perception, and statistical software. Written for readers with a strong statistics background who are not necessarily computing experts.
- **Guidelines URL:** https://www.tandfonline.com/journals/ucgs20/about-this-journal (full Instructions for Authors page returned 403/inaccessible in this environment; scope and policy details reconstructed from journal "about" summaries, third-party bibliometric pages, and an empirical study of JCGS supplementary-material practices)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 3 titles/abstracts directly (via search snippets and citing pages: "A Generalized Mean Approach for Distributed-PCA," "Scalable Estimation and Two-Sample Testing for Large Networks via Subsampling," "Approximate Bayesian Computation with Deep Learning and Conformal Prediction"), plus a secondary empirical analysis of 80 non-editorial JCGS articles' supplementary-material practices (R-bloggers summary of a bibliometric study). Full text was not accessible (tandfonline.com blocked WebFetch with 403 on all pages tried, including guidelines and abstract pages). This is a below-target sample; findings below are conservatively scoped and flagged accordingly.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Not independently verifiable from accessible sources. JCGS is a statistics-methodology journal, not an empirical-economics journal: papers are near-universally organized around a proposed method/algorithm rather than an economic identification strategy. Expect Introduction, Methodology/Model, Theoretical Properties (if applicable), Simulation Study, Real-Data Application/Example, Discussion/Conclusion, with technical proofs and additional simulations deferred to online Supplementary Materials. This is a PRACTICE ONLY inference from titles and the reproducibility study, not confirmed against a guidelines page.

### Length
Not accessible in this environment.

### Abstract
Not accessible in this environment. Abstracts observed in search snippets are unstructured, single-paragraph, method-and-contribution focused (e.g., "we propose... to their knowledge, the first..."), consistent with FIELD_SKILL's results-preview norm.

### Citations
Not independently verified. No evidence of deviation from author-year norm.

### Headings
Not accessible in this environment.

### Tables and Figures
Not accessible in this environment. Given the journal's explicit graphical-methods scope, figures illustrating algorithm behavior, convergence, or visualization innovations are likely more central than in a typical econ empirical paper — PRACTICE ONLY, inferred from journal scope rather than confirmed by guideline text.

### Explicit Prohibitions
Not accessible in this environment.

### Reproducibility and Supplementary Code
ENFORCED (well-documented Taylor & Francis / JCGS-wide policy, corroborated by empirical study): authors are expected to make custom code, software, or algorithms used to generate results available, typically as online Supplementary Materials submitted alongside the manuscript. An empirical analysis of 80 non-editorial JCGS articles across six recent issues found 71 included computer code in supplementary materials (R the dominant language at 57% of software instances, followed by MATLAB, C, and C++). This is materially stronger and more specific than anything in FIELD_SKILL, which is silent on code-sharing as a structural expectation.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Not independently confirmed at full-text level; sample too thin to assert a delta. Given the journal's computational/statistical-methods orientation, expect more algorithmic and mathematical register (pseudocode, theorem-proof blocks, computational complexity statements) than a typical FIELD_SKILL economics paper, and correspondingly less policy-relevance framing in the introduction. PRACTICE ONLY / low-confidence — flagged for a future, deeper pass rather than asserted as a stated norm.

### Statistical Reporting
PRACTICE ONLY, low-prevalence signal: methods papers report algorithmic/computational performance (convergence rates, runtime, estimation accuracy in simulation) as a primary result category, not just parameter estimates with economic magnitudes. This is additive to, not a replacement for, FIELD_SKILL's quantitative-specificity norm.

### Citation Density
No delta observed; insufficient evidence either way.

### Structural Deviations
PRACTICE ONLY: papers appear to route almost all proofs, extended simulations, and code into a formal online Supplementary Materials package rather than an appendix within the main PDF, more systematically than the "standalone appendix" practice described in FIELD_SKILL. See Reproducibility constraint above.

### Other Journal-Specific Patterns
None confirmed beyond the code/reproducibility point.

---

## Dimensions With No Delta
- Citation format and paraphrase-vs-quotation norms: FIELD DEFAULT (no evidence of deviation)
- Hedging intensity: FIELD DEFAULT (no evidence of deviation)
- Contribution-statement conventions in the introduction: FIELD DEFAULT (as observed in the few accessible abstracts)

---

## Common Pitfalls
- Treating this as an empirical economics outlet: JCGS papers center on a computational/statistical method, not an economic identification strategy — a paper framed around policy relevance without a clear methodological/algorithmic contribution is a poor fit.
- Omitting a code/software supplementary package: the overwhelming majority of published JCGS articles (89% in the sampled 80-article study) include runnable code: absence of this is atypical for the venue.

---

## Avoiding AI-Writing Patterns

<!-- academic-humanizer:start v0.3.3 -->
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
<!-- academic-humanizer:end -->

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://www.tandfonline.com/journals/ucgs20/about-this-journal | Guidelines/About | WebFetch returned 403; scope reconstructed from WebSearch snippets and third-party summaries (Wikipedia, Resurchify, Research.com) |
| https://www.tandfonline.com/journals/ucgs20 | Journal homepage | WebFetch 403; WebSearch snippet only |
| R-bloggers summary of empirical study, "R and The Journal of Computational and Graphical Statistics" | Secondary analysis (80-article code/reproducibility survey) | WebFetch succeeded |
| "A Generalized Mean Approach for Distributed-PCA" (JCGS 35(2), 2025) | Abstract snippet | WebSearch snippet only; tandfonline abstract page returned 403 |
| "Scalable Estimation and Two-Sample Testing for Large Networks via Subsampling" (JCGS 34(3), 2024/2025) | Abstract snippet | WebSearch snippet only |
| "Approximate Bayesian Computation with Deep Learning and Conformal Prediction" (JCGS 35(1), 2025) | Abstract snippet | WebSearch snippet only |

**Access limitation note:** tandfonline.com blocked all WebFetch attempts (403 Forbidden) on the guidelines page, about-this-journal page, and individual article abstract/full-text pages. All journal-specific findings above rely on WebSearch result snippets and one secondary bibliometric analysis rather than direct full-text or guidelines access. This falls well short of the 15-article target; confidence in the "Hard Constraints" and structural-delta sections is correspondingly low and should be revisited if institutional access becomes available.
