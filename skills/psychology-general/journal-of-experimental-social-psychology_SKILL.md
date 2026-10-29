---
name: journal-of-experimental-social-psychology-writing-style
description: >
  Journal-specific writing conventions for Journal of Experimental Social Psychology
  (ABS 4, PSYCH (GENERAL)). Use alongside psychology-general-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Experimental Social Psychology",
  "submit to Journal of Experimental Social Psychology", "match Journal of Experimental Social Psychology style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Experimental Social Psychology

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** PSYCH (GENERAL)
- **Publisher:** Elsevier (on behalf of the Society of Experimental Social Psychology, SESP)
- **Scope:** Primary empirical reports using experimental or quasi-experimental methods that extend or create conceptual advances in social psychology (social cognition, attitudes, intergroup relations, self/identity, affect/emotion).
- **Guidelines URL:** https://www.sciencedirect.com/journal/journal-of-experimental-social-psychology/publish/guide-for-authors (guide accessible via search snippets only; full page returns 403 to automated fetch)
- **Field baseline:** psychology-general-field-writing-style
- **Articles spot-checked:** 3 with substantive access (Xu & Petty 2025, doi:10.1016/j.jesp.2025.104807; Dang et al. 2025, doi:10.1016/j.jesp.2024.104711 — abstract/metadata only, full PDFs were image-encoded and not text-extractable) plus editorial/policy evidence drawn from the Replicability Report 2024 analysis of JESP's published statistical practices (aggregate analysis of hundreds of JESP articles) and Elsevier guideline snippets. Full-text access was blocked by ScienceDirect (403) for the guide-for-authors page and by image-only PDF encoding for individual articles; findings below rely on guideline text, editorial-policy announcements, and aggregate replicability-analysis evidence rather than close reading of full manuscripts.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Standard IMRaD / multi-study structure per FIELD_SKILL. Manuscripts submitted for open-science badges must include an **"Open Practices" section placed before the References section**, containing statements/links directing readers to each study's preregistration, materials, and data.

### Length
Full-length research articles have no hard page limit but "normally" run 30-40 pages (~10,000 words) of text. **Single-study manuscripts are discouraged** — accepted only on an exceptional basis, and must show unusually strong theoretical grounding plus an exceptional method (e.g., high power for a small-to-medium effect, preregistration, or an unusually representative sample). This is stricter than FIELD_SKILL, which does not specify a number-of-studies expectation.

### Abstract
Unstructured, factual abstract, **250 words maximum** (not fully specified in FIELD_SKILL, which leaves length unstated). Must stand alone (often displayed separately from the article): avoid citations unless essential (author-year form only), define non-standard abbreviations at first use. 1-6 keywords required.

### Citations
No delta from FIELD_SKILL beyond standard APA-style author-year in-text citation (confirmed via EndNote/citation-template evidence; not independently verified in full text).

### Headings
Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm (integrated near first reference).

### Explicit Prohibitions / Reporting Requirements
JESP operates a **10-item submission checklist (introduced 2022)** that goes beyond FIELD_SKILL's general reporting norms and is treated as a condition of review, not just good practice:
- A priori power analysis and sample-size justification required for every study.
- Full reporting of all statistics, including non-significant results (not merely focal tests).
- For any correlational, regression, or SEM design: a correlation or variance-covariance matrix among all model variables, in the main text or Supplementary Materials.
- For any preregistered study: all deviations from the original preregistered plan must be reported, either narratively in the main text or as a table in Supplementary Materials.
- Registered Reports (a submission track JESP offers) require a cover letter attesting ethics approval, adequate funding/resources, design powered to detect the target effect at 90% power, and a commitment to publish regardless of outcome.
- Double-anonymized (blind) review process — author identity must be removed from the submitted manuscript.

---

## Observed Deltas from FIELD_SKILL

### Statistical Reporting
ENFORCED, tightening FIELD_SKILL. FIELD_SKILL already expects exact test statistics and effect sizes for focal tests; JESP's checklist extends this to a stronger, checklist-gated standard: mandatory a priori power analysis, mandatory full reporting of *all* statistics (not just focal/significant ones), and mandatory correlation/covariance matrices for correlational designs. The Replicability Report 2024 analysis (aggregate review of JESP's published output) found meaningful post-2015 improvement in power and reduction of selection bias, consistent with the checklist having real editorial teeth rather than being guideline-only.

### Structural Deviations
ENFORCED. The "Open Practices" section immediately before References is a JESP-specific structural element not present in the generic FIELD_SKILL structure list; it is optional in the sense that it's tied to requesting OSF open-science badges, but where badges are requested this section is required.

### Other Journal-Specific Patterns
ENFORCED (submission policy, ABS-tier-consistent tightening). Single-study papers are discouraged more explicitly and specifically than the field baseline implies — JESP names concrete bars a single-study paper must clear (high power, preregistration, or an unusually representative sample) rather than a general preference for multi-study evidentiary strategies.

---

## Dimensions With No Delta
- Voice, person, and register: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Argumentation and rhetorical moves (CARS-model introductions): FIELD DEFAULT
- Discussion and conclusion norms: FIELD DEFAULT
- Citation density and literature engagement: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Headings and table/figure placement: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a single-study manuscript without an explicit, strong justification (high power, preregistration, or exceptional sample) — JESP treats single studies as exception-only, not merely disfavored.
- Omitting non-significant statistics or a required correlation matrix — the 10-item checklist makes this a review-stoppable gap, not just a weakness.
- Requesting open-science badges without adding the required "Open Practices" section before References.
- Leaving identifying information in the manuscript body — review is double-anonymized.

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
| ScienceDirect Guide for Authors (JESP) | Guidelines | Search-snippet extraction only; direct fetch returned 403 |
| Elsevier JESP Registered Reports Guidelines (.docx) | Guidelines | Search-snippet extraction |
| Replicability Report 2024: JESP (replicationindex.com) | Aggregate practice analysis | Full-text fetch successful |
| Xu & Petty 2025, JESP, doi:10.1016/j.jesp.2025.104807 | Metadata/abstract | Search-snippet; galley PDF image-encoded, not text-extractable |
| Dang et al. 2025, JESP, doi:10.1016/j.jesp.2024.104711 | Metadata/abstract | Search-snippet; PDF image-encoded, not text-extractable |
| Elsevier "JESP Editorial Guidelines" news page | Guidelines | Page retired/redirected, content unavailable |
