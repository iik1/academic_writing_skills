---
name: scandinavian-journal-of-statistics-writing-style
description: >
  Journal-specific writing conventions for Scandinavian Journal of Statistics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Scandinavian Journal of Statistics",
  "submit to Scandinavian Journal of Statistics", "match Scandinavian Journal of Statistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Scandinavian Journal of Statistics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON (classified under ABS list, but content is general statistical methodology/theory, not economics)
- **Publisher:** John Wiley & Sons, on behalf of four Scandinavian statistical societies (Danish Society for Theoretical Statistics, Finnish Statistical Society, Norwegian Statistical Association, Swedish Statistical Association)
- **Scope:** International journal publishing original contributions to statistical methodology, theory, and applications; quarterly, established 1974. Not an economics journal in subject matter — articles are statistics/probability papers (estimation theory, asymptotics, survival analysis, spatial/functional data, time series) with econometrics as only one of many application areas.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/14679469/homepage/forauthors.html (partially accessible; full page paywalled/blocked from automated fetch, so several manuscript-length/section-order specifics could not be confirmed and are marked as such below)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 15 (abstracts/front matter only, full text inaccessible): Bladt & Furrer "Conditional Aalen–Johansen estimation" (sjos.12774); Wang "Mode-adaptive factor models" (sjos.12785); Ebner et al. "Stein's method of moments" (sjos.70003); Gardes & Podgorny "Dimension reduction for the estimation of the conditional tail index" (sjos.12792); Mazzonetto et al. "Parameters estimation of a threshold CKLS process" (sjos.70005); Kurisu, Ishihara & Sugasawa "Adaptively robust small area estimation" (sjos.12778); Ziersen & Martinussen "Variable importance measures for heterogeneous treatment effects with survival outcome" (sjos.70001); Zhang et al. "Learning under commission and omission event outliers" (sjos.70012); Virta "Spatial depth for data in metric spaces" (sjos.70054); Ameijeiras-Alonso & Gijbels "Semiparametric regression for circular response with application in ecology" (sjos.70027); Virta "Projection-based estimators for matrix/tensor-valued data" (sjos.70021); Helland "On optimal linear prediction" (sjos.70006); unnamed authors "Extended generalized Marshall–Olkin model for dependent censoring"; Gandy & Matcham "A proper concordance index for models with crossing hazards" (sjos.70000); "A conversation with Nils Lid Hjort" (interview/retrospective piece, vol. 51(3)).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Not confirmed from accessible guideline content beyond generic Wiley conventions (no fixed IMRaD template mandated; statistics papers organize by theory/method rather than the ECON empirical template). Treat FIELD_SKILL's empirical-paper structure as inapplicable — this journal's papers are theory/methods papers, closer to FIELD_SKILL's "Theory and structural papers" track (Introduction, model/setup, theoretical results, simulation/application, conclusion), but with no standalone "Related Literature" section observed as separate from the Introduction in the sampled abstracts/titles.

### Length
Not confirmed (guidelines page inaccessible for word/page limits). No explicit limit could be verified; do not assert one.

### Abstract
Single-paragraph, unstructured abstract (no labeled subsections) in every article sampled. Abstracts are dense and technical from the first sentence — they typically open by stating the statistical problem or naming the estimator/method directly, rather than with a motivating real-world hook. A brief mention of a simulation study or real-data application typically closes the abstract, but this is compressed to one clause or one short sentence, not a preview of quantitative results in the ECON sense (no "increases X by Y%" framing — instead "consistency and asymptotic normality are established," "the method is compared... and results confirm effectiveness").

### Citations
Not independently confirmed beyond standard Wiley/statistics norms; no evidence of deviation from author-year convention.

### Headings
Not confirmed from accessible guideline text.

### Tables and Figures
Not confirmed from accessible guideline text. Online Supporting Information (supplementary material, e.g., proofs, extra simulations) submitted alongside the main manuscript is explicitly supported by the submission portal.

### Explicit Prohibitions
Guidelines state a manuscript must not have been published elsewhere and must not be under consideration elsewhere; extended conference-proceedings versions are permitted only with substantial new contribution, explicit disclosure in the cover letter, and citation of the original proceedings paper.

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Voice and Register
RELAXATION / PRACTICE ONLY. FIELD_SKILL's "we"-centric, low-hedging register describes empirical/policy economics prose. This journal's papers are mathematical-statistics papers: prose is dominated by theorem-proof logic, precise technical statement of assumptions, and estimator properties (consistency, asymptotic normality) rather than economic argumentation, motivation via real-world stylized facts, or policy implications. First-person plural still appears ("we propose," "we establish"), consistent with FIELD_SKILL, but the surrounding content is proof-oriented rather than narrative/interpretive — this is a disciplinary difference in subject matter, not a stated journal rule, so it is PRACTICE ONLY.

