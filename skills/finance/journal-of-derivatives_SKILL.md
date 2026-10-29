---
name: journal-of-derivatives-writing-style
description: >
  Journal-specific writing conventions for Journal of Derivatives
  (ABS 2, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Derivatives",
  "submit to Journal of Derivatives", "match Journal of Derivatives style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Derivatives

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** FINANCE
- **Publisher:** Portfolio Management Research (Pageant Media / PMR), formerly Institutional Investor Journals
- **Scope:** Contingent claims theory and practice — derivative instruments and markets, risk management, asset price process models, and applications of derivatives concepts to insurance, corporate finance, and banking. Explicitly positioned at the interface between practitioners and academics.
- **Guidelines URL:** https://jod.pm-research.com/authors (current site); full content/submission guidelines PDF archived at https://pages.stern.nyu.edu/~sfiglews/documents/JOD_Submit%202017.pdf (Version of August 2017, still the operative statement per current site links)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 8 (abstract/front-matter level; full text paywalled). "Evaluation of Deep Learning Algorithms for Quadratic Hedging" (Dai, Li, Zhang, 2022); "Geometric Local Variance Gamma Model" (Carr & Itkin, 2019); "Currency Target Zones as Mirrored Options" (Lera, Leiss, Sornette, 2019); "Universal Arbitrage-Free Estimation of State Price Density" (Newton & Hu, 2021); "Interrelations among Cross-Currency Basis Swap Spreads" (2019); "Quantum Option Pricing and Quantum Finance" (2020); "The Premium Reduction of European, American, and Perpetual Log Return Options" (2021); "American Options in Time-Dependent One-Factor Models" (Pimbley, 2024).

**Access limitation note:** jod.pm-research.com blocks automated fetches (403/404 on direct page requests); all article-level evidence below comes from search-engine-cached abstract text and third-party mirrors (SSRN, ResearchGate, arXiv companion preprints), not full text. No full-text methods/results/discussion sections were read. This is a thinner evidence base than a full-text spot-check; findings below are correspondingly conservative and abstract-level only.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No fixed section template is mandated. The guidelines describe content scope, not manuscript structure. Most published articles follow standard finance-paper structure, but the journal explicitly also publishes non-standard formats: an "Innovations" section for expository articles on significant new developments, and separately, purely educational/expository pieces on technical subjects that are not original-research papers at all. When writing an Innovations-style or expository piece, standard empirical-paper structure (Data, Results, Robustness) does not apply.

### Length
Not specified in the guidelines. No explicit word or page limit found.

### Abstract
No structured/unstructured format specified in the guidelines. Observed abstracts are single-paragraph, unstructured, and description-of-method-and-result in style (see Voice and Register delta below).

### Citations
Not specified in the guidelines document itself. No deviation from field-standard author-year format observed in available front matter.

### Headings
Not specified.

### Tables and Figures
Guidelines state only: "Very small fonts and diagrams, and nonstandard notation are to be avoided" at initial submission, and that formatting details are not a concern at the review stage — the priority is that a referee can read and evaluate the manuscript easily.

### Explicit Prohibitions
None framed as prohibitions on content. The only explicit quality bar stated is on presentation: mathematics must be "expressed in as clear and simple a form as possible" and should be "separable to the maximum extent possible from the logical flow of the discussion, so that articles can be understood by the more casual reader who does not wish to follow the math step by step." This is a distinctive, explicitly stated journal norm — heavy math is welcome ("a relatively high level of mathematical analysis is acceptable where appropriate — derivatives are inherently mathematical") but must be isolable from the narrative argument (e.g., via boxed derivations, appendices, or clearly demarcated technical subsections) rather than woven inline in a way that blocks a non-technical reader from following the paper's logic.

Guidelines also explicitly state tolerance for imperfect English/typos at initial submission ("we are relatively tolerant of typos, and language mistakes by non-native English speakers"), though they warn that excessive errors create a bad impression on referees and recommend professional copyediting if English is weak.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
GUIDELINE + PRACTICE: The journal explicitly targets "a broad audience of sophisticated practitioners and academics" and requires a "clear and accessible style," a dual-audience framing not present in FIELD_SKILL (which assumes an academic-only readership). Consistent with this, sampled abstracts read as plain technical descriptions of what a method does and produces ("the authors develop...", "this paper describes...") rather than the contribution-forward, rhetorically framed abstracts typical of ABS 4/4* empirical papers. Abstracts are matter-of-fact summaries of the model or method and its results, with little of the significance-framing or gap-identification rhetoric FIELD_SKILL describes for introductions. This is consistent with a journal whose core genre is methodological/quantitative (pricing models, hedging algorithms) rather than empirical hypothesis-testing, so the standard "contribution paragraph" convention is less prominent in the sample.

### Structural Deviations
GUIDELINE: The "Innovations" section and stand-alone expository/educational articles are a journal-specific structural feature absent from FIELD_SKILL, which assumes a single canonical empirical-paper template. Authors targeting this outlet should consider whether their piece is (a) an original-research paper following standard structure, or (b) an expository/pedagogical piece, which follows a looser format built around explaining a technique or development rather than testing a hypothesis.

### Other Journal-Specific Patterns
ENFORCED: Math-narrative separation is a stated, distinctive requirement — more explicit and stronger than the general FIELD_SKILL norm that "equations are integrated into prose with proper grammatical introduction." At JOD, authors are expected to actively isolate heavy derivations from the main argument so a non-mathematical reader can still follow the paper's logic and conclusions.

RELAXATION (ABS 2 tier): Formatting is explicitly not scrutinized at initial review ("we are not concerned with formatting details at the initial review stage"), and typographical/language imperfections are explicitly tolerated more than the polish FIELD_SKILL implies is expected at the ABS 4*/4 level. This is a genuine relaxation, not a new norm — final published versions still undergo copyediting.

---

## Dimensions With No Delta
- Citation format (author-year): FIELD DEFAULT
- Statistical/economic significance reporting norms: FIELD DEFAULT (where applicable; many JOD articles are methodological/theoretical rather than hypothesis-testing empirical work, so this dimension applies less often)
- Hedging and epistemic caution conventions: FIELD DEFAULT
- Conclusion structure: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a paper where mathematics is embedded inline throughout the argument rather than separable (e.g., in an appendix or clearly bounded technical subsection) — this is a named journal priority, not a generic finance-journal expectation.
- Writing only for an academic audience: JOD explicitly wants papers legible to sophisticated practitioners as well, so unexplained jargon or purely academic framing in the introduction is a worse fit here than at a typical ABS 4 empirical-finance journal.
- Treating an expository/technique-explainer submission as if it needs the full empirical-paper apparatus (Data section, robustness battery, hypothesis tests) — the "Innovations" and educational-article formats do not require this.

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
| https://jod.pm-research.com/authors | Guidelines (current landing page) | WebSearch snippet (direct fetch returned 404/403) |
| https://pages.stern.nyu.edu/~sfiglews/documents/JOD_Submit%202017.pdf | Guidelines (full content/submission PDF, Aug 2017) | Full text read via PDF fetch |
| jod.pm-research.com/content/early/2022/07/07/jod.2022.1.165 (Dai, Li, Zhang 2022) | Abstract | WebSearch snippet / SSRN cross-listing |
| jod.pm-research.com/content/27/2/7.abstract (Carr & Itkin 2019) | Abstract | WebSearch snippet / arXiv preprint cross-listing |
| jod.pm-research.com/content/26/3/53.abstract (Lera, Leiss, Sornette 2019) | Abstract | WebSearch snippet / SSRN cross-listing |
| jod.pm-research.com/content/early/2020/11/21/jod.2020.1.123.abstract (Newton & Hu 2021) | Abstract | WebSearch snippet / ResearchGate/Bath research portal |
| jod.pm-research.com/content/early/2019/04/04/jod.2019.1.073.abstract (Cross-currency basis swap spreads, 2019) | Abstract | WebSearch snippet |
| jod.pm-research.com/content/28/1/79.abstract (Quantum Option Pricing and Quantum Finance, 2020) | Title/topic only | WebSearch (abstract not retrievable) |
| jod.pm-research.com/content/28/4/7.abstract (Log Return Options, 2021) | Title/topic only | WebSearch snippet |
| Pimbley, "American Options in Time-Dependent One-Factor Models" (Spring 2024) | Title only | WebSearch snippet |
