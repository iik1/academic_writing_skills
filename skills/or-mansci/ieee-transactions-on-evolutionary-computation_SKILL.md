---
name: ieee-transactions-on-evolutionary-computation-writing-style
description: >
  Journal-specific writing conventions for IEEE Transactions on Evolutionary Computation
  (ABS 4, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for IEEE Transactions on Evolutionary Computation",
  "submit to IEEE Transactions on Evolutionary Computation", "match IEEE Transactions on Evolutionary Computation style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: IEEE Transactions on Evolutionary Computation

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** OR&MANSCI
- **Publisher:** IEEE (IEEE Computational Intelligence Society)
- **Scope:** Publishes archival-quality original papers on evolutionary computation and related nature-inspired, population-based optimization methods (genetic algorithms, genetic programming, evolution strategies, swarm-adjacent hybrids), plus applications that yield general field-level insight rather than pure domain results.
- **Guidelines URL:** https://cis.ieee.org/publications/t-evolutionary-computation/tevc-guidelines-for-paper-submission and https://cis.ieee.org/publications/t-evolutionary-computation/tevc-information-for-authors (both returned HTTP 418/blocked to automated fetch; guideline facts below are drawn from WebSearch snippets of these pages and corroborating third-party citation-style pages)
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 4 confirmed IEEE-TEVC-accepted preprints, read via arXiv abstract/comments pages (full text not accessible — IEEE Xplore blocks automated fetch): "Bridging Evolutionary Multiobjective Optimization and GPU Acceleration via Tensorization" (arXiv:2503.20286, Liang et al.), "Adapting Rule Representation With Four-Parameter Beta Distribution for Learning Classifier Systems" (arXiv:2506.03602), "Enabling Population-Level Parallelism in Tree-Based Genetic Programming for GPU Acceleration" / EvoGP (arXiv:2501.17168), "Batched Data-Driven Evolutionary Multi-Objective Optimization Based on Manifold Interpolation" (arXiv:2109.05639). Journal-issue table of contents for Vol. 29 Issue 4 (Aug 2025) also reviewed for topical range, titles only (no abstracts accessible).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Standard IEEE transactions article format (not detailed further in accessible guideline text). Three article types: regular papers, letters, survey papers — each has distinct length tiers (see Length). No unique required section beyond IEEE norms was identifiable from available sources.

### Length
- **Regular papers:** target 10 pages in IEEE two-column transactions format; mandatory over-length page charge ($200/page) applies beyond 10; hard maximum 15 pages.
- **Letters:** target ≤6 pages; hard maximum 9 pages.
- **Survey papers:** target 15 pages; mandatory over-length charge beyond 15; hard maximum 21 pages.
This three-tier length structure (with an explicit Letters category) is not part of FIELD_SKILL and should guide format choice before drafting.

### Abstract
No unique structured-abstract requirement found; standard single-paragraph unstructured abstract as used across IEEE journals.

### Citations
**IEEEtran numbered bracket style** — in-text citations are numbered as they first appear ("[1]", "[2]"), not author-year. This is a firm delta from FIELD_SKILL, which describes citation density and engagement norms but assumes no particular numbering convention; IEEE journals uniformly use numeric bracket citations rather than author-year prose citation.

### Headings
No IEEE-specific heading numbering scheme documented beyond standard IEEEtran conventions (numbered sections, Roman-numeral or Arabic numbering per IEEE house style).

### Tables and Figures
- All pages, including illustrations, must be numbered in a single series with no omitted numbers; illustrations are conventionally grouped at the end of the manuscript for review.
- Figure captions must appear on a separate page from both the references and the main content — not placed directly on the illustrations themselves.
- References must be placed on a separate page, formatted in IEEE style.

### Explicit Prohibitions
No explicit content-based prohibitions (e.g., banned phrasing) were found in accessible guideline text.

---

## Observed Deltas from FIELD_SKILL

### Citation Density
FIELD_SKILL's citation-engagement description (dense in Introduction/Related Work, moderate in Methods, low in Results/Appendix) held across the sampled abstracts and titles — no observable delta in density pattern, only in the numbering mechanism noted above (ENFORCED, IEEE house style).

### Structural Deviations
**Letters as a distinct short-form article type** (ENFORCED, stated in guidelines): unlike the FIELD_SKILL baseline's assumption of a single regular-paper structure, TEVC formally supports a short "Letters" track (≤6 pages target, 9 max) alongside regular papers and 15-page surveys. Authors should decide up front which track a contribution targets, since expected scope and depth differ substantially by tier.

### Other Journal-Specific Patterns
**Code/data availability as de facto practice** (PRACTICE ONLY, not confirmed as a mandatory guideline in accessible text): all four sampled accepted papers publicly link a GitHub repository for their implementation in the abstract or abstract-adjacent metadata (e.g., "Source codes are available at..."). This is consistent with a broader reproducibility push documented in EC-community literature (e.g., Reproducibility in Evolutionary Computation, arXiv:2102.03380) but was not confirmed as an enforced TEVC submission requirement from the guidelines pages themselves (which were largely inaccessible). Authors should treat a public code link as strongly expected practice rather than a stated mandate.

**Field-general contribution framing in abstracts**: the sampled abstracts (e.g., GPU-tensorization paper, EvoGP) consistently foreground a generalizable computational or algorithmic mechanism (e.g., "framework," "tensorized representation," speedup figures) ahead of any single application domain, consistent with FIELD_SKILL's contribution-framing norm — no delta, but notably strong and consistent in this sample, reinforcing rather than modifying the baseline.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction argumentation (CARS model, gap-then-contribution): FIELD DEFAULT
- Methods tense conventions: FIELD DEFAULT
- Results/reporting norms: FIELD DEFAULT
- Discussion/Conclusion norms: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Abstract format (unstructured, single paragraph): FIELD DEFAULT

---

## Common Pitfalls
- Drafting a manuscript without first deciding regular-paper vs. Letter vs. Survey track — the three tiers carry materially different length budgets (9 vs. 15 vs. 21 max pages) and over-length page charges apply beyond the target length in each tier.
- Using author-year in-text citations instead of IEEEtran numbered brackets.
- Embedding figure captions directly on illustrations or interleaving them with references, rather than keeping captions on their own separate page as IEEE format requires.
- Omitting a public code repository link — not formally mandatory per accessible guidelines, but absent from none of the sampled accepted papers, making its absence a plausible reviewer friction point.

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
| cis.ieee.org/publications/t-evolutionary-computation/tevc-guidelines-for-paper-submission | Guidelines | WebFetch blocked (HTTP 418); facts drawn from WebSearch result snippets of this page |
| cis.ieee.org/publications/t-evolutionary-computation/tevc-information-for-authors | Guidelines | WebFetch blocked (HTTP 418); facts drawn from WebSearch result snippets |
| Bridging Evolutionary Multiobjective Optimization and GPU Acceleration via Tensorization (arXiv:2503.20286) | Abstract + comments field | WebFetch of arXiv abstract page, confirmed "Accepted by IEEE TEVC" |
| Adapting Rule Representation With Four-Parameter Beta Distribution for Learning Classifier Systems (arXiv:2506.03602) | Abstract | WebFetch of arXiv abstract page; publication in TEVC (2025) confirmed via search snippet |
| Enabling Population-Level Parallelism in Tree-Based GP for GPU Acceleration / EvoGP (arXiv:2501.17168) | Abstract + comments field | WebFetch of arXiv abstract page, confirmed "Accepted by IEEE TEVC" |
| Batched Data-Driven Evolutionary Multi-Objective Optimization Based on Manifold Interpolation (arXiv:2109.05639) | Abstract | WebFetch of arXiv abstract page; identified via TEVC-related WebSearch, journal acceptance not independently confirmed on this specific page |
| IEEE Transactions on Evolutionary Computation, Vol. 29, Issue 4 (ieee-cis.blogspot.com) | Table of contents (titles only) | WebFetch, titles only, no abstracts available |
| Citationsy / Paperpal IEEE-TEVC citation style pages | Citation format reference | WebSearch snippet, corroborating IEEEtran numbered style |