### Statistical Reporting
RELAXATION. FIELD_SKILL's expectation of quantitative quantitative claims ("increased employment by 4 percentage points") does not apply. Results are reported as formal theoretical properties (consistency, rates of convergence, asymptotic normality, "the method is proper if and only if...") rather than estimated magnitudes with economic interpretation. Empirical/simulation sections, where present, illustrate theoretical claims rather than serving as the paper's primary contribution.

### Citation Density
Not assessable from abstracts alone; no delta documented.

### Structural Deviations
PRACTICE ONLY. Abstracts across the sample never use the ECON-style "gap in the literature / contribution" framing explicit in FIELD_SKILL's introduction template. Instead, abstracts move directly from problem statement to method to theoretical property to (optional) illustrative application — literature positioning, where present, is condensed into a single relative clause rather than an explicit contribution list.

### Other Journal-Specific Patterns
PRACTICE ONLY. Several sampled papers are explicitly framed as extending or generalizing a named prior estimator or classical result (e.g., "reduces to the conditional Kaplan–Meier estimator in the special case," "extends... to matrix/tensor-valued data," "reduces to the classical spatial depth in a Euclidean space"). This "generalizes/nests known special case" framing recurs often enough across the sample to note as a common rhetorical move, though it is not stated in any guideline and is PRACTICE ONLY, not enforced.

---

## Dimensions With No Delta
- Citation format (author-year): FIELD DEFAULT (unconfirmed but no evidence of deviation)
- Paraphrase vs. direct quotation: FIELD DEFAULT
- Use of "we" as default voice: FIELD DEFAULT

---

## Common Pitfalls
- Do not import FIELD_SKILL's empirical-economics introduction template (motivating hook, gap framing, quantitative preview of results, enumerated contributions) wholesale — this journal's abstracts and introductions read as statistics-theory papers, opening with the technical problem rather than a real-world motivating fact.
- Do not report results in ECON-style economic-magnitude language; report them as formal statistical properties (consistency, asymptotic normality, efficiency, properness of an index) with simulation/application as secondary illustration.
- Do not assume a fixed empirical-paper section order (Data, Empirical Strategy, Results, Robustness) — organize instead around problem setup, method/estimator construction, theoretical properties, and (optional) numerical illustration.

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
| https://onlinelibrary.wiley.com/page/journal/14679469/homepage/forauthors.html | Guidelines | WebFetch returned HTTP 402 (paywalled); partial content recovered via WebSearch snippets only |
| https://en.wikipedia.org/wiki/Scandinavian_Journal_of_Statistics | Journal profile | WebFetch, full text |
| sjos.12774 (Bladt & Furrer) | Abstract | WebSearch snippet + arXiv 2303.02119 |
| sjos.12785 (Wang) | Abstract | WebSearch snippet |
| sjos.70003 (Ebner et al.) | Abstract | WebSearch snippet + arXiv 2305.19031 |
| sjos.12792 (Gardes & Podgorny) | Abstract | WebSearch snippet + HAL preprint |
| sjos.70005 (Mazzonetto et al.) | Title only | WebSearch listing |
| sjos.12778 (Kurisu, Ishihara & Sugasawa) | Abstract | WebSearch snippet + arXiv 2108.11551 |
| sjos.70001 (Ziersen & Martinussen) | Abstract | WebSearch snippet + arXiv 2412.11790 |
| sjos.70012 (Zhang et al.) | Abstract | WebSearch snippet + arXiv 2501.13599 |
| sjos.70054 (Virta) | Abstract | WebSearch snippet + arXiv 2306.09740 |
| sjos.70027 (Ameijeiras-Alonso & Gijbels) | Abstract | WebSearch snippet |
| sjos.70021 (Virta) | Abstract | WebSearch snippet |
| sjos.70006 (Helland) | Abstract | WebSearch snippet + arXiv 2412.19186 |
| Extended generalized Marshall-Olkin model for dependent censoring | Abstract (partial) | WebSearch snippet + HAL preprint |
| sjos.70000 (Gandy & Matcham) | Abstract | WebSearch snippet + arXiv 2208.03213 |
| IDEAS/RePEc journal listing (ideas.repec.org/s/bla/scjsta.html) | Table of contents | WebFetch, full text |
