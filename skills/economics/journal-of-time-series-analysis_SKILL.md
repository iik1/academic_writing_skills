---
name: journal-of-time-series-analysis-writing-style
description: >
  Journal-specific writing conventions for Journal of Time Series Analysis
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Time Series Analysis",
  "submit to Journal of Time Series Analysis", "match Journal of Time Series Analysis style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Time Series Analysis

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Wiley-Blackwell
- **Scope:** Publishes theoretical and methodological research in time series analysis and related areas of mathematical statistics and econometrics (e.g., cointegration, structural breaks, spectral methods, count/functional time series), rather than applied empirical economics.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/14679892/homepage/forauthors.html
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 12 (titles/abstracts): "Self-Normalized KPSS Tests With Power Enhancement" (Peng-Zhou & Song); "Local GMM Estimation for Nonparametric Time-Varying Coefficient Moment Condition Models" (Bai); "Markov Determinantal Point Process for Dynamic Random Sets" (Gouriéroux & Lu); "Time Series Models on Compact Spaces" (Franchi & Truquet); "Extremely Fast Maximum Likelihood Estimation of High-Order Autoregressive Models" (Schmidt & Makalic); "Moving Sum Procedure for Multiple Change Point Detection in Large Factor Models" (Barigozzi, Cho & Trapani); "Online Network Change Point Detection With Missing Values" (Xu, Dubey & Yu); "Online Detection of Forecast Model Inadequacies Using Forecast Errors" (Grundy, Killick & Svetunkov, jtsa.12843); "The Granger–Johansen Representation Theorem for Integrated Time Series on Banach Space" (Howlett, jtsa.12766); "Sequential Monitoring for Changes in GARCH(1,1) Models Without Assuming Stationarity" (Horváth, jtsa.12824); "Cointegrating Polynomial Regressions With Power Law Trends" (Lin, jtsa.12805); "Time Series Quantile Regression Using Random Forests" (Shiraishi, jtsa.12731). Full text was inaccessible (paywalled); titles, abstracts, and author/keyword metadata were assessed via search-engine snippets and the RePEc/IDEAS listing.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No mandated section list is specified in the guidelines beyond a required cover page (title, author names/affiliations, corresponding email). No fixed empirical-paper template is imposed; structure is left to the author, consistent with the journal's mathematical-statistics orientation.

### Length
Papers should ideally be no more than 35 pages in total. Single-column format, minimum 11pt font, at least 1.5 line spacing.

### Abstract
Abstract must not exceed 200 words. Unstructured (no mandated subheadings/fields).

### Citations
Not specified beyond general Wiley practice; no explicit style mandated in the guidelines text retrieved.

### Headings
Not specified in the guidelines beyond the cover-page requirement.

### Tables and Figures
Not specified in the guidelines text retrieved.

### Explicit Prohibitions
Footnotes should be avoided; where essential, they must be numbered in-text and grouped together at the end of the article (not page-bottom footnotes). Authors must disclose any potential conflicts of interest. A mandatory Mathematics Subject Classification (MSC) code and up to six keywords must be provided; JEL codes are optional. Submitting author must supply an ORCID iD. Papers with empirical data applications must upload the data as supplementary files; this becomes a condition of publication upon acceptance (Expects Data Sharing policy).

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Voice and Register
FIELD_SKILL is calibrated to applied/theoretical economics prose. JTSA papers are more consistently written in the register of mathematical statistics: dense use of formal theorem/proof/lemma environments is the norm rather than the exception, even outside dedicated "theory" papers (e.g., Howlett's Granger–Johansen representation theorem paper, Schmidt & Makalic's high-order AR estimation paper). "We" is still used for framing ("we propose," "we develop"), consistent with FIELD_SKILL, but a larger share of the paper's body is occupied by formal statements and proofs than is typical of ABS 4/4* empirical economics papers. PRACTICE ONLY / FIELD DEFAULT hybrid — voice matches FIELD_SKILL, but proof-driven exposition is more prevalent than the baseline implies for a general ECON journal.

### Citation Density
Abstracts and titles sampled show technical, method-focused framing (e.g., "we propose univariate and multivariate CPRs that incorporate power law deterministic trends") with essentially no engagement with policy relevance or motivating real-world hooks in the abstract itself — the abstract states the technical contribution directly rather than opening with a motivating fact or puzzle. This is a RELAXATION of the FIELD_SKILL introduction/abstract convention (motivating hook before method), consistent with the ABS 3 tier's latitude to relax rather than redefine the baseline.

### Structural Deviations
Mandatory MSC classification code alongside (optional) JEL codes is a discipline-specific requirement not present in FIELD_SKILL, reflecting the journal's dual audience of statisticians and econometricians. ENFORCED (stated in guidelines; consistent with the applied-math orientation visible in sampled titles).

### Other Journal-Specific Patterns
Footnote policy (grouped endnotes rather than page footnotes) is ENFORCED and is stricter than typical ECON practice, where footnotes are used more liberally for qualifications.

---

## Dimensions With No Delta
- Sentence and paragraph style: FIELD DEFAULT
- Results and reporting norms: FIELD DEFAULT
- Discussion/Conclusion norms: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Handling of prior-work disagreement: FIELD DEFAULT

---

## Common Pitfalls
- Writing an abstract with a motivating real-world hook before the technical contribution — JTSA abstracts sampled go directly to the methodological contribution within the 200-word limit.
- Using page-bottom footnotes instead of grouped endnotes.
- Omitting the mandatory MSC classification code (JEL codes alone are insufficient).
- Underestimating the expected density of formal theorem/proof content relative to a typical applied-economics ABS 3 outlet.

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
| https://onlinelibrary.wiley.com/page/journal/14679892/homepage/forauthors.html | Guidelines | WebSearch snippet extraction (direct fetch returned 402) |
| https://ideas.repec.org/s/bla/jtsera.html | Article listing (titles/authors) | WebFetch |
| jtsa.12843 (Grundy, Killick & Svetunkov, 2025) | Title/context | WebSearch snippet |
| jtsa.12766 (Howlett, 2025) | Title/abstract | WebSearch snippet |
| jtsa.12824 (Horváth, 2025) | Title/abstract | WebSearch snippet |
| jtsa.12805 (Lin, 2026) | Abstract | WebSearch snippet |
| jtsa.12731 (Shiraishi, 2024) | Title/abstract | WebSearch snippet |
| Additional titles (Vol 47 Issues 3-4, 2026) | Titles only | WebFetch of RePEc listing |
