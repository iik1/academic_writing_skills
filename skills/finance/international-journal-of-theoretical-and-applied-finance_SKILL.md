---
name: international-journal-of-theoretical-and-applied-finance-writing-style
description: >
  Journal-specific writing conventions for International Journal of Theoretical and Applied Finance
  (ABS 2, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for International Journal of Theoretical and Applied Finance",
  "submit to International Journal of Theoretical and Applied Finance", "match International Journal of Theoretical and Applied Finance style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: International Journal of Theoretical and Applied Finance

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** FINANCE
- **Publisher:** World Scientific Publishing Co. Pte. Ltd. (Singapore)
- **Scope:** Mathematical and quantitative finance — derivative pricing, stochastic volatility, option pricing models, portfolio optimization, credit and funding risk (xVA), market microstructure, and increasingly climate/carbon finance. Editor-in-Chief L. P. Hughston. This is a quant/applied-math finance journal, not an empirical corporate finance or asset pricing journal.
- **Guidelines URL:** https://www.worldscientific.com/page/ijtaf/submission-guidelines (returned 403 on direct fetch; content triangulated via search-engine snippets and World Scientific's shared house style pages)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 12 (2017-2024): "Kelly Trading and Market Equilibrium" (2023); "Rough-Heston Local-Volatility Model" (2023); "Vix Versus Vxx: A Joint Analytical Framework" (2020); "Statistics of Vix Futures and Applications to Trading Volatility Exchange-Traded Products" (2019); "Approximation Methods for Inhomogeneous Geometric Brownian Motion" (2019); "Pricing Index Options by Static Hedging Under Finite Liquidity" (2018); "Derivative Pricing with Collateralization and FX Market Dislocations" (2017); "The Financial Impact of Carbon Emissions on Power Utilities Under Climate Scenarios" (2024); "Efficient Wrong-Way Risk Modeling for Funding Valuation Adjustments" (2024); "Netting and Novation in Repo Networks" (2024); "A Greedy Algorithm for Habit Formation Under Multiplicative Utility" (2024); "Parasian Over Parisian, How Much Earlier Should One Exercise?" (2024). All accessed via IDEAS/RePEc abstract pages (full text paywalled).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Not separately specified beyond standard World Scientific journal norms; no explicit required-section list found on the public guidelines page.

### Length
No explicit word/page limit found on the public guidelines page. No page charges.

### Abstract
World Scientific's shared house style (applied across its journals including IJTAF) calls for an abstract "summarizing the context, content, and conclusions of the paper" in under ~200 words, single paragraph, unstructured. This is shorter than the FIELD_SKILL norm of 150-250 words only at the margin — treat as GUIDELINE ONLY since it was confirmed via the shared WSPC style page rather than the IJTAF page itself.

### Citations
Manuscripts prepared in LaTeX are preferred and strongly encouraged; WSPC-provided style/class files are recommended. No journal-specific citation format details found beyond this (WSPC house numbering/author-date conventions vary by journal and were not independently confirmed for IJTAF).

### Headings
No IJTAF-specific heading conventions found beyond standard numbered sections.

### Tables and Figures
No IJTAF-specific rules found.

### Explicit Prohibitions
Submission implies the paper is not published or under consideration elsewhere (standard exclusivity clause). No other explicit prohibitions found.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Articles are written in a technical, mathematics-paper register rather than the empirical-economics register FIELD_SKILL describes. Prose is dense with formal derivation language ("we develop," "we establish," "the resulting equilibrium is characterized as...") rather than empirical claim language ("we find," "we document"). PRACTICE ONLY — consistent across the sample, but not a stated journal rule; it reflects the journal's mathematical-finance scope rather than an editorial register requirement.

### Statistical Reporting
Essentially inapplicable to most articles: no regression tables, no standard errors, no significance stars, no economic-magnitude discussion in the FIELD_SKILL sense. Where empirical calibration appears (e.g., historical VIX data, Eskom case study), results are reported as model fit/calibration accuracy and numerical examples rather than as estimated coefficients with inferential statistics. PRACTICE ONLY — the field baseline's entire "Results and Reporting Norms" and most of "Methods Conventions" (identification strategy, robustness batteries, clustering) do not apply to the bulk of this journal's papers, which are theoretical/computational rather than reduced-form empirical.

### Citation Density
JEL classification codes are frequently absent (present in only 1 of 12 sampled abstracts). Keyword lists lean toward mathematical/technical terms (e.g., "Fourier sine transform," "Gaussian approximation," "rehypothecation") rather than economics subfield terms. PRACTICE ONLY.

### Structural Deviations
No standalone "Data" section pattern observed in sampled abstracts — consistent with the journal's theoretical/computational-finance orientation rather than an explicit journal rule. FIELD DEFAULT does not fully apply here since so many papers have no empirical data section at all; this is scope-driven rather than a formatting instruction, so treat as PRACTICE ONLY / low confidence given abstract-only access.

### Other Journal-Specific Patterns
Papers frequently pair applied/practitioner-adjacent topics (funding valuation adjustments, repo networks, carbon risk hedging) with heavy technical machinery (PDEs, stochastic processes, Monte Carlo, convex optimization), suggesting the journal favors technically rigorous treatments of both classical and emerging (climate/carbon) finance topics. PRACTICE ONLY, based on title/abstract sample only — full text was not accessible to confirm depth of technical exposition.

---

## Dimensions With No Delta
- Overall confidence calibration and hedging vocabulary in abstracts: FIELD DEFAULT (moderate hedging, e.g., "the model demonstrates flexibility," "reveals challenging financial trajectories")
- Author-year style citation convention where visible: FIELD DEFAULT (no evidence of numbered-citation deviation)
- Conclusion/contribution framing in visible abstract text: FIELD DEFAULT (abstracts state contributions directly, consistent with field norm)

---

## Common Pitfalls
- Do not submit a paper written as a reduced-form empirical finance paper (regression tables, identification strategy, robustness section) expecting it to fit journal norms — the great majority of published IJTAF papers are theoretical/computational (pricing models, PDEs, stochastic calculus, algorithms), not panel-data empirical work.
- Do not assume JEL codes are required — most sampled abstracts omit them entirely.
- Access to the journal's own guidelines page was blocked (403) during this review; treat abstract-length and citation-format specifics as provisional pending direct access to the WSPC guidelines page.

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
| https://www.worldscientific.com/page/ijtaf/submission-guidelines | Guidelines | Blocked (403); content triangulated via WebSearch snippet extraction |
| WSPC shared LaTeX/abstract style guidance (e.g., worldscientific.com/page/us/stylefiles-readme-2e) | Guidelines (house style, not IJTAF-specific) | WebSearch snippet |
| ideas.repec.org/a/wsi/ijtafx/v26y2023i01ns0219024923500012.html (Kelly Trading and Market Equilibrium) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v26y2023i06n07ns0219024923500218.html (Rough-Heston Local-Volatility Model) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v23y2020i05ns0219024920500338.html (Vix Versus Vxx) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v22y2019i01ns0219024918500619.html (Statistics of Vix Futures) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v22y2019i02ns0219024918500553.html (Approximation Methods for IGBM) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v21y2018i06ns0219024918500449.html (Pricing Index Options by Static Hedging) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v20y2017i06ns0219024917500406.html (Derivative Pricing with Collateralization) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v27y2024i01ns0219024924500134.html (Financial Impact of Carbon Emissions) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v27y2024i02ns0219024924500109.html (Efficient Wrong-Way Risk Modeling) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v27y2024i03n04ns0219024924500171.html (Netting and Novation in Repo Networks) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v27y2024i03n04ns0219024923500279.html (Greedy Algorithm for Habit Formation) | Abstract | WebFetch |
| ideas.repec.org/a/wsi/ijtafx/v27y2024i05n06ns0219024924500225.html (Parasian Over Parisian) | Abstract | WebFetch |
