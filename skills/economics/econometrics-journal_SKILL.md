---
name: econometrics-journal-writing-style
description: >
  Journal-specific writing conventions for Econometrics Journal
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Econometrics Journal",
  "submit to Econometrics Journal", "match Econometrics Journal style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Econometrics Journal

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Oxford University Press, on behalf of the Royal Economic Society
- **Scope:** Publishes original theoretical and applied econometrics research; requires that every paper — including purely theoretical/methodological contributions — demonstrate applied relevance through an empirical application.
- **Guidelines URL:** https://academic.oup.com/ectj/pages/general_instructions (points to detailed requirements at https://res.org.uk/submissions/)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 22 (front-matter/title/abstract level: 15 advance articles from academic.oup.com/ectj/advance-articles including "Synthetic control inference for staggered adoption" (Cao et al.), "Debiased Inference for Dynamic Nonlinear Panels with Multi-dimensional Heterogeneities" (Leng et al.), "Inflation expectations and monetary policy: what have we learned and to what end?" (Coibion and Gorodnichenko); 7 articles from Volume 28 Issue 2 (May 2025) including "One-step smoothing splines instrumental regression" (Beyhum and Lapenta, full abstract read, 2025 Denis Sargan Prize winner) and "Robustify and Tighten the Lee Bounds" (Okamoto, Vol 28 Issue 3, summary read))

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No mandated section list beyond standard econometrics-paper conventions. The one binding structural requirement: **every submission, including purely theoretical/methodological papers, must include an empirical application** demonstrating applied relevance — this is stated as a condition of acceptance, not a stylistic preference. ENFORCED.

### Length
Papers must **not normally exceed 20 pages, including the printed appendix**. Simulation results in the main text must be concisely summarised, normally within one page using a single key table or graph, with full detail relegated to an online appendix. ENFORCED — this is materially tighter than the untyped, no-limit norm in FIELD_SKILL.

### Abstract
Unstructured summary of **no more than 150 words**. ENFORCED.

### Citations
Not explicitly specified beyond referring authors to the journal's LaTeX template/style files. No observed deviation from FIELD_SKILL author-year convention.

### Headings
Not specified in guidelines. No observed deviation from FIELD_SKILL.

### Tables and Figures
Simulation evidence must be compressed into one summary table/graph in the main text, with the remainder pushed to an online appendix — RELAXATION of the field default (FIELD_SKILL treats full reporting of robustness/simulation evidence in the main text or standard appendix as normal; this journal enforces stricter offloading given its length cap). Authors must supply alt-text for all figures, inserted directly under each figure legend as "Alt text: ...". ENFORCED (accessibility requirement, distinctive to this journal's submission system).

### Explicit Prohibitions
None stated beyond standard COPE-aligned publication-ethics prohibitions (no falsification, fabrication, plagiarism, or duplicate publication) — FIELD DEFAULT, not journal-specific.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm.

### Statistical Reporting
Follows FIELD_SKILL norm, with the one exception already noted under Tables and Figures (simulation evidence compression is a length-driven RELAXATION/constraint, not a reporting-style delta).

### Citation Density
Follows FIELD_SKILL norm.

### Structural Deviations
The mandatory empirical-application requirement functions as a structural delta for theory/methods papers: unlike a generic ABS 4/4* theory paper (per FIELD_SKILL, "Extensions" and "Applications" are optional), an applications/illustration section is effectively compulsory here even for purely methodological contributions. ENFORCED.

### Other Journal-Specific Patterns
Spot-checked titles and abstracts skew heavily toward technical, methods-first framing (e.g., "Debiased Inference for Dynamic Nonlinear Panels with Multi-dimensional Heterogeneities," "Closed-form estimation and inference for panels with attrition and refreshment samples") rather than applied-question framing. This is consistent with FIELD_SKILL's theory-paper introduction pattern and not a delta — noted only because the journal's mix is more methods-heavy than a typical general-interest ECON outlet.

---

## Dimensions With No Delta
- Voice, person, and register: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction structure and rhetorical moves: FIELD DEFAULT
- Citation format and literature engagement: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Discussion/conclusion norms: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a purely theoretical/methodological paper without an empirical illustration — this journal requires one regardless of paper type.
- Writing an abstract over 150 words (FIELD_SKILL sets no field-wide abstract limit; this journal enforces one strictly).
- Reporting full simulation tables in the main text instead of compressing to one table/graph and moving detail to an online appendix, given the 20-page cap.
- Omitting alt-text under figure legends, which the submission system requires.

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
| https://academic.oup.com/ectj/pages/general_instructions | Guidelines | WebFetch, direct |
| https://res.org.uk/submissions/ | Guidelines (detailed) | WebFetch, direct |
| https://academic.oup.com/ectj/advance-articles | Advance articles (15 titles/authors) | WebFetch, direct |
| https://academic.oup.com/ectj/issue/28/2 | Issue 28(2) table of contents (7 articles) | WebFetch, direct |
| "One-step smoothing splines instrumental regression" (Beyhum & Lapenta, Vol 28(2), 2025 Sargan Prize winner) | Full abstract | WebSearch snippet |
| "Robustify and Tighten the Lee Bounds" (Okamoto, Vol 28(3), 2025) | Summary/abstract | WebFetch of advance-article page |
