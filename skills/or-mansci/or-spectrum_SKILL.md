---
name: or-spectrum-writing-style
description: >
  Journal-specific writing conventions for OR Spectrum
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for OR Spectrum",
  "submit to OR Spectrum", "match OR Spectrum style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: OR Spectrum

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Springer Nature (in cooperation with Gesellschaft für Operations Research e.V.)
- **Scope:** Publishes applied and theoretical papers developing and applying quantitative approaches to strategic, tactical, and operational problem-solving and decision-making; accepts surveys, theoretical papers, application-oriented papers, and case studies, plus software and book reviews.
- **Guidelines URL:** https://link.springer.com/journal/291/submission-guidelines (login-redirect wall blocked direct fetch in this environment; generic Springer Nature manuscript template details were retrieved via search cache instead — see Sources)
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 6 abstracts read in full, plus ~85 additional titles/keywords scanned across issues from March 2022 through June 2026 (RePEc/IDEAS listing). Full-text access blocked by Springer login wall; abstract-level pages used throughout (see Sources for individual article links).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No journal-specific structural mandate found beyond FIELD_SKILL norms. Follows FIELD_SKILL norm.

### Length
No explicit journal-specific page/word limit found in accessible sources.

### Abstract
Unstructured abstract, approximately 150–250 words (Springer Nature journal-wide default, confirmed applicable to OR Spectrum via search). This aligns with typical FIELD_SKILL abstract expectations; no journal-specific tightening observed.

### Citations
No journal-specific citation style beyond the standard Springer Nature reference format (author-year, "sn-basic" style commonly used in the LaTeX template). Follows FIELD_SKILL norm.

### Headings
Follows FIELD_SKILL norm.

### Tables and Figures
Standard Springer Nature formatting (Arabic numeral table numbering, sequential in-text citation, EPS for vector figures / TIFF for halftones). This is the generic Springer Nature production requirement, not a distinctive OR Spectrum norm — noted here only because it is an explicit guideline-page instruction rather than a discovered convention.

### Explicit Prohibitions
Standard Springer Nature originality/simultaneous-submission prohibition; single-blind peer review (reviewer identities never disclosed to authors). No OR Spectrum-specific prohibitions beyond Springer's boilerplate found.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm.

### Statistical Reporting
Follows FIELD_SKILL norm.

### Citation Density
Follows FIELD_SKILL norm.

### Structural Deviations
Follows FIELD_SKILL norm.

### Other Journal-Specific Patterns
- **No JEL codes.** Across all abstracts and abstract pages checked (including finance/pricing/portfolio papers where JEL codes would be typical in an econ-adjacent outlet), none listed JEL classification codes. PRACTICE ONLY — consistent with OR Spectrum's identity as an OR/management-science venue rather than an economics journal, even when covering finance-adjacent topics (portfolio optimization, market power, pricing).
- **Very high concentration of applied, algorithmic/computational papers.** The spot-checked issues are dominated by vehicle routing, scheduling, warehousing/logistics, DEA/efficiency, and revenue/pricing management topics, with a comparatively small share of purely abstract theoretical papers. This is a RELAXATION within the ABS 3 tier: OR Spectrum leans more applied/computational on average than the ABS 4/4* theoretical benchmark in FIELD_SKILL, though it still publishes some theory-forward papers (e.g., cooperative game theory, fractional programming). PRACTICE ONLY, not a stated rule.
- **Literature-review and survey articles are a recognized, regularly published article type** (e.g., "Assortment optimization: a systematic literature review," "Optimization models for disaster response operations: a literature review"), consistent with the stated scope permitting surveys. FIELD DEFAULT for surveys generally, but worth noting as a more visible share of the journal's output than typical for ABS 4/4* outlets.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence/paragraph style: FIELD DEFAULT
- Argumentation structure (CARS model): FIELD DEFAULT
- Methods conventions and tense usage: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Discussion/Conclusion norms: FIELD DEFAULT
- Citation style and reference formatting: FIELD DEFAULT (standard Springer author-year)

---

## Common Pitfalls
- Do not add JEL classification codes — not used by this journal even for finance/economics-adjacent submissions.
- Do not assume a purely theoretical framing will be favored over an applied/computational one; the journal's actual output skews toward applied algorithmic and logistics/OR problems, so purely abstract theory papers are a minority rather than the norm.
- Single-blind review: do not anonymize the manuscript under the assumption of double-blind review.

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
| https://link.springer.com/journal/291/submission-guidelines | Guidelines | Blocked by Springer login redirect; generic Springer Nature template details retrieved via WebSearch cache snippets |
| https://link.springer.com/journal/291/aims-and-scope | Guidelines (scope) | Blocked by Springer login redirect; scope text retrieved via WebSearch cache snippets |
| https://ideas.repec.org/s/spr/orspec.html | Journal listing | Full-text fetch (RePEc/IDEAS) |
| https://ideas.repec.org/a/spr/orspec/v47y2025i2d10.1007_s00291-024-00782-y.html | Abstract | Full-text fetch (RePEc/IDEAS) |
| https://ideas.repec.org/a/spr/orspec/v46y2024i4d10.1007_s00291-024-00752-4.html | Abstract | Full-text fetch (RePEc/IDEAS) |
| https://ideas.repec.org/a/spr/orspec/v45y2023i1d10.1007_s00291-022-00693-w.html | Abstract | Full-text fetch (RePEc/IDEAS) |
| https://ideas.repec.org/a/spr/orspec/v46y2024i3d10.1007_s00291-024-00750-6.html | Abstract | Full-text fetch (RePEc/IDEAS) |
| https://ideas.repec.org/a/spr/orspec/v45y2023i4d10.1007_s00291-023-00728-w.html | Abstract | Full-text fetch (RePEc/IDEAS) |
| https://ideas.repec.org/a/spr/orspec/v44y2022i2d10.1007_s00291-022-00679-8.html | Abstract (unavailable for this item) | Full-text fetch (RePEc/IDEAS) |
