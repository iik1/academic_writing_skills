---
name: psychological-bulletin-writing-style
description: >
  Journal-specific writing conventions for Psychological Bulletin
  (ABS 4, PSYCH (GENERAL)). Use alongside psychology-general-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Psychological Bulletin",
  "submit to Psychological Bulletin", "match Psychological Bulletin style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Psychological Bulletin

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** PSYCH (GENERAL)
- **Publisher:** American Psychological Association
- **Scope:** Publishes syntheses of research in scientific psychology — comprehensive reviews and quantitative meta-analyses that summarize findings across multiple investigations addressing related hypotheses, assess the state of knowledge, and identify unresolved issues.
- **Guidelines URL:** https://www.apa.org/pubs/journals/bul (dedicated "Instructions to authors" page not independently retrievable; content triangulated via APA journal page and secondary submission-guide sources)
- **Field baseline:** psychology-general-field-writing-style
- **Articles spot-checked:** 5 (2025 issues): "How Does Perceived Social Support Relate to Human Thriving? A Systematic Review With Meta-Analyses" (bul0000491); "Electronic Screen Use and Children's Socioemotional Problems: A Systematic Review and Meta-Analysis of Longitudinal Studies" (bul0000468); "Acute Effects of Fasting on Cognitive Performance: A Systematic Review and Meta-Analysis" (bul0000492); "Trust and Subjective Well-Being Across the Lifespan: A Multilevel Meta-Analysis"; "Feeds, Feelings, and Focus: A Systematic Review and Meta-Analysis Examining the Cognitive and Mental Health Correlates of Short-Form Video Use" — abstract/press-release level access only, no full text.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Unlike the empirical-report IMRaD default in FIELD_SKILL, every accepted article at this journal is itself a research synthesis (comprehensive narrative review or meta-analysis) — there is no primary-empirical-study track. For meta-analyses specifically, a PRISMA flow diagram, full inclusion/exclusion criteria, and a complete effect-size dataset are required elements of the manuscript.

### Length
Not independently confirmed from a primary guidelines page; no specific word/page limit could be verified. Treat as unspecified rather than assuming a figure.

### Abstract
Structured/word-limit specifics could not be independently confirmed from a primary source; secondary sources indicate an abstract under 250 words per standard APA 7th-edition convention. Do not treat as confirmed beyond that.

### Citations
APA 7th-edition style, per general APA journal policy. No journal-specific citation deltas found.

### Headings
Follows FIELD_SKILL norm (thematic, researcher-defined headings for review/synthesis articles).

### Tables and Figures
PRISMA flow diagram required for meta-analyses (see Structure). Otherwise follows FIELD_SKILL norm.

### Explicit Prohibitions
Masked/anonymized peer review is required: the main manuscript file must be fully anonymized (no author names, institutional affiliations, or acknowledgements; self-citations suppressed or written in third person), with identifying information submitted separately on a title page. Reviewer-blinding is unusually strict here — author identities are withheld from reviewers even after the final decision, disclosed only upon request and with author permission. For meta-analyses, a pre-registered protocol reference (e.g., PROSPERO, OSF) is expected.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
This journal is exclusively a synthesis/meta-analysis venue (both invited and unsolicited submissions accepted directly, unlike invitation-only Annual Review of Psychology). FIELD_SKILL treats review journals as one branch among several; here it is the only branch. ENFORCED.

### Statistical Reporting
Spot-checked meta-analyses consistently report pooled/aggregate effect sizes (r+, g, b) with confidence or credible intervals and heterogeneity statistics (e.g., τ), and some use hierarchical/multilevel or Bayesian random-effects models rather than fixed-effect pooling — an emphasis on multilevel/hierarchical meta-analytic modeling beyond what FIELD_SKILL's general effect-size-and-CI norm specifies. PRACTICE ONLY / ENFORCED for the PRISMA and effect-size dataset requirements specifically (stated in guidelines and consistent with observed articles); the hierarchical-modeling preference itself is PRACTICE ONLY (observed, not stated as a requirement).

### Other Journal-Specific Patterns
Masked review with delayed/optional identity disclosure to reviewers is a distinctive procedural norm not addressed by FIELD_SKILL (which is silent on peer-review mechanics). ENFORCED (stated in guidelines).

---

## Dimensions With No Delta
- Voice, person, and register: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Argumentation and rhetorical moves: FIELD DEFAULT
- Discussion and conclusion norms: FIELD DEFAULT
- Citation density and literature engagement: FIELD DEFAULT (high throughout, consistent with FIELD_SKILL's note on review journals)
- Hedging and epistemic caution: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a primary empirical study rather than a review/meta-analysis — this journal does not publish standalone empirical reports.
- Omitting a PRISMA flow diagram, pre-registration reference, or complete effect-size dataset for a meta-analysis submission.
- Failing to fully anonymize the manuscript body (including self-citations) for masked review.

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
| apa.org/pubs/journals/bul | Guidelines/journal scope | WebFetch, direct |
| apa.org/pubs/journals/bul/sample | Sample article list | WebFetch, direct |
| Secondary submission-guide summaries (manusights.com and search-aggregated guideline text) | Guidelines (unverified against primary APA instructions page, which returned 404) | WebSearch snippets |
| bul0000491 (Human Thriving meta-analysis) | Abstract/press release | WebSearch snippet + APA press PDF |
| bul0000468 (Electronic Screen Use meta-analysis) | Abstract/press release | WebSearch snippet + APA press PDF |
| bul0000492 (Fasting and Cognitive Performance meta-analysis) | Abstract/press release | WebSearch snippet + APA press PDF |
| Trust and Subjective Well-Being Across the Lifespan | Citation/partial abstract | WebSearch snippet |
| Feeds, Feelings, and Focus (short-form video meta-analysis) | Citation/partial abstract | WebSearch snippet |
