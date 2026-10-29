---
name: journal-of-the-royal-statistical-society-series-b-statistical-methodology-writing-style
description: >
  Journal-specific writing conventions for Journal of the Royal Statistical Society. Series B: Statistical Methodology
  (ABS 4, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of the Royal Statistical Society. Series B: Statistical Methodology",
  "submit to Journal of the Royal Statistical Society. Series B: Statistical Methodology", "match Journal of the Royal Statistical Society. Series B: Statistical Methodology style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of the Royal Statistical Society. Series B: Statistical Methodology

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** ECON
- **Publisher:** Oxford University Press (for the Royal Statistical Society)
- **Scope:** Statistical methodology and theory — new methods, their theoretical properties, and computational implementation, spanning Bayesian and frequentist inference, causal inference, high-dimensional statistics, and machine-learning-adjacent theory. Not an economics journal in subject matter; included here as an ABS-listed methodology outlet used by econometricians.
- **Guidelines URL:** https://academic.oup.com/jrsssb/pages/general-instructions ; https://rss.org.uk/RSS/media/File-library/Publications/RSS-journal-notes-for-authors-2025.pdf
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 8 (Conformalized Bayesian Inference, arXiv 2511.05746; "On the statistical analysis of grouped data..." Algeri & Khmaladze, doi 10.1093/jrsssb/qkag084; "Long-term causal inference under persistent confounding via data combination," JRSSB 87(2):362; discussion contribution to Whiteley et al. "Statistical exploration of the Manifold Hypothesis," JRSSB 88(2):418; "Efficient sampling for sparse Bayesian learning using hierarchical prior normalization," arXiv 2505.23753; "Normal approximations in nonparametric empirical Bayes," arXiv 2605.31599; plus advance-article title/abstract listings for Online Inference Under Over-Parameterized Models, Time Series Classification, HMC Sampling, Adaptive Experiment Inference, Causal Inference with Network Spillovers)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No single mandated section template; standard is Introduction, methodology/theory development, theoretical results, numerical/simulation studies, application, conclusion — a statistics-paper structure rather than the empirical-economics Data/Empirical Strategy/Results template in FIELD_SKILL. A distinct submission track exists for **Discussion Papers**: papers read before the Society at an Ordinary Meeting, published with formal written discussion contributions and an authors' reply, on a quarterly deadline cycle (1 Jan, 1 Apr, 1 Jul, 1 Oct). Discussion-paper submissions are capped at 16 pages.

### Length
Target under 30 journal pages; papers "much longer than about 35 pages" are discouraged and papers over 30 pages are "unlikely to be accepted." Abstract maximum 200 words. Discussion contributions (for Discussion Papers) are capped at 400 words (800 for invited discussants).

### Abstract
Unstructured, maximum 200 words, followed by five or six keywords listed alphabetically. Reference citations and abbreviations must not be used in the abstract.

### Citations
Authors may format references "in any readable style" at submission; the journal standardizes to Harvard/author-year style at production. Authors remain responsible for reference accuracy.

### Headings
Theorems, lemmas, propositions, and corollaries are numbered sequentially and individually by type (Theorem 1, Theorem 2, Proposition 1, ...), not nested under section numbers — a formal mathematical-writing convention beyond FIELD_SKILL's general numbering guidance.

### Tables and Figures
Tables placed at the end of the main text, numbered with Arabic numerals, no vertical rules between columns and no horizontal rules within the table body. Figures submitted as individual image files (not embedded in .doc/.docx) and not as .jpeg/.jpg; each figure requires a title, legend, and alt-text description for accessibility.

### Explicit Prohibitions
No data falsification, plagiarism, or duplicate publication. No supplementary data repositories used as a substitute for making data/code available — datasets and reproducible code must be publicly available with DOIs before acceptance (exceptions only in "very rare circumstances"). AI use must be disclosed both in the cover letter and in the Methods or Acknowledgements section. UK spelling required throughout (except in quotations and references). Manuscripts double-spaced, 12-point font, ~28 lines/page.

---

## Observed Deltas from FIELD_SKILL

### Statistical Reporting
Papers foreground theoretical guarantees (consistency, convergence rates, asymptotic properties, minimax bounds) ahead of or alongside empirical/simulation results; a "Numerical Studies" or "Simulation Studies" section functions the way FIELD_SKILL's empirical "Results" section does, but the paper's main contribution is typically the theoretical result itself rather than a substantive empirical finding. PRACTICE ONLY / FIELD DEFAULT for statistics venues — not a deviation FIELD_SKILL needs to encode further, since FIELD_SKILL's Methods conventions already anticipate theory-paper tense mixing.

### Structural Deviations
Genre split not present in FIELD_SKILL: a large share of Series B content is either (a) a standard methods paper (Introduction, Related Work, Setup, Identification/Theory, Estimation, Numerical Studies, Conclusion) or (b) a **Discussion Paper** package consisting of the main paper plus short (max 400-word) discussant contributions and an authors' reply, published together. Discussion contributions open with a congratulatory framing toward the authors ("We congratulate X for their insightful paper...") before raising a substantive extension or critique, and close on a constructive, forward-looking note rather than a critical one. This is ENFORCED (explicit submission track with its own deadlines and word limits) and confirmed in the sampled discussion contribution.

### Other Journal-Specific Patterns
Formal theorem/lemma/proposition numbering (see Headings above) is used more heavily and more formally than typical econometric theory papers under FIELD_SKILL, consistent with a statistics-journal readership. PRACTICE ONLY, but grounded in the explicit numbering instruction in the guidelines, so treat as ENFORCED for any paper containing formal results.

---

## Dimensions With No Delta
- Voice, person, and register: FIELD DEFAULT (first-person plural, active voice, formal but economical register)
- Introduction structure (motivation, question, approach, results preview, contribution, roadmap): FIELD DEFAULT
- Citation density by section and author-year in-text format: FIELD DEFAULT
- Hedging conventions for external validity and assumptions: FIELD DEFAULT
- Robustness/extensions as standard component: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a manuscript over 30 pages without checking the journal's stated page-length discouragement — trim or move material to an online appendix.
- Including references or abbreviations in the abstract, which the guidelines explicitly prohibit.
- Submitting figures embedded in Word or as .jpg/.jpeg files instead of individual accepted image formats.
- Treating "Discussion Paper" as a synonym for a regular submission — it is a distinct track with its own 16-page cap, quarterly deadlines, and requirement that the paper be suitable for oral presentation and open discussion at a Society meeting.

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
| https://academic.oup.com/jrsssb/pages/general-instructions | Guidelines | WebFetch, full text |
| https://rss.org.uk/RSS/media/File-library/Publications/RSS-journal-notes-for-authors-2025.pdf | Guidelines (PDF) | WebFetch, partial extraction |
| https://rss.org.uk/RSS/media/File-library/Publications/Discussion-Paper-Meeting-guidelines2025.pdf (via search snippet) | Guidelines | WebSearch snippet only |
| arXiv 2511.05746 (Conformalized Bayesian Inference) | Abstract | WebFetch |
| doi 10.1093/jrsssb/qkag084 (grouped-data goodness-of-fit) | Abstract + keywords | WebFetch |
| JRSSB 87(2):362 (long-term causal inference) | Abstract + structure | WebFetch |
| JRSSB 88(2):418 (discussion contribution to Whiteley et al.) | Full short text | WebFetch |
| arXiv 2505.23753 (sparse Bayesian learning) | Abstract/structure (partial, PDF binary) | WebFetch |
| arXiv 2605.31599 (empirical Bayes normal approximations) | Abstract/structure (partial, PDF binary) | WebFetch |
| Advance articles listing (Online Inference, Time Series Classification, HMC, Adaptive Experiment, Network Spillovers) | Title/summary only | WebFetch of advance-articles page |
