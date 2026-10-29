---
name: european-actuarial-journal-writing-style
description: >
  Journal-specific writing conventions for European Actuarial Journal
  (ABS 2, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for European Actuarial Journal",
  "submit to European Actuarial Journal", "match European Actuarial Journal style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: European Actuarial Journal

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** FINANCE
- **Publisher:** Springer Nature (Springer International Publishing AG)
- **Scope:** Promotion and development of actuarial science and actuarial finance — life and non-life insurance, pension funds, reinsurance, risk management, asset-liability management, solvency, catastrophe modeling, and longevity. Formed as the successor to six national European actuarial journals; explicitly positioned as a bridge between actuarial theory and practice.
- **Guidelines URL:** https://link.springer.com/journal/13385/submission-guidelines (paywalled via login redirect; content reconstructed from cached/search snippets) and https://link.springer.com/journal/13385/aims-and-scope
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 7 (with abstract/structure visibility; a further 3-4 identified by title/topic only)
  - "Lapse-supported life insurance and adverse selection" (Haçarız, Kleinow, Macdonald, 2025, DOI 10.1007/s13385-025-00434-7)
  - "Sustainable portfolio optimization and sustainable taxation" (Korn, Nurkanović, 2025, DOI 10.1007/s13385-025-00423-w)
  - "From point to probabilistic gradient boosting for claim frequency and severity prediction" (Chevalier, Côté, 2025, DOI 10.1007/s13385-025-00428-5)
  - "Modelling and forecasting mortality improvement rates with random effects" (2021, DOI 10.1007/s13385-021-00274-1)
  - "A general framework for analysing the mortality experience of a large portfolio of lives: with an application to the UK universities superannuation scheme" (2022, DOI 10.1007/s13385-022-00309-1)
  - "Longevity risk and capital markets: the 2023-2024 update" (Blake, Cairns, 2025, DOI 10.1007/s13385-025-00421-y) — identified as a recurring short update piece
  - "Risk sensitive control and an optimal reinsurance model of a network of insurance companies" (2024, DOI 10.1007/s13385-024-00404-5) — title/abstract only

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No single mandated section template; structure is mathematics/actuarial-paper style (Introduction ... Conclusion, with subsections and formal Propositions/Corollaries/Assumptions common in theoretical papers). The journal publishes several distinct article types beyond standard research papers, each with different length/structure norms:
- **Research papers** — theoretical or applied original research.
- **Survey papers** — comprehensive reviews of a topic area.
- **Letters** — up to 5 pages; a novel idea, insight, clarification, or short curious result; reviewed within 6 weeks; same refereeing standard as full papers.
- **Discussions** — 1-3 pages; practitioner-authored commentary on practical applications, often responding to a published paper.
- **Editorials / book reviews / comments** — short, may require a disclosure statement depending on content.

### Length
No general page/word limit stated for standard research papers beyond normal journal-article length. Letters are capped at 5 pages; Discussions at 1-3 pages. These are hard, journal-specific caps with no equivalent in FIELD_SKILL.

### Abstract
Structured requirement: 150-250 words, single paragraph, no undefined abbreviations, no unspecified references. 4-6 keywords required for indexing. (FIELD_SKILL states a similar word count for finance broadly, but the explicit "no undefined abbreviations/unspecified references" instruction and required keyword count are journal-specific and should be followed literally.)

### Citations
**Numbered citation system** — in-text citations are bracketed numbers, e.g. "[6]", "[1, 2]", "[1-4]", not author-year. Reference list is numbered (either in citation order or alphabetically with numbers assigned) with format: `Author(s) (Year) Title. Journal Volume:Pages`. This is a direct, hard override of FIELD_SKILL's author-year parenthetical norm.

### Headings
Arabic numeral section numbering as in FIELD_SKILL; no journal-specific deviation observed. Formal mathematical statements (Proposition, Corollary, Assumption, Theorem) are commonly numbered and set off, more so than typical FIELD_SKILL empirical papers, reflecting the journal's mathematical/actuarial-science orientation.

### Tables and Figures
No journal-specific rule beyond standard Springer formatting found. Papers in the sample use sensitivity plots (2D/3D) and numerical examples liberally alongside formal derivations — a heavier reliance on numerical illustration of theoretical results than typical FIELD_SKILL empirical papers.

### Explicit Prohibitions
Standard Springer/COPE originality requirements: no simultaneous submission, no prior publication in any form/language (exception: expansions of previous work must be declared). Author list and order must be finalized at submission; changes during revision require justification and are disallowed after acceptance.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
No delta from FIELD_SKILL's general register observed in visible abstracts/intros, but the sample skews mathematical/theoretical (propositions, formal proofs, numerical examples) rather than the reduced-form empirical register FIELD_SKILL primarily describes. Where a paper is a theory/methods paper (common at this journal), expect proof-and-proposition structure rather than identification-strategy narrative — PRACTICE ONLY, not universal (applied/data papers in the sample, e.g. the USS mortality study, follow a more standard empirical structure).

### Statistical Reporting
No delta from FIELD_SKILL beyond the citation-format override above.

### Citation Density
Follows FIELD_SKILL norm for density; format differs (see Hard Constraints — Citations).

### Structural Deviations
ENFORCED: numbered citation style (see above).
GUIDELINE ONLY / RELAXATION: shorter alternative formats (Letters, Discussions) are a lower-tier-journal feature not present in FIELD_SKILL's ABS 4*/4 baseline — this journal explicitly relaxes the "always a full research article" assumption by offering fast-track short formats aimed at practitioners.
PRACTICE ONLY: heavier use of formal Proposition/Corollary numbering and standalone "Discussion" plus "Concluding comments/Conclusions" as two separate closing sections (seen in the mortality-improvement-rates paper) rather than FIELD_SKILL's single merged Conclusion — observed in more than one theory-oriented article, so flagged as a real but not universal pattern.

### Other Journal-Specific Patterns
The journal explicitly welcomes practitioner contributions and frames itself as a theory-practice bridge (successor to six national actuarial journals). This is a scope/identity delta, not a prose-style delta, but it explains why some published pieces (Discussions, practitioner commentary) read less formally and more application-focused than a typical ABS 4*/4 finance article.

---

## Dimensions With No Delta
- Overall sentence/paragraph density: FIELD DEFAULT
- Hedging conventions: FIELD DEFAULT
- Introduction rhetorical structure (for standard research papers): FIELD DEFAULT
- Robustness/results reporting conventions (for applied papers): FIELD DEFAULT
- Table design conventions: FIELD DEFAULT

---

## Common Pitfalls
- Using author-year in-text citations instead of the required numbered bracket system — this is the single most likely formatting error given the strong FIELD_SKILL default toward author-year.
- Writing a full-length research-article structure for a submission intended as a Letter (5-page cap) or Discussion (1-3 page cap) — these formats have their own brevity expectations, not scaled-down versions of the standard template.
- Omitting formal numbered statements (Proposition/Assumption/Corollary) in theory-heavy submissions, where the sample shows this is a common structuring device for mathematical actuarial content.

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
| link.springer.com/journal/13385/submission-guidelines | Guidelines | Login-redirected; reconstructed via WebSearch snippets |
| link.springer.com/journal/13385/aims-and-scope | Guidelines/Scope | Fetched via idp.springer.com auth-redirect chain |
| paperpile.com/s/european-actuarial-journal-citation-style | Citation style reference | Fetched directly |
| link.springer.com/article/10.1007/s13385-025-00434-7 | Abstract/Structure | Fetched via idp.springer.com auth-redirect chain |
| link.springer.com/article/10.1007/s13385-025-00423-w | Abstract/Structure | Fetched via idp.springer.com auth-redirect chain |
| link.springer.com/article/10.1007/s13385-025-00428-5 (PMC12575580) | Full text | Fetched via PMC open-access mirror |
| link.springer.com/article/10.1007/s13385-021-00274-1 | Abstract/Structure | Fetched via idp.springer.com auth-redirect chain |
| link.springer.com/article/10.1007/s13385-022-00309-1 | Abstract/Structure | Fetched via idp.springer.com auth-redirect chain |
| link.springer.com/article/10.1007/s13385-025-00421-y | Title/topic | WebSearch snippet only |
| link.springer.com/article/10.1007/s13385-024-00404-5 | Title/abstract | WebSearch snippet only |
