---
name: computational-statistics-and-data-analysis-writing-style
description: >
  Journal-specific writing conventions for Computational Statistics and Data Analysis
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Computational Statistics and Data Analysis",
  "submit to Computational Statistics and Data Analysis", "match Computational Statistics and Data Analysis style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Computational Statistics and Data Analysis

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON (ABS classification only — journal is a statistics/computational-methods venue, not an economics journal in practice)
- **Publisher:** Elsevier
- **Scope:** Publishes methodological and applied research on computational statistics (impact of computing on statistical methodology, statistical software/algorithms) and statistical methodology for data analysis (biostatistics, chemometrics, classification, density estimation, image analysis, psychometrics, etc.). Economic applications are rare; most authors and content originate from statistics, not economics, departments.
- **Guidelines URL:** https://www.sciencedirect.com/journal/computational-statistics-and-data-analysis/publish/guide-for-authors (ScienceDirect blocked direct fetch; content reconstructed via search-engine cache/snippets)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 8 distinct articles with abstract/title-level detail (Kaddaj et al. 2026; Tomilina, Jaffrézic & Mazo 2026; Fasano & Rebaudo 2026; Li & Zhou 2026; Goepp, Bouaziz & Nuel 2025 — full abstract; Stindl, Bi & Grazian 2025 — full abstract; Wang & Yao 2026 — abstract; Zheng, Zhang & Chen — title only), plus 13 additional titles catalogued across volumes 202–223 (2024–2026) via IDEAS/RePEc for structural/topical triangulation. ScienceDirect article pages returned 403 for direct fetch; abstracts were retrieved via WebSearch snippets, IDEAS/RePEc, and secondary sources.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No fixed IMRaD section mandate is stated beyond standard Elsevier conventions. Papers are organized around a methodological contribution (model/algorithm/estimator) rather than the empirical-paper skeleton in FIELD_SKILL.

### Length
No explicit word/page limit found in accessible guideline text.

### Abstract
Unstructured, single paragraph, maximum 250 words. Must stand alone (no citations unless essential, in which case cite author and year). Avoid non-standard or uncommon abbreviations.

### Citations
No delta from FIELD_SKILL's author-year convention found in accessible guideline text.

### Headings
No explicit deviation found in accessible guideline text.

### Tables and Figures
No explicit deviation found in accessible guideline text beyond standard Elsevier artwork rules.

### Explicit Prohibitions
AI tools may support manuscript preparation but must not substitute for human critical thinking/expertise; use requires human oversight, and authors remain fully accountable for content. Generative AI/AI-assisted tools may not be used to produce artwork (including graphical abstracts).

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
FIELD_SKILL describes economics argumentation norms (motivating hook tied to policy/real-world puzzle, contributions framed against an economics literature, causal identification language). Articles here are framed instead around a statistical/computational problem (e.g., an estimation or algorithmic limitation) with no policy motivation, no "identification strategy," and no economic-significance interpretation of results. This is a structural/disciplinary delta rather than an ABS-tier relaxation: the journal's content is statistical methodology, and FIELD_SKILL's economics-specific argumentation moves (gap framing via literature debate, "we contribute to the literature on X by Y") do not appear in the sampled abstracts. PRACTICE ONLY / FIELD DEFAULT is not the right label here — treat as OUT-OF-DOMAIN: apply general scientific/statistical writing register rather than the econ-paper rhetorical template when writing for this outlet.

### Statistical Reporting
Abstracts report methodological properties (consistency, asymptotic normality, algorithmic behavior, sampling efficiency) rather than economic magnitudes or coefficients. FIELD_SKILL's expectation of quantitative economic-significance narration ("increased employment by 4 percentage points") does not apply; the analogous norm here is precise statement of theoretical/statistical properties (rates, asymptotics, computational complexity) and empirical performance versus competing methods (simulation/benchmark comparisons). PRACTICE ONLY.

### Citation Density
Abstracts and introductions position the contribution against prior statistical/computational methods (e.g., "existing methods...suffer from convergence issues") rather than against an economics literature. Not a density difference per se, but the literature being engaged is methodological/statistical, not economic. PRACTICE ONLY.

### Structural Deviations
No "Data," "Empirical Strategy/Identification," or economics-style "Institutional Setting" sections appear in the sampled work. Typical shape instead: problem/motivation, model or algorithm specification, theoretical properties, simulation study, real-data application, conclusion. This mirrors general statistics-journal structure rather than the FIELD_SKILL empirical or theory templates. PRACTICE ONLY (observed consistently across sampled titles/abstracts, but not stated as a formal requirement in guidelines).

### Other Journal-Specific Patterns
Simulation studies and a real-data illustrative application are near-universal components (seen across sampled abstracts: seismicity forecasting, treatment-effect estimation, spline regression, varying-coefficient models). This functions as the paper's "results" section in place of FIELD_SKILL's empirical-results reporting norms. PRACTICE ONLY.

---

## Dimensions With No Delta
- Abstract length ceiling of 250 words: consistent with typical field practice — FIELD DEFAULT.
- Author-year citation format: FIELD DEFAULT (no evidence of deviation).
- Hedging on external validity/data limitations: not distinctly observed either way in abstract-level text; assume FIELD_SKILL default applies where relevant.

---

## Common Pitfalls
- Writing an economics-style introduction (policy hook, literature-gap framing, "we contribute to the literature on X") for this journal is a mismatch — the audience and editors expect a statistical/computational problem framing instead.
- Omitting a simulation study: sampled articles consistently pair theoretical development with simulation evidence and a real-data application; a purely theoretical or purely empirical paper without either component would be atypical for this outlet.
- Treating this as an economics journal because of its ABS ECON classification — its actual content and readership are statistics/computational methods, and the FIELD_SKILL economics argumentation template only partially transfers.

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
| https://www.sciencedirect.com/journal/computational-statistics-and-data-analysis/publish/guide-for-authors | Guidelines | ScienceDirect returned 403 on direct fetch; content reconstructed via WebSearch snippet excerpts |
| https://ideas.repec.org/s/eee/csdana.html | Article listing | Fetched via WebFetch (RePEc mirror), volumes 202–223 |
| Goepp, Bouaziz & Nuel, "Spline regression with automatic knot selection" (CSDA 2025) | Abstract | WebSearch snippet (via arXiv preprint + IDEAS record) |
| Stindl, Bi & Grazian, "Bayesian forecasting of Italian seismicity using the spatiotemporal RETAS model" (CSDA 2025) | Abstract | WebSearch snippet |
| Wang & Yao, "Adaptive robust estimation for varying coefficient models" (CSDA 2026) | Abstract | WebSearch snippet |
| Kaddaj et al.; Tomilina, Jaffrézic & Mazo; Fasano & Rebaudo; Li & Zhou; Zheng, Zhang & Chen; and 8 additional titles (vols 202–223) | Title only | WebFetch via IDEAS/RePEc mirror |
