---
name: computers-operations-research-writing-style
description: >
  Journal-specific writing conventions for Computers and Operations Research
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Computers and Operations Research",
  "submit to Computers and Operations Research", "match Computers and Operations Research style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Computers and Operations Research

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Elsevier
- **Scope:** Computational methods for operations research problems; covers optimisation, scheduling, routing, and combinatorial problems with an emphasis on algorithmic solutions, computational complexity, and numerical validation.
- **Guidelines URL:** https://www.sciencedirect.com/journal/computers-and-operations-research/publish/guide-for-authors
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 2 (arXiv:2411.18381 / COR 2025 vol.184 nr.107219; ScienceDirect pii/S0305054824003381)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm for body sections. Additionally requires: title page, abstract, keywords, **highlights** (mandatory), and graphical abstract (optional) before the main body. Supplementary material permitted.

### Length
No explicit word or page limit stated in guidelines.

### Abstract
**ENFORCED — partial structure within unstructured format.** Abstract is unstructured prose (no labelled headers) but must explicitly cover all three of: (1) the investigated problem(s), (2) the theoretical or methodological contribution, and (3) the insights derived. No word limit specified in guidelines.

### Highlights
**ENFORCED.** A highlights section is mandatory (Elsevier requirement). Typically 3–5 bullet points summarising the main contributions; appears immediately after the abstract on the journal page. Not part of FIELD_SKILL baseline.

### Citations
**GUIDELINE ONLY for Harvard; PRACTICE is numbered brackets.** Guidelines state "Harvard style adopted," but spot-checked articles consistently use numbered brackets (e.g., [1], [21]) for in-text citations and a numbered reference list. Authors should follow the numbered-bracket convention as observed in published articles, not author–year format.

### Headings
Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm. Standard Elsevier figure and table formatting applies.

### Explicit Prohibitions
- **ENFORCED.** Papers must demonstrate "constructive algorithmic complexity and extensive numerical experiments." Numerical illustrations (worked examples) are explicitly insufficient as standalone evidence — a full computational study is required.
- **ENFORCED.** Metaheuristics and heuristics that are not well-established algorithms must be described in **metaphor-free language**. Nature-inspired or animal-metaphor framings (e.g., "the wolf hunts prey") are rejected.
- **ENFORCED.** The journal does not publish papers arising in the context of warfare activities planning.
- **ENFORCED.** Long formulations for variants/extensions of existing problems solved only by well-established approximate methods without novel analytical contribution are not endorsed.

### Reproducibility
**ENFORCED — stricter than FIELD_SKILL baseline.** Fully reproducible results are mandatory for acceptance. Authors must grant full access to the data and code underlying their work. This is stated as a core publication requirement, not a recommendation.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Statistical Reporting / Computational Evidence Standard
**RELAXATION relative to ABS 4*/4 norms; ENFORCED as journal-specific floor.** The journal explicitly requires extensive numerical experiments — not just proof sketches or illustrative examples — but its threshold is computational breadth rather than the rigorous theoretical-plus-empirical depth expected at ABS 4*/4. Algorithmic papers without a full computational study will be desk-rejected; however, purely theoretical contributions without computational validation appear less common in this venue than at Operations Research or Management Science.

### Metaheuristic Language
**PRACTICE ONLY (reinforced by ENFORCED guideline).** The prohibition on metaphor-laden metaheuristic descriptions is not a FIELD_SKILL norm — it is specific to this journal. In practice, papers presenting heuristics describe them in algorithmic/procedural terms (pseudocode, step-by-step logic) rather than bio-inspired narrative. This applies even when the underlying algorithm is inspired by natural processes.

### Structural Deviations
Related Work appears as a subsection within the Introduction (numbered subsection, e.g., Section 1.2) rather than a free-standing section. This aligns with the FIELD_SKILL norm but is more consistently applied here than in theoretical OR journals where a standalone Related Work section is sometimes used.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person plural "we" dominates; passive used selectively)
- Sentence and paragraph style: FIELD DEFAULT
- Argumentation (CARS structure): FIELD DEFAULT
- Tense conventions: FIELD DEFAULT
- Hedging: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Conclusion structure: FIELD DEFAULT
- Appendix use: FIELD DEFAULT

---

## Common Pitfalls
1. **Submitting a paper with only numerical illustrations.** The guidelines explicitly reject papers where the computational evidence consists of worked examples rather than a systematic computational study on benchmark or randomly generated instances.
2. **Using metaphor-laden metaheuristic descriptions.** Describing a heuristic as "wolves hunting prey" or "bees foraging" will trigger desk rejection. Reframe entirely in algorithmic/procedural terms before submission.
3. **Omitting highlights.** Highlights are mandatory and must be prepared as 3–5 bullet points covering key contributions; omitting them will require revision before review.
4. **Citing in author–year format.** Despite the guideline's reference to "Harvard style," published articles use numbered brackets. Submitting with parenthetical author–year citations creates an inconsistency that may require reformatting.
5. **Not providing code/data access.** Full reproducibility is a mandatory acceptance condition, not a reviewer recommendation. Papers that do not include accessible code and data will not be accepted.

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
| https://www.sciencedirect.com/journal/computers-and-operations-research/publish/guide-for-authors | Guidelines | Direct fetch (via redirect from elsevier.com) |
| arXiv:2411.18381 (Nicosia et al., COR 2025, vol.184) | Full-text HTML | arxiv.org/html/2411.18381 |
| ScienceDirect pii/S0305054824003381 | Abstract + metadata | Direct fetch |