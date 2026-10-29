---
name: biometrika-writing-style
description: >
  Journal-specific writing conventions for Biometrika
  (ABS 4, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Biometrika",
  "submit to Biometrika", "match Biometrika style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Biometrika

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** ECON (journal is a general statistics/methodology outlet; classified under ECON in the ABS list)
- **Publisher:** Oxford University Press (for Biometrika Trust)
- **Scope:** Original theoretical and methodological contributions in statistics and probability, of direct or potential value in applications; not an applied-econometrics or empirical-economics outlet.
- **Guidelines URL:** https://academic.oup.com/biomet/pages/General_Instructions ; https://academic.oup.com/biomet/pages/publishing-in-biometrika
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 5 (abstracts/metadata only — full text paywalled). "Treatment choice with nonlinear regret" (doi:10.1093/biomet/asag008); "Extremal correlation coefficient for functional data" (doi:10.1093/biomet/asaf077); "Geodesic Optimal Transport Regression" (doi:10.1093/biomet/asaf086); "Log-Gaussian Cox process on general metric graphs" (doi:10.1093/biomet/asag043); "Bayesian clustering of high-dimensional data via latent repulsive mixtures" (Vol 112, Issue 2, 2025). Sample smaller than the target 15 because full text is behind institutional paywall and advance-article abstract pages are the only reliably accessible front matter; no new structural deltas were emerging beyond what guidelines already state, so the set was judged to have stabilised.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Three paper types, each with different expectations: Regular papers (standard research articles); Synthesis papers (must either introduce an emerging non-statistical area to a statistical audience, or synthesize multiple statistical areas with fundamental new insight — application-focused papers are excluded from this category and require a cover letter stating which criterion is met); Miscellanea (short papers, same quality bar as regular papers but no requirement to demonstrate the same breadth). No mandated section-by-section outline is published; LaTeX template governs formatting mechanics, not required headings.

### Length
Regular and synthesis papers: typically under 20 pages. Miscellanea: maximum 8 pages. This is a hard length ceiling by paper type, tighter than FIELD_SKILL's ABS 4*/4 econ norm of no stated universal limit.

### Abstract
No word limit or structural (labeled-subsection) format specified in guidelines. All sampled abstracts were single unstructured paragraphs — consistent with absence of a stated requirement.

### Citations
No specific citation style (author-year vs. numbered) mandated by the journal. Datasets specifically must be cited in a fixed format: "[dataset] Authors, Year, Title, Publisher, Identifier," following Force11 Data Citation Principles, with accession number or DOI. This dataset-citation rule has no analogue in FIELD_SKILL.

### Headings
No journal-specific heading convention stated beyond the LaTeX template.

### Tables and Figures
Alt-text descriptions are mandatory for every figure, placed directly beneath the figure legend with an "Alt text:" prefix — a concrete accessibility requirement not present in FIELD_SKILL.

### Explicit Prohibitions
Manuscript must not be previously published or under simultaneous review elsewhere (standard). AI-assisted writing must be disclosed; AI tools cannot be listed as authors.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Abstracts and visible front matter use terse, formal "we propose / we derive / we apply" constructions consistent with FIELD_SKILL's first-person-plural default, but sentences are denser with formal mathematical objects (estimators, coefficients, asymptotic properties) stated compactly, reflecting the journal's methodological/theoretical scope rather than an applied-economics register. PRACTICE ONLY — not stated in guidelines, and not a deviation in kind from FIELD_SKILL's theory-paper voice, only in degree of mathematical density.

### Structural Deviations
Hard page ceilings by paper type (20 pages regular/synthesis, 8 pages miscellanea) are tighter and more explicit than anything in FIELD_SKILL, which specifies no universal length norm. ENFORCED.
Three-way paper-type taxonomy (regular/synthesis/miscellanea) with distinct admission criteria has no counterpart in FIELD_SKILL. ENFORCED.

### Other Journal-Specific Patterns
Mandatory per-figure alt-text captioning is a concrete accessibility rule absent from FIELD_SKILL. ENFORCED.
Fixed dataset-citation format tied to Force11 principles is a journal-specific reference convention layered on top of FIELD_SKILL's general author-year norm. ENFORCED.

---

## Dimensions With No Delta
- Overall citation format (author-year, no numbered footnote references): FIELD DEFAULT
- Paraphrase over direct quotation: FIELD DEFAULT
- Hedging intensity and contexts: FIELD DEFAULT
- Active voice preference: FIELD DEFAULT
- Introduction argumentation pattern (motivation, question, preview of results, roadmap): FIELD DEFAULT — where visible in abstracts, results are previewed directly ("we derive closed-form fractions...", "a consistent estimator is proposed and justified...").

---

## Common Pitfalls
- Submitting an applications-focused paper under the Synthesis category — it will be excluded regardless of quality; applications belong under Regular or Miscellanea.
- Omitting the required cover letter explaining which synthesis criterion (new area to statistics, or cross-area synthesis) is met when submitting a Synthesis paper.
- Missing alt-text lines under figure legends, which the journal explicitly requires at submission.
- Exceeding the 8-page Miscellanea limit while still framing the piece as a short note rather than a Regular paper.

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
| https://academic.oup.com/biomet/pages/General_Instructions | Guidelines | WebFetch, publicly accessible |
| https://academic.oup.com/biomet/pages/publishing-in-biometrika | Guidelines | WebFetch, publicly accessible |
| Treatment choice with nonlinear regret (doi:10.1093/biomet/asag008) | Abstract | WebFetch, publicly accessible abstract page |
| Extremal correlation coefficient for functional data (doi:10.1093/biomet/asaf077) | Abstract | WebFetch, publicly accessible abstract page |
| Geodesic Optimal Transport Regression (doi:10.1093/biomet/asaf086) | Abstract snippet | WebSearch result |
| Log-Gaussian Cox process on general metric graphs (doi:10.1093/biomet/asag043) | Title/metadata only | WebFetch of advance-articles listing |
| Bayesian clustering of high-dimensional data via latent repulsive mixtures | Abstract snippet | WebSearch result |
