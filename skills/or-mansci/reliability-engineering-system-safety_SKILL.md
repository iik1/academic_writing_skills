---
name: reliability-engineering-system-safety-writing-style
description: >
  Journal-specific writing conventions for Reliability Engineering and System Safety
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Reliability Engineering and System Safety",
  "submit to Reliability Engineering and System Safety", "match Reliability Engineering and System Safety style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Reliability Engineering and System Safety

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Elsevier
- **Scope:** Reliability and safety of complex technological systems (nuclear plants, chemical facilities, transportation networks, infrastructure); emphasis on probabilistic methods and real-system application.
- **Guidelines URL:** https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety/publish/guide-for-authors
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 2 (Verleijsdonk et al. 2026, doi:10.1016/j.ress.2026.112773, via arXiv:2410.18246; Nozhati et al. 2019, doi:10.1016/j.ress.2018.09.037, via arXiv:1803.01451)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Required submission elements in order: Title page → Abstract → Keywords → **Highlights** (required) → Graphical abstract (optional) → Main body → References → Declarations (competing interests, funding, generative AI use, CRediT authorship contributions).

### Length
No explicit word or page limit stated in accessible guidelines.

### Abstract
Unstructured (plain paragraph). Word limit not confirmed from accessible guidelines; both spot-checked articles have abstracts of approximately 150–220 words. Label: **GUIDELINE ONLY** (limit unconfirmed).

### Citations
Numbered Vancouver-style references, cited as [1], [2, 3], [6–10] in text, listed numerically at the end. Confirmed in both spot-checked articles. Not explicitly stated in accessible guidelines sections. Label: **PRACTICE ONLY**.

### Headings
Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm.

### Explicit Prohibitions
- **Fuzzy sets and non-probabilistic methods**: "The journal does not normally publish articles that involve fuzzy sets and related non-probabilistic methods unless they contribute significantly to the solution of substantive problems related to the analysis of real systems." This applies equally to possibility theory, rough sets, and related non-probabilistic uncertainty frameworks. Label: **ENFORCED**.
- AI tools may not be listed as co-authors.
- Authorship changes not permitted after acceptance.

---

## Observed Deltas from FIELD_SKILL

### Citations
**Field norm (unspecified in FIELD_SKILL baseline):** FIELD_SKILL notes that referencing style is journal-specific and excludes it from the baseline.
**This journal:** Numbered [1], [2] style throughout. Both spot-checked articles use this format consistently. Authors accustomed to author-year (Harvard) style from management science journals should switch to numbered references. Label: **PRACTICE ONLY**.

### Structural Deviations
**Field norm:** FIELD_SKILL expects results structured around theorems, algorithms, or empirical models; does not foreground case study as a distinct section type.
**This journal:** Industrial case study is a formal article type and commonly appears as a standalone top-level section after (or in place of) simulation/numerical experiments. Article 1 has distinct sections for Simulation Study (§5) and Case Study (§6); both report performance on real-world equipment data. Papers without an applied case component are less characteristic of the journal. Label: **PRACTICE ONLY**.

### Other Journal-Specific Patterns
**Highlights requirement:** Elsevier requires authors to submit 3–5 highlights (short bullet-point statements of key results) as a distinct submission component. This is absent from FIELD_SKILL baseline. Not visible in arXiv preprints but confirmed as a required element by guidelines. Label: **ENFORCED**.

**Scope constraint — probabilistic framing:** The fuzzy sets prohibition signals a broader editorial expectation: contributions should be grounded in probabilistic reliability theory (Markov models, Bayesian inference, Monte Carlo methods, stochastic processes). Non-probabilistic uncertainty representations require an unusually strong justification tied to a real system. This is narrower than the broader OR&MANSCI baseline. Label: **ENFORCED**.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Register and formality: FIELD DEFAULT
- Abstract format (unstructured): FIELD DEFAULT
- Related work placement (standalone Section 2 or subsection of Introduction): FIELD DEFAULT
- Contribution enumeration in Introduction: FIELD DEFAULT
- Appendix use (proofs, robustness): FIELD DEFAULT
- Hedging norms: FIELD DEFAULT
- Separate Discussion section (absent): FIELD DEFAULT
- Statistical reporting precision: FIELD DEFAULT

---

## Common Pitfalls
1. **Fuzzy set submissions:** Submitting a paper centred on fuzzy reliability indices, fuzzy FMEA, or possibility-based risk measures without a compelling demonstration of value for a real industrial system invites desk rejection. The prohibition is strong and editorial.
2. **Missing highlights:** Elsevier's highlights are a mandatory submission element, not optional. Forgetting them delays processing.
3. **Author-year citations:** Using "(Smith et al., 2020)" in-text when the journal uses numbered "[1]" style marks the manuscript as not prepared for submission.
4. **Theory-only manuscripts:** RESS favours contributions validated on real or realistic system data (power grids, chemical plants, aviation, medical equipment). Purely abstract theoretical results without engineering grounding are unlikely to fit the journal's editorial profile, even if methodologically sound by OR standards.

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
| https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety/publish/guide-for-authors | Guidelines | Direct fetch (partial — page truncated) |
| arXiv:2410.18246 (Verleijsdonk et al. 2026, RESS doi:10.1016/j.ress.2026.112773) | Full-text | PDF via arXiv |
| arXiv:1803.01451 (Nozhati et al. 2019, RESS doi:10.1016/j.ress.2018.09.037) | Full-text | PDF via arXiv |