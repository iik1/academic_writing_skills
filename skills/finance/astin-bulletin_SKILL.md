---
name: astin-bulletin-writing-style
description: >
  Journal-specific writing conventions for ASTIN Bulletin
  (ABS 2, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for ASTIN Bulletin",
  "submit to ASTIN Bulletin", "match ASTIN Bulletin style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: ASTIN Bulletin

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** FINANCE
- **Publisher:** Cambridge University Press, on behalf of the International Actuarial Association (IAA)
- **Scope:** Actuarial science and insurance mathematics; publishes quantitative/scientific papers drawing on mathematical sciences, statistics, probability, financial mathematics, and econometrics. Founded 1958; three issues/year (Jan, May, Sep), ~30 articles/year.
- **Guidelines URL:** https://www.cambridge.org/core/journals/astin-bulletin-journal-of-the-iaa/information/instructions-contributors (and linked "Preparing your materials" subpage)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 13 (12 FirstView abstracts from 2026 issues + 1 full-text open-access article: Landriault, Liu & Shi, "Worst-case reinsurance strategy with likelihood ratio uncertainty," Astin Bulletin 55, 2025, pp. 492-513)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Title, author name(s), abstract, and keyword list must appear on the first page. No other required section list is mandated (unlike FIELD_SKILL's near-universal empirical-finance skeleton of Data / Empirical Analysis / Robustness). Papers are typically organized as Introduction, Preliminaries/Model setup, one or more technical sections presenting results, Conclusion, References, and often a mathematical Appendix containing proofs.

### Length
No hard word limit stated, but papers exceeding ~30 pages are discouraged; authors are advised to split longer contributions into shorter papers.

### Abstract
Single paragraph, no explicit word limit specified. Keywords list required, no explicit count limit (observed articles use 4-6 keywords).

### Citations
Author-year format (matches FIELD_SKILL), but with specific formatting requirements: references arranged alphabetically and chronologically by author; journal citations require author(s), year, title, journal name in italics, volume in boldface, and pages; book citations require author(s), year, title in italics, publisher, and city.

### Headings
No explicit hierarchy mandated; guidelines direct authors to check recent issues for style consistency.

### Tables and Figures
Must be cited in text, numbered consecutively in Arabic numerals, captions required in all cases. Color figures permitted online only; print color requires author payment.

### Explicit Prohibitions
- No simultaneous submission to other journals.
- Footnotes should be avoided.
- AI tools cannot be listed as authors.
- Authors, not editors/referees/publisher, are responsible for English-language quality prior to submission.

### Data/Code and Other
Single-blind review (author identity known to reviewers, not vice versa). Authors are encouraged (not required at submission, but expected for accepted papers) to provide data and code to allow replication; R or Python preferred. From 31 July 2026, all accepted articles will be open access under a Creative Commons license.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
ENFORCED/PRACTICE ONLY (major delta). FIELD_SKILL's structure (Data section, Empirical Analysis with regression tables, standalone Robustness section) does not apply. ASTIN Bulletin papers are predominantly theoretical/mathematical: sections are organized around model setup ("Preliminaries"), formal results (definitions, propositions, lemmas, theorems with proofs), and illustrative numerical examples — not empirical hypothesis testing. Proofs are typically deferred to a formal Appendix, separate from the main text. This is a fundamentally different paper architecture than the FIELD_SKILL empirical-finance template; it resembles applied mathematics/operations research writing, not empirical asset pricing or corporate finance writing. Numbered equations, formal Definition/Lemma/Proposition/Theorem/Corollary/Remark/Example environments with explicit "Proof." blocks are the norm, not the exception.

### Voice and Register
PRACTICE ONLY (relaxation from FIELD_SKILL's empirical register). First-person plural "we" is used, consistent with FIELD_SKILL, but is applied to mathematical derivation and problem construction ("we establish," "we characterize," "we propose") rather than empirical claims ("we find," "we document"). No discussion of statistical significance, effect sizes, or economic magnitude in the FIELD_SKILL sense — findings are stated as mathematical results (equalities, inequalities, closed-form solutions) rather than estimated coefficients.

### Statistical Reporting
FIELD_SKILL norm does not apply (RELAXATION). There is no regression-table reporting, no standard-error clustering discussion, no statistical/economic significance distinction. Numerical illustrations (e.g., parameterized examples with specific distributional assumptions) are used instead, typically presented as one or two supporting figures rather than tables of regression coefficients.

### Citation Density
FIELD DEFAULT with formatting relaxation. Citation density in the introduction is high, similar to FIELD_SKILL, with dense positioning against prior theoretical/methodological literature. However, ASTIN Bulletin's required reference format (boldface volume numbers, italicized journal/book titles) is a Cambridge-house-style detail not covered by FIELD_SKILL.

### Other Journal-Specific Patterns
PRACTICE ONLY. Contribution statements in the introduction are common (e.g., "contributions of our results are four-fold") and numbered, similar to FIELD_SKILL's expectation — this is a FIELD DEFAULT that holds even in the mathematical-finance register. Papers commonly close the introduction with both a literature contextualization and an explicit section-by-section roadmap, matching FIELD_SKILL.

---

## Dimensions With No Delta
- Author-year citation basic format: FIELD DEFAULT
- Contribution statement style (numbered, assertive): FIELD DEFAULT
- Introduction roadmap closing: FIELD DEFAULT
- Person (first-person plural "we"): FIELD DEFAULT
- Direct quotation avoidance (paraphrase and cite): FIELD DEFAULT
- Framing of disagreement with prior work as extension, not refutation: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a paper structured like an empirical asset-pricing paper (Data, Results, Robustness sections with regression tables) will misalign with the journal's dominant mathematical/theoretical article type; most published papers use Definition/Theorem/Proof architecture instead.
- Embedding proofs in the main text rather than an appendix is inconsistent with common practice in sampled articles (proofs are typically deferred to Appendix A).
- Using footnotes for substantive asides is discouraged by the guidelines; incorporate such content into the main text instead.
- Omitting boldface volume numbers or italicized journal/book titles in the reference list deviates from the journal's specific Cambridge house style.

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
| https://www.cambridge.org/core/journals/astin-bulletin-journal-of-the-iaa/information/instructions-contributors | Guidelines | WebFetch |
| https://www.cambridge.org/core/journals/astin-bulletin-journal-of-the-iaa/information/author-instructions/preparing-your-materials | Guidelines (manuscript preparation detail) | WebFetch |
| Landriault, Liu & Shi, "Worst-case reinsurance strategy with likelihood ratio uncertainty," Astin Bulletin 55 (2025), 492-513, doi:10.1017/asb.2025.1 | Full-text (open access PDF) | WebFetch |
| Oh, Jeong, Kim & Jung, "Matrix-based factor analysis on the prediction of insurance claims probability" (2026) | Abstract (FirstView) | WebFetch |
| Miao, Li & Chen, "Gradient boosted multi-population mortality modeling with high-frequency data" (2026) | Abstract (FirstView) | WebFetch |
| Andraos, Ghossoub, Li & Shi, "Stackelberg equilibria in monopoly insurance markets with probability weighting" (2026) | Abstract (FirstView) | WebFetch |
| Wang, Hanewald, Shao & Bateman, "A two-generation model with altruism for reverse mortgage demand" (2026) | Abstract (FirstView) | WebFetch |
| Avanzi, Li, Taylor & Wong, "Dynamic Financial Analysis (DFA) of general insurers under climate change" (2026) | Abstract (FirstView) | WebFetch |
| Rusyda, Shi & Shang, "A hierarchical copula-based sparse VECM for cause-of-death mortality rates" (2026) | Abstract (FirstView) | WebFetch |
| Müller, Albrecher & Bladt, "Regularized matrix exponential distributions and lapse modeling" (2026) | Abstract (FirstView) | WebFetch |
| Alonso-García, Thirurajah & Ziveyi, "A two-account pricing framework for hybrid variable annuity contracts" (2026) | Abstract (FirstView) | WebFetch |
| Albrecher, Lindskog & Zumbach, "Cost-of-capital valuation with risky assets" (2026) | Abstract (FirstView) | WebFetch |
| Peng, Rong, Tao & Zhao, "Excess of age transfer policy for life annuities under longevity risk" (2026) | Abstract (FirstView) | WebFetch |
| Maggistro, Marino & Olivieri, "A Markov ageing-based multi-state group self-annuitisation" (2026) | Abstract (FirstView) | WebFetch |
| Wen & Liu, "A new credibility estimation of process variance with applications" (2026) | Abstract (FirstView) | WebFetch |
| Biessy, "Whittaker-Henderson Smoothing" (2025) | Abstract (search snippet) | WebSearch |
