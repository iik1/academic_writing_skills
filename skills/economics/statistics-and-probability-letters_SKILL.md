---
name: statistics-and-probability-letters-writing-style
description: >
  Journal-specific writing conventions for Statistics and Probability Letters
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Statistics and Probability Letters",
  "submit to Statistics and Probability Letters", "match Statistics and Probability Letters style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Statistics and Probability Letters

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON (cross-listed statistics/probability theory journal; FIELD_SKILL's econ conventions apply loosely since this is a mathematical statistics venue, not an applied economics venue)
- **Publisher:** Elsevier
- **Scope:** New statistical methods, theoretical probability results, and innovative applications of statistics and probability to other scientific disciplines. Publishes short, concise theoretical notes rather than full-length empirical studies. Proofs may be omitted or sketched if supporting material allows verification.
- **Guidelines URL:** https://www.sciencedirect.com/journal/statistics-and-probability-letters/publish/guide-for-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 3 full-text (Kokoszka, Singh & Wang 2022, SPL 184:109387; Chen & Xie 2023, SPL 199:109854; Sarma & Selvamuthu 2024, SPL 214:110192), plus recent tables of contents (vols. 235–237, 2026) for topical corroboration.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No mandated section template. Papers are theorem/proof-driven notes, not empirical IMRAD papers. A short, undivided Introduction is followed by numbered results sections and (often) an Appendix containing proofs. No mandated Data/Methods/Results split.

### Length
Articles limited to 6 journal pages (approx. 13 double-spaced typed pages), including references and figures.

### Abstract
No structured/unstructured requirement stated explicitly in the guide, but observed practice is a single unstructured paragraph. Any abbreviations used in the abstract must be defined at first mention.

### Citations
Author-year (Harvard-style), consistent with FIELD_SKILL. Elsevier "num" or "name-date" reference list styles are supported; observed articles use name-date.

### Headings
No specific numbering mandate; observed practice uses Arabic numerals ("1. Introduction," "2. Main results," etc.).

### Tables and Figures
Word submissions: single-column; LaTeX submissions may use double-column. Standard Elsevier figure/table formatting rules apply (no journal-specific deviation found).

### Explicit Prohibitions
None found beyond standard Elsevier submission requirements (editable source files only; PDF not accepted as source).

### Other
- **Keywords:** 1–7 required, single words preferred (avoid "and"/"of" compounds); abbreviations only if field-standard.
- **Highlights:** Encouraged (not mandatory) — short bullet points of novel results, submitted as a separate file.
- **MSC codes:** Observed in all three spot-checked articles (AMS Mathematics Subject Classification codes listed alongside keywords in the article-info block) — not mentioned in the prose guide but a consistent practice.
- **Data availability statement:** Present in all three spot-checked articles ("No data was used for the research described in the article."), reflecting Elsevier's group-wide mandatory data statement policy, not a journal-specific rule.
- **Review type:** Single-anonymized.

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Structural Deviations
DELTA (ENFORCED via page limit, confirmed by all 3 articles). This is a theory/mathematics-statistics journal, not an empirical economics journal, so FIELD_SKILL's empirical-paper section template (Data, Empirical Strategy, Robustness) does not apply and its theory-paper template applies only loosely:
- No standalone "Related Literature" section observed in any of the three articles; prior work is reviewed within the Introduction (or a short "Preliminaries and literature review" section merged with technical setup, as in Sarma & Selvamuthu 2024).
- A dense sequence of numbered Theorem/Lemma/Proposition/Corollary/Definition/Remark/Example environments is the primary body structure — heavier and more central than typical ABS 4/4* theory papers, since the entire paper is essentially the "Analysis" section with no separate prose "Results" discussion.
- Proofs are typically inline immediately after each result (short papers) or collected in a final numbered "Proofs" section (Kokoszka et al.) or Appendix (Chen & Xie). Either placement is normal PRACTICE ONLY — no stated convention.
- An explicit "Organisation of the paper" or roadmap paragraph at the end of the Introduction is near-universal (matches FIELD_SKILL's roadmap norm but is applied even in very short 6-10 page notes, where FIELD_SKILL would not necessarily expect one).
- Conclusion, where present, is very short (a single paragraph) and sometimes titled "Conclusion and future work"; one of three articles (Kokoszka et al., the shortest at 6 pages) has no standalone conclusion at all — the paper ends after the final proof. This is a RELAXATION of FIELD_SKILL's expectation that a conclusion is near-universal.

### Voice and Register
FIELD_DEFAULT with one addition: the word "note" is sometimes used self-referentially ("this note that is dedicated to...") to describe the paper itself, reflecting the journal's short-format identity (PRACTICE ONLY, low prevalence — seen in 1 of 3).

### Citation Density
DELTA (PRACTICE ONLY, confirmed in 2 of 3). Literature engagement is markedly thinner than FIELD_SKILL's ABS 4*/4 baseline: reference lists run 10-25 items (vs. dozens in top-tier empirical papers), and the "positioning relative to prior work" is typically a single dense paragraph naming 3-6 closely related papers rather than an extended contributions discussion. Consistent with RELAXATION expected at ABS 2.

### Other Journal-Specific Patterns
- MSC (Mathematics Subject Classification) codes appear alongside keywords in all three spot-checked articles — a mathematics-journal convention not present in FIELD_SKILL (which is derived from applied/empirical economics journals). PRACTICE ONLY but consistent (3/3).
- Assumptions are frequently stated as formally numbered, labeled objects ("Assumption 2.1") parallel to theorems, rather than embedded in prose — a stronger formalization than FIELD_SKILL's theory-paper norm.

---

## Dimensions With No Delta
- Sentence and paragraph style: FIELD DEFAULT (dense, technical, no simplification for lay readers)
- Hedging and epistemic caution: FIELD DEFAULT (low; claims are asserted plainly, mathematical results stated as derived facts)
- Tense conventions: FIELD DEFAULT (present tense for stated results, mixed with procedural past tense where relevant)
- Robustness checks: not applicable (no empirical robustness section norm in this theoretical venue; not a deviation, just an inapplicable FIELD_SKILL dimension)

---

## Common Pitfalls
- Treating this as an empirical-economics ABS journal and adding a Data/Empirical Strategy/Robustness structure — this journal is pure mathematical statistics/probability; that structure will look out of place.
- Over-writing the Introduction with an extended literature review — the journal's very tight page limit (6 pages) means literature positioning must be compressed into one or two paragraphs.
- Omitting MSC classification codes — not stated in the prose guide but present in every spot-checked article's article-info block.
- Expecting a substantial standalone Conclusion — many notes end directly after the last proof, or with a single short paragraph.

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
| https://www.sciencedirect.com/journal/statistics-and-probability-letters/publish/guide-for-authors | Guidelines | WebSearch-extracted summary (direct WebFetch returned 403) |
| Kokoszka, Singh & Wang (2022), "Long term behavior of incomplete and time varying product ratings," SPL 184:109387 | Full-text | Open PDF via author's personal faculty page (stat.colostate.edu) |
| Chen & Xie (2023), "Estimating heterogeneous treatment effects versus building individualized treatment rules," SPL 199:109854 | Full-text | Open PDF via author's personal faculty page (stat.purdue.edu) |
| Sarma & Selvamuthu (2024), "Study of discrete-time Hawkes process and its compensator," SPL 214:110192 | Full-text | Open PDF via author's personal faculty page (web.iitd.ac.in) |
| IDEAS/RePEc journal listing (stapro) | Table of contents / recent titles | WebFetch, titles only (vols. 235-237, 2026) for topical corroboration |
