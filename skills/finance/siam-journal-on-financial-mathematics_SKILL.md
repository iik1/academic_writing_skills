---
name: siam-journal-on-financial-mathematics-writing-style
description: >
  Journal-specific writing conventions for SIAM Journal on Financial Mathematics
  (ABS 2, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for SIAM Journal on Financial Mathematics",
  "submit to SIAM Journal on Financial Mathematics", "match SIAM Journal on Financial Mathematics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: SIAM Journal on Financial Mathematics

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** FINANCE
- **Publisher:** Society for Industrial and Applied Mathematics (SIAM)
- **Scope:** Publishes theoretical developments in financial mathematics and computational/algorithmic breakthroughs in implementing them. Serves mathematicians working on the mathematical theory of finance and practitioners doing rigorous scientific computation for applied financial mathematics (stochastic analysis, PDE/viscosity-solution methods, rough path theory, optimal execution, asset pricing theorems, calibration algorithms).
- **Guidelines URL:** https://epubs.siam.org/journal/sifin/instructions-for-authors (and https://epubs.siam.org/journal/sifin/editorial-policy)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 12 (abstracts/metadata; full text largely paywalled) — "Hedging with memory: shallow and deep learning with signatures" (arXiv 2508.02759); "Unbiased Rough Integrators and No Free Lunch in Rough-Path-Based Market Models" (arXiv 2509.14529); "On Robust Fundamental Theorems of Asset Pricing in Discrete Time" (SIFIN 15(3), 571–600); "Malliavin calculus for signatures with applications to finance" (arXiv 2604.22528); "Model-Free Analysis of Dynamic Trading Strategies" (SIFIN 16(2), 643–666, DOI 10.1137/23M1581881); "Signature volatility models: Pricing and hedging with Fourier" (SIFIN 16(2), 606–642); "Optimal Execution under Liquidity Uncertainty" (arXiv 2506.11813); "Signature-based models: Theory and calibration" (SIFIN 14, 910–957); "Deep curve-dependent PDEs for affine rough volatility" (SIFIN 14(2), 353–382); "Weak error rates of numerical schemes for rough volatility" (SIFIN 14(2), 475–496); "Joint SPX-VIX calibration with Gaussian polynomial volatility models" (arXiv 2212.08297, published in SIFIN); "Decentralised Finance and Automated Market Making: Predictable Loss and Optimal Liquidity Provision" (arXiv 2309.08431, forthcoming SIFIN).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Manuscript + cover letter submitted as PDF via SIAM's Journal Submission & Tracking System. Article types: full-length research articles, Short Communications (max 10–12 pages, fast review), and Erratum. No prescribed section list comparable to empirical-finance journals (no mandated "Data" or "Empirical Analysis" section) — structure follows mathematical-paper convention (Introduction, Model/Setup, Main Results/Theorems, Proofs, Numerical Examples, Conclusion), not the FIELD_SKILL empirical-paper template.

### Length
Short Communications: ≤10–12 pages. No stated page limit for full research articles. Running head (abbreviated title) must not exceed 50 characters including spaces.

### Abstract
One paragraph, **not exceeding 250 words** (vs. FIELD_SKILL's 150–250, so upper bound is explicit and binding). Must stand independently of the paper. Mathematical formulas and bibliographic references "should be kept to a minimum" in the abstract. Any reference used must be written out in full — not cited by number. No structured/labeled-field abstract; no separate JEL codes (this journal uses MSC — Mathematics Subject Classification — codes instead, e.g., 60H07, 91B70, 49L25).

### Citations
Guidelines permit reference lists ordered alphabetically OR by citation order (author's choice), with in-text citation styles including numeric-bracket forms: `[#, p. XX]` or `Author [#, p. XX]`, alongside the author-year form `Author (Year, p. XX)`. This is a mathematics-journal convention distinct from FIELD_SKILL's exclusively author-year parenthetical norm — numbered/bracketed citation is explicitly sanctioned here.

### Headings
Not explicitly specified in guidelines beyond standard sequential structure; no journal-specific heading vocabulary found.

### Tables and Figures
All illustrations must be professional quality, no handwritten elements (explicitly prohibited: hand-drawn artwork; SIAM will not redraw figures). Tables and algorithms are excluded from figure numbering (separate numbering streams). Figures/tables numbered consecutively and cited in text. Minimum line weight one point. Accepted formats: TeX, PDF, PNG, JPG, EPS. Color permitted at no extra cost. Figures must be embedded inline in the manuscript PDF at submission.

### Explicit Prohibitions
- The "Lena image" (a commonly used test image in image-processing literature) is explicitly banned.
- Simultaneous submission elsewhere is prohibited; significant self-duplication is prohibited.
- If a preliminary version appeared in conference proceedings, this must be disclosed in the cover letter and in a title-page footnote.
- Hand-drawn/handwritten figure elements prohibited.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Findings are stated as mathematically established (proven theorems, derived closed-form results), not as empirically "suggestive" patterns. Sampled abstracts use direct assertion — "We show," "We establish," "is shown to satisfy" — with essentially no hedging even for claims that in an empirical-finance paper would be softened (e.g., "is shown to satisfy Hamilton–Jacobi–Bellman variational inequalities," "uniqueness of the viscosity solution" stated flatly). This is a lower-hedging register than FIELD_SKILL's "low to moderate" baseline — appropriate because claims are proof-backed rather than statistically inferred. PRACTICE ONLY / consistent across sample.

### Statistical Reporting
FIELD_SKILL's regression-table and economic-significance conventions (coefficients, standard errors, t-stats, dollar/bp magnitude framing) do not apply to the modal SIFIN paper. Results are theorems, closed-form pricing formulas, or numerical-scheme error rates/convergence results, not estimated coefficients. Where numerical experiments appear, they report algorithmic performance (accuracy, convergence rate, computational cost — e.g., "orders of magnitude less training compute") rather than statistical significance or economic-magnitude translation. FIELD DEFAULT does not apply; this is a structural mismatch driven by the journal's theoretical/computational scope, not a stylistic choice. PRACTICE ONLY.

### Citation Density
Abstracts are told to minimize bibliographic references ("references should be kept to a minimum" — HARD_CONSTRAINT), sharper than FIELD_SKILL's general silence on abstract-level citation. Introductions still position the paper against prior literature, but density in the sampled abstracts is lower than typical empirical-finance abstracts.

### Structural Deviations
No universal "Data" section (most papers are not data-driven); no standalone "Robustness" section (mathematical papers do not test alternative specifications/samples in the empirical-finance sense — internal validation is via proof rigor or numerical convergence checks instead). MSC classification codes replace JEL codes as the field-tagging convention. RELAXATION of FIELD_SKILL's structural expectations, consistent with ABS 2 tier and the journal's mathematical rather than econometric orientation.

### Other Journal-Specific Patterns
Numbered/bracketed in-text citation (`[#, p. XX]`) is explicitly permitted per guidelines — a mathematics-community convention not seen in ABS 4/4* finance journals, which use author-year exclusively.

---

## Dimensions With No Delta
- Formality and technical density: FIELD DEFAULT (high technical density, no colloquialisms, consistent with FIELD_SKILL).
- Equation integration and notation-on-first-use: FIELD DEFAULT.
- Conclusion brevity and closing-moves pattern (restate finding, implications, limitations, future work): FIELD DEFAULT where a conclusion section is present.
- Framing of disagreement with prior literature (non-adversarial, credit-then-extend): FIELD DEFAULT in sampled introductions.

---

## Common Pitfalls
- Treating this as an empirical-finance journal and forcing a Data/Empirical Analysis/Robustness section structure onto a theory or numerical-methods paper — SIFIN papers follow mathematical-paper structure (setup, theorem, proof, numerics), not the FIELD_SKILL empirical template.
- Exceeding the 250-word abstract cap or padding the abstract with citations/formulas, which guidelines explicitly discourage.
- Using author-year-only citation when the paper's reference list is numbered — check which convention was chosen and stay consistent, per guidelines' dual-format allowance.
- Submitting hand-drawn or non-vector figures; guidelines are explicit that SIAM will not redraw them.

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
| https://epubs.siam.org/journal/sifin/instructions-for-authors | Guidelines | WebFetch (full text retrieved) |
| https://epubs.siam.org/journal/sifin/editorial-policy | Guidelines | WebFetch (page not rendering guideline text; navigation shell only) |
| https://epubs.siam.org/journal/sifin/about | Scope | WebSearch snippet |
| arXiv 2508.02759 (Hedging with memory: shallow and deep learning with signatures) | Abstract | WebFetch |
| arXiv 2509.14529 (Unbiased Rough Integrators and No Free Lunch in Rough-Path-Based Market Models) | Abstract | WebFetch |
| SIFIN 15(3) 571-600, DOI 10.1137/23M156032X (On Robust Fundamental Theorems of Asset Pricing in Discrete Time) | Abstract | WebFetch via institutional repository page |
| arXiv 2604.22528 (Malliavin calculus for signatures with applications to finance) | Abstract | WebFetch |
| SIFIN 16(2) 643-666, DOI 10.1137/23M1581881 (Model-Free Analysis of Dynamic Trading Strategies) | Abstract | WebSearch snippet |
| SIFIN 16(2) 606-642 (Signature volatility models: Pricing and hedging with Fourier) | Metadata/abstract | WebSearch snippet |
| arXiv 2506.11813 (Optimal Execution under Liquidity Uncertainty) | Abstract | WebFetch |
| SIFIN 14, 910-957, DOI 10.1137/22M1512338 (Signature-based models: Theory and calibration) | Metadata | WebSearch snippet |
| SIFIN 14(2) 353-382 (Deep curve-dependent PDEs for affine rough volatility) | Metadata | WebSearch snippet |
| SIFIN 14(2) 475-496 (Weak error rates of numerical schemes for rough volatility) | Metadata | WebSearch snippet |
| arXiv 2212.08297 (Joint SPX-VIX calibration with Gaussian polynomial volatility models) | Abstract | WebSearch snippet |
| arXiv 2309.08431 (Decentralised Finance and Automated Market Making, forthcoming SIFIN) | Abstract | WebSearch snippet |

**Access limitation note:** SIAM's epubs.siam.org platform serves a JavaScript-rendered shell to unauthenticated fetches, so publisher table-of-contents and full-text pages could not be read directly; findings rely on the Instructions for Authors page (fully retrieved), WebSearch result snippets, arXiv preprint abstracts, and third-party metadata mirrors (dblp, institutional repositories). No full-text article bodies were read; observations on structure and voice are based on abstracts, MSC codes, and available metadata only.
