---
name: naval-research-logistics-writing-style
description: >
  Journal-specific writing conventions for Naval Research Logistics
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Naval Research Logistics",
  "submit to Naval Research Logistics", "match Naval Research Logistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Naval Research Logistics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Wiley
- **Scope:** Publishes modeling and analysis of problems motivated by real-world applications, major methodological advances in operations research and applied statistics, and expository or survey pieces of lasting value. Coverage includes search theory, scheduling, reliability, combat models, routing, stochastic programming, and supply chain — with historical emphasis on defense-relevant applications.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/15206750/homepage/forauthors.html
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 1 (Lejeune, Royset & Ma 2024, "Multi-Agent Search for a Moving and Camouflaging Target", NRL 71(4):532–552; arXiv:2309.02629)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm. No required section template is mandated (Free Format submission).

### Length
No explicit word or page limit stated. Free Format submission accepts any file format.

### Abstract
Unstructured prose, maximum 250 words. A separate **Keywords** line (5 keywords) is required immediately after the abstract. [ENFORCED — confirmed in article: abstract ~100 words, keywords listed separately]

### Citations
Free Format: any consistent reference style is accepted at submission. In practice, published articles use **numbered** references `[1]`, `[2]`, etc., not author-year. [PRACTICE ONLY — guidelines permit any style, numbered observed in article]

### Headings
Follows FIELD_SKILL norm. Numbered sections and subsections are standard. Bold inline subheadings within sections (e.g., **Computational Tests.**) are used in practice for thematic sub-units that do not warrant a full numbered subsection.

### Tables and Figures
Follows FIELD_SKILL norm.

### Practitioner Points
Guidelines offer an optional element: up to 3 "Practitioner Points" — short bullet-style statements written for practitioners, to be published alongside the article. These are separate from the abstract. [GUIDELINE ONLY — not observed as a formal box in spot-checked article; practitioner insights instead appeared as a closing paragraph in the Conclusion]

### Explicit Prohibitions
**Appendices must not appear in the main manuscript body.** All supplementary material must be submitted as separate supporting information files. [ENFORCED — this overrides FIELD_SKILL, which treats appendices in the main body as near-universal at ABS 4*/4 level. At NRL, appendices and proofs must be detached from the main document entirely]

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Citation Style
**Field norm:** Leading ABS 4*/4 OR&MANSCI journals (MS, OR, Math Prog, EJOR) use author-year citation format.
**NRL practice:** Numbered citations `[n]` throughout, including in-text and reference list.
**Label:** PRACTICE ONLY (guidelines accept any consistent style)

### Appendix Handling
**Field norm:** Appendices in the main document body are near-universal; they house full proofs, extended tables, and robustness checks.
**NRL constraint:** Appendices and supplementary material must be submitted as separate supporting information files, not embedded in the manuscript. Authors intending to place proofs or robustness tables in an appendix must instead prepare these as standalone supplementary files.
**Label:** ENFORCED

### Abstract Length
**Field norm:** Abstracts at ABS 4*/4 level typically run 150–200 words.
**NRL practice:** Abstracts are notably brief — approximately 100 words in the spot-checked article, well below the 250-word ceiling. The concise format is consistent with the journal's applied-methods orientation.
**Label:** RELAXATION (ABS 3 journal; shorter abstract is accepted, not a new norm)

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Register and formality: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction CARS structure: FIELD DEFAULT (territory → gap → contributions → roadmap)
- Contribution enumeration: FIELD DEFAULT
- Tense conventions: FIELD DEFAULT
- Theorem/model/algorithm presentation: FIELD DEFAULT (formal notation, assumptions numbered, inline intuition after formal statements)
- Hedging and epistemic caution: FIELD DEFAULT
- Results reporting: FIELD DEFAULT (tables primary vehicle, prose interprets key comparisons)
- Literature engagement: FIELD DEFAULT (paraphrase and attribution, no quotation, respectful framing of prior work)
- Related work placement: FIELD DEFAULT (literature integrated within Introduction, no standalone section)
- Conclusion structure: FIELD DEFAULT (synthesises contributions, reconnects to gap, pointers to future work)

---

## Common Pitfalls

1. **Placing proofs or supplementary material in an appendix within the main PDF.** NRL explicitly prohibits this; such content must be a separate supporting information file. Authors accustomed to ABS 4*/4 norms (where main-body appendices are expected) will need to restructure.

2. **Submitting without a Keywords line.** Five keywords are required as a separate labelled line following the abstract. Omitting this or folding keywords into the abstract text does not meet the guidelines.

3. **Using author-year citations in the submitted manuscript.** While the journal accepts any consistent style, the house style in published articles is numbered `[n]`. Switching style post-acceptance may require reformatting the entire manuscript.

4. **Neglecting the optional Practitioner Points.** For papers with applied or managerial implications, the three-point practitioner summary is a journal-specific opportunity to improve reach and editorial reception. It is absent from purely theoretical submissions but expected for applied modelling papers.

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
| https://onlinelibrary.wiley.com/page/journal/15206750/homepage/forauthors.html | Guidelines | Web search extraction (direct fetch blocked 403) |
| Lejeune, Royset & Ma (2024), NRL 71(4):532–552; arXiv:2309.02629 | Full-text article | arXiv preprint PDF |