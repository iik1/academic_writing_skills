---
name: annals-of-actuarial-science-writing-style
description: >
  Journal-specific writing conventions for Annals of Actuarial Science
  (ABS 1, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Annals of Actuarial Science",
  "submit to Annals of Actuarial Science", "match Annals of Actuarial Science style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Annals of Actuarial Science

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** FINANCE
- **Publisher:** Cambridge University Press (on behalf of the Institute and Faculty of Actuaries)
- **Scope:** Publishes rigorous research across actuarial science and related fields (life/non-life insurance, pensions, health insurance, finance and investment, quantitative risk management), plus contiguous non-traditional areas (machine learning/AI, computational finance, climate science, cyber/operational risk, actuarial software) provided relevance to insurance/actuarial practice is clearly demonstrated.
- **Guidelines URL:** https://www.cambridge.org/core/journals/annals-of-actuarial-science/information/author-instructions/preparing-your-materials
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 12 (titles/abstracts only, via FirstView listing and search-engine snippets; full text was not accessible without institutional access). Sample: "Mortality modeling for short-term climate stress test in France" (Raynal & Loisel); "Quantifying and pricing crop yield risk under climate change" (Zhang et al.); "Arbitrage-free catastrophe reinsurance valuation for compound dynamic contagion claims" (Jang et al.); "The Three-step method in a dynamic setting" (Belhouari et al.); "Bi-level optimization of security investment and insurance pricing" (Zhang et al.); "Earthquake solvency capital requirements' re-assessment" (Bairakdar et al.); "Analyzing pension fund mortality with Gaussian processes" (de Melo et al.); "No-arbitrage valuation and Solvency Capital Requirement for equity-linked contracts" (Clemente et al.); "State-space dynamic functional regression for multicurve fixed income spread analysis" (He et al.); "Intergenerational cross-subsidies in UK collective defined contribution funds" (Armstrong et al.); "On technological and analytical innovations in insurance research" (review article, Fang et al.); "GEMAct: a Python package for non-life (re)insurance modeling" (Pittarello et al., 2024).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Required manuscript order: Title; Author name(s); Abstract; Keywords; Correspondence details; Main text; Acknowledgements; Competing Interest Statement; Data Availability Statement; Funding Statement; References; Appendices. Accepted article types: original research papers, review papers, and actuarial software papers (a category not typical of mainstream finance journals — software papers describe a tool's design, implementation, and relevance to actuarial practice rather than an empirical/theoretical contribution).

### Length
Maximum 35 pages total. Excess material (e.g., extended appendices) should be submitted as supplementary material rather than included in the main manuscript — this is a firmer numeric cap than typical ABS 4*/4 finance journals, consistent with the ABS 1 tier.

### Abstract
150–200 words, single paragraph, placed after author names and before keywords (structurally identical position to FIELD_SKILL, but with a narrower, explicit word band vs. FIELD_SKILL's looser 150–250).

### Citations
Harvard (author-year) referencing system, explicitly named as such in the guidelines. Functionally consistent with FIELD_SKILL's author-year parenthetical norm; no departure in practice.

### Headings
No explicit heading rules given; authors are directed to consult published articles for house style. No delta observed in practice beyond FIELD_SKILL's Arabic-numeral norm.

### Tables and Figures
Tables and figures (including diagrams, graphs, maps, boxes, and code snippets) must be cited in text, numbered consecutively in Arabic numerals, and captioned. Accessibility (alt-text) descriptions are explicitly required for all figures and tables — a formatting requirement not mentioned in FIELD_SKILL.

### Explicit Prohibitions
- Simultaneous submission to other publications is prohibited.
- AI tools cannot be listed as authors.
- Prior publication must be disclosed; preprints do not count as prior publication.
- Manuscripts must be written in UK English (not US English), and writing "should be clear and concise," with the introduction expected to let readers grasp aims, conclusions, literature fit, and practical relevance.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm, with one addition: articles more consistently foreground practical/industry relevance (regulatory, solvency, pricing, or risk-management implications) in the abstract itself, reflecting the journal's explicit scope requirement that contributions demonstrate clear relevance to actuarial/insurance practice. This is a PRACTICE-level emphasis tied directly to the stated scope, not a new voice register.

### Statistical Reporting
Follows FIELD_SKILL norm — insufficient full-text access to confirm any delta; abstracts show standard quantitative framing (e.g., magnitude comparisons against regulatory benchmarks) consistent with the field baseline's expectation of economic-significance reporting.

### Citation Density
Follows FIELD_SKILL norm.

### Structural Deviations
Actuarial software papers (a distinct accepted article type) are PRACTICE + GUIDELINE: the journal's scope page and sampled software papers (e.g., GEMAct) indicate this category follows a distinct implicit structure emphasizing the real-world problem addressed, implementation details, and practical/actuarial relevance rather than the standard empirical-paper structure (data, identification, results) in FIELD_SKILL. This applies only when writing a software paper for this journal.

### Other Journal-Specific Patterns
None observed beyond the above; sample size and depth (abstracts only) limit further granularity — see Sources and limitations note.

---

## Dimensions With No Delta
- Overall article structure (Introduction/Data/Results/Conclusion core): FIELD DEFAULT
- Person and active voice: FIELD DEFAULT
- Citation format (author-year): FIELD DEFAULT
- Hedging conventions: FIELD DEFAULT
- Introduction rhetorical moves (gap, contribution list, roadmap): FIELD DEFAULT
- Robustness and methods transparency: FIELD DEFAULT

---

## Common Pitfalls
- Exceeding the 35-page cap by embedding extensive appendices in the main manuscript instead of submitting them as supplementary material.
- Writing in US English rather than the required UK English.
- Abstract outside the 150–200 word band (narrower than the general FIELD_SKILL range).
- For software submissions: presenting the paper as a standard empirical study rather than clearly motivating the real-world actuarial problem the software solves.

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
| https://www.cambridge.org/core/journals/annals-of-actuarial-science/information/author-instructions/preparing-your-materials | Guidelines | WebFetch, full page rendered |
| https://www.cambridge.org/core/journals/annals-of-actuarial-science/information/author-instructions | Guidelines (overview) | WebFetch |
| https://www.cambridge.org/core/journals/annals-of-actuarial-science/firstview | Article listing (12 titles/abstracts) | WebFetch |
| GEMAct: a Python package for non-life (re)insurance modeling (Pittarello, Luini & Marchione, 2024, AAS 18(2)) | Abstract | WebSearch snippet |
| Remaining 11 sampled articles (FirstView, 2026) | Abstract/title only | WebFetch/WebSearch snippets; full text not accessible without institutional login |

**Limitation:** No full-text articles were accessible (no EZProxy/institutional access in this environment). All article-level observations are based on titles and abstracts only, which constrains confidence on structural/statistical-reporting deltas — these are marked accordingly above.
