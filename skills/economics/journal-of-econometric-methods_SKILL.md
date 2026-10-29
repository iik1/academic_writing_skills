---
name: journal-of-econometric-methods-writing-style
description: >
  Journal-specific writing conventions for Journal of Econometric Methods
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Econometric Methods",
  "submit to Journal of Econometric Methods", "match Journal of Econometric Methods style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Econometric Methods

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** Walter de Gruyter (De Gruyter Brill)
- **Scope:** Theoretical and applied econometrics of direct relevance to empirical economics research; aims to bridge the gap between econometric method development and empirical practice. Publishes short methodological notes, pedagogical pieces, and full research articles.
- **Guidelines URL:** https://www.degruyterbrill.com/publication/journal_key/JEM/downloadAsset/JEM_JEM%20Instructions%20for%20Authors.pdf (accessible; generic De Gruyter template shared across many of the publisher's journals, not econometrics-specific)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 6 with full abstract/JEL/keyword front matter (Gillen 2025 v14i2p49-57; Winkelmann 2025 v14i2p59-69; Alejo 2026 v15i1p1-17; Korolev 2026 v15i1p19-45; plus two 2016 v5i1 abstracts via search snippets), plus title-level review of ~45 articles across Volumes 8-15 (2019-2026) via IDEAS/RePEc tables of contents. Full text was not accessible (paywalled); front matter (abstract, JEL codes, keywords, title) was sufficient to judge structural and stylistic deltas.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No mandated section list for research articles (the guidelines' explicit section checklist — title page, abstract, keywords, list of abbreviations, introduction, body, expert opinion, outlook, highlights, references — is a generic De Gruyter template written for review articles in general science/medicine, not specific to this journal's econometrics articles; do not apply "expert opinion"/"highlights" to a standard econometrics paper). Cover letter required with every submission, briefly highlighting the contribution's main features.

### Length
No explicit word/page limit stated in the guidelines. In practice, observed articles vary widely, from very short notes (as short as 4 pages) to full-length articles (up to ~200 pages for a large unified-framework paper); short methodological notes and pedagogical pieces are common and clearly acceptable at this journal, unlike the near-uniform full-length format of ABS 4*/4 outlets.

### Abstract
Unstructured, no explicit word limit stated. Observed abstracts are brief (roughly 60-120 words), technical, and result-focused, consistent with FIELD_SKILL's preview-of-results norm. JEL classification codes and 2-4 keywords are standard and expected (confirmed present in every spot-checked article).

### Citations
Chicago Manual of Style author-date system is the mandated citation style — this is a deviation from the economics-field-standard author-date convention only in that authors must follow CMS specifics precisely (e.g., "et al." is NOT allowed in the reference list; all authors must be listed regardless of number). This is stricter than the common economics practice of truncating long author lists to "et al." in the reference list (in-text citation still uses "et al." for four or more authors, matching field norm). DOIs required wherever available; full URLs (no shorteners) plus access date required when no DOI exists.

### Headings
No fixed hierarchy mandated, but heading style (headline case vs. sentence case) must be applied consistently throughout the manuscript once chosen.

### Tables and Figures
Tables must not contain lists, images, or dashed lines; large/complex tables should be moved to supplementary material or an appendix. Figures must be submitted as separate files, not embedded in text, with captions collected at the end of the manuscript. Equations must be typed with a formula editor (not images), numbered sequentially, with a blank line before and after each.

### Explicit Prohibitions
"et al." usage is explicitly disallowed in the reference list (all co-authors must be named). Short/shortened URLs are not acceptable. Mathematical expressions must not be displayed as images. Colored text discouraged for body text; color for emphasis discouraged.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
This journal publishes a substantial share of short-form content — brief methodological notes (as short as 4 pages), pedagogical/teaching-oriented papers (e.g., undergraduate econometrics applications using ride-share or theme-park data), and software/package notes (e.g., an R package note) — alongside standard full-length empirical/methods papers. FIELD_SKILL's assumption of a uniform full-length IMRAD-style empirical or theory paper does not hold uniformly here; shorter pieces compress or omit sections (e.g., a literature review subsection) that a full ABS 4/4* paper would include. This is PRACTICE ONLY (not stated in guidelines, observed structurally across the title sample) and reflects a RELAXATION appropriate to ABS 1 tier, not a new norm.

### Citation Density
Consistent with FIELD_SKILL's low citation density in short notes; the prevalence of brief notes further compresses literature engagement relative to typical ABS 4/4* introductions, since space constraints in short pieces leave little room for an extended related-literature discussion. PRACTICE ONLY.

### Other Journal-Specific Patterns
Many articles are pitched as pedagogical or teaching-note contributions explicitly aimed at econometrics instruction (e.g., "Introduction to Latent Variable Estimation for Undergraduate Econometrics," "Econometrics Pedagogy and Cloud Computing"). This teaching/pedagogy angle is a recognizable niche for the journal not present in FIELD_SKILL's ABS 4*/4 sample. PRACTICE ONLY / journal niche, evidenced by recurring titles across multiple volumes (2020, 2021, 2024).

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction rhetorical structure (motivation, question, preview of results, contribution, roadmap): FIELD DEFAULT
- Statistical reporting precision and tense conventions: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Tables as primary vehicle for quantitative results: FIELD DEFAULT

---

## Common Pitfalls
- Do not truncate reference-list author lists to "et al." — this journal's CMS-based style requires all authors listed in the bibliography (in-text citation may still use "et al." for 4+ authors).
- Do not assume a full IMRAD structure is mandatory — short notes and pedagogical pieces are an accepted, recurring format at this journal; forcing a short methodological contribution into a full-length empirical paper template is unnecessary.
- Do not submit mathematical expressions as images; use a formula editor and number equations sequentially with blank lines surrounding each.
- Follow CMS author-date exactly for reference formatting (including DOI/URL/access-date requirements), not a generic economics author-date style.

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
| JEM Instructions for Authors (De Gruyter Brill PDF) | Guidelines | Direct PDF download |
| Gillen, "A Moment-Based Representation for Heteroskedasticity Robust Standard Errors" (2025, v14i2) | Abstract/JEL/Keywords | IDEAS/RePEc |
| Winkelmann, "Regression as Best Linear Prediction: The Case of Discrete Regressors" (2025, v14i2) | Abstract/JEL/Keywords | IDEAS/RePEc |
| Alejo, "A Simple Approach to Simultaneous Quantile Regression under Partial Homogeneity Constraints" (2026, v15i1) | Abstract/JEL/Keywords | IDEAS/RePEc |
| Korolev, "A Consistent LM-Type Specification Test for Semiparametric Panel Data Models" (2026, v15i1) | Abstract/JEL/Keywords | IDEAS/RePEc |
| Two Volume 5/1 (2016) articles (quantile regression w/ clustered data; frequentist model averaging) | Abstract snippets | Search-engine-extracted snippet from degruyterbrill.com |
| ~45 article titles, Volumes 8-15 (2019-2026) | Titles/ToC | IDEAS/RePEc journal series page |
| degruyterbrill.com direct volume/issue pages | Blocked (405 on WebFetch; JS-rendered on curl) | Not usable; relied on IDEAS/RePEc mirror instead |
