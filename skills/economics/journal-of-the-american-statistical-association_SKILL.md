---
name: journal-of-the-american-statistical-association-writing-style
description: >
  Journal-specific writing conventions for Journal of the American Statistical Association
  (ABS 4, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of the American Statistical Association",
  "submit to Journal of the American Statistical Association", "match Journal of the American Statistical Association style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of the American Statistical Association

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** ECON (cross-listed as a statistics/methodology journal; NHH ABS list treats it as ECON)
- **Publisher:** Taylor & Francis, on behalf of the American Statistical Association (ASA)
- **Scope:** Publishes original research in statistical theory and methods, and in the application of statistics to substantive problems across the sciences, business, and government. Organized into three sections: Theory and Methods, Applications and Case Studies, and Review (occasional).
- **Guidelines URL:** ASA Style Guide (https://files.taylorandfrancis.com/asa-style-guide.pdf); JASA Reproducibility Guide (https://jasa-acs.github.io/repro-guide/pages/author-guidelines.html)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 10 (Kock & Preinerstorfer, "Enhanced Power Enhancements for Testing Many Moment Equalities," DOI 10.1080/01621459.2025.2591282; Chernozhukov & Newey et al., "Adversarial Estimation of Riesz Representers," DOI 10.1080/01621459.2025.2588833; Schirripa Spagnolo et al., "Bias Control for M-Quantile-Based Small Area Estimators," DOI 10.1080/01621459.2025.2587316; Tian, Sun & He, "Efficient Analysis of Latent Spaces in Heterogeneous Networks," DOI 10.1080/01621459.2025.2604316; "Checking the Cox Proportional Hazards Model with Interval-Censored Data," DOI 10.1080/01621459.2025.2520460; "Successive Classification Learning for Estimating Quantile Optimal Treatment Regimes," DOI 10.1080/01621459.2026.2664228; "Bi-SCORE for Weighted Bipartite Networks with Application in Knowledge Source Discovery" (arXiv 2508.21467, JASA-track); Zhan & Datta, "Neural Networks for Geospatial Data," JASA 120(549); Yu, Wang & Wang, "Distributed Heterogeneity Learning for Generalized Partially Linear Models," JASA 120(550); Yan & Luo, "Bayesian Integrative Region Segmentation in Spatially Resolved Transcriptomic Studies," JASA 119(547))

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Fixed manuscript order: Title Page; Author Footnote (in lieu of a separate Acknowledgments section); Abstract and Key Words; Article Text; Appendices; References; Tables; Figures with captions. JASA places acknowledgments (funding, colleague thanks) inside the Author Footnote rather than a standalone Acknowledgments section. A single appendix is headed "APPENDIX: [descriptive title]"; multiple appendices are "APPENDIX A," "APPENDIX B," etc., with sub-elements numbered A.1, A.2. ASA strongly encourages placing appendices as online supplements rather than in the main text.

### Length
No explicit page/word limit stated in the style guide beyond the abstract cap; length is governed by editorial discretion and typical practice (papers run to ASA two-column typeset format).

### Abstract
Hard 200-word limit, enforced by copyediting if exceeded. Must summarize results, topics discussed, and main conclusions. No displays, no complex mathematical notation, and no references permitted in the abstract — a stricter constraint than FIELD_SKILL, which places no notation restriction on abstracts. Followed by 3–6 key words/phrases not already in the title, singular form preferred, no acronyms or math symbols.

### Citations
Author-year, ASA-specific variant: direct citation "Gentleman (1978)"; indirect "(Smith 1980)"; page-specific citations use "sec.," "chap.," "p.," "pp." after the date, preceded by a comma. Two-author works always cited in full; three-to-five-author works spelled out on first mention only, then "et al."; six-or-more-author works use "et al." from first citation — more permissive toward "et al." than is typical in many econ outlets. Multiple works by the same author(s) cited together drop repeated names ("Tukey 1965, 1980"). Reference list requires ALL authors' names in full (never truncated to "et al." in the list itself).

### Headings
Numbered headings are mandatory (not optional as in FIELD_SKILL): main headings use Arabic numerals with a period, in full caps (e.g., "1. INTRODUCTION," "2. ANALYSIS OF DATA"). Subheadings use decimal Arabic numbering (1.1, 1.2), upper/lowercase, flush left, no underline; a minimum of two subheadings is required under any main heading that has subheadings at all. A third level, if needed, is an indented, italicized, run-in paragraph heading ending with a period.

### Tables and Figures
Tables and figures are placed at the end of the manuscript (after References), not embedded in text, for initial submission. Tables use no vertical rules; horizontal rules only at three points (below title, below column heads, closing the body). Numbers should be heavily rounded (rarely more than two effective digits). Figure captions must fully describe the display (what is graphed, then salient features) since figures are evaluated on caption clarity; abbreviations must be defined in the caption itself, not just in text.

### Explicit Prohibitions
Double-blind review is mandatory for JASA. Self-citations in the blinded manuscript must be phrased in third person ("as seen previously in Smith (2002)"), never first person ("as we showed in earlier work"). No author names, affiliations, acknowledgments, or identifying web links may appear anywhere in the blinded submission. Reproducibility: authors must submit an Author Contributions Checklist (ACC) and, for Applications and Case Studies submissions particularly, provide code/data suitable for reproduction (deposited to Figshare/Harvard Dataverse on acceptance); anonymized repositories are required pre-acceptance if code/data are shared with reviewers.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
No delta beyond mechanics already covered in Hard Constraints. Articles spot-checked use "we propose," "we develop," "we establish" consistent with FIELD_SKILL's first-person-plural norm. FIELD DEFAULT.

### Statistical Reporting
Structural, not rhetorical, delta: articles foreground theoretical guarantees (convergence rates, oracle error rates, consistency) before or alongside empirical illustration, more heavily weighted toward asymptotic/finite-sample theoretical statements than a typical FIELD_SKILL empirical paper. This reflects the journal's Theory and Methods orientation rather than a stated norm — PRACTICE ONLY, and applies mainly to Theory and Methods submissions; Applications and Case Studies papers are expected to foreground the substantive problem instead (per editorial policy on "what makes a great ACS paper" — a submission is commonly rejected for being miscategorized between the two sections).

### Structural Deviations
Every spot-checked article pairs a general methodological contribution with a single concrete real-data illustration late in the paper (e.g., ARIC study, journal citation networks, spatial transcriptomics) rather than a dedicated multi-section empirical Results arc — the application functions as a validating case study, not as the paper's primary contribution (except in the Applications and Case Studies section, where the reverse holds). PRACTICE ONLY / FIELD DEFAULT depending on section; not itself inconsistent with FIELD_SKILL's structure but the balance of "theory sections vs. empirical sections" skews further toward theory/methods than a typical ABS 4 economics paper.

### Other Journal-Specific Patterns
JASA runs three distinct submission tracks (Theory and Methods; Applications and Case Studies; occasional Review) with materially different expectations for what "results" should emphasize; authors are expected to self-select the correct track, and editorial guidance explicitly warns that miscategorization is a leading cause of desk rejection. This tripartite structure has no analogue in FIELD_SKILL.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction rhetorical structure (hook, question, approach, preview, contributions, roadmap): FIELD DEFAULT
- Hedging norms: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Robustness/identification conventions: Follows FIELD_SKILL norm, adapted to statistical rather than causal-identification framing (assumptions and regularity conditions occupy the role identification strategy plays in econometric papers).

---

## Common Pitfalls
1. Submitting a paper to the wrong section (Theory and Methods vs. Applications and Case Studies) — a stated, evidenced leading cause of rejection per JASA editorial commentary.
2. Exceeding the 200-word abstract limit or including references/math displays in the abstract — will be mechanically edited or flagged.
3. Leaving first-person self-citation phrasing ("as we showed previously") in the blinded manuscript, breaking double-blind review.
4. Omitting the required Author Contributions Checklist and reproducibility materials (code, data, documented workflow) expected under JASA's reproducibility program.

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
| ASA Style Guide (files.taylorandfrancis.com/asa-style-guide.pdf) | Guidelines | Full PDF fetched directly |
| JASA Reproducibility Guide (jasa-acs.github.io/repro-guide) | Guidelines | Full text fetched directly |
| Kock & Preinerstorfer, "Enhanced Power Enhancements..." | Abstract | arXiv/RePEc mirror (2407.17888) |
| Chernozhukov & Newey, "Adversarial Estimation of Riesz Representers" | Abstract | arXiv mirror (2101.00009) |
| Schirripa Spagnolo et al., "Bias Control for M-Quantile-Based Small Area Estimators" | Abstract | Publisher abstract via search snippet + institutional announcement |
| "Checking the Cox Proportional Hazards Model with Interval-Censored Data" | Abstract | PubMed/PMC abstract |
| Tian, Sun & He, "Efficient Analysis of Latent Spaces in Heterogeneous Networks" | Abstract | arXiv mirror (2412.02151) |
| "Successive Classification Learning for Estimating Quantile Optimal Treatment Regimes" | Abstract | arXiv mirror (2507.11255) |
| "Bi-SCORE for Weighted Bipartite Networks..." | Abstract | arXiv (2508.21467) |
| Zhan & Datta, "Neural Networks for Geospatial Data" | Title/citation | Search snippet, JASA 120(549) |
| Yu, Wang & Wang, "Distributed Heterogeneity Learning..." | Title/citation | Search snippet, JASA 120(550) |
| Yan & Luo, "Bayesian Integrative Region Segmentation..." | Title/citation | Search snippet, JASA 119(547) |

Note: tandfonline.com abstract and full-text pages consistently returned HTTP 403 in this environment; all article-level evidence was obtained via arXiv/RePEc preprint mirrors, PubMed/PMC, institutional announcements, or search-engine-extracted abstract snippets, as permitted by the task instructions.
